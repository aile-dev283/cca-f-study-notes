<!-- markdownlint-disable -->

# Code Execution with MCP + Advanced Tool Use

**URL（前半）:** <https://www.anthropic.com/engineering/code-execution-with-mcp>  
**URL（後半）:** <https://www.anthropic.com/engineering/advanced-tool-use>  
**対応ドメイン:** D2 / D5  
**優先度:** S

---

## Part 1: Code Execution with MCP

### 主要問題：コンテキスト過負荷

数千のツールに接続する時代、すべてのツール定義を事前ロードすると：
- 数十万トークンを消費
- 実測例：**150,000 トークン → 2,000 トークン（98.7% 削減）**

ツール呼び出しの各結果もコンテキストを圧迫。例：2時間の会議記録で追加 50,000 トークン。

### ソリューション：コード実行ベースのアプローチ

#### ファイルシステムベースのツール構成

ツールをファイル構造として提示 → エージェントが必要な定義だけオンデマンド読み込み：

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
```

#### コード実行による統合例

```typescript
const transcript = (await gdrive.getDocument({ 
  documentId: 'abc123' 
})).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

### コード実行アプローチの利点

| 利点 | 説明 |
|------|------|
| Progressive Disclosure | オンデマンドでツール定義を読み込み、`search_tools` で関連定義を検索 |
| コンテキスト効率 | 大規模データをコード環境でフィルタ・変換してから返す |
| プライバシー保護 | 中間結果は実行環境に留まり、機密データがモデルコンテキストに入らない |
| 制御フロー効率 | ループ・条件分岐・エラーハンドリングを従来コードパターンで実装 |
| 状態永続化 | 中間結果をファイルに保存し、後続セッションで再開可能 |

> **注意**：コード実行には適切なサンドボックス化・リソース制限・モニタリングが必要。直接ツール呼び出しより運用上の複雑性が増す。

---

## Part 2: Advanced Tool Use（Beta 機能）

### 背景

2025年11月24日リリース。5サーバー設定（GitHub, Slack, Sentry, Grafana, Splunk）で約 **55,000 トークン**、Jira 追加で **100,000 トークン超**という課題への回答。

### 機能 1: Tool Search Tool

**目的**：ツール定義によるトークン過多を削減

**仕組み**：`defer_loading: true` でマークしたツールをオンデマンド発見

**成果：**

| 指標 | 改善 |
|------|------|
| トークン使用量 | 約 **85% 削減** |
| Opus 4 精度 | 49% → **74%** |
| Opus 4.5 精度 | 79.5% → **88.1%** |

**使用場面：**
- ツール定義が 10,000 トークン超
- ツール選択精度の問題がある場合
- 複数サーバーの MCP システム構築時

> ツールは名前と description で検索されるため、**明確なツール定義が発見精度に直結**する。

### 機能 2: Programmatic Tool Calling

**目的**：大規模データ処理時のコンテキスト汚染と推論オーバーヘッドを削減

**仕組み**：Claude が自然言語ではなく Python コードでツール実行を編成

**実例**：予算超過チェック
- 従来：20人分の経費データ（50KB 超）がコンテキストに蓄積
- 新方式：わずか 1KB の結果のみ表示

**成果：**

| 指標 | 改善 |
|------|------|
| トークン削減 | 複雑タスクで平均 **37% 削減**（43,588 → 27,297） |
| 知識検索精度 | 25.6% → **28.5%** |

**実装**：`allowed_callers: ["code_execution_20250825"]` でツールをオプトイン

**使用場面：**
- 大規模データから集計結果のみ必要
- 3つ以上の従属ツール呼び出し
- 並列操作（50エンドポイント確認など）

### 機能 3: Tool Use Examples

**目的**：JSON スキーマでは表現できない使用パターンを明確化

**問題**：スキーマはデータ型を定義するが以下は指定不可：
- 日付形式（"2024-11-06" vs "Nov 6, 2024"）
- ID の慣例（UUID vs "USR-12345"）
- ネストされた構造の使用パターン
- パラメータ間の相関関係

**実装**：`input_examples` 配列にサンプルコール 3〜5 件を提供

**成果**：複雑なパラメータ処理で精度 72% → **90%**

**使用場面：**
- 複雑なネストされた構造
- 多くのオプションパラメータ
- API ドメイン固有の慣例
- 類似ツール間の区別が必要

### Beta 機能の有効化

```python
client.beta.messages.create(
    betas=["advanced-tool-use-2025-11-20"],
    model="claude-sonnet-4-5-20250929",
    # ...
)
```

---

## 試験対策：ボトルネック別の対応

| ボトルネック | 正解アプローチ | 罠 |
|------------|-------------|-----|
| ツール定義肥大化 | Tool Search Tool（defer_loading） | 全定義を事前ロード |
| 中間結果のコンテキスト汚染 | Programmatic Tool Calling / code execution | 全ツール結果をコンテキストに流す |
| パラメータエラー | Tool Use Examples（input_examples） | 自然文で「正しい形式で」と頼む |
| ツールが多すぎる | 役割別エージェント分割 + Tool Search | 1 agent に全ツール付与 |
