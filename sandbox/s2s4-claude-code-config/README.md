# S2/S4: Claude Code Configuration (D3)

CLAUDE.md とカスタムスラッシュコマンドによる Claude Code のカスタマイズを学ぶ。

## 試し方

このディレクトリを Claude Code で開く:

```bash
cd sandbox/s2s4-claude-code-config
claude  # または Claude Desktop でこのフォルダを開く
```

## ファイル構成

| ファイル | 種別 | 説明 |
|---------|------|------|
| `CLAUDE.md` | プロジェクト設定 | チーム規約・Claude への指示・禁止事項 |
| `.claude/commands/refactor.md` | スラッシュコマンド | `/refactor <file>` でリファクタリング |
| `.claude/commands/explain-legacy.md` | スラッシュコマンド | `/explain-legacy <file>` でコード解説 |

## 試験で問われる判断ポイント

| 機能 | 使いどころ |
|------|----------|
| `CLAUDE.md` | すべての会話に適用したい**常時**の規約・指示 |
| スラッシュコマンド | 特定タスク時に**明示的に**呼び出したい手順 |
| スキル（`.claude/skills/`）| Claude が**自動で**認識してほしい専門知識 |
| サブエージェント（`.claude/agents/`）| 独立したコンテキストで**委任**したいタスク |

## CLAUDE.md 階層のルール

```
~/.claude/CLAUDE.md          ← 全プロジェクト共通（個人設定）
project/CLAUDE.md            ← このプロジェクト専用
project/subdir/CLAUDE.md     ← サブディレクトリ専用（パス固有ルール）
```

Claude は上位から下位へすべての CLAUDE.md を読み込み、
より具体的なルール（下位）が上位を上書きする。
