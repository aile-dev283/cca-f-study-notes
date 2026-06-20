# MCP Lab: 全プリミティブの実験場 (D2)

MCP の6つのプリミティブを1つずつ動かして体感する。

## 実行順序

```bash
# sandbox/ から実行

# --- Basic: 基本3プリミティブ ---
uv run python mcp-lab/basic/01_tools/client.py
uv run python mcp-lab/basic/02_resources/client.py
uv run python mcp-lab/basic/03_prompts/client.py

# MCP Inspector（ブラウザで試す）
uv run mcp dev mcp-lab/basic/01_tools/server.py

# --- Advanced: 応用3プリミティブ ---
uv run python mcp-lab/advanced/04_sampling/client.py      # Anthropic API キー必要
uv run python mcp-lab/advanced/05_log_progress/client.py
uv run python mcp-lab/advanced/06_roots/client.py
```

## プリミティブ一覧

| # | プリミティブ | 概要 | 方向 |
|---|------------|------|------|
| 01 | **Tools** | 関数呼び出し。エージェントがアクションを実行する | Client → Server |
| 02 | **Resources** | データ/ファイルを URI で公開する | Server → Client |
| 03 | **Prompts** | 再利用可能なプロンプトテンプレート | Server → Client |
| 04 | **Sampling** | サーバーがクライアントに LLM 呼び出しを委譲する | Server → Client → LLM |
| 05 | **Log/Progress** | 長時間処理の進捗をリアルタイム通知 | Server → Client |
| 06 | **Roots** | クライアントが許可するファイルシステム境界を宣言 | Client → Server |

## 試験で問われる判断ポイント

- Tools vs Resources: アクション（副作用あり）vs 参照（副作用なし）の使い分け
- Sampling が有用なケース: 公開 MCP サーバー（サーバーが API キーを持たない設計）
- Roots のセキュリティ: `is_path_allowed()` を SDK が自動強制しない点（自分で実装が必要）
