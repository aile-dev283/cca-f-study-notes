<!-- markdownlint-disable -->

# Code execution with MCP: Building more efficient agents（MCPによるコード実行: より効率的なエージェントの構築）

**URL:** <https://www.anthropic.com/engineering/code-execution-with-mcp>  
**対応ドメイン:** D2 / D5  
**優先度:** S

---

[Model Context Protocol（MCP）](https://modelcontextprotocol.io/) は、AIエージェントを外部システムに接続するためのオープン標準です。従来、エージェントをツールやデータに接続するには、組み合わせごとにカスタム統合を用意する必要があり、断片化と重複した作業が生じて、真に接続されたシステムをスケールさせることが困難でした。MCPは普遍的なプロトコルを提供します。開発者はエージェントに一度MCPを実装すれば、統合のエコシステム全体を利用できるようになります。

2024年11月のMCPのローンチ以来、その普及は急速に進んできました。コミュニティは数千もの [MCPサーバー](https://github.com/modelcontextprotocol/servers) を構築し、主要なすべてのプログラミング言語向けに [SDK](https://modelcontextprotocol.io/docs/sdk) が提供され、業界はMCPをエージェントとツール・データを接続するための事実上の標準として採用しています。

今日、開発者は数十ものMCPサーバーにまたがる数百から数千ものツールにアクセスできるエージェントを日常的に構築しています。しかし、接続されるツールの数が増えるにつれて、すべてのツール定義を事前に読み込み、中間結果をコンテキストウィンドウ越しに受け渡すことが、エージェントの動作を遅くし、コストを増大させます。

本ブログでは、コード実行によってエージェントがより多くのツールを扱いつつ、より少ないトークンでMCPサーバーとより効率的にやり取りできるようにする方法を探っていきます。

## Excessive token consumption from tools makes agents less efficient（ツールによる過剰なトークン消費がエージェントの効率を下げる）

MCPの利用がスケールするにつれ、エージェントのコストとレイテンシを増大させ得る、一般的な2つのパターンがあります。

1. ツール定義がコンテキストウィンドウを過負荷にする

2. 中間的なツール結果が追加のトークンを消費する

### 1. Tool definitions overload the context window（1. ツール定義がコンテキストウィンドウを過負荷にする）

ほとんどのMCPクライアントは、すべてのツール定義を事前にコンテキストへ直接読み込み、直接的なツール呼び出し構文を用いてモデルにそれらを公開します。こうしたツール定義は次のような見た目になります。

```
gdrive.getDocument
     Description: Retrieves a document from Google Drive
     Parameters:
                documentId (required, string): The ID of the document to retrieve
                fields (optional, string): Specific fields to return
     Returns: Document object with title, body content, metadata, permissions, etc.
```

```
salesforce.updateRecord
    Description: Updates a record in Salesforce
    Parameters:
               objectType (required, string): Type of Salesforce object (Lead, Contact,      Account, etc.)
               recordId (required, string): The ID of the record to update
               data (required, object): Fields to update with their new values
     Returns: Updated record object with confirmation
```

ツールの説明はコンテキストウィンドウの領域をより多く占有し、応答時間とコストを増大させます。エージェントが数千ものツールに接続されている場合、リクエストを読む前に数十万トークンを処理する必要が生じます。

### 2. Intermediate tool results consume additional tokens（2. 中間的なツール結果が追加のトークンを消費する）

ほとんどのMCPクライアントは、モデルがMCPツールを直接呼び出すことを許可しています。たとえば、エージェントに次のように依頼するかもしれません。「Google Driveから私の会議の文字起こしをダウンロードして、それをSalesforceのリードに添付して。」

モデルは次のような呼び出しを行います。

```
TOOL CALL: gdrive.getDocument(documentId: "abc123")
        → returns "Discussed Q4 goals...\n[full transcript text]"
           (loaded into model context)

TOOL CALL: salesforce.updateRecord(
			objectType: "SalesMeeting",
			recordId: "00Q5f000001abcXYZ",
  			data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
		)
		(model needs to write entire transcript into context again)
```

すべての中間結果はモデルを通過しなければなりません。この例では、通話の文字起こし全文が2回流れます。2時間のセールス会議であれば、追加で50,000トークンを処理することになりかねません。さらに大きなドキュメントになると、コンテキストウィンドウの上限を超えてしまい、ワークフローが壊れる可能性もあります。

大きなドキュメントや複雑なデータ構造を扱う場合、モデルがツール呼び出し間でデータをコピーする際にミスを犯しやすくなる可能性があります。

*MCPクライアントはツール定義をモデルのコンテキストウィンドウに読み込み、各ツール呼び出しとその結果が処理の合間にモデルを通過するメッセージループをオーケストレーションします。*

## Code execution with MCP improves context efficiency（MCPによるコード実行はコンテキスト効率を向上させる）

エージェント向けのコード実行環境がより一般的になってきたことを踏まえると、解決策の一つは、MCPサーバーを直接的なツール呼び出しではなくコードAPIとして提示することです。そうすれば、エージェントはMCPサーバーとやり取りするためのコードを書くことができます。このアプローチは両方の課題に対処します。エージェントは必要なツールだけを読み込み、結果をモデルに返す前に実行環境内でデータを処理できるのです。

これを実現する方法はいくつもあります。一つのアプローチは、接続されたMCPサーバーから利用可能なすべてのツールのファイルツリーを生成することです。以下はTypeScriptを使った実装例です。

```
servers
├── google-drive
│   ├── getDocument.ts
│   ├── ... (other tools)
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   ├── ... (other tools)
│   └── index.ts
└── ... (other servers)
```

そして、各ツールは次のようなファイルに対応します。

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

先ほどのGoogle DriveからSalesforceへの例は、次のコードになります。

```typescript
// Read transcript from Google Docs and add to Salesforce prospect
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

エージェントはファイルシステムを探索することでツールを発見します。`./servers/` ディレクトリの一覧を取得して利用可能なサーバー（`google-drive` や `salesforce` など）を見つけ、次に必要な特定のツールファイル（`getDocument.ts` や `updateRecord.ts` など）を読んで各ツールのインターフェースを理解します。これにより、エージェントは現在のタスクに必要な定義だけを読み込めます。これによってトークン使用量は150,000トークンから2,000トークンへと削減され、時間とコストを98.7%節約できます**。**

Cloudflareも [同様の知見を発表](https://blog.cloudflare.com/code-mode/) しており、MCPによるコード実行を「Code Mode」と呼んでいます。核心となる洞察は同じです。LLMはコードを書くことに長けており、開発者はこの強みを活かして、MCPサーバーとより効率的にやり取りするエージェントを構築すべきなのです。

## Benefits of code execution with MCP（MCPによるコード実行の利点）

MCPによるコード実行は、ツールをオンデマンドで読み込み、データがモデルに到達する前にフィルタリングし、複雑なロジックを一度のステップで実行することで、エージェントがコンテキストをより効率的に使えるようにします。このアプローチを使うことには、セキュリティや状態管理上の利点もあります。

### Progressive disclosure（段階的開示）

モデルはファイルシステムをナビゲートすることが得意です。ツールをファイルシステム上のコードとして提示することで、モデルはすべてを事前に読み込むのではなく、必要に応じてツール定義を読めるようになります。

あるいは、関連する定義を見つけるために `search_tools` ツールをサーバーに追加することもできます。たとえば、上で使った仮想的なSalesforceサーバーを扱う際、エージェントは「salesforce」を検索し、現在のタスクに必要なツールだけを読み込みます。`search_tools` ツールに詳細レベルのパラメータを含め、必要な詳細度（名前のみ、名前と説明、あるいはスキーマを含む完全な定義など）をエージェントが選択できるようにすることも、エージェントがコンテキストを節約し、効率的にツールを見つける助けになります。

### Context efficient tool results（コンテキスト効率の良いツール結果）

大規模なデータセットを扱う場合、エージェントは結果を返す前にコード内でフィルタリングや変換を行えます。10,000行のスプレッドシートを取得する場合を考えてみましょう。

```typescript
// Without code execution - all rows flow through context
TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
        → returns 10,000 rows in context to filter manually

// With code execution - filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(row => 
  row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only log first 5 for review
```

エージェントは10,000行ではなく5行を見るだけで済みます。同様のパターンは、集計、複数データソースにまたがる結合、特定フィールドの抽出にも有効です。いずれもコンテキストウィンドウを肥大化させることなく行えます。

#### More powerful and context-efficient control flow（より強力でコンテキスト効率の良い制御フロー）

ループ、条件分岐、エラー処理は、個々のツール呼び出しを連鎖させるのではなく、使い慣れたコードのパターンで実現できます。たとえば、Slackでデプロイ完了通知が必要な場合、エージェントは次のように書けます。

```typescript
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({ channel: 'C123456' });
  found = messages.some(m => m.text.includes('deployment complete'));
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

このアプローチは、エージェントループを通じてMCPツール呼び出しとスリープコマンドを交互に繰り返すよりも効率的です。

加えて、実行される条件分岐のツリーを書き出せることは、「最初のトークンまでの時間（time to first token）」のレイテンシ削減にもつながります。モデルがif文を評価するのを待つのではなく、エージェントはコード実行環境にそれを任せられるのです。

### Privacy-preserving operations（プライバシーを保護する操作）

エージェントがMCPによるコード実行を使う場合、中間結果はデフォルトで実行環境内に留まります。こうすることで、エージェントが見るのは明示的にログ出力または返却したものだけになります。つまり、モデルと共有したくないデータは、モデルのコンテキストに一切入ることなくワークフロー内を流れていけるのです。

さらに機微なワークロードに対しては、エージェントのハーネスが機微なデータを自動的にトークン化できます。たとえば、スプレッドシートから顧客の連絡先情報をSalesforceにインポートする必要があるとします。エージェントは次のように書きます。

```typescript
const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
for (const row of sheet.rows) {
  await salesforce.updateRecord({
    objectType: 'Lead',
    recordId: row.salesforceId,
    data: { 
      Email: row.email,
      Phone: row.phone,
      Name: row.name
    }
  });
}
console.log(`Updated ${sheet.rows.length} leads`);
```

MCPクライアントはデータを傍受し、それがモデルに到達する前にPII（個人を特定できる情報）をトークン化します。

```
// What the agent would see, if it logged the sheet.rows:
[
  { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
  { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
  ...
]
```

そして、別のMCPツール呼び出しでそのデータが共有される際には、MCPクライアント内のルックアップによってトークンが元に戻されます。実際のメールアドレス、電話番号、名前はGoogle SheetsからSalesforceへと流れますが、モデルを通過することは決してありません。これにより、エージェントが誤って機微なデータをログ出力したり処理したりすることが防がれます。また、これを使って決定論的なセキュリティルールを定義し、データがどこへ・どこから流れてよいかを選択することもできます。

### State persistence and skills（状態の永続化とスキル）

ファイルシステムへのアクセスを伴うコード実行により、エージェントは複数の操作にまたがって状態を維持できます。エージェントは中間結果をファイルに書き出せるため、作業を再開したり進捗を追跡したりできます。

```typescript
const leads = await salesforce.query({ 
  query: 'SELECT Id, Email FROM Lead LIMIT 1000' 
});
const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\n');
await fs.writeFile('./workspace/leads.csv', csvData);

// Later execution picks up where it left off
const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');
```

エージェントは、自分自身のコードを再利用可能な関数として永続化することもできます。あるタスクのために動作するコードを開発したら、その実装を将来の利用のために保存できます。

```typescript
// In ./skills/save-sheet-as-csv.ts
import * as gdrive from './servers/google-drive';
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}

// Later, in any agent execution:
import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
const csvPath = await saveSheetAsCsv('abc123');
```

これは [Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)（スキル）の概念と密接に結びついています。Skillsとは、モデルが専門的なタスクでのパフォーマンスを向上させるための、再利用可能な手順・スクリプト・リソースをまとめたフォルダのことです。これらの保存された関数にSKILL.mdファイルを追加すると、モデルが参照・利用できる構造化されたスキルになります。時間が経つにつれ、これによってエージェントはより高度な能力のツールボックスを構築し、最も効果的に作業するために必要な足場（スキャフォールディング）を進化させていくことができます。

なお、コード実行はそれ自体の複雑さをもたらすことに注意してください。エージェントが生成したコードを実行するには、適切な [サンドボックス化](https://www.anthropic.com/engineering/claude-code-sandboxing)、リソース制限、モニタリングを備えた安全な実行環境が必要です。こうしたインフラ要件は、直接的なツール呼び出しでは避けられる運用上のオーバーヘッドとセキュリティ上の考慮事項を追加します。コード実行の利点（トークンコストの削減、レイテンシの低減、ツール合成の改善）は、これらの実装コストと比較検討すべきです。

## Summary（まとめ）

MCPは、エージェントが多くのツールやシステムに接続するための基盤となるプロトコルを提供します。しかし、接続されるサーバーが多くなりすぎると、ツール定義や結果が過剰なトークンを消費し、エージェントの効率を低下させてしまいます。

ここで挙げた問題の多く（コンテキスト管理、ツール合成、状態の永続化）は新規のものに感じられますが、ソフトウェアエンジニアリングには既知の解決策があります。コード実行はこうした確立されたパターンをエージェントに適用し、使い慣れたプログラミング構文を用いてMCPサーバーとより効率的にやり取りできるようにします。このアプローチを実装する場合は、ぜひ [MCPコミュニティ](https://modelcontextprotocol.io/community/communication) に知見を共有してください。

### Acknowledgments（謝辞）

*この記事はAdam JonesとConor Kellyによって書かれました。本稿の草稿へのフィードバックをくださったJeremy Fox、Jerome Swannack、Stuart Ritchie、Molly Vorwerck、Matt Samuels、Maggie Voに感謝します。*
