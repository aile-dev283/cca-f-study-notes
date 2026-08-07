# CCAR-F Study Notes

**Claude Certified Architect – Foundations（CCAR-F）** 試験対策のノートをまとめたリポジトリ。

[ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) をベースに、Anthropic Skilljar コースのノートと公式ブログの試験対策まとめを追加したもの。

> Anthropicの認定制度は2026年7月に単一の「CCA-F」から **CCAR-F**（Architect – Foundations）・**CCAR-P**（Architect – Professional）・**CCAO-F**（Associate – Foundations）・**CCDV-F**（Developer – Foundations）の4種類に分かれた。本リポジトリは従来どおり **CCAR-F** に特化している。他3種の参考PDFは [`exams/`](exams/README.md) に配置している。

---

## 試験概要

**Claude Certified Architect – Foundations（CCAR-F）**  
公式トップページ: <https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request>

| 項目 | 内容 |
|------|------|
| 対象 | Claudeで本番システムを設計・実装するソリューションアーキテクト（実務経験6ヶ月以上目安） |
| 形式 | 60問・multiple-choice / multiple-response混在・120分・Pearson VUE（オンライン監督 or テストセンター） |
| 合格ライン | 1000点満点中720点 |
| 受験料 | $125（Claude Partner Network 加盟企業は割引あり） |
| 結果通知 | 受験直後（ドメイン別スコアレポート付き） |
| 合格特典 | CCAR-Fバッジ（Credly・LinkedIn共有可） |
| 有効期間 | 認定日から12ヶ月 |
| 再受験 | 1回目不合格後14日、2回目後30日、3回目後90日。ローリング12ヶ月で最大4回 |
| 受験登録 | パートナー企業のメールアドレスが必要（Anthropic Partner Academy経由） |

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

> 詳細は公式 Exam Guide の [Markdown 版](exams/ccar-f/CCAR-F_Certification_Exam_Guide.md)（[日本語訳](exams/ccar-f/CCAR-F_Certification_Exam_Guide.ja.md)・[原本 PDF](exams/ccar-f/_originals/CCAR-F_Certification_Exam_Guide.pdf)（パートナー登録後にダウンロード可））を参照。

---

## 学習コンテンツ

詳細は **[`study/`](study/README.md)** を参照。Exam Guide や受験関連ドキュメントは **[`exams/`](exams/README.md)** を参照。

| フェーズ | 内容 |
|---------|------|
| Phase 0 | オリエンテーション（Claude 101 / Cowork） |
| Phase 1 | 開発基盤（Platform / AI Fluency / Claude API） |
| Phase 2 | MCP & Agentic（MCP intro・advanced・Subagents） |
| Phase 3 | Claude Code（101 / in Action / Agent Skills） |
| Phase 4 | 公式ブログ補強（Agent SDK・Tool Design・Context Engineering・Security・Evals） |

---

## 問題演習トレーナー（`cca-f-trainer` スキル）

`.claude/skills/cca-f-trainer/` に、CCAR-F の問題演習用 Claude Code スキルを同梱している（スキル名は歴史的経緯で `cca-f-trainer` のまま）。
このリポジトリのコーパス（Exam Guide・公式ブログ7本・Skilljarノート11本・docs 148本）に
グラウンディングして**シナリオベースの単一正解問題**を生成し、ブラウザでそのまま解ける**自己完結 HTML**（`quiz.html`）として保存する。

**スキルは「作成」のみを行う**（出題・採点は Claude Code の外＝ブラウザ側で完結する）。
問題生成は重いが、一度 `quiz.html` を作れば何度でも開いて解ける。

- **作成**: コーパスから問題を生成し、`banks/<バンク名>/quiz.html` として保存する。60問の模試なども事前に作り置きできる。
- **出題・採点**: 生成された `quiz.html` をブラウザで開いて自分で解く（サイドバーの進捗・選択直後の正誤ハイライト・解説・最終スコアと誤答一覧つき）。

**特徴:**

- 出題は公式どおりシナリオベース（6原型）。難易度は設計判断を問う L3 を主軸。
- 生成時に**正解キーのセルフチェック**（解説を伏せてコーパスから正解を再導出）を行い、自作問題の「正解が間違っている」リスクを低減。
- ディストラクタは「もっともらしいアンチパターン」を強制（頻出トラップを含む）。
- `quiz.html` は正解・解説を埋め込んだ自己完結アプリ（出題前に正解を隠すファイル分割は行わない。段階的にチャットで出題する経路を廃止した引き換え）。
- 解いた後、画面の「Download Results (JSON)」で結果をダウンロードし、`exams/ccar-f/reports/quiz-results/` に保存すると、
  次にバンクを作るとき「弱点ターゲット」focus でそのフォルダ内の全結果を自動集計し、間隔反復的に弱点へ出題を寄せる。

### 使い方

1. **リポジトリをローカルに配置する**
   ```bash
   git clone https://github.com/aile-dev283/cca-f-study-notes.git
   cd cca-f-study-notes
   ```

2. **Claude Code でフォルダを開く**
  - **Claude Desktop（Claude Code / Cowork）の場合**: 「フォルダを開く」でクローン／解凍したフォルダを選択する
  - **CUI（Claude Code）の場合**: ターミナルでそのフォルダに移動し `claude` を実行する

3. **スキルを起動する**
  - チャット欄で `/cca-f-trainer` を実行する
  - もしくは「CCAR-F の模試を作って」「D2 集中で10問作成」「弱点復習用に10問」など自然文で指示する
  - 未完のバンクがあれば自動で再開確認される。無ければそのまま作成設定の質問から始まる

4. **問題を作成する**
  - **問題数**（10/20/60フル模試）・**focus**（ドメイン横断／特定ドメイン集中／弱点ターゲット）・**HTML の言語**（英語のみ／英語の設問＋日本語解説／日本語）を選ぶ
  - `banks/<バンク名>/quiz.html` に保存される（例 `mock-60-2026-06-20`）。60問など大きいバンクはバッチ生成され、途中で止めても次回続きから作れる

5. **問題を解く**
  - `banks/<バンク名>/quiz.html` をブラウザでそのまま開く（ダブルクリックで開ける自己完結ファイル）
  - 選択直後に正誤と解説が出る。最後まで進んだら「Finish & Review」で素点と誤答一覧を確認できる
  - ダウンロードボタンが2つある
    - **Download Results (JSON)** — `exams/ccar-f/reports/quiz-results/` に保存すると次回の弱点ターゲット生成に自動集計される（簡素なコード形式）
    - **Download for AI Analysis (Markdown)** — 全問の設問・選択肢・自分の回答・正解・解説を人が読める形でまとめたファイル。このチャットや他の AI チャットにそのまま貼って「弱点と次の復習先を分析して」のように使える

### 出力先

- 問題バンク: `.claude/skills/cca-f-trainer/banks/<バンク名>/`（`manifest.json`・`quiz.html`）
  → **Git 管理対象**（チームで共有・再利用できる）
- 演習結果: `exams/ccar-f/reports/quiz-results/<バンク名>-results-<タイムスタンプ>.json`（`quiz.html` からダウンロードして手動配置）

※ 演習結果は個人の学習記録のため Git 管理対象外（`exams/ccar-f/reports/.gitignore`）。問題バンクのみ共有用にコミットされる。

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

`study/` と `exams/` は upstream に存在しないため、通常はコンフリクトしない。

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
- `study/`・`exams/` の試験対策ノートは Anthropic Skilljar・Anthropic 公式ブログ・Anthropic Certification Program Exam Guide を出典とする
