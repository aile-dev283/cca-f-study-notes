<!-- markdownlint-disable -->

# CCA-F 学習コース一覧

全コースのレッスン内容を取得・Markdown化したもの。  
ソース: <https://anthropic.skilljar.com/>

このディレクトリは日本語版です。原文ファイルは一つ上の階層にあります。  
各コースファイルは全文訳ではなく、試験対策向けに要点を圧縮した学習用サマリーです。

---

## 試験概要（公式情報）

**Claude Certified Architect - Foundations（CCA-F）**  
公式トップページ: <https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request>

| 項目 | 内容 |
|------|------|
| 対象 | Anthropic パートナー企業の技術者（おおむね 301 レベルまで） |
| 形式 | 60問・4択・120分・プロクター監視（ProctorFree） |
| 合格ライン | 1000点満点中720点（目安: Practice Exam で 900+/1000） |
| 受験料 | $99（Claude Partner Network 加盟企業は割引あり） |
| 結果通知 | 受験から2営業日以内（ドメイン別スコアレポート付き） |
| 合格特典 | CCA-F バッジ（LinkedIn 共有可） |
| 試験回数 | 1回のみ（再受験不可） |
| 受験登録 | パートナー企業のメールアドレスが必要 |

**前提条件（公式）:**

- Skilljar の 200 レベルコースをすべて完了していること
- Agent SDK・Claude Code・Anthropic API・MCP での実装経験があること

---

## ドメイン別出題割合（公式）

| ドメイン | 内容 | 割合 |
|---------|------|------|
| D1 | Agentic Architecture & Orchestration | **27%** |
| D2 | Tool Design & MCP Integration | **18%** |
| D3 | Claude Code Configuration & Workflows | **20%** |
| D4 | Prompt Engineering & Structured Output | **20%** |
| D5 | Context Management & Reliability | **15%** |

> 公式ページ（2026年6月時点）より。

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

### Phase 0 - オリエンテーション（約2時間）

Claude をエンドユーザー目線で理解する。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 1 | [Claude 101](https://anthropic.skilljar.com/claude-101) | 14 | D4 | [phase0-01-claude-101.md](phase0-01-claude-101.md) |
| 2 | [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork) | 15 | D4 | [phase0-02-claude-cowork.md](phase0-02-claude-cowork.md) |

### Phase 1 - 開発基盤（約12〜14時間）

Claude プラットフォームの全体像、AI Fluency、API 詳細の順に学ぶ。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 3 | [Claude Platform 101](https://anthropic.skilljar.com/claude-platform-101) | 14 | D1, D4, D5 | [phase1-01-claude-platform-101.md](phase1-01-claude-platform-101.md) |
| 4 | [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | 15 | D4, D5 | [phase1-02-ai-fluency.md](phase1-02-ai-fluency.md) |
| 5 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 85 | D1, D4, D5 | [phase1-03-building-with-api.md](phase1-03-building-with-api.md) |

### Phase 2 - MCP & Agentic（約8〜10時間）

D1（27%）と D2（18%）で合計45%。最重要フェーズ。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 6 | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | 14 | D2 | [phase2-01-mcp-intro.md](phase2-01-mcp-intro.md) |
| 7 | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | 15 | D2 | [phase2-02-mcp-advanced.md](phase2-02-mcp-advanced.md) |
| 8 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | 4 | D1 | [phase2-03-subagents-intro.md](phase2-03-subagents-intro.md) |

### Phase 3 - Claude Code（約3〜5時間）

公式定義や出題範囲と照合する。

| # | コース | レッスン数 | ドメイン | ファイル |
|---|--------|-----------|---------|--------|
| 9 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | 13 | D3 | [phase3-01-claude-code-101.md](phase3-01-claude-code-101.md) |
| 10 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | 21 | D3 | [phase3-02-claude-code-action.md](phase3-02-claude-code-action.md) |
| 11 | [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | 6 | D3 | [phase3-03-agent-skills.md](phase3-03-agent-skills.md) |

---

## 合計: 11コース・216レッスン

| Phase | コース数 | レッスン数 |
|-------|---------|-----------|
| Phase 0 | 2 | 29 |
| Phase 1 | 3 | 114 |
| Phase 2 | 3 | 33 |
| Phase 3 | 3 | 40 |
| **合計** | **11** | **216** |

---

## ドメイン別タスクステートメント詳細（公式 Exam Guide より）

### D1: Agentic Architecture & Orchestration（27%）

| # | タスクステートメント |
|---|-------------------|
| 1.1 | 自律的なタスク実行のための agentic loop を設計・実装する |
| 1.2 | coordinator-subagent パターンでマルチエージェントシステムをオーケストレーションする |
| 1.3 | subagent の呼び出し、コンテキスト受け渡し、生成を設定する |
| 1.4 | enforcement と handoff パターンを使って複数ステップのワークフローを実装する |
| 1.5 | Agent SDK hooks を適用してツール呼び出しの介入やデータ正規化を行う |
| 1.6 | 複雑なワークフロー向けのタスク分解戦略を設計する |
| 1.7 | session state、resumption、forking を管理する |

**主要論点:**

- Agentic loop のライフサイクル: `stop_reason` が `"tool_use"` なら継続、`"end_turn"` なら終了。
- Hub-and-spoke アーキテクチャでは、コーディネーターがサブエージェント間通信、エラー処理、情報ルーティングを管理する。
- サブエージェントはコーディネーターのコンテキストを自動継承しないため、必要な情報をプロンプトで明示的に渡す。
- `Task` ツールがサブエージェント生成の入口になる。コーディネーターの `allowedTools` に `"Task"` が必要。
- プロンプトだけの指示より、フックや前提条件ゲートによるプログラム的 enforcement の方が信頼性が高い。

### D2: Tool Design & MCP Integration（18%）

| # | タスクステートメント |
|---|-------------------|
| 2.1 | 明確な説明と境界を持つ効果的なツールインターフェイスを設計する |
| 2.2 | MCP ツールの構造化エラーレスポンスを実装する |
| 2.3 | ツールをエージェント間に適切に配分し、tool choice を設定する |
| 2.4 | MCP サーバーを Claude Code とエージェントワークフローに統合する |
| 2.5 | Read、Write、Edit、Bash、Grep、Glob などの組み込みツールを効果的に選択・適用する |

**主要論点:**

- ツール説明文は LLM のツール選択に大きく影響する。曖昧な説明は誤ルーティングの原因になる。
- MCP の `isError`、`errorCategory`、`isRetryable` で、再試行可能エラーと非再試行エラーを区別する。
- 1つのエージェントに過剰なツールを与えると選択信頼性が下がる。
- `.mcp.json` の環境変数展開（`${GITHUB_TOKEN}`）でシークレットのコミットを避ける。
- Resources は探索的なツール呼び出しを減らすためのコンテンツカタログとして機能する。

### D3: Claude Code Configuration & Workflows（20%）

| # | タスクステートメント |
|---|-------------------|
| 3.1 | 階層、スコープ、モジュール性を考慮して CLAUDE.md を設定する |
| 3.2 | カスタムスラッシュコマンドと skills を作成・設定する |
| 3.3 | パス固有ルールを使って条件付きで規約を読み込む |
| 3.4 | plan mode と direct execution の使い分けを判断する |
| 3.5 | iterative refinement により段階的に改善する |
| 3.6 | Claude Code を CI/CD パイプラインに統合する |

**主要論点:**

- CLAUDE.md はユーザーレベル、プロジェクトレベル、ディレクトリレベルで階層化できる。
- `@import` でルールをモジュール化し、`.claude/rules/` でトピック別に分割する。
- スキルの `context: fork` はメインセッションの汚染を避けるために有効。
- plan mode は大規模変更や複数アプローチがある場面、direct execution は明確で小さい変更に向く。
- CI/CD では `-p`（`--print`）や `--output-format json --json-schema` が重要。

### D4: Prompt Engineering & Structured Output（20%）

| # | タスクステートメント |
|---|-------------------|
| 4.1 | 明示的な基準を持つプロンプトで精度を高め、false positive を減らす |
| 4.2 | few-shot prompting で出力の一貫性と品質を高める |
| 4.3 | tool use と JSON schemas で構造化出力を強制する |
| 4.4 | 抽出品質のための validation、retry、feedback loop を実装する |
| 4.5 | 効率的な batch processing 戦略を設計する |
| 4.6 | multi-instance / multi-pass review アーキテクチャを設計する |

**主要論点:**

- 「何を抽出するか」だけでなく「何を除外するか」まで明示すると精度が上がる。
- JSON schema や tool use を使うと、パース可能な構造化出力を安定させやすい。
- 抽出タスクでは検証、再試行、フィードバックループを前提に設計する。

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

- progressive summarization では金額、日付、注文番号、顧客の期待値などの具体情報を曖昧にしない。重要な取引事実は `case facts` のような永続ブロックに分離する。
- lost-in-the-middle を避けるため、重要な発見は集約入力の先頭に置き、詳細結果には明示的なセクション見出しを付ける。
- エスカレーション条件は明示する。顧客が人間対応を求めた場合、ポリシーに穴がある場合、意味ある進捗が出ない場合は human-in-the-loop に送る。
- self-reported confidence や感情だけをエスカレーション判断に使わない。複数候補が返った場合は推測で選ばず、追加識別子を確認する。
- subagent の失敗は failure type、試した query、partial results、代替案を含む構造化エラーとして coordinator に渡す。空結果とアクセス失敗を区別する。
- 大規模コードベース探索では subagent、scratchpad files、`/compact`、structured state manifest を使って探索結果を維持する。
- 抽出タスクでは field-level confidence を labeled validation set で校正し、document type と field ごとに精度を確認してから自動化範囲を広げる。
- synthesis では claim-source mapping、publication/data collection date、conflicting values を保持し、確立した発見と contested findings を分けて書く。
