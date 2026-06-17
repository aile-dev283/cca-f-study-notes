<!-- markdownlint-disable -->

# Introduction to Claude Cowork

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork>  
**所要時間:** 未記載  
**対象ドメイン:** D4  
**フェーズ:** Phase 0 - オリエンテーション  

---

## カリキュラム

### レッスン 01: Claude Cowork とは何か

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444164>  

**推定時間:** 8分

**学習目標**

- Claude Cowork を定義し、Claude との新しい働き方として何が違うのかを説明する。
- Cowork を、自分の files、apps、tools の中で Claude が働く mode として理解する。
- Chat、Cowork、Code の違いを見分け、どれを使うべきか判断する。

**重要ポイント**

- Cowork は答えを返すだけでなく、作業を完了するための Claude である。local machine、cloud apps、browser など、自分の仕事場で動く。
- Cowork の本質は delegating である。Chat は思考、draft、質問に向き、Cowork は outcome を説明して Claude に計画・実行・納品まで任せる。
- Cowork は multi-step、longer-running work に向く。複数 tool にまたがり、時間がかかり、real artifact で終わる task に適している。
- 利用者は control を保つ。Claude は開始前に plan を示し、送信・削除・共有のような重要 action では原則確認を求める。

Cowork は desktop app 内の mode で、folder を指定し、Gmail、Slack、Google Drive、calendar などを接続し、やりたいことを説明すると、Claude が plan を立てて作業を進め、成果物を folder に保存する。

Chat は turn-by-turn の対話、Cowork は複数 tool をまたぐ持続的な作業、Code は codebase 内で terminal と git を使う software development 向けである。

### レッスン 02: Claude Cowork の setup

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444165>  

**推定時間:** 8分

**学習目標**

- Claude Desktop app で Cowork を開き、working folder を指定する。
- 仕事で使う apps を接続する。
- Claude が実行前に確認する action と、確認なしで進める action を理解する。

Cowork は Mac / Windows の Claude Desktop app 内で動作する。`claude.com/download` から install し、sign in したうえで mode selector から Cowork を選ぶ。表示されない場合は paid plan や新しい desktop app が必要な場合がある。

folder の指定は最重要の setup である。Claude はその folder 内の files を読み、成果物を同じ場所に保存する。task に必要な最小の folder を選ぶと、context が絞られ、安全性も高まる。

Connectors は Claude が email、calendar、messaging、CRM、cloud storage などにアクセスするための入口である。Gmail、Google Calendar、Slack、Google Drive などを task ごとに toggle できる。

cloud connector の権限は connector ごとに異なる。read/search のみの場合もあれば create/edit できる場合もある。最も確実な作業場所は local working folder である。

### レッスン 03: Claude Cowork にできること

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444169>  

**推定時間:** 11分

**学習目標**

- Cowork に適した3つの work pattern（multi-step、file-based、multi-tool）を見分ける。
- `/schedule` で scheduled task を設定する。
- Dispatch を使って phone から Claude に task を送る。

Cowork に向く task は、複数 step がある、real files の context を使う、複数 tools にまたがる、という特徴を持つ。たとえば会議メモ、Slack threads、emails、deck を横断して executive summary を作るような作業である。

Scheduled tasks は、定期的な report、weekly summary、status update などに向いている。Dispatch を使うと、移動中に phone から task を投げ、desktop 側の Cowork に実行させられる。

### レッスン 04: Claude Cowork に最初の task を渡す

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444166>  

良い Cowork prompt は、outcome、context、source、constraints、deliverable を明確にする。単なる質問ではなく、「何を完成させてほしいか」を伝える。

例:

> Look across the meeting notes, email threads, and proposal decks for Q3 pricing decisions. Pull the findings together into a one-page summary I can send to the exec team.

Claude は plan を提示し、必要に応じて確認を求める。途中で方向修正したい場合は、task の進行中でも指示できる。

### レッスン 05: より速く良い結果を得る

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444171>  

Cowork で良い結果を得るには、folder scope、connector selection、deliverable format、review criteria を明確にする。Claude が迷う余地を減らすほど、作業は早く正確になる。

task を投げる前に、必要な files が folder にあるか、connector が有効か、Claude に触ってほしくない範囲がないか確認する。最初の plan を読み、必要なら早めに修正する。

### レッスン 06: standing context: global instructions と projects

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444167>  

Global instructions は、すべての作業に適用したい好みやルールを置く場所である。Projects は特定の workstream に関する context、files、instructions をまとめる場所である。

standing context を使うと、tone、format、decision criteria、review style などを毎回説明しなくてよくなる。ただし、古い情報や広すぎる instructions は誤解の原因になるため、定期的に見直す。

### レッスン 07: Skills: Claude Cowork に自分のやり方を教える

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444170>  

Skills は、繰り返し行う作業の手順、quality bar、templates、examples を Claude に渡す仕組みである。brief 作成、competitive analysis、support response、reporting など、組織固有のやり方を再利用できる。

良い skill は、trigger、inputs、workflow、output format、edge cases を明確にする。

### レッスン 08: Plugins: チームの専門知を encode する

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444168>  

Plugins は skills、tools、connectors などを組み合わせ、チームの定型 workflow を Claude に組み込むための仕組みである。個人の作業手順を team-wide に共有し、一貫した成果物を作りやすくする。

plugin 化する候補は、繰り返し発生し、判断基準が明確で、成果物の形式が安定している作業である。

### レッスン 09: Claude in Chrome

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/485947>  

Claude in Chrome は、connector がない internal dashboards、vendor portals、login behind web apps などを扱うための bridge である。Claude が browser page を読み、必要に応じて page 上で action できる。

利用時は、どの page を対象にするか、どの action まで許可するか、送信・削除・共有のような重要操作で確認が必要かを意識する。

### レッスン 10: Claude for Microsoft 365

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/485948>  

Claude for Microsoft 365 は Outlook、Teams、SharePoint、OneDrive などにある work context を Claude が扱えるようにする。meeting context、email threads、documents、team conversations を横断して要約や draft に使える。

connector ごとの read/write capability を確認し、組織の data policy に沿って利用する。

### レッスン 11: 安全に働くための best practices

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444173>  

Cowork は実際の files や apps に触れるため、scope と permission が重要である。最小限の folder、必要な connector だけを有効化し、plan を確認し、high-impact actions では人間が判断する。

送信、削除、共有、外部公開、重要データの変更などは human confirmation を前提にする。機密情報や個人情報を扱うときは、抽象化・最小化・アクセス制限を徹底する。

### レッスン 12: plugins のための skills を検証する

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/485949>  

plugin に含める skill は、実際の task で validation する。期待する inputs、edge cases、output format、failure modes を確認し、曖昧な instructions を減らす。

skill の評価では、同じ task を複数回実行して一貫性を見る。必要に応じて examples、checklists、constraints を追加する。

### レッスン 13: 作ったものを team と共有する

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/485950>  

Skills や plugins は team で共有できる。共有前に、機密情報が含まれていないか、特定個人や顧客に依存しすぎていないか、汎用的な手順になっているかを確認する。

共有後は feedback を集め、workflow と instructions を改善する。

### レッスン 14: まとめと次の steps

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/444174>  

Cowork は、Chat では人間がつなぎ合わせていた複数 step の作業を、Claude に委任できる mode である。適切な folder、connectors、standing context、skills を組み合わせることで、実際の成果物まで到達できる。

次は、自分の仕事の中から multi-step、file-based、multi-tool な task を一つ選び、小さく試す。

### レッスン 15: Claude Cowork quiz

**URL:** <https://anthropic.skilljar.com/introduction-to-claude-cowork/452288>  

この quiz では、Cowork の使いどころ、Chat / Code との違い、folder と connector の scope、安全な delegating の考え方を確認する。
