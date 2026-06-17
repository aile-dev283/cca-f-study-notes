<!-- markdownlint-disable -->

# CCA-F 学習コース一覧

全コースのレッスン内容を取得・Markdown化したもの。  
ソース: <https://anthropic.skilljar.com/>

---

## 試験概要（公式情報）

**Claude Certified Architect – Foundations（CCA-F）**  
公式トップページ: <https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request>

| 項目 | 内容 |
|------|------|
| 対象 | Anthropicパートナー企業の技術者（〜301レベル） |
| 形式 | 60問・4択・120分・プロクター監視（ProctorFree） |
| 合格ライン | 1000点満点中720点（目安：Practice Exam で 900+/1000） |
| 受験料 | $99（Claude Partner Network 加盟企業は割引あり） |
| 結果通知 | 受験から2営業日以内（ドメイン別スコアレポート付き） |
| 合格特典 | CCA-Fバッジ（LinkedIn共有可） |
| 試験回数 | 1回のみ（再受験不可） |
| 受験登録 | パートナー企業のメールアドレスが必要 |

**前提条件（公式）:**

- Skilljarの200レベルコースをすべて完了していること
- Agent SDK・Claude Code・Anthropic API・MCPでの実装経験があること

---

## ドメイン別出題割合（公式）

| ドメイン | 内容 | 割合 |
|---------|------|------|
| D1 | Agentic Architecture & Orchestration | **27%** |
| D2 | Tool Design & MCP Integration | **18%** |
| D3 | Claude Code Configuration & Workflows | **20%** |
| D4 | Prompt Engineering & Structured Output | **20%** |
| D5 | Context Management & Reliability | **15%** |

> ※公式ページ（2026年6月時点）より。

---

## 出題シナリオ（全6種・本番は4種をランダム抽出）

| # | シナリオ名 | 関連ドメイン |
|---|-----------|------------|
| 1 | Customer Support Resolution Agent | D1・D2・D5 |
| 2 | Code Generation with Claude Code | D3・D5 |
| 3 | Multi-Agent Research System | D1・D2・D5 |
| 4 | Developer Productivity with Claude | D2・D3・D1 |
| 5 | Claude Code for Continuous Integration | D3・D4 |
| 6 | Structured Data Extraction | D4・D5 |

> 詳細は公式 Exam Guide PDF（パートナー登録後にダウンロード可）を参照。

---

## フェーズ別コース一覧

### Phase 0 — オリエンテーション（約2時間）

Claudeをエンドユーザー目線で把握する。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Claude 101](https://anthropic.skilljar.com/claude-101) | 14 | D4 | [phase0-01-claude-101.md](phase0-01-claude-101.md) |
| 2 | [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork) | 15 | D4 | [phase0-02-claude-cowork.md](phase0-02-claude-cowork.md) |

### Phase 1 — 開発基盤（約12〜14時間）

Claudeプラットフォームの全体像→思考フレームワーク→API詳細の順に習得。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 3 | [Claude Platform 101](https://anthropic.skilljar.com/claude-platform-101) | 14 | D1, D4, D5 | [phase1-01-claude-platform-101.md](phase1-01-claude-platform-101.md) |
| 4 | [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | 15 | D4, D5 | [phase1-02-ai-fluency.md](phase1-02-ai-fluency.md) |
| 5 | [Building with the Claude API ★](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 85 | D1, D4, D5 | [phase1-03-building-with-api.md](phase1-03-building-with-api.md) |

### Phase 2 — MCP & Agentic（約8〜10時間）

D1（27%）＋ D2（18%）で合計45%。最重要フェーズ。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 6 | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | 14 | D2 | [phase2-01-mcp-intro.md](phase2-01-mcp-intro.md) |
| 7 | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | 15 | D2 | [phase2-02-mcp-advanced.md](phase2-02-mcp-advanced.md) |
| 8 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | 4 | D1 | [phase2-03-subagents-intro.md](phase2-03-subagents-intro.md) |

### Phase 3 — Claude Code（約3〜5時間）

公式定義と出題範囲の照合が主目的。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 9 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | 13 | D3 | [phase3-01-claude-code-101.md](phase3-01-claude-code-101.md) |
| 10 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | 21 | D3 | [phase3-02-claude-code-action.md](phase3-02-claude-code-action.md) |
| 11 | [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | 6 | D3 | [phase3-03-agent-skills.md](phase3-03-agent-skills.md) |

---

### Phase 4 — 公式ブログ補強（約8〜10時間）

コースでは不十分な4領域（最新 Agent SDK 設計・大量 MCP ツール時代の Tool Design・Context Engineering・安全設計）を公式ブログ・Docs で補強する。

| # | 内容 | 対応ドメイン | 優先度 | ファイル |
|---|------|------------|--------|--------|
| 12 | [Building Agents with Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | D1/D3/D5 | S | [12-building-agents-with-sdk.md](phase4/12-building-agents-with-sdk.md) |
| 13 | [Writing Effective Tools for AI Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | D2/D4 | S | [13-writing-effective-tools.md](phase4/13-writing-effective-tools.md) |
| 14 | [Code Execution with MCP + Advanced Tool Use](https://www.anthropic.com/engineering/code-execution-with-mcp) | D2/D5 | S | [14-code-execution-mcp-advanced-tool-use.md](phase4/14-code-execution-mcp-advanced-tool-use.md) |
| 15 | [Effective Context Engineering + Context Management](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | D5 | S | [15-context-engineering-and-management.md](phase4/15-context-engineering-and-management.md) |
| 16 | [Claude Code 最新 Docs 補強（Memory/Rules/Skills/Hooks）](https://docs.anthropic.com/en/docs/claude-code/memory) | D3/D1 | S | [16-claude-code-latest-docs.md](phase4/16-claude-code-latest-docs.md) |
| 17 | [Auto Mode + How We Contain Claude](https://www.anthropic.com/engineering/claude-code-auto-mode) | D3/D5 | A | [17-auto-mode-and-security.md](phase4/17-auto-mode-and-security.md) |
| 18 | [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | D4/D5 | A | [18-demystifying-evals.md](phase4/18-demystifying-evals.md) |
| 19 | [Effective Harnesses for Long-Running Agents + Agent Skills](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | D1/D5/D3 | A/B | [19-effective-harnesses-and-agent-skills.md](phase4/19-effective-harnesses-and-agent-skills.md) |

---

## 合計: 11コース・216レッスン + Phase 4 補強記事

| Phase | コース数 | レッスン数 |
|-------|---------|-----------|
| Phase 0 | 2 | 29 |
| Phase 1 | 3 | 114 |
| Phase 2 | 3 | 33 |
| Phase 3 | 3 | 40 |
| Phase 4 | 8記事 | — |
| **合計** | **11コース + 8記事** | **216** |

---

## ターゲット受験者像（公式）

**ソリューションアーキテクト**として本番アプリケーションを設計・実装する人材。以下の実務経験が前提：

- Claude Agent SDK によるエージェントアプリ構築（マルチエージェント・サブエージェント委譲・ツール統合・ライフサイクルフック）
- CLAUDE.md・Agent Skills・MCP サーバー統合・プランモードを使った Claude Code チームワークフロー設定
- バックエンドシステム統合のための MCP ツール・リソースインターフェース設計
- JSON スキーマ・Few-shot 例・抽出パターンを活用した構造化出力プロンプト設計
- 長文書・マルチターン・マルチエージェントハンドオフにわたるコンテキストウィンドウ管理
- CI/CDパイプラインへのClaudeの統合（自動コードレビュー・テスト生成・PRフィードバック）
- エラーハンドリング・Human-in-the-loop・自己評価パターンを含むエスカレーション設計

> 実務経験目安：Claude APIs・Agent SDK・Claude Code・MCP での構築 **6ヶ月以上**

---

## ドメイン別タスクステートメント詳細（公式 Exam Guide より）

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
