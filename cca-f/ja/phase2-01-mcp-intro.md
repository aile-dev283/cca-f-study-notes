<!-- markdownlint-disable -->

# Model Context Protocol 入門

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol>  
**所要時間:** 未記載  
**対象ドメイン:** D2  
**フェーズ:** Phase 2  

---

## カリキュラム

### レッスン 01: Welcome to the course

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/303756>  

Open in Claude
0 seconds of 1 minute, 4 secondsVolume 90%

UV インストールガイドへの直接リンク: https://docs.astral.sh/uv/
Model Context Protocol の紹介: https://modelcontextprotocol.io/introduction

---

### レッスン 02: Introducing MCP

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296689>  

Open in Claude

Model Context Protocol（MCP）は、面倒な統合コードを大量に書かなくても Claude に context と tools を提供する communication layer である。tool の定義と実行の負担を、あなたの server から専用の MCP server へと移すための手段だと考えればよい。

MCP に初めて触れると、基本的なアーキテクチャを示す図を目にするだろう。MCP Client（あなたの server）が、tools・prompts・resources を含む MCP Server に接続する、という図だ。各 MCP Server は、何らかの外部サービスへの interface として機能する。

MCP が解決する問題

たとえば、ユーザーが自分の GitHub データについて Claude に質問できる chat interface を構築しているとしよう。ユーザーは「自分のすべての repository にまたがって、open な pull request はどれだけあるか？」と尋ねるかもしれない。これに対応するには、Claude が GitHub の API にアクセスするための tools を必要とする。

GitHub には膨大な機能がある——repository、pull request、issue、project、その他多数。MCP がなければ、GitHub のすべての機能を扱うために、信じられないほど多くの tool schema や function を自分で作成する必要があるだろう。

つまり、そうした統合コードをすべて自分で記述・テスト・保守しなければならない。これは多大な労力であり、継続的な保守負担でもある。

MCP の仕組み

MCP は、tool の定義と実行をあなたの server から専用の MCP server へと移すことで、この負担を肩代わりする。GitHub の tools をすべて自分で書く代わりに、GitHub 用の MCP Server がそれを担ってくれる。

MCP Server は GitHub にまつわる膨大な機能をまとめ上げ、標準化された一連の tools として公開する。あなたの application は、すべてをゼロから実装する代わりに、この MCP server に接続する。

MCP Servers の解説

MCP Servers は、外部サービスが実装しているデータや機能へのアクセスを提供する。標準化された方法で tools・prompts・resources を公開する、専用の interface として機能する。

先ほどの GitHub の例では、GitHub 用の MCP Server には `get_repos()` のような tool が含まれ、GitHub の API に直接接続する。あなたの server は MCP server と通信し、MCP server が GitHub 固有の実装の詳細をすべて処理する。

よくある質問
MCP Servers は誰が作るのか？

MCP server の実装は誰でも作成できる。多くの場合、サービス提供者自身が公式の MCP 実装を作る。たとえば AWS が、各種サービス向けの tools を備えた公式 MCP server をリリースするかもしれない。

API を直接呼ぶのと何が違うのか？

MCP server は、すでに定義済みの tool schema と function を提供してくれる。API を直接呼びたい場合は、それらの tool 定義を自分で書くことになる。MCP はその実装作業を省いてくれる。

MCP は結局 tool use と同じではないのか？

これはよくある誤解だ。MCP server と tool use は互いに補完的だが別の概念である。MCP server はすでに定義済みの tool schema と function を提供するのに対し、tool use は Claude が実際にそれらの tool をどう呼び出すかに関するものだ。重要な違いは「誰が作業をするか」である——MCP では、誰かがすでに tools をあなたのために実装してくれている。

利点は明確だ。複雑な統合の一式を自分で保守する代わりに、外部サービスへの接続という重労働を肩代わりしてくれる MCP server を活用できる。

---

### レッスン 03: MCP clients

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690>  

Open in Claude

MCP client は、あなたの server と MCP servers の間の communication bridge として機能する。MCP server が提供するすべての tools へのアクセス窓口であり、メッセージ交換や protocol の詳細を処理してくれるので、あなたの application はそれを気にせずに済む。

Transport に依存しない通信

MCP の重要な強みの一つは transport agnostic であること——これは、設定に応じて client と server が異なる protocol で通信できることを意味する洒落た言い回しだ。

最も一般的な構成では、MCP client と server の両方を同じマシン上で実行し、標準入出力（standard input/output）を通じて通信する。ただし、次のような方法で接続することもできる。

HTTP
WebSockets
その他さまざまなネットワーク protocol

MCP の Message Types

接続が確立すると、client と server は MCP 仕様で定義された特定の message type を交換する。主に扱うことになるのは次のものだ。

ListToolsRequest/ListToolsResult: client が server に「どんな tools を提供しているか？」と尋ね、利用可能な tools のリストを受け取る。

CallToolRequest/CallToolResult: client が server に対し、指定した引数で特定の tool を実行するよう求め、その結果を受け取る。

すべてがどう連携するか

ここでは、ユーザーのクエリがシステム全体を通してどのように流れるかを示す完全な例を見ていく——あなたの server から、MCP client を経由し、GitHub のような外部サービスへ、そして Claude へと戻る流れだ。

たとえばユーザーが「自分はどんな repository を持っているか？」と尋ねたとしよう。ステップごとの流れは次のとおりだ。

User Query: ユーザーが質問をあなたの server に送信する
Tool Discovery: あなたの server は、Claude に送るために利用可能な tools を把握する必要がある
List Tools Exchange: あなたの server が MCP client に利用可能な tools を尋ねる
MCP Communication: MCP client が MCP server に ListToolsRequest を送り、ListToolsResult を受け取る
Claude Request: あなたの server が、ユーザーのクエリと利用可能な tools を Claude に送る
Tool Use Decision: Claude が、質問に答えるために tool を呼ぶ必要があると判断する
Tool Execution Request: あなたの server が、Claude の指定した tool を実行するよう MCP client に求める
External API Call: MCP client が MCP server に CallToolRequest を送り、MCP server が実際の GitHub API 呼び出しを行う
Results Flow Back: GitHub が repository データを返し、それが MCP server を通じて CallToolResult として戻ってくる
Tool Result to Claude: あなたの server が tool の結果を Claude に返す
Final Response: Claude が repository データを使って最終的な回答を組み立てる
User Gets Answer: あなたの server が Claude の応答をユーザーに届ける

確かにこの流れには多くのステップが含まれるが、各コンポーネントには明確な責務がある。MCP client は server 通信の複雑さを抽象化してくれるので、あなたは強力な外部の tools やデータソースへのアクセスを得ながら、application のロジックに集中できる。

この流れを理解することは極めて重要だ。というのも、この後のセクションで自分自身の MCP client と server を構築する際に、これらすべての要素を目にすることになるからだ。

---

### レッスン 04: Project setup

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296694>  

Open in Claude
Downloads
cli_project.zip
(opens in new tab)
cli_project_COMPLETE.zip
(opens in new tab)

---

### レッスン 05: Defining tools with MCP

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296697>  

Open in Claude

公式の Python SDK を使うと、MCP server の構築はずっと簡単になる。複雑な JSON schema を手で書く代わりに、decorator で tools を定義し、重労働は SDK に任せられる。

この例では、2 つの中核的な tool を備えた document 管理 server を作成する。1 つは document を読む tool、もう 1 つは document を更新する tool だ。すべての document は、キーが document ID、値が content となる単純な dictionary としてメモリ上に存在する。

MCP Server のセットアップ

Python MCP SDK は server の作成を簡単にしてくれる。server はわずか 1 行で初期化できる。

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

document は単純な dictionary 構造で保持できる。

docs = {
"deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
"report.pdf": "The report details the state of a 20m condenser tower.",
"financials.docx": "These financials outline the project's budget and expenditures",
"outlook.pdf": "This document presents the projected future performance of the system",
"plan.md": "The plan outlines the steps for the project's implementation.",
"spec.txt": "These specifications define the technical requirements for the equipment"
}
Decorator による Tool 定義

SDK は decorator を使って tools を定義する。JSON schema を手作業で書く代わりに、Python の type hint と field の説明を使える。SDK が、Claude が理解できる適切な schema を自動的に生成する。

Document Reader Tool の作成

最初の tool は、ID によって document の内容を読み取る。完全な実装は次のとおりだ。

@mcp.tool(
name="read_doc_contents",
description="Read the contents of a document and return it as a string."
)
def read_document(
doc_id: str = Field(description="Id of the document to read")
):
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")

return docs[doc_id]

decorator は tool の name と description を指定し、function の parameter は必要な引数を定義する。Pydantic の Field クラスは引数の説明を提供し、各 parameter が何を期待しているかを Claude が理解するのに役立つ。

Document Editor Tool の構築

2 つ目の tool は、document に対して単純な検索置換（find-and-replace）を行う。

@mcp.tool(
name="edit_document",
description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
doc_id: str = Field(description="Id of the document that will be edited"),
old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
new_str: str = Field(description="The new text to insert in place of the old text.")
):
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")

docs[doc_id] = docs[doc_id].replace(old_str, new_str)

この tool は 3 つの parameter を取る。document ID、検索するテキスト、置換するテキストだ。実装には、document が見つからない場合のエラー処理が含まれ、素直な文字列置換を実行する。

SDK アプローチの主な利点
JSON schema を手作業で書く必要がない
type hint が自動的な検証を提供する
明確な parameter の説明が、Claude の tool 利用の理解を助ける
エラー処理が Python の例外と自然に統合される
tool の登録は decorator を通じて自動的に行われる

MCP Python SDK は、tool の作成を複雑な schema 記述の作業から、単純な Python の function 定義へと変える。このアプローチにより、Claude に正しくフォーマットされた tool 仕様が渡されることを保証しつつ、MCP server の構築と保守がはるかに容易になる。

---

### レッスン 06: The server inspector

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296693>  

Open in Claude

MCP server を構築する際には、完全な application に接続することなく機能をテストする方法が必要になる。Python MCP SDK には、ブラウザベースの inspector が組み込まれており、server をリアルタイムで debug・テストできる。

Inspector の起動

まず、Python 環境が有効化されていることを確認する（正確なコマンドはプロジェクトの README を参照）。次に、以下で inspector を実行する。

mcp dev mcp_server.py

これにより開発用 server が起動し、http://127.0.0.1:6274 のようなローカル URL が得られる（通常はこのような形式）。この URL をブラウザで開くと、MCP Inspector にアクセスできる。

Inspector インターフェースの使い方

inspector のインターフェースは現在も活発に開発が進められているため、利用時には見た目が異なるかもしれない。しかし、中核的な機能は一貫している。次の主要な要素を探してほしい。

MCP server を起動する Connect ボタン
Resources、Tools、Prompts、その他の機能のためのナビゲーションタブ
tools の一覧表示とテストのパネル

まず Connect ボタンをクリックして server を初期化する。接続状態が「Disconnected」から「Connected」に変わるのが分かる。

Tools のテスト

Tools セクションに移動し、「List Tools」をクリックすると、server から利用可能なすべての tools が表示される。tool を選択すると、右側のパネルにその詳細と入力フィールドが表示される。

たとえば、document を読み取る tool をテストするには次のようにする。

read_doc_contents tool を選択する
document ID（「deposition.md」など）を入力する
「Run Tool」をクリックする
成功したか、期待した出力が得られたかを結果で確認する

inspector は成功ステータスと実際に返されたデータの両方を表示するので、tool が正しく動作するかを簡単に検証できる。

Tool 連携のテスト

複数の tool を順番にテストして、複雑な workflow を検証できる。たとえば、edit tool を使って document を変更した後、すぐに read tool をテストして、変更が正しく適用されたことを確認できる。

inspector は tool 呼び出しの間も server の状態を保持するので、編集内容は永続化され、MCP server の完全な機能を検証できる。

開発ワークフロー

MCP Inspector は開発プロセスの不可欠な一部となる。別途テストスクリプトを書いたり、完全な application に接続したりする代わりに、次のことができる。

tool の実装を素早く反復する
エッジケースやエラー条件をテストする
tool の連携と状態管理を検証する
問題をリアルタイムで debug する

この即時的なフィードバックループにより、MCP server の開発がはるかに効率的になり、開発プロセスの早い段階で問題を捉えるのに役立つ。

---

### レッスン 07: Course satisfaction survey

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/297281>  

Open in Claude
Loading...

---

### レッスン 08: Implementing a client

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696>  

Open in Claude

MCP server が動作するようになったので、いよいよ client 側を構築する。client は、application のコードが MCP server と通信し、その機能にアクセスできるようにするものだ。

Client アーキテクチャの理解

現実の多くのプロジェクトでは、MCP client か MCP server のいずれかを実装することになり、両方を実装することはない。このプロジェクトで両方を構築するのは、両者がどのように連携するかを見てもらうためにすぎない。

MCP client は 2 つの主要なコンポーネントから成る。

MCP Client - session の利用を容易にするために作る独自のクラス
Client Session - server への実際の接続（MCP Python SDK の一部）

client session は慎重なリソース管理を必要とする——使い終わったら接続を適切にクリーンアップする必要があるのだ。だからこそ、すべてのクリーンアップを自動的に処理する独自のクラスでそれをラップする。

Client が Application にどう収まるか

先ほどの application フロー図を思い出してほしい。client は、2 つの重要なポイントで、コードが MCP server とやり取りできるようにするものだ。

CLI のコードは client を使って次のことを行う。

Claude に送るために、利用可能な tools のリストを取得する
Claude が要求したときに tools を実行する
中核となる Client Function の実装

2 つの不可欠な function を実装する必要がある。list_tools() と call_tool() だ。

List Tools Function

この function は、MCP server からすべての利用可能な tools を取得する。

async def list_tools(self) -> list[types.Tool]:
result = await self.session().list_tools()
return result.tools

これは単純明快だ——session（server への接続）にアクセスし、組み込みの list_tools() メソッドを呼び出し、結果から tools を返す。

Call Tool Function

この function は、server 上で特定の tool を実行する。

async def call_tool(
self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
return await self.session().call_tool(tool_name, tool_input)

tool の name と入力 parameter（Claude が提供したもの）を server に渡し、その結果を返す。

Client のテスト

client ファイルの末尾には、単純なテストハーネスが含まれている。これを直接実行して、すべてが動作することを確認できる。

uv run mcp_client.py

これは MCP server に接続し、利用可能な tools を出力する。説明や入力 schema を含む tool 定義が表示されるはずだ。

すべてを組み合わせる

client function を実装したら、メインの application を実行して、完全な流れをテストできる。

uv run main.py

次のように尋ねてみよう。「report.pdf という document の内容は何か？」

舞台裏で起きていることは次のとおりだ。

application が client を使って利用可能な tools を取得する
これらの tools が、あなたの質問とともに Claude に送られる
Claude が read_doc_contents tool を使うことを決める
application が client を使ってその tool を実行する
結果が Claude に返され、Claude があなたに応答する

client は、application のロジックと MCP server の機能の間の橋渡しとして機能し、強力な tools を AI ワークフローに簡単に組み込めるようにする。

---

### レッスン 09: Defining resources

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296699>  

Open in Claude

MCP server における Resources は、典型的な HTTP server における GET リクエストハンドラーと同様に、データを client に公開できる仕組みである。アクションを実行するのではなく、情報を取得する必要があるシナリオに最適だ。

例を通して Resources を理解する

たとえば、ユーザーが @document_name と入力してファイルを参照できる、document mention 機能を構築したいとしよう。これには 2 つの操作が必要だ。

利用可能なすべての document のリストを取得する（autocomplete のため）
特定の document の内容を取得する（mention されたとき）

ユーザーが document を mention すると、システムはその document の内容を、Claude に送られる prompt に自動的に注入する。これにより、Claude が情報を取得するために tools を使う必要がなくなる。

Resources の仕組み

Resources はリクエスト・レスポンスのパターンに従う。client がデータを必要とするとき、どの resource が欲しいかを識別するための URI を含む ReadResourceRequest を送る。MCP server はこのリクエストを処理し、ReadResourceResult としてデータを返す。

流れは次のようになる。あなたのコードが MCP client に resource を要求し、client がそのリクエストを MCP server に転送する。server は URI を処理し、適切な function を実行して、結果を返す。

Resources の種類

resource には 2 種類ある。

Direct Resources

Direct resource は、決して変わらない静的な URI を持つ。parameter を必要としない操作に最適だ。

@mcp.resource(
"docs://documents",
mime_type="application/json"
)
def list_docs() -> list[str]:
return list(docs.keys())
Templated Resources

Templated resource は、URI に parameter を含む。Python SDK はこれらの parameter を自動的に解析し、function にキーワード引数として渡す。

@mcp.resource(
"docs://documents/{doc_id}",
mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")
return docs[doc_id]

実装の詳細

resource はあらゆる種類のデータを返せる——文字列、JSON、バイナリデータなど。mime_type parameter を使って、どのような種類のデータを返しているかのヒントを client に与える。

"application/json" は構造化データ用
"text/plain" はプレーンテキスト用
"application/pdf" はバイナリファイル用

MCP Python SDK は、戻り値を自動的にシリアライズする。オブジェクトを手動で JSON 文字列に変換する必要はない——データ構造を返すだけで、シリアライズは SDK に任せられる。

Resources のテスト

MCP Inspector を使って resource をテストできる。次のコマンドで server を起動する。

uv run mcp dev mcp_server.py

そして、ブラウザで inspector に接続する。2 つのセクションが表示される。

Resources - direct/静的な resource を一覧表示する
Resource Templates - templated resource を一覧表示する

任意の resource をクリックしてテストする。templated resource の場合は、parameter の値を指定する必要がある。inspector は、MIME type やシリアライズされたデータを含め、client が受け取る正確なレスポンス構造を表示する。

Resources は、MCP server から読み取り専用のデータを公開する明快な方法を提供し、tool 呼び出しの複雑さなしに client が情報を取得できるようにする。

---

### レッスン 10: Accessing resources

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296695>  

Open in Claude

MCP における Resources は、データにアクセスするために tool 呼び出しを必要とするのではなく、prompt に直接含められる情報を server が公開できるようにする。これにより、AI モデルに context を提供するより効率的な方法が生まれる。

上の図は resource の仕組みを示している。ユーザーが「What's in the @...」のように入力すると、私たちのコードはこれを resource リクエストとして認識し、MCP server に ReadResourceRequest を送り、実際の content を含む ReadResourceResult を受け取る。

Resource Reading の実装

MCP client で resource アクセスを有効にするには、read_resource function を実装する必要がある。まず、必要な import を追加する。

import json
from pydantic import AnyUrl

中核の function は、MCP server にリクエストを行い、その MIME type に基づいてレスポンスを処理する。

async def read_resource(self, uri: str) -> Any:
result = await self.session().read_resource(AnyUrl(uri))
resource = result.contents[0]

if isinstance(resource, types.TextResourceContents):
if resource.mimeType == "application/json":
return json.loads(resource.text)

return resource.text
レスポンス構造の理解

resource を要求すると、server は contents リストを含む結果を返す。通常は一度に 1 つの resource しか必要としないため、最初の要素にアクセスする。レスポンスには次のものが含まれる。

実際の content（テキストまたはデータ）
content をどう解析するかを伝える MIME type
resource に関するその他のメタデータ
Content Type の処理

function は MIME type をチェックして、content をどう処理するかを決める。

application/json であれば、テキストを JSON として解析し、解析されたオブジェクトを返す
そうでなければ、生のテキスト content を返す

このアプローチは、構造化データ（JSON など）とプレーンテキストの document の両方をシームレスに処理する。

Resource Access のテスト

実装が済んだら、CLI application を通じて resource 機能をテストできる。「@」に続けて resource 名を入力すると、システムは次のことを行う。

利用可能な resource を autocomplete リストで表示する
矢印キーとスペースで resource を選択させる
resource の content を prompt に直接含める
追加の tool 呼び出しを必要とせずに、すべてを AI モデルに送る

これは、AI モデルが document の内容にアクセスするために別個の tool 呼び出しを行う場合と比べて、はるかにスムーズなユーザー体験を生み出す。resource の content が最初の context の一部となるため、データについて即座に応答できる。

---

### レッスン 11: Defining prompts

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296698>  

Open in Claude

MCP server における Prompts は、client がゼロから自分で prompt を書く代わりに使える、事前構築された高品質な指示を定義できるようにする。ユーザーが自分で思いつくものよりも良い結果をもたらす、入念に作り込まれたテンプレートだと考えればよい。

なぜ Prompts を使うのか？

ここでの重要な洞察はこうだ。ユーザーはすでに、ほとんどのタスクを Claude に直接頼むことができる。たとえば、ユーザーは「reformat the report.pdf in markdown」と入力して、それなりの結果を得られる。しかし、エッジケースを処理しベストプラクティスに従う、十分にテストされた専門的な prompt を提供すれば、ユーザーははるかに良い結果を得られる。

MCP server の作者として、あなたはさまざまなシナリオで一貫して機能する prompt の作成・テスト・評価に時間をかけられる。ユーザーは、自分自身が prompt engineering の専門家になる必要なく、その専門知識の恩恵を受けられる。

Format コマンドの構築

実用的な例を実装してみよう。document を markdown に変換する format コマンドだ。ユーザーは /format doc_id と入力し、document をプロフェッショナルにフォーマットした markdown 版を受け取る。

ワークフローは次のようになる。

ユーザーが / を入力して利用可能なコマンドを見る
format を選択し、document ID を指定する
Claude があなたの事前構築された prompt を使って document を読み、再フォーマットする
結果は、適切なヘッダー、リスト、フォーマットを備えたきれいな markdown になる
Prompts の定義

Prompts は、tools や resources と同様の decorator パターンを使う。

@mcp.prompt(
name="format",
description="Rewrites the contents of the document in Markdown format."
)
def format_document(
doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""

return [
base.UserMessage(prompt)
]

function は、Claude に直接送られるメッセージのリストを返す。複数の user メッセージや assistant メッセージを含めて、より複雑な会話フローを作ることもできる。

Prompts のテスト

デプロイする前に、MCP Inspector を使って prompt をテストしよう。

inspector は、変数が prompt テンプレートにどう補間されるかを含め、Claude に送られる正確なメッセージを表示する。これにより、ユーザーが頼り始める前に、prompt が正しく見えるかを検証できる。

主な利点
一貫性 - ユーザーは毎回信頼できる結果を得られる
専門知識 - ドメインの知識を prompt に符号化できる
再利用性 - 複数の client application が同じ prompt を使える
保守性 - 一箇所で prompt を更新すれば、すべての client が改善される

Prompts は、MCP server のドメインに特化したものであるときに最も効果を発揮する。document 管理 server なら、フォーマット、要約、document の分析のための prompt を持つかもしれない。データ分析 server なら、レポートや可視化を生成するための prompt を持つかもしれない。

目標は、ユーザーが自分で指示をゼロから書くよりも好んで使うほど、十分に作り込まれてテストされた prompt を提供することだ。

---

### レッスン 12: Prompts in the client

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296692>  

Open in Claude

MCP client 構築の最後のステップは、prompt 機能の実装だ。これにより、server からすべての利用可能な prompt を一覧表示し、変数が埋め込まれた特定の prompt を取得できるようになる。

List Prompts の実装

list_prompts メソッドは単純明快だ。session の list prompts function を呼び出し、prompt を返す。

async def list_prompts(self) -> list[types.Prompt]:
result = await self.session().list_prompts()
return result.prompts
個々の Prompt の取得

get_prompt メソッドは、変数の補間を扱うため、より興味深い。prompt を要求するとき、prompt function にキーワード引数として渡される引数を提供する。

async def get_prompt(self, prompt_name, args: dict[str, str]):
result = await self.session().get_prompt(prompt_name, args)
return result.messages

たとえば、server に doc_id parameter を期待する format_document prompt があるなら、引数の dictionary は {"doc_id": "plan.md"} を含むことになる。この値が prompt テンプレートに補間される。

Prompts を実際にテストする

実装が済んだら、CLI を通じて prompt をテストできる。スラッシュ（/）を入力すると、利用可能な prompt がコマンドとして表示される。「format」のような prompt を選択すると、利用可能な document から選ぶよう促される。

document を選択すると、システムは完全な prompt を Claude に送る。AI はフォーマットの指示と document ID の両方を受け取り、利用可能な tools を使って content を取得・処理する。

Prompts の仕組み

Prompts は、client が使える user メッセージと assistant メッセージの集合を定義する。それらは高品質で、十分にテストされ、MCP server の目的に関連したものであるべきだ。ワークフローは次のとおりだ。

server の機能に関連する prompt を書いて評価する
@mcp.prompt decorator を使って MCP server に prompt を定義する
client はいつでもその prompt を要求できる
client が提供する引数が、prompt function のキーワード引数になる
function は、AI モデル向けに整形されたメッセージを返す

このシステムは、変数によるカスタマイズを可能にしながら一貫性を保つ、再利用可能でパラメータ化された prompt を作り出す。これは、AI が毎回適切に構造化された指示を確実に受け取ることを保証したい、複雑なワークフローにおいて特に有用だ。

---

### レッスン 13: Final assessment on MCP

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/297196>  

Open in Claude
Loading...

---

### レッスン 14: MCP review

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296691>  

Open in Claude

MCP server を構築したので、3 つの中核的な server primitive を振り返り、それぞれをいつ使うべきかを理解しよう。重要な洞察は、各 primitive が application スタックの異なる部分によって制御されるということだ。

Tools: Model-Controlled

Tools は完全に Claude によって制御される。AI モデルがこれらの function をいつ呼ぶかを決め、その結果は Claude がタスクを達成するために直接利用する。

Tools は、Claude が自律的に使える追加の能力を与えるのに最適だ。Claude に「JavaScript を使って 3 の平方根を計算する」よう頼むと、JavaScript 実行 tool を使って計算を行うことを決めるのは Claude である。

Resources: App-Controlled

Resources は、あなたの application のコードによって制御される。app が、いつ resource データを取得し、それをどう使うかを決める——典型的には UI 要素のためや、会話に context を追加するためだ。

このプロジェクトでは、resources を 2 つの方法で使った。

UI の autocomplete オプションを埋めるためにデータを取得する
追加の context で prompt を補強するために content を取得する

Claude のインターフェースにある「Add from Google Drive」機能を思い浮かべてほしい——どの document を表示するかを application のコードが決め、それらの content を chat の context に注入する処理を扱う。

Prompts: User-Controlled

Prompts は、ユーザーのアクションによってトリガーされる。ユーザーが、ボタンのクリック、メニューの選択、スラッシュコマンドといった UI 操作を通じて、これらの定義済みワークフローをいつ実行するかを決める。

Prompts は、ユーザーがオンデマンドでトリガーできるワークフローの実装に理想的だ。Claude のインターフェースでは、チャット入力欄の下にあるワークフローボタンが prompt の例である——ユーザーがワンクリックで開始できる、定義済みで最適化されたワークフローだ。

正しい Primitive の選択

簡単な意思決定ガイドを示す。

Claude に新しい能力を与える必要があるか？ tools を使う
UI や context のためにデータを app に取り込む必要があるか？ resources を使う
ユーザー向けに定義済みのワークフローを作りたいか？ prompts を使う

3 つの primitive すべてが実際に動作している様子は、Claude の公式インターフェースで見ることができる。ワークフローボタンは prompts を、Google Drive 統合は resources を実演しており、Claude がコードを実行したり計算を行ったりするときは、舞台裏で tools を使っている。

これらは、あなたの特定のユースケースに合った正しい primitive を選ぶのに役立つ、高レベルのガイドラインだ。それぞれが application スタックの異なる部分を担う——tools はモデルに、resources はあなたの app に、prompts はあなたのユーザーに奉仕する。

---
