# CCA-F Sandbox

CCA-F 試験対策の実習環境。Anthropic API・MCP・マルチエージェントの各シナリオを実際に動かす。

## セットアップ（初回のみ）

```bash
cd sandbox
cp .env.example .env        # .env を開いて ANTHROPIC_API_KEY=sk-ant-... を設定
uv sync                     # .venv/ が作られる
```

## 実行方法（sandbox/ ディレクトリから）

```bash
uv run python s6-structured-extraction/01_basic.py
uv run python mcp-lab/basic/01_tools/client.py

# MCP Inspector（ブラウザで Tools/Resources/Prompts を試す）
uv run mcp dev mcp-lab/basic/01_tools/server.py
```

## 実習ステップ

| Step | ディレクトリ | 内容 | 試験ドメイン |
|------|------------|------|------------|
| 1 | s6-structured-extraction/01_basic.py | tool_use + JSON スキーマ抽出 | D4 |
| 2 | s6-structured-extraction/02_retry.py | Pydantic validation + retry ループ | D4 |
| 3 | s1-customer-support/01_agent_basic.py | inline tool エージェントループ | D1+D2 |
| 4 | mcp-lab/basic/01_tools/ | MCP Tools プリミティブ | D2 |
| 5 | mcp-lab/basic/02_resources/ | MCP Resources プリミティブ | D2 |
| 6 | mcp-lab/basic/03_prompts/ | MCP Prompts プリミティブ | D2 |
| 7 | mcp-lab/advanced/04_sampling/ | Sampling（LLM呼び出し委譲） | D2応用 |
| 8 | mcp-lab/advanced/05_log_progress/ | Log & Progress 通知 | D2応用 |
| 9 | mcp-lab/advanced/06_roots/ | Roots（アクセス境界制御） | D2応用 |
| 10 | s1-customer-support/02_agent_mcp.py | MCP 経由エージェント（Step3と対比） | D1+D2 |
| 11 | s3-multi-agent/coordinator.py | Pure API オーケストレーター | D1 |
| 12 | s2s4-claude-code-config/ | CLAUDE.md + slash commands | D3 |

## ディレクトリ構成

```
sandbox/
├── shared/                     共通クライアント factory
├── s6-structured-extraction/   D4: tool_use で JSON 抽出
├── s1-customer-support/        D1+D2: エージェントループ (inline → MCP)
├── mcp-lab/
│   ├── basic/                  MCP 基本3プリミティブ
│   └── advanced/               MCP 応用3プリミティブ
├── s3-multi-agent/             D1: オーケストレーター + サブエージェント
└── s2s4-claude-code-config/    D3: Claude Code 設定演習
```
