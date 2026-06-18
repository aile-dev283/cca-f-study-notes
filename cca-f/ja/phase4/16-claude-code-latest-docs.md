<!-- markdownlint-disable -->

# Claude Code 最新 Docs 補強：Memory / Rules / Skills / Hooks / Subagents

**参照ドキュメント（フォーク内 docs/ に収録済み）:**
- `docs/memory.md` — <https://docs.anthropic.com/en/docs/claude-code/memory>
- `docs/skills.md` — <https://docs.anthropic.com/en/docs/claude-code/skills>
- `docs/hooks.md` / `docs/hooks-guide.md` — <https://docs.anthropic.com/en/docs/claude-code/hooks>
- `docs/sub-agents.md` — <https://docs.anthropic.com/en/docs/claude-code/sub-agents>
- `docs/features-overview.md`

**対応ドメイン:** D3 / D1  
**優先度:** S

---

## Claude Code 設定要素の全体像

| 要素 | スコープ | 読み込みタイミング | 主な用途 |
|------|---------|----------------|---------|
| `CLAUDE.md`（ユーザーレベル） | 全プロジェクト | 常時 | ユーザー個人の共通指示 |
| `CLAUDE.md`（プロジェクトレベル） | プロジェクト全体 | 常時 | プロジェクト共通ルール・文脈 |
| `.claude/rules/`（path-scoped） | パス条件付き | 条件マッチ時 | 言語別・ディレクトリ別ルール |
| `Skill`（SKILL.md） | タスク特化 | オンデマンド | 繰り返しワークフロー・手順 |
| `Hook` | イベント特化 | 自動実行 | 実行前後の強制・検証 |
| `Subagent` | 独立コンテキスト | 明示的起動 | 専門タスクの分離実行 |
| `Plugin` | 配布単位 | インストール時 | Skills/Agents/Hooks/MCP のパッケージ化 |

---

## CLAUDE.md の階層

```
~/.claude/CLAUDE.md        ← ユーザーレベル（全プロジェクト共通）
<project>/CLAUDE.md        ← プロジェクトレベル
<project>/subdir/CLAUDE.md ← ディレクトリレベル（そのサブディレクトリのみ）
```

- `@import` 構文でファイルをモジュール化
- `.claude/rules/` でトピック別にルールファイルを分割
- `paths` フィールドでグロブパターンによる条件付きルールロード

**内容の指針：**
- 毎回必要なプロジェクト共通知識を短くまとめる
- 手順書化して肥大化したら Skill に切り出す
- 個人設定（ユーザーレベル）とプロジェクト設定を混在させない

---

## Skills（SKILL.md）

### 基本構造
```markdown
---
name: pr-review
description: Review a pull request for correctness and style
---

# PR Review Skill
[手順の詳細...]
```

- **name** と **description** が必須のフロントマター
- Claude が description でスキルとリクエストをマッチングして自動活用
- **Personal skills**：`~/.claude/skills/` → 全プロジェクトで利用可能
- **Project skills**：`.claude/skills/` → リポジトリと共有

### 読み込みタイミング
- CLAUDE.md（常時）とは異なり、**タスク特化でオンデマンド**
- スラッシュコマンドとは異なり、**明示的起動不要で自動活用**

### フロントマターオプション

| オプション | 説明 |
|----------|------|
| `context: fork` | フォーク済みサブエージェントとして実行（メインセッション汚染防止） |
| `allowed-tools` | スキル実行中のツールアクセスを制限 |
| `argument-hint` | 引数プロンプト |

### スラッシュコマンドとの関係
- `.claude/commands/deploy.md` と `.claude/skills/deploy/SKILL.md` はどちらも `/deploy` として機能
- カスタムコマンドは Skills に統合されつつある

---

## Hooks

### 概要
Claude Code のライフサイクル上の特定イベントで自動実行される：
- Shell command
- HTTP endpoint
- LLM prompt

### フック種別

| フック | タイミング |
|-------|---------|
| `PreToolUse` | ツール実行前（ブロック・変換が可能） |
| `PostToolUse` | ツール実行後（結果変換・ログ記録） |
| `Stop` | Claude が停止する前 |
| `Notification` | Claude が通知を送る前 |

### 主な用途
- フォーマット強制（lint、format）
- コマンドバリデーション（危険コマンドのブロック）
- プロジェクトルールの強制
- 通知・ログ記録

### 試験上の重要ポイント

> **Hooks = プロンプトで守れないルールをプログラム的に守る手段**

- `PostToolUse` フックでツール結果を変換（データ形式正規化、ポリシー違反ブロック）
- プロンプトベースの指示は非ゼロ失敗率。強制したいルールは Hook で実装

---

## Subagents（サブエージェント）

### 特徴
- **独立コンテキスト**で専門タスクを実行
- メインセッションのコンテキストを汚染しない
- `Task` ツールが生成の入口。コーディネーターの `allowedTools` に `"Task"` が必要

### 設計原則
- コーディネーターのコンテキストを自動継承しない → **必要な文脈だけを明示的に渡す**
- 失敗時は failure type・試した query・partial results・代替案を含む構造化エラーを coordinator に渡す
- 空結果とアクセス失敗を区別して返す

### Explore サブエージェント（Claude Code 固有）
- 詳細な発見フェーズをアイソレート → メインコンテキストを保護
- 大規模コードベース調査に有効

---

## Plan Mode

| 適用場面 | 説明 |
|---------|------|
| 大規模変更 | 多ファイル影響がある変更 |
| 複数有効アプローチ | 実装方法の選択が必要 |
| アーキテクチャ決定 | 影響範囲調査が必要 |
| 不明瞭な要件 | 実装前に計画の承認が必要 |

**直接実行**：明確なスコープの単純変更（単一バグ修正・単一バリデーション追加等）

起動：`claude --permission-mode plan` または `Shift+Tab`

---

## CI/CD 統合

- `-p`（`--print`）フラグで非インタラクティブモード起動
- `--output-format json --json-schema` で構造化出力
- **セッションコンテキスト分離**：同一セッションによる自己レビューは独立したレビューインスタンスより効果が低い
- CI では別セッション・別パスでのレビューが推奨

---

## 設定場所の使い分け（試験頻出）

| 何を実現したいか | 正しい設定場所 |
|---------------|-------------|
| 全プロジェクト共通の個人設定 | `~/.claude/CLAUDE.md` |
| プロジェクト共通ルール | `CLAUDE.md`（プロジェクトルート） |
| 言語別・ディレクトリ別ルール | `.claude/rules/`（paths フィールド） |
| 繰り返しワークフロー | `.claude/skills/` の SKILL.md |
| 強制したい安全ルール | Hooks（PreToolUse / PostToolUse） |
| 専門タスクの分離 | Subagent |
| チームへの配布 | Plugin |
