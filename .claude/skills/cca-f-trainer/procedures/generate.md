# 作成プロセス（generate）— 問題バンクをHTMLで生成する

このスキルは**作成のみ**を行う（出題・採点は行わない）。出力は永続バンク `banks/<bank-name>/`（コミット対象）で、
中身は `manifest.json` と、ブラウザでそのまま開いて解ける自己完結 HTML（`quiz.html`）の2点だけ。
解答・解説は `quiz.html` に埋め込まれる（クイズアプリとして機能させるため、事前に正解を伏せる2ファイル分割は行わない。
これはチャット経路で出題しないことの引き換えであり、想定利用者は自分自身なので許容する）。

SKILL.md の「共通の不変条件」（正解位置ランダム化／公式仕様・ドメイン重み／コーパス・グラウンディング／trivia 禁止／セルフチェック）は**全て守る**。

## ステップ G0: 未完バンクの再開チェック（最初に行う）

`banks/*/manifest.json` を読み、`status: "generating"`（生成途中）のバンクがあれば、ユーザに
「未完のバンク `<name>`（{generated}/{total} 問）があります。続きから生成しますか？」と確認する。
続けるなら、そのバンクの `quiz.html` から埋め込み済みの `QUESTIONS` 配列を抽出して現状を把握し（下記「HTML からの読み出し」参照）、
**`generated+1` 問目から再開**する（ステップ G3 へ。設定質問はスキップ）。新規で作るなら下の G1 へ。

### HTML からの読み出し（既出把握・再開の両方で使う共通手順）

`quiz.html` は `const QUESTIONS = [...];` という1行に全問題データを埋め込んでいる。次の Python ワンライナー相当で取り出す。

```python
import re, json
text = open('banks/<name>/quiz.html', encoding='utf-8').read()
m = re.search(r'const QUESTIONS = (\[.*?\]);\n', text, re.S)
questions = json.loads(m.group(1))  # 各要素に domain/task_statement/scenario_code/difficulty/situation/question/options/correct/explanation を含む
```

## ステップ G1: 作成設定（AskUserQuestion 1回・最大4問）

`date +%F` で日付を取得。AskUserQuestion で次を確認する。

1. **対象** — 「新規バンクを作る」／「既存バンクに問題を追加する」
   - 「既存に追加」→ 次ターンでどのバンクかを1問聞き、その manifest の focus・language を引き継いで追加する。
2. **問題数** — 10 / 20 / **60（フル模試）** / その他
3. **focus（出題内容）** — 「ドメイン横断（公式重み比例）」／「特定ドメイン集中」／「弱点ターゲット（過去の結果 JSON を参照）」
   - 「特定ドメイン集中」→ 次ターンでどのドメイン（D1〜D5）かを1問聞く。
   - 「弱点ターゲット」→ `exams/ccar-f/reports/quiz-results/*.json`（無ければ `mkdir -p` だけして空扱い）を全て読み、
     ドメイン／task_statement 別の誤答率を集計して優先出題する（詳細はステップ G2）。ファイルが1つも無ければ「横断」にフォールバックし、その旨を伝える。
4. **HTML の言語** — 「英語のみ（本番と同じ）」／「英語の設問＋日本語の解説（推奨）」／「日本語（設問・選択肢も翻訳）」
   - 出題は静的 HTML なので、**この場で選んだ言語がそのままファイルに焼き込まれる**（後から変更するには再生成が必要）。
   - 迷ったら「英語の設問＋日本語の解説」を勧める（本番の英語に慣れつつ理解は日本語で深められるため）。
   - 内部的には `stem`・`options` を選んだ言語で執筆する（英語のみ／英語+日本語解説 は英語で執筆、日本語 は日本語で執筆。技術用語・コード識別子は原語のまま残す）。`explanation` は「英語のみ」なら英語、それ以外は日本語で書く。

回答が揃ったら**バンク名を自動命名**する（例: `mock-60-2026-06-20` / `focus-D2-2026-06-20` / `weakness-2026-06-20`。同名衝突時は `-2` を付す）。
`banks/<bank-name>/` を作り（`mkdir -p`）、`manifest.json` を初期化する（`question-schema.json` の `bank_manifest` 定義に従う。
`status:"generating"`・`generated:0`・`total`・`focus`・`language`・`domain_distribution` を埋める）。

問題数に応じてドメイン配分を決める。横断は**公式重みに比例**（例: 60問なら D1×16, D3×12, D4×12, D2×11, D5×9。20問なら D1×5, D3×4, D4×4, D2×4, D5×3。端数は D1 に寄せる）。
特定ドメイン集中はそのドメインに全問。弱点ターゲットは弱点 TS の属するドメインへ寄せつつ、公式重みから極端に外れないようにする。
難易度は **L3（トレードオフ判断）を主軸**に、L2（応用）を従にする。

**シナリオ配分もここで決める（ドメイン配分と同時）。** ステップ G2 で集計する既存バンクのシナリオ被覆を踏まえ、次の規則で割り当てる。

- **横断（mixed）で 12 問以上なら、S1〜S6 の全6シナリオを最低1問ずつ含める**。本番は6本中4本がランダム抽出されるため、
  「今回出たシナリオだけ」「今回出なかったシナリオだけ」に寄せるのは両方とも誤り。
- 11 問以下の横断では、**既存バンクで出題数の少ないシナリオから順に**採用する。
- 既存バンク横断で出題数が 0 または極端に少ないシナリオがあれば、そこへ**規定配分の 1.5〜2 倍**を寄せる。
- 特定ドメイン集中・弱点ターゲットでは、そのドメイン／TS を自然に包めるシナリオに限ってよい（`scenarios.yaml` の対応関係に従う）。
  ただし**単一シナリオに全問を寄せない**（同一シナリオは全体の 50% を上限とする）。

決めたシナリオ配分は `manifest.json` の `source` に一言残す（例: `S6 を厚め（既存バンクでの出題4問と最少のため）`）。

## ステップ G2: コーパス読込と既出・弱点の把握（生成前に1回）

`blueprint.yaml`・`scenarios.yaml`・`antipattern-playbook.md`・`question-schema.json` を読み込む。

**出題履歴を読み込む（重複防止・最重要）**: **既存の全バンク**から問題を抽出し、既出の `(task_statement × scenario)` と stem の要旨を一覧化する。
これを「既出セット」とし、今回の問題が過去のどのバンクとも被らないように生成する。履歴が無ければ全 task_statement から均等に選ぶ。

抽出には**下のシナリオ被覆集計と同じ `load()` ヘルパを使う**（`quiz.html` だけを見ると旧形式バンクを取りこぼし、
そのバンクの既出問題を再生産してしまう）。

**シナリオ被覆を集計して未演習シナリオを警告する（必須）**: S1〜S6 の**過去の総出題数**を出す。素朴に数えると誤るので、次の2点を必ず処理する。

- **旧形式バンクを取りこぼさない** — 初期のバンクは `quiz.html` ではなく `quiz-questions.json`（`{"bank":..., "questions":[...]}`）で、
  シナリオが `scenario_code` ではなく **`scenario` フィールドにコード（"S3" 等）で入っている**。
- **ローカライズ版を二重計上しない** — `focus-S4S6-2026-08-04` と `focus-S4S6-2026-08-04-ja` のように、
  **英日で同一問題セットのバンクがある**。`(task_statement, scenario_code)` の並びが一致するバンクは1つとして数える。

```python
import re, json, glob, os
from collections import Counter

def load(d):
    for p in (f'{d}/quiz.html', f'{d}/quiz-questions.json'):
        if not os.path.exists(p): continue
        if p.endswith('.html'):
            m = re.search(r'const QUESTIONS = (\[.*?\]);\n', open(p, encoding='utf-8').read(), re.S)
            return json.loads(m.group(1)) if m else []
        o = json.load(open(p, encoding='utf-8'))
        return o['questions'] if isinstance(o, dict) else o
    return []

code = lambda q: q.get('scenario_code') or q.get('scenario')   # 旧形式フォールバック
seen, cov = {}, Counter()
for d in sorted(glob.glob('banks/*')):
    qs = load(d)
    sig = tuple((q.get('task_statement'), code(q)) for q in qs)
    if sig in seen: continue                                    # ローカライズ版は畳む
    seen[sig] = d
    cov.update(code(q) for q in qs)

S = ('S1','S2','S3','S4','S5','S6')
mean    = sum(cov[s] for s in S) / 6
missing = [s for s in S if cov[s] == 0]
thin    = [s for s in S if 0 < cov[s] < mean * 0.6]             # 平均の6割未満を「手薄」
```

`missing` または `thin` が空でなければ、**生成を始める前にユーザへ一言警告する**。例（2026-08-09 時点の実測値）:

> ⚠️ これまでの演習はシナリオが偏っています（S3:26 / S1:21 / S4:14 / S6:10 / **S5:8** / **S2:5**）。
> 本番は6シナリオ中4本がランダム抽出されるため、演習の薄いシナリオがそのまま失点になります。今回は S2・S5 を厚めに配分します。

> **なぜこのチェックがあるか**: 2026-08-08 の本試験（580点・不合格）では、直前の準備が S1/S2/S3/S5 に偏っており、
> **実際に出題されたのは S1/S2/S4/S6** だった。未演習だった S4・S6 の推定正答率は 43% / 19% で、ここが不合格の直接原因になった。
> 詳細: `exams/ccar-f/reports/CCAR-F_ExamAttempt1_Analysis_2026-08-09.md` §2

**弱点ターゲット時の集計**: `exams/ccar-f/reports/quiz-results/*.json` を全て読み、各ファイルの `results[]`（`domain`/`task_statement`/`scenario`/`is_correct`）を集計する。
task_statement ごとに次のスコアで優先度をつける: `priority = 2*(誤答率) + 1*(直近ファイルほど重い誤答への重み) + 0.5*(結果ファイルに一度も登場していない task_statement への基礎優先度)`。
直近の結果ファイルで連続正解している task_statement は優先度を下げる。上位の task_statement を多めに配分する。

## ステップ G3: バッチ生成（5問ずつ・各バッチ後に保存）

**一度に全部作らない。5問ずつのバッチで生成し、各バッチ後に `quiz.html` を再構築して manifest を更新する。**
こうすると 60 問のような大物でも、途中で止まっても G0 の再開で続けられ、1ターンの作業量も抑えられる。

各問は**必ず次を満たす**こと。満たせない問題は破棄して作り直す。

- **既出と被らせない（多様化）**: 同じ `(task_statement × scenario)` の組を既出セットから再利用しない。
  やむなく同じ task_statement を使う場合でも、**シナリオ・具体的な制約や数値・どのアンチパターンを罠にするか・問う角度を必ず変え**、過去とほぼ同一の stem を絶対に再生産しない。
  横断では blueprint の task_statement プール（約30）を**巡回**し、出題回数が少ない／長く出していない TS を優先採用してドメイン内の偏りを解消する（公式ドメイン重みは維持）。
- **シナリオに包む**: `scenarios.yaml` の原型を選び、その文脈で問う。trivia（用語暗記）禁止。必ず**シナリオ＋制約＋設計判断**の粒度。各 task_statement は複数シナリオで枠付けでき、毎回同じ TS↔シナリオの結びつきに固定しない。
  **G1 で決めたシナリオ配分を守る**。バッチごとに `scenario_code` の累計を数え、配分から外れていれば次バッチで補正する。
- **「壊れた本番系を直す」フレーミングを優先する**: 実試験は「ゼロから何を作るか」より、**既に動いている本番系に症状が出ていて、根本原因をどのレイヤーで最小修正するか**を問う。シナリオが許す限り stem を「症状（誤動作・取りこぼし・ハング・スキーマは通るが意味的に誤った値 など）が観測されている → 何を直すべきか」型にする。各シナリオの `failure_framing` を素材に使う。純粋なグリーンフィールドの抽象設問（「どう設計すべきか」だけ）に偏らせない（多様性のため一部は可）。
- **根拠を紐付ける**: 正解には必ずコーパス内の出典（ファイルパス＋タスクステートメント番号や見出し）を確認できること。根拠を示せない問題は作らない。第一の根拠は Exam Guide のタスクステートメント、補強は公式ブログ・docs。
- **ディストラクタを「もっともらしいアンチパターン」にする**: `antipattern-playbook.md` から素材を引く。少なくとも1つは「技術的には成立するが設計的に劣る」選択肢にする。頻出トラップ4種（単一スーパーエージェント／文脈自動継承の誤解／CI で `-p` 無し対話実行／高リスクで人間監督を減らす）は特に有効。
- **誤答は2方向の「設計反射のズレ」を狙う**: 実試験の不正解は知識不足より反射の方向ズレから生まれる。可能なら1問のディストラクタに **(a) 決定論が要る所でソフト指示／プロンプト依存に逃げる型** と **(b) 最小修正で済む所にコンポーネント／上位モデル／コンテキスト窓を足す（over-engineering）型** の両方向を含める。残り1つは「正しい方向だが誤ったレイヤー／粒度」にすると迷いどころが増える。
- **正解位置をランダム化**: 正解を A 固定にしない。A〜D にばらつかせ、バンク全体で正解分布が概ね均等か生成後に自己チェックする。
- **タグ付け**: `domain`（D1〜D5）・`task_statement`（例 "1.4"）・`scenario_code`（S1〜S6）・`difficulty`（L2/L3）。

**各問のセルフチェック（必須）**: 自作問題の最大リスクは正解キー誤り。別エージェントは使わず、**この場で自己点検**する。
各問について**自分が書いた解説をいったん伏せ**、コーパス（第一根拠は Exam Guide のタスクステートメント、補強は
`study/official-blog/`・`docs/`・`study/skilljar-courses/`）から最良の選択肢を**ゼロから再導出**し、`correct` と一致するか確認する。
あわせて ①一意に最良か ②ディストラクタがもっともらしい誤りか ③出典が正解を支持するか ④trivia でないか を点検し、**1つでも満たさなければ修正または作り直す**。

**正解側の3原則チェック（CCAR-F の設計判断の背骨）**: 再導出した正解が次の方向に沿うかを確認する。沿っていない正解候補は疑い、再検討する（例外はあるが、外れるときは出典で明確に正当化できること）。
- **Constrain, don't add（足すより制約する）** — 効率・品質・信頼性の問題に対し、コンポーネント／上位モデル／コンテキスト窓を**足す**より、制約・分離・縮小・最小修正で根本に当てているか。
- **Prompts suggest; systems enforce（重要ルールはシステムで強制）** — 金銭・本人確認・方針例外など決定論的遵守が要るルールを、プロンプトの指示でなくフック／コード／スキーマ等の**システム側**で強制しているか。
- **Fix the earliest layer（最も早いレイヤーを最小修正）** — 症状の下流で糊塗せず、根本原因の**最も早いレイヤー**を最小の介入で直しているか。

### バッチごとの保存（`quiz.html` の再構築）

各問を次の JS オブジェクト形（`templates/quiz-template.html` の `QUESTIONS` 配列要素）で組み立てる。

```json
{
  "n": 1,
  "scenario": "<scenarios.yaml の name。例 Developer Productivity with Claude>",
  "domain": "D2",
  "task_statement": "2.5",
  "scenario_code": "S4",
  "difficulty": "L3",
  "situation": "<シナリオ文脈・状況設定。最後の設問文は含めない>",
  "question": "<最後の設問文のみ。例 What is the most effective fix?>",
  "options": [
    { "letter": "A", "text": "<選択肢全文>", "correct": false },
    { "letter": "B", "text": "<選択肢全文>", "correct": true },
    { "letter": "C", "text": "<選択肢全文>", "correct": false },
    { "letter": "D", "text": "<選択肢全文>", "correct": false }
  ],
  "correct": "B",
  "explanation": "<正解の理由＋他3つがなぜアンチパターンか。設定言語に従う>",
  "global_n": 1
}
```

`id`/`global_n` は通し番号（既存の続きから）。生成手順:

1. **新規バンクの初回バッチ**: `templates/quiz-template.html` を読み、次のプレースホルダを置換して `banks/<name>/quiz.html` に書き出す。
   - `__TITLE__` → `Claude Certified Architect — Practice Quiz: <バンク名>`
   - `__TOPBAR_TITLE__` → `CCAR-F Practice — <バンクの説明。例 "Focus: D2 Tool Design & MCP (20Q)">`
   - `__BANK_NAME__` → バンク名（JS 文字列リテラルとして安全な形。ダブルクォートや `</script>` を含めない）
   - `__RESULTS_HINT_PATH__` → `exams/ccar-f/reports/quiz-results/`（リポジトリルートからの相対パス。バックスラッシュ等の JS 特殊文字はエスケープ）
   - `__QUESTIONS_JSON__` → その時点までに生成した全問題（このバッチ分のみ）を `json.dumps(questions, ensure_ascii=False)` した文字列
2. **2バッチ目以降・再開時**: 既存の `quiz.html` から「HTML からの読み出し」で現在の `QUESTIONS` を取り出し、新バッチ分を末尾に追加し、
   同じテンプレートで**ファイル全体を作り直す**（プレースホルダの再置換ではなく、`QUESTIONS` 配列だけを更新すればよい）。
3. 保存したら `manifest.json` の `generated` を更新する。**まだ目標数に達していなければ、次のバッチを続ける**（ターンを跨いでよい。1ターンに1〜数バッチ）。

日本語出力を選んだ場合、`situation`/`question`/`options[].text` を自然な日本語で書く（技術用語・コード識別子・固有名詞は原語のまま）。
「英語+日本語解説」の場合は `situation`/`question`/`options[].text` を英語、`explanation` のみ日本語にする。

## ステップ G4: 完成

`generated == total` になったら `manifest.json` の `status` を `"ready"` にする。
最後にバンク全体で次の2点を自己チェックする（`quiz.html` の `QUESTIONS` を読み出して数える）。

1. **正解分布が特定キーに偏っていないか**（`correct` の A〜D 分布）。
2. **シナリオ配分が G1 の計画どおりか**（`scenario_code` の分布）。横断で 12 問以上なのに出題 0 のシナリオが残っていたら、その分を差し替える。

ユーザに**完成を一言で報告**する（バンク名・問題数・ドメイン配分・**シナリオ配分**・focus・言語）。
G2 で未演習・手薄なシナリオを検出していた場合は、**今回それをどれだけ埋めたか**（例: 「S6 を 4問 → 累計 10問 に増やしました」）も併せて伝える。続けて次を案内する:

- 「`banks/<name>/quiz.html` をブラウザで開いて解いてください（ダブルクリックで開けます）」
- 「解き終えたら『Finish & Review』画面に2つのダウンロードボタンがあります」
  - 「**Download Results (JSON)**」→ `exams/ccar-f/reports/quiz-results/` に保存すると、次に弱点ターゲットのバンクを作るときこのフォルダの全ファイルを自動集計する（この skill 専用の簡素なコード形式）
  - 「**Download for AI Analysis (Markdown)**」→ 設問・選択肢・自分の回答・正解・解説を全問ぶん人が読める形でまとめたファイル。保存場所は問わず、このチャットや他の AI チャットにそのまま貼って「弱点と次にやるべきことを分析して」のように使える
