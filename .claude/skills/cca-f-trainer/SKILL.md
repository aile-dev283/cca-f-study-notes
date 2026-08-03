---
name: cca-f-trainer
description: >-
  CCAR-F（Claude Certified Architect – Foundations）試験対策の問題演習トレーナー。
  このリポジトリのコーパス（Exam Guide・公式ブログ7本・Skilljarノート11本・Claude Code docs 148本）に
  グラウンディングしてシナリオベースの単一正解問題を生成し、ブラウザでそのまま解ける自己完結 HTML の問題バンク
  （banks/<name>/quiz.html）として保存する。出題・採点はブラウザ側で完結し、解いた結果は JSON としてダウンロードして
  リポジトリ内の gitignore 済みフォルダに保存すれば、次回の弱点ターゲット生成がそれを読んで弱点を優先出題する。
  ユーザが「CCAR-F」「CCA-F」「練習問題を出して」「模試」「mock exam」「問題演習」「問題を作って／作成」
  「弱点復習」「ドメイン別に出題」「試験対策」「過去問」「クイズして」などと言ったとき、また CCAR-F の特定ドメイン
  （Agentic / MCP / Claude Code / Prompt / Context）の理解度を測りたい・鍛えたいと述べたときは必ずこのスキルを使うこと。
  単発の用語確認ではなく、設計判断を問う本番形式の演習・問題作成を行いたい場面で強くトリガーする。
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, TaskCreate, TaskUpdate
---

# CCAR-F Trainer

CCAR-F 試験対策の問題演習トレーナー（スキル名は歴史的経緯で `cca-f-trainer` のまま）。**自作問題の最大リスクは「正解キーが間違っていること」**なので、
このスキルは「コーパスに根拠を持つ問題だけを、生成時のセルフチェックを通してから」ブラウザ用クイズ HTML として書き出すことを最優先に設計されている。

## このスキルは「作成のみ」を行う

**Claude Code 側で出題・採点は行わない。** 生成した `banks/<name>/quiz.html` をブラウザで開いて自分で解く。
問題生成は重い（コーパス読込＋全問セルフチェック）ため、一度作れば何度でも再利用できるバンクとして永続化する。

典型フロー: ①作成でバンク（`quiz.html`）を作る → ②ブラウザで開いて解く → ③『Finish & Review』画面の2つのダウンロードボタンを使う——
「Download Results (JSON)」は `exams/ccar-f/reports/quiz-results/` に置くと次回の弱点ターゲット生成が自動集計する簡素な結果ファイル、
「Download for AI Analysis (Markdown)」は全問の設問・選択肢・自分の回答・正解・解説を人が読める形でまとめたファイルで、
このチャットや他の AI チャットにそのまま貼って弱点分析を頼める → ④次にバンクを作るとき「弱点ターゲット」を選ぶと quiz-results/ の結果を自動集計して弱点へ寄せる。

## 起動時のディスパッチ

`banks/*/manifest.json` に `status: "generating"`（未完バンク）があれば、`procedures/generate.md` のステップ G0 に従い再開確認する。
無ければそのまま `procedures/generate.md` を読んでステップ G1（作成設定の AskUserQuestion）から始める。**「作成する/解く」を選ばせる分岐は無い**（このスキルは作成しかしない）。

> このファイルは常時ロードされる薄い入口。重い手順は `procedures/generate.md` に置き、起動したときだけ読む。

## 共通の不変条件

### 公式仕様（Exam Guide `exams/ccar-f/CCAR-F_Certification_Exam_Guide.md` の確定事項）

| 項目 | 確定事項 | 実装 |
|---|---|---|
| 回答形式 | 各問は**正解1つ＋ディストラクタ3つの単一正解（single-best-answer）** | quiz.html は単一選択の4択で出題する |
| 出題 | シナリオベース。6本中4本がランダム選出され、**全問がシナリオに紐づく** | 6シナリオ原型を内蔵し、問題を必ずシナリオに包む |
| ディストラクタ | 明らかな誤答ではなく本気で迷う設計。**2択が技術的に成立するが片方が設計的に優れている** | 「もっともらしいアンチパターン」を強制し、**2方向の誤反射**（ソフト指示に逃げる／コンポーネントを足す）を狙う |
| スコア | 100〜1000のスケールドスコア。**720は素点72%ではない**（難問が重み付け） | quiz.html は素点のみ表示。**素点85〜90%を安全圏の目安**とユーザに伝える |
| 無回答 | 無回答は誤答扱い | quiz.html の Finish 画面で未回答数を警告表示する |

**ドメイン重み:** D1 Agentic 27% / D3 Claude Code 20% / D4 Prompt 20% / D2 MCP 18% / D5 Context 15%。

**カンニング防止についての注記**: `quiz.html` は正解・解説を `QUESTIONS` 配列に埋め込む自己完結アプリであり（ページソースを見れば分かる）、
出題前に正解を隠すファイル分割は行わない。これは Claude Code 内で段階的に出題する経路を廃止したことの引き換えであり、
想定利用者は自分自身なので許容する。UI 上は選択するまで正解をハイライトしない（練習としての体験は保つ）。

### 品質に関する不変条件

1. **根拠なき問題は出さない** — コーパスで裏付けられない、またはセルフチェックで出典不支持と判定した問題は破棄。
2. **trivia を出さない** — 暗記でなく設計判断を問う。シナリオに包めない問題は破棄。
   問題設計の背骨は **「壊れた本番系を最も早いレイヤーで最小修正する」**。正解は原則 **Constrain, don't add／Prompts suggest, systems enforce／Fix the earliest layer** の側に立ち、ディストラクタは「ソフト指示に逃げる／コンポーネントを足す」誤反射を突く（詳細は `procedures/generate.md`・`antipattern-playbook.md`）。
3. **正解は生成時にセルフチェックする** — 自分の生成理由で正解を正当化しない。解説をいったん伏せてコーパスから正解を再導出し、一致を確認する。
4. **正解位置をランダム化** — 正解を A 固定にしない。生成後に分布を自己チェック。
5. **状態は外部ファイルに持つ** — バンクの生成進捗は `manifest.json` に書き、ターン開始時に必ず読み直す（中断・再開に対応するため）。
6. **毎回同じ問題を出さない** — 生成前に出題履歴（既存 `banks/*/quiz.html` に埋め込まれた `QUESTIONS`）を読み、既出の `(task_statement × scenario)` や同一 stem を再利用しない。
7. **弱点ターゲットは実データに基づく** — `exams/ccar-f/reports/quiz-results/*.json` を集計して優先度を決める。無ければ横断にフォールバックし、その旨を伝える。

## ファイル構成

- `procedures/generate.md` — **作成プロセス**の手順（唯一のプロセス）。起動時に必ず読む。
- `templates/quiz-template.html` — 出題 HTML のひな形。`__TITLE__`／`__TOPBAR_TITLE__`／`__BANK_NAME__`／`__RESULTS_HINT_PATH__`／`__QUESTIONS_JSON__` を置換して `banks/<name>/quiz.html` を作る。
- `blueprint.yaml` — 5ドメイン×タスクステートメントの網羅チェックリスト＋ドメイン別の復習先リンク。**作成時に必読**。
- `scenarios.yaml` — 6シナリオ原型。問題を包む文脈として必ず使う。**作成時に必読**。
- `antipattern-playbook.md` — ディストラクタ素材（頻出トラップ＋各タスクのアンチパターン）。**作成時に必読**。
- `question-schema.json` — JSON スキーマ（`bank_manifest`／`quiz_html_question`／`quiz_result`）。
- `banks/` — **永続バンク（コミット対象）**。各バンク `banks/<name>/` に `manifest.json`・`quiz.html`。
- 結果ファイル: `exams/ccar-f/reports/quiz-results/<bank>-results-<timestamp>.json`（quiz.html からダウンロードして手動配置。gitignore 済み）。
