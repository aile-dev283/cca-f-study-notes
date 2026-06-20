# S1: Customer Support Resolution Agent (D1+D2)

エージェントループ + MCP ツール統合。2ファイルの対比が学習の核心。

## 実行

```bash
# sandbox/ から実行
uv run python s1-customer-support/01_agent_basic.py    # inline tools
uv run python s1-customer-support/02_agent_mcp.py      # MCP tools（要: mcp-lab step 実施後）
```

## ファイル対比

| | 01_agent_basic.py | 02_agent_mcp.py |
|--|------------------|-----------------|
| ツール定義 | Python dict（inline） | MCP サーバーから取得 |
| ツール実行 | 直接関数呼び出し | `session.call_tool()` |
| エージェントループ | **同じ** | **同じ** |

→ この対比が「なぜ MCP か」（D2 の核心）を体感させる。

## スタブデータ

- Customer: `CUST-4471` (Jane Doe, gold tier), `CUST-1001` (Bob Smith)
- Order: `ORD-88421` (Laptop Stand, $89.99, delivered)

## 試験で問われる判断ポイント

- エスカレーション条件をシステムプロンプトで制御する設計
- エージェントループの終了条件 (`stop_reason == "end_turn"` vs タイムアウト)
- MCP でツールを外部化するメリット: サーバー・クライアント間の実装分離
