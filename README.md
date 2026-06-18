# CCA-F Study Notes

CCA-F（Claude Certified Architect – Foundations）試験対策のノートをまとめたリポジトリ。

[ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) をベースに、Anthropic Skilljar コースのノートと公式ブログの試験対策まとめを追加したもの。

---

## 試験概要

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

- Skilljar の 200 レベルコースをすべて完了していること
- Agent SDK・Claude Code・Anthropic API・MCP での実装経験があること

### ドメイン別出題割合

| ドメイン | 内容 | 割合 |
|---------|------|------|
| D1 | Agentic Architecture & Orchestration | **27%** |
| D2 | Tool Design & MCP Integration | **18%** |
| D3 | Claude Code Configuration & Workflows | **20%** |
| D4 | Prompt Engineering & Structured Output | **20%** |
| D5 | Context Management & Reliability | **15%** |

**各ドメインの詳細:**

- **D1 — Agentic Architecture & Orchestration（27%）**  
  エージェント的ループの設計、コーディネーター・サブエージェントパターンによるマルチエージェントシステムのオーケストレーション、タスク分解の実装、セッション状態とワークフロー強制の管理。
- **D2 — Tool Design & MCP Integration（18%）**  
  明確な境界を持つ効果的なツールインターフェースの設計、構造化されたエラーレスポンスの実装、MCP サーバーの統合、エージェント間での適切なツール分配。
- **D3 — Claude Code Configuration & Workflows（20%）**  
  CLAUDE.md 階層の構成、カスタムスラッシュコマンドの作成、パス固有ルールの適用、プランモードを使うべき場面の判断、CI/CD パイプラインへの統合。
- **D4 — Prompt Engineering & Structured Output（20%）**  
  明示的な基準を持つプロンプトの設計、few-shot 技法の適用、JSON スキーマによる構造化出力の強制、検証とリトライループの実装。
- **D5 — Context Management & Reliability（15%）**  
  長い対話にわたる重要情報の保持、エスカレーションパターンの設計、マルチエージェントシステムにおけるエラー伝播の管理、確信度キャリブレーションによる不確実性への対処。

> ※公式ページ（2026年6月時点）より。

### 出題シナリオ（全6種・本番は4種をランダム抽出）

| # | シナリオ名 | 関連ドメイン |
|---|-----------|------------|
| 1 | Customer Support Resolution Agent | D1・D2・D5 |
| 2 | Code Generation with Claude Code | D3・D5 |
| 3 | Multi-Agent Research System | D1・D2・D5 |
| 4 | Developer Productivity with Claude | D2・D3・D1 |
| 5 | Claude Code for Continuous Integration | D3・D4 |
| 6 | Structured Data Extraction | D4・D5 |

**各シナリオの詳細:**

- **シナリオ1 — Customer Support Resolution Agent**  
  Claude Agent SDK を使って顧客サポートの解決エージェントを構築する。返品、請求の異議、アカウントの問題といった曖昧性の高いリクエストを処理する。カスタム MCP ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じてバックエンドシステムにアクセスできる。目標は、エスカレーションすべきタイミングを見極めつつ、初回接触での解決率 80% 以上を達成すること。  
  関連ドメイン: Agentic Architecture & Orchestration / Tool Design & MCP Integration / Context Management & Reliability
- **シナリオ2 — Code Generation with Claude Code**  
  Claude Code を使ってソフトウェア開発を加速する。チームはコード生成、リファクタリング、デバッグ、ドキュメント作成に利用する。カスタムスラッシュコマンドや CLAUDE.md 設定を用いて開発ワークフローに統合し、プランモードと直接実行をいつ使い分けるかを理解する必要がある。  
  関連ドメイン: Claude Code Configuration & Workflows / Context Management & Reliability
- **シナリオ3 — Multi-Agent Research System**  
  Claude Agent SDK を使ってマルチエージェントのリサーチシステムを構築する。コーディネーターエージェントが専門サブエージェントに委任する：1つは Web を検索し、1つはドキュメントを分析し、1つは調査結果を統合し、1つはレポートを生成する。システムはトピックを調査し、引用付きの包括的なレポートを生成する。  
  関連ドメイン: Agentic Architecture & Orchestration / Tool Design & MCP Integration / Context Management & Reliability
- **シナリオ4 — Developer Productivity with Claude**  
  Claude Agent SDK を使って開発者の生産性向上ツールを構築する。エンジニアが馴染みのないコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復作業を自動化するのを支援する。組み込みツール（Read、Write、Bash、Grep、Glob）を使い、MCP サーバーと統合する。  
  関連ドメイン: Tool Design & MCP Integration / Claude Code Configuration & Workflows / Agentic Architecture & Orchestration
- **シナリオ5 — Claude Code for Continuous Integration**  
  Claude Code を CI/CD パイプラインに統合する。システムは自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを提供する。実行可能なフィードバックを提供し、誤検知（false positive）を最小化するプロンプトを設計する必要がある。  
  関連ドメイン: Claude Code Configuration & Workflows / Prompt Engineering & Structured Output
- **シナリオ6 — Structured Data Extraction**  
  Claude を使って構造化データ抽出システムを構築する。システムは非構造化ドキュメントから情報を抽出し、JSON スキーマで出力を検証し、高い精度を維持する。エッジケースを適切に処理し、下流システムと統合できなければならない。  
  関連ドメイン: Prompt Engineering & Structured Output / Context Management & Reliability

> 詳細は公式 Exam Guide の [Markdown 版](cca-f/CCA-F_Certification_Exam_Guide.md)（[原本 PDF](cca-f/_originals/CCA-F_Certification_Exam_Guide.pdf)・パートナー登録後にダウンロード可）を参照。

---

## 学習コンテンツ

詳細は **[`cca-f/`](cca-f/README.md)** を参照。

| フェーズ | 内容 |
|---------|------|
| Phase 0 | オリエンテーション（Claude 101 / Cowork） |
| Phase 1 | 開発基盤（Platform / AI Fluency / Claude API） |
| Phase 2 | MCP & Agentic（MCP intro・advanced・Subagents） |
| Phase 3 | Claude Code（101 / in Action / Agent Skills） |
| Phase 4 | 公式ブログ補強（Agent SDK・Tool Design・Context Engineering・Security・Evals） |

---

## 問題演習トレーナー（`cca-f-trainer` スキル）

`.claude/skills/cca-f-trainer/` に、CCA-F の問題演習用 Claude Code スキルを同梱している。
このリポジトリのコーパス（Exam Guide・公式ブログ7本・Skilljarノート11本・docs 148本）に
グラウンディングして**シナリオベースの単一正解問題**を生成・出題・採点する。

**特徴:**

- 出題は公式どおりシナリオベース（6原型）。難易度は設計判断を問う L3 を主軸。
- **独立 Evaluator** が正解キーを知らない状態で全問を検品し、出典整合・正解一意性・ディストラクタ妥当性を担保（自作問題の「正解が間違っている」リスクを低減）。
- ディストラクタは「もっともらしいアンチパターン」を強制（頻出トラップを含む）。
- 採点後、ドメイン別正答率・苦手サブドメイン・**リポジトリ内の復習先ファイルパス**・次回推奨モードを1枚のレポートにまとめる。
- セッションを跨いで弱点を蓄積し、**弱点復習モード**で間隔反復的に出題が最適化される。

### 使い方

1. **リポジトリをローカルに配置する**
   ```bash
   git clone https://github.com/aile-dev283/cca-f-study-notes.git
   cd cca-f-study-notes
   ```

2. **Claude Code でフォルダを開く**
  - **Claude Desktop（Claude Code / Cowork）の場合**: 「フォルダを開く」でクローン／解凍したフォルダを選択する
  - **CUI（Claude Code）の場合**: ターミナルでそのフォルダに移動し `claude` を実行する

3. **問題演習を開始する**
  - チャット欄で `/cca-f-trainer` を実行する
  - もしくは「CCA-F の練習問題を出して」「D2 集中で10問」「弱点復習」「模試」など自然文で指示する
  - 起動時に **言語**（英語問題＋日本語解説／英語のみ／日本語のみ）・**問題数**（5/10/20/60）・**出題モード**（横断／ドメイン集中／弱点復習）・**フィードバック**（演習＝1問ずつ即解説／模試＝まとめて一括採点）を選ぶ

### 出力先

- 演習レポート: `cca-f/reports/<YYYY-MM-DD>-session.md`
- 弱点ログ: `cca-f/reports/weakness-log.json`

※ いずれも個人の学習記録のため Git 管理対象外。

---

## Claude Code ドキュメントミラー

`docs/` には [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) 由来の Claude Code 公式ドキュメントミラーが含まれる。GitHub Actions で定期自動更新。

### upstream の更新を手動で取り込む

初回のみ、フォーク元を `upstream` として登録する。

```bash
git remote add upstream https://github.com/ericbuess/claude-code-docs.git
```

以降は以下でフォーク元の更新を取り込む。

```bash
git fetch upstream
git merge upstream/main
git push
```

`cca-f/` は upstream に存在しないため、通常はコンフリクトしない。

### `/docs` コマンドのインストール

```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```

インストール後、Claude Code で以下が使用可能：

```bash
/docs hooks       # hooks ドキュメントを参照
/docs mcp         # MCP ドキュメントを参照
/docs memory      # memory ドキュメントを参照
/docs -t          # 最終更新時刻を確認
/docs what's new  # 最近の更新差分を表示
/docs changelog   # Claude Code リリースノートを参照
```

インストール・アンインストールの詳細は [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) を参照。

---

## ライセンス

- `docs/` 内のドキュメントコンテンツは Anthropic に帰属
- ミラーツール部分（install.sh など）は [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) に帰属
- `cca-f/` の試験対策ノートは Anthropic Skilljar および Anthropic 公式ブログを出典とする
