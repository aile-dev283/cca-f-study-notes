<!-- markdownlint-disable -->

# CCA-F 学習コース一覧

Anthropic Skilljar の全コースおよび公式ブログの試験対策まとめ。  
試験概要・ドメイン構成・出題シナリオは [リポジトリ直下の README](../README.md) を参照。

直下に日本語版を正として配置し、英語原文は `_originals/` 配下に同じ構成で置いている（`_` 接頭は「補助・参照用」を表す）。

| ディレクトリ | 出典 | 対応フェーズ |
|------------|------|------------|
| [`skilljar-courses/`](skilljar-courses/) | Anthropic Skilljar コース（日本語） | Phase 0〜3 |
| [`official-blog/`](official-blog/) | Anthropic 公式ブログ／Docs（日本語） | Phase 4 |
| [`_originals/`](_originals/) | 上記各ファイルの英語原文（補助） | — |

公式の試験ガイド原本（PDF）も `_originals/` に置いている: [`CCA-F_Certification_Exam_Guide.pdf`](_originals/CCA-F_Certification_Exam_Guide.pdf)（パートナー登録後にダウンロード可）。

---

## フェーズ別コース一覧

### Phase 0 — オリエンテーション

Claudeをエンドユーザー目線で把握する。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Claude 101](https://anthropic.skilljar.com/claude-101) | 14 | D4 | [phase0-01-claude-101.md](skilljar-courses/phase0-01-claude-101.md) |
| 2 | [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork) | 15 | D4 | [phase0-02-claude-cowork.md](skilljar-courses/phase0-02-claude-cowork.md) |

### Phase 1 — 開発基盤

Claudeプラットフォームの全体像→思考フレームワーク→API詳細の順に習得。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Claude Platform 101](https://anthropic.skilljar.com/claude-platform-101) | 14 | D1, D4, D5 | [phase1-01-claude-platform-101.md](skilljar-courses/phase1-01-claude-platform-101.md) |
| 2 | [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | 15 | D4, D5 | [phase1-02-ai-fluency.md](skilljar-courses/phase1-02-ai-fluency.md) |
| 3 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 85 | D1, D4, D5 | [phase1-03-building-with-api.md](skilljar-courses/phase1-03-building-with-api.md) |

### Phase 2 — MCP & Agentic

D1（27%）＋ D2（18%）で合計45%。最重要フェーズ。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | 14 | D2 | [phase2-01-mcp-intro.md](skilljar-courses/phase2-01-mcp-intro.md) |
| 2 | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | 15 | D2 | [phase2-02-mcp-advanced.md](skilljar-courses/phase2-02-mcp-advanced.md) |
| 3 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | 4 | D1 | [phase2-03-subagents-intro.md](skilljar-courses/phase2-03-subagents-intro.md) |

### Phase 3 — Claude Code

公式定義と出題範囲の照合が主目的。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | 13 | D3 | [phase3-01-claude-code-101.md](skilljar-courses/phase3-01-claude-code-101.md) |
| 2 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | 21 | D3 | [phase3-02-claude-code-action.md](skilljar-courses/phase3-02-claude-code-action.md) |
| 3 | [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | 6 | D3 | [phase3-03-agent-skills.md](skilljar-courses/phase3-03-agent-skills.md) |

### Phase 4 — 公式ブログ補強

コースでは手薄な4領域（最新 Agent SDK 設計・大量 MCP ツール時代の Tool Design・Context Engineering・安全設計）を補強する。

| # | 内容 | 対応ドメイン | 優先度 | ファイル |
|---|------|------------|--------|--------|
| 1 | [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | D1/D3/D5 | S | [official-blog/01-building-agents-with-sdk.md](official-blog/01-building-agents-with-sdk.md) |
| 2 | [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | D2/D4 | S | [official-blog/02-writing-effective-tools.md](official-blog/02-writing-effective-tools.md) |
| 3 | [Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp) | D2/D5 | S | [official-blog/03-code-execution-mcp-advanced-tool-use.md](official-blog/03-code-execution-mcp-advanced-tool-use.md) |
| 4 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | D5 | S | [official-blog/04-context-engineering-and-management.md](official-blog/04-context-engineering-and-management.md) |
| 5 | [How we built Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | D3/D5 | A | [official-blog/05-auto-mode-and-security.md](official-blog/05-auto-mode-and-security.md) |
| 6 | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | D4/D5 | A | [official-blog/06-demystifying-evals.md](official-blog/06-demystifying-evals.md) |
| 7 | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | D1/D5/D3 | A/B | [official-blog/07-effective-harnesses-and-agent-skills.md](official-blog/07-effective-harnesses-and-agent-skills.md) |

---

## ドメイン別タスクステートメント詳細（[公式 Exam Guide](_originals/CCA-F_Certification_Exam_Guide.pdf) より）

### D1: Agentic Architecture & Orchestration（27%）

| # | タスクステートメント |
|---|-------------------|
| 1.1 | Design and implement agentic loops for autonomous task execution |
| 1.2 | Orchestrate multi-agent systems with coordinator-subagent patterns |
| 1.3 | Configure subagent invocation, context passing, and spawning |
| 1.4 | Implement multi-step workflows with enforcement and handoff patterns |
| 1.5 | Apply Agent SDK hooks for tool call interception and data normalization |
| 1.6 | Design task decomposition strategies for complex workflows |
| 1.7 | Manage session state, resumption, and forking |

**主要論点:**

- Agentic ループのライフサイクル: `stop_reason` が `"tool_use"` → ループ継続、`"end_turn"` → 終了
- Hub-and-spoke アーキテクチャ: コーディネーターが全サブエージェント通信・エラー処理・情報ルーティングを管理
- サブエージェントはコーディネーターのコンテキストを自動継承しない（プロンプトに明示的に渡す必要あり）
- `Task` ツールがサブエージェントを生成する機構。コーディネーターの `allowedTools` に `"Task"` が必要
- `AgentDefinition` 設定: descriptions・system prompts・tool restrictions
- `PostToolUse` フックでツール結果を変換（データ形式正規化、ポリシー違反ブロック等）
- プログラム的エンフォースメント（フック・前提条件ゲート）vs プロンプトベースの指示（非ゼロ失敗率）
- `--resume <session-name>` で名前付きセッション継続、`fork_session` で分岐アプローチ探索
- 固定シーケンシャルパイプライン（プロンプトチェーン）vs 中間発見に基づく動的適応型分解

---

### D2: Tool Design & MCP Integration（18%）

| # | タスクステートメント |
|---|-------------------|
| 2.1 | Design effective tool interfaces with clear descriptions and boundaries |
| 2.2 | Implement structured error responses for MCP tools |
| 2.3 | Distribute tools appropriately across agents and configure tool choice |
| 2.4 | Integrate MCP servers into Claude Code and agent workflows |
| 2.5 | Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively |

**主要論点:**

- ツール説明文がLLMのツール選択の主要メカニズム。曖昧な説明はミスルーティングを招く
- MCP の `isError` フラグパターン: `errorCategory`（transient/validation/permission）・`isRetryable` boolean
- リトライ可能エラー vs 非リトライエラーの区別（generic "Operation failed" は不適切）
- エージェントへのツール過多（例: 18個 vs 4-5個）は選択信頼性を低下させる
- `tool_choice` 設定: `"auto"` / `"any"` / 強制選択 `{"type": "tool", "name": "..."}`
- MCP サーバースコープ: プロジェクトレベル（`.mcp.json`）vs ユーザーレベル（`~/.claude.json`）
- `.mcp.json` での環境変数展開（`${GITHUB_TOKEN}`）によるシークレットのコミット回避
- MCP Resources: コンテンツカタログをエージェントに公開し、探索的ツール呼び出しを削減
- Grep（コンテンツ検索）/ Glob（ファイルパスパターンマッチング）/ Read・Write vs Edit（ユニークテキスト一致）の使い分け

---

### D3: Claude Code Configuration & Workflows（20%）

| # | タスクステートメント |
|---|-------------------|
| 3.1 | Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization |
| 3.2 | Create and configure custom slash commands and skills |
| 3.3 | Apply path-specific rules for conditional convention loading |
| 3.4 | Determine when to use plan mode vs direct execution |
| 3.5 | Apply iterative refinement techniques for progressive improvement |
| 3.6 | Integrate Claude Code into CI/CD pipelines |

**主要論点:**

- CLAUDE.md 階層: ユーザーレベル（`~/.claude/CLAUDE.md`）→ プロジェクトレベル（`CLAUDE.md`）→ ディレクトリレベル
- `@import` 構文でファイルをモジュール化。`.claude/rules/` でトピック別ルールファイルを分割
- プロジェクトスコープのスラッシュコマンド（`.claude/commands/`）vs ユーザースコープ（`~/.claude/commands/`）
- スキルの `context: fork` フロントマターでスキルをフォーク済みサブエージェントとして実行（メインセッション汚染防止）
- `allowed-tools` でスキル実行中のツールアクセスを制限、`argument-hint` で引数プロンプト
- `.claude/rules/` の `paths` フィールドでグロブパターンによる条件付きルールロード
- プランモード適用場面: 大規模変更・複数有効アプローチ・アーキテクチャ決定・マルチファイル変更
- 直接実行適用場面: 明確なスコープの単純変更（単一バグ修正・単一バリデーション追加等）
- Explore サブエージェントで詳細な発見フェーズをアイソレート→メインコンテキストを保護
- CI/CD での `-p`（`--print`）フラグで非インタラクティブモード起動、`--output-format json --json-schema` で構造化出力
- セッションコンテキスト分離: 同一セッションによる自己レビューは独立したレビューインスタンスより効果が低い

---

### D4: Prompt Engineering & Structured Output（20%）

| # | タスクステートメント |
|---|-------------------|
| 4.1 | Design prompts with explicit criteria to improve precision and reduce false positives |
| 4.2 | Apply few-shot prompting to improve output consistency and quality |
| 4.3 | Enforce structured output using tool use and JSON schemas |
| 4.4 | Implement validation, retry, and feedback loops for extraction quality |
| 4.5 | Design efficient batch processing strategies |
| 4.6 | Design multi-instance and multi-pass review architectures |

**主要論点:**

- 明示的基準 vs 曖昧な指示（「保守的に」は精度を改善しない、具体的カテゴリ基準が有効）
- Few-shot例: 詳細な指示だけでは不一致が生じる場合に最も効果的。2-4個の標的例で判断を一般化
- `tool_use` + JSON スキーマが構造化出力の最も信頼できるアプローチ（JSONシンタックスエラーを排除）
- ただし JSON スキーマはシンタックスエラーを排除するが、セマンティックエラーは防げない（値の不一致など）
- Retry-with-error-feedback: バリデーションエラーをプロンプトに追記して再試行
- リトライが無効な場合: 必要情報がソース文書にそもそも存在しない場合
- Message Batches API: コスト50%削減・最大24時間処理ウィンドウ・保証されたレイテンシSLAなし
- バッチ処理適用: 非ブロッキング・レイテンシ許容ワークロード（overnight reports / weekly audits）
- バッチ処理不適切: ブロッキングワークフロー（pre-merge checks）
- 自己レビューの限界: 生成時の推論コンテキストを保持するため、自分の決定に疑問を持ちにくい
- マルチパスレビュー: ファイル単位のローカル分析パス + クロスファイル統合パスで注意希薄化を防止

---

### D5: Context Management & Reliability（15%）

| # | タスクステートメント |
|---|-------------------|
| 5.1 | 長いやり取りの中で重要情報を失わないよう会話コンテキストを管理する |
| 5.2 | 効果的なエスカレーションと曖昧性解消パターンを設計する |
| 5.3 | マルチエージェントシステム全体のエラー伝播戦略を実装する |
| 5.4 | 大規模コードベース探索でコンテキストを効果的に管理する |
| 5.5 | human review workflow と confidence calibration を設計する |
| 5.6 | マルチソース統合で情報の provenance と不確実性を保持する |

**主要論点:**

- progressive summarization では金額、日付、注文番号、顧客の期待値などの具体情報を曖昧にしない。重要な取引事実は `case facts` のような永続ブロックに分離する
- lost-in-the-middle を避けるため、重要な発見は集約入力の先頭に置き、詳細結果には明示的なセクション見出しを付ける
- エスカレーション条件は明示する。顧客が人間対応を求めた場合、ポリシーに穴がある場合、意味ある進捗が出ない場合は human-in-the-loop に送る
- self-reported confidence や感情だけをエスカレーション判断に使わない。複数候補が返った場合は推測で選ばず、追加識別子を確認する
- subagent の失敗は failure type、試した query、partial results、代替案を含む構造化エラーとして coordinator に渡す。空結果とアクセス失敗を区別する
- 大規模コードベース探索では subagent、scratchpad files、`/compact`、structured state manifest を使って探索結果を維持する
- 抽出タスクでは field-level confidence を labeled validation set で校正し、document type と field ごとに精度を確認してから自動化範囲を広げる
- synthesis では claim-source mapping、publication/data collection date、conflicting values を保持し、確立した発見と contested findings を分けて書く
