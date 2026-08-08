# banks — 問題バンク（Git 管理対象外・ローカルのみ）

`cca-f-trainer` スキルが生成した問題バンクの置き場。各バンクは `banks/<バンク名>/` に
`manifest.json` と `quiz.html`（ブラウザでそのまま解ける自己完結アプリ）を持つ。

## なぜコミットしないのか

focus に「弱点ターゲット」を選んだバンクは、`exams/ccar-f/reports/quiz-results/` の演習結果を集計し、
**誤答分析（＝個人の弱点）に基づいて出題内容を決める**。生成されたバンクとその `manifest.json` の
`source` フィールドには、どの task_statement をなぜ狙ったかが残る。
これは演習結果と同じ性質の個人の学習記録なので、Git 管理対象外にしている（リポジトリルートの `.gitignore`）。

共有されるのは**スキル本体**（`SKILL.md`・`procedures/`・`blueprint.yaml`・`scenarios.yaml`・
`antipattern-playbook.md`・`question-schema.json`・`templates/`）だけ。バンクは各自の環境で生成する。

## ローカルでは残しておくこと

このフォルダの中身は、同一環境では**生成のたびに読まれる**。消すと次の2つが機能しなくなる。

- **重複防止** — 既出の `(task_statement × scenario)` と stem を照合して同じ問題の再生産を防ぐ
- **シナリオ被覆チェック** — S1〜S6 の出題実績を集計し、未演習・手薄なシナリオへ配分を寄せる

なお集計は `quiz.html` 形式と旧 `quiz-questions.json` 形式の両方を読み、
英日で同一問題のローカライズ版は二重計上しない（`procedures/generate.md` ステップ G2）。
