<!-- markdownlint-disable -->

# Writing Effective Tools for AI Agents

**URL:** <https://www.anthropic.com/engineering/writing-tools-for-agents>  
**対応ドメイン:** D2 / D4  
**優先度:** S

---

## 核心メッセージ

「エージェントはそれに与えるツールと同じくらい有能でしかない」。ツール設計はプロンプトエンジニアリングと同等の重要性を持つ。

---

## ツール開発プロセス（3ステップ）

### Step 1: プロトタイプ構築
- 完全実装前にクイックプロトタイプを作成
- ローカル MCP サーバー or Desktop extension 経由で接続
- `claude mcp add <name> <command>` で Claude Code 統合

### Step 2: 評価実行
- **タスク生成**：実際のワークフローに基づくリアルな複数ステップ評価プロンプトを作成
  - 弱い例：単一操作
  - 強い例：「Jane と来週ミーティングを設定し、前回のメモを添付して会議室を予約する」
- **実行**：シンプルな agentic loop で精度・実行時間・トークン・エラー率を計測
- **分析**：エージェント推論トランスクリプトをレビューし、ツール呼び出しの非効率を発見

### Step 3: エージェントと協働
- 評価トランスクリプトを Claude Code に貼り付けてツールをリファクタリング
- 「この記事のアドバイスのほとんどは、Claude Code で内部ツールを繰り返し最適化して得られた」

---

## コア設計原則

### 1. 適切なツール選択（Quality over Quantity）
- ツールが多いほど良い結果になるわけではない
- エージェントはコンテキストウィンドウの制限がある
- **統合戦略**：個別 API エンドポイントではなく、関連操作を単一ツールにバンドル

**改善例:**

| 悪い設計（分散） | 良い設計（統合） |
|---------------|---------------|
| `list_users` + `list_events` + `create_event` | `schedule_event` |
| 生ログ読み取り | `search_logs`（コンテキスト付き） |
| 個別クエリ 3 本 | `get_customer_context`（統合結果） |

### 2. Namespacing
- サービス・リソースタイプ別にツール名をプレフィックス付けで整理
- 例：`asana_projects_search`、`asana_users_search`
- 類似ツール間の混同を減らし、選択精度を向上

### 3. 意味のあるコンテキストを返す
- UUID より自然言語識別子を優先
- mime_type・256px_image_url などの低信号フィールドを除外
- レスポンスフォーマット enum で "concise" / "detailed" を選択可能に
- Slack ツールの実績："concise" フォーマットで 72 トークン vs 206 トークン（⅓ 削減）

### 4. トークン効率の最適化
- ページネーション・フィルタリング・レンジ選択・切り捨てを実装
- Claude Code はデフォルトで 25,000 トークンに制限
- **エラーレスポンス**：`"Invalid parameter"` → `"Please use format 'YYYY-MM-DD' for date parameters"`（行動可能な指示）

### 5. ツール説明のプロンプトエンジニアリング（最重要）

> 「ツール説明は LLM のツール選択の主要メカニズム。曖昧な説明はミスルーティングを招く」

- 専門家が暗黙的に理解することを説明に含める
- `user` でなく `user_id` のように曖昧さのないパラメータ名
- 新入社員に説明するつもりで書く
- 期待する入出力フォーマットとリソース間の関係を明示
- **実績**：Claude Sonnet 3.5 が SWE-bench で SOTA 達成した要因のひとつはツール説明の精緻化

---

## 評価結果

| ツール | 改善内容 |
|-------|---------|
| Slack MCP | 人間作成 vs Claude 最適化で精度大幅向上 |
| Asana MCP | ホールドアウトテストセットでも同様の改善 |

---

## 試験対策：判断軸

| 状況 | 正解寄り | 罠 |
|------|---------|-----|
| 似たツールの誤選択 | name・description・引数・境界を明確化 | 「Claudeに気をつけて使って」と書く |
| ツールが多すぎる | 役割別エージェント分割、統合ツール設計 | 1 agent に全ツールを渡す |
| 中間結果が大きい | tool 側でフィルタ・ページネーション | 全結果をコンテキストへ貼る |
| エラーレスポンス | retry 可否・error category・修正方法を返す | `"Operation failed"` だけ返す |
| スキーマ誤り | JSON Schema + tool examples で明確化 | 「正しい形式で返して」と自然文で頼む |
| API key 管理 | environment variables / vault | `.mcp.json` に直書き |
