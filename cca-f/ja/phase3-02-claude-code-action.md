<!-- markdownlint-disable -->

# Claude Code in Action

**URL:** <https://anthropic.skilljar.com/claude-code-in-action>  
**所要時間:** 約1時間  
**対象ドメイン:** D3  
**フェーズ:** Phase 3  

---

## カリキュラム

### レッスン 01: Introduction（はじめに）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303233>  

Open in Claude

---

### レッスン 02: What is a coding assistant?（coding assistant とは何か）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303235>  

Open in Claude

coding assistant は、単に code を書くツールというだけではなく、language model を用いて複雑な programming タスクに取り組む高度なシステムである。これらの assistant が裏側でどのように動作しているかを理解することで、真に強力な coding companion を生み出すものが何なのかを正しく評価できるようになる。

coding assistant の仕組み

error message に基づいて bug を修正するような task を coding assistant に与えると、人間の developer が問題に取り組むのと同様のプロセスをたどる。

context を集める - その error が何を指しているのか、codebase のどの部分が影響を受けるのか、どの files が関連するのかを理解する
plan を立てる - code を変更し、tests を実行して修正を検証するなど、問題をどう解決するかを決める
action を起こす - files を更新し、commands を実行することで、実際に解決策を実装する

ここで重要な洞察は、最初と最後のステップでは assistant が外の世界と相互作用する必要があるという点である。files を読み、documentation を取得し、commands を実行し、code を編集する、といったことである。

tool use の課題

ここからが面白いところである。language model はそれ自体では text を処理して text を返すことしかできず、実際に files を読んだり commands を実行したりはできない。スタンドアロンの language model に file を読むよう頼んでも、その能力を持っていないと答えるだろう。

では coding assistant はこの問題をどう解決しているのか。それは「tool use」と呼ばれる巧妙なシステムを使う。

tool use の仕組み

coding assistant に request を送ると、その assistant は自動的にあなたの message へと指示を追加し、language model に対して action を要求する方法を教え込む。たとえば、次のような text を追加するかもしれない。「file を読みたいときは、'ReadFile: file の名前' と応答せよ」

完全なフローは次のとおりである。

あなたが尋ねる: 「main.go ファイルにはどんな code が書かれているか?」
coding assistant が tool の指示をあなたの request に追加する
language model が応答する: 「ReadFile: main.go」
coding assistant が実際の file を読み、その内容を model に送り返す
language model が file の内容に基づいて最終的な答えを提供する

このシステムによって、language model は実際には注意深くフォーマットされた text 応答を生成しているだけであるにもかかわらず、効果的に「files を読み」「code を書き」「commands を実行する」ことができるようになる。

なぜ Claude の tool use が重要なのか

すべての language model が等しく tool の利用に長けているわけではない。Claude シリーズの models は、tool が何をするのかを理解し、それを効果的に用いて複雑な task を完了する点で特に優れている。

この tool use の強さは、Claude Code にいくつかの重要な利点をもたらす。

強力な tool use の利点
より難しい task に取り組める - Claude は異なる tools を組み合わせて複雑な作業を処理でき、見たことのない tool でも使いこなす
拡張可能な platform - Claude Code には新しい tools を簡単に追加でき、workflow が進化するにつれて Claude はそれらを使うよう適応する
より高いセキュリティ - Claude Code は indexing を必要とせずに codebase をナビゲートできるため、多くの場合、codebase 全体を external サーバーへ送らずに済む
重要なポイント

coding assistant を理解することは、いくつかの本質的な点に集約される。

coding assistant は language model を用いて様々な task を完了する
language model は、実世界の programming タスクの大半を処理するために tools を必要とする
すべての language model が同じ skill level で tools を使えるわけではない
Claude の強力な tool use は、Claude Code におけるより高いセキュリティ、カスタマイズ性、そして長期的な持続性を可能にする

この tool use の能力こそが、単なる text 生成 model を、files を読み、codebase を理解し、project に意味のある変更を加えられる強力な coding assistant へと変えるものである。

---

### レッスン 03: Claude Code in action（Claude Code の実演）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303242>  

Open in Claude

Claude Code には、files の読み取り、code の記述、commands の実行、directories の管理といった一般的な開発 task を扱う、包括的な組み込み tools 一式が付属している。しかし Claude Code を真に強力にしているのは、これらの tools をいかに知的に組み合わせて、複雑で多段階の問題に取り組むかという点である。

---

### レッスン 04: Claude Code setup（Claude Code の setup）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/301614>  

Open in Claude

ローカルで Claude Code を setup する番である!

完全な setup 手順はこちらで確認できる: https://code.claude.com/docs/en/quickstart

要点として、次のことを行う必要がある。

Claude Code を install する
MacOS, Linux, WSL: curl -fsSL https://claude.ai/install.sh | bash
Windows PowerShell: irm https://claude.ai/install.ps1 | iex
Windows Command Prompt (cmd.exe): curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
MacOS (Homebrew): brew install --cask claude-code
install 後、terminal で claude を実行する。初めてこの command を実行すると、terminal の color theme を選び、claude.ai の認証情報で authenticate するよう求められる

install 後に claude が見つからないというエラーが出る場合や、network や permissions のエラーに遭遇した場合は、docs の Troubleshoot installation issues を参照すること。

Amazon Bedrock、Google Cloud Vertex AI、または Microsoft Foundry 経由で Claude Code を使っているか? 追加の setup 手順については third-party provider setup を参照すること。

---

### レッスン 05: Project setup（project setup）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/301615>  

Open in Claude

Claude Code を使った作業は、取り組む project があるとより面白くなる。

Claude Code で探索するための小さな project を用意した。これは以前の動画で示したのと同じ UI 生成アプリである。注意: この project を実行する必要はない。望むなら、course の残りを自分自身の code base で進めても構わない!

Setup

この project にはわずかな setup が必要である。

ローカルに Node JS が install されていることを確認する。install 手順へのリンク。
この講義に添付されている uigen.zip という zip ファイルをダウンロードして展開する
project ディレクトリで npm run setup を実行し、依存関係を install してローカルの SQLite database を setup する
オプション: この project は Anthropic API を通じて Claude を使い UI コンポーネントを生成する。アプリを完全にテストしたい場合は、Anthropic API にアクセスするための API key を提供する必要がある。これはスキップでき、その場合でもアプリはいくつかの静的なダミー code を生成する。API key は次のように設定できる。
https://console.anthropic.com/ で Anthropic API key を取得する
.env ファイルに API key を配置する。リテラルの text your-api-key-here を Anthropic console から取得した key で置き換える。
npm run dev を実行して project を起動する
Downloads
uigen.zip
(opens in new tab)

---

### レッスン 06: Adding context（context の追加）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303241>  

Open in Claude
0 seconds of 5 minutes, 14 secondsVolume 90%

注意: 上の動画では、すでに削除された古い # の「memory mode」ショートカットが映っている。代わりに /memory と直接の CLAUDE.md 編集を使う、以下のテキストに従うこと。

coding project で Claude を扱うとき、context 管理は極めて重要である。あなたの project には何十、何百もの files があるかもしれないが、Claude が効果的にあなたを助けるために必要なのは適切な情報だけである。無関係な context が多すぎると、実際には Claude の performance が低下するため、関連する files や documentation へと導く方法を学ぶことが不可欠である。

/init コマンド

新しい project で初めて Claude を起動するときは、/init コマンドを実行する。これは Claude に codebase 全体を分析し、次のことを理解するよう指示する。

project の目的とアーキテクチャ
重要な commands と critical な files
coding パターンと構造

code を分析した後、Claude は要約を作成し、それを CLAUDE.md ファイルに書き込む。Claude がこのファイルの作成許可を求めてきたら、Enter を押して各 write 操作を承認するか、Shift+Tab を押して session を通じて Claude が自由に files を書けるようにできる。

CLAUDE.md ファイル

CLAUDE.md ファイルは主に2つの目的を果たす。

codebase を通じて Claude を導き、重要な commands、アーキテクチャ、coding スタイルを指し示す
Claude に具体的またはカスタムの指示を与えられるようにする

このファイルは Claude へのすべての request に含まれるため、project 用の永続的な system prompt を持っているようなものである。

CLAUDE.md ファイルの配置場所

Claude は3つの一般的な配置場所にある3種類の CLAUDE.md ファイルを認識する。

CLAUDE.md - /init で生成され、source control に commit され、他の engineer と共有される
CLAUDE.local.md - 他の engineer とは共有されず、Claude 向けの個人的な指示やカスタマイズを含む
~/.claude/CLAUDE.md - あなたのマシン上のすべての project で使われ、すべての project で Claude に従ってほしい指示を含む
カスタム指示の追加

CLAUDE.md ファイルに指示を追加することで、Claude の振る舞いをカスタマイズできる。たとえば、Claude が code に多すぎるコメントを追加している場合、このファイルを更新することで対処できる。エディタで CLAUDE.md を直接編集するか、Claude Code 内で /memory を実行してファイルを開く。Use comments sparingly. Only comment complex code.（コメントは控えめに。複雑な code にのみコメントを付ける）のような指示を追加する。

Claude はすべての会話の冒頭でこのファイルを読むため、変更は次の message から適用される。
'@' によるファイルの言及

Claude に特定の files を見てほしいときは、@ 記号に続けて file path を入力する。これにより、その file の内容が自動的に request に含まれる。

たとえば authentication system について尋ねたく、関連する files が分かっている場合、次のように入力できる。

How does the auth system work? @auth

Claude は選択できる auth 関連 files のリストを表示し、選んだ file を会話に含める。

CLAUDE.md でのファイル参照

同じ @ 構文を使って、CLAUDE.md ファイル内で直接 files に言及することもできる。これは project の多くの側面に関連する files に特に有用である。

たとえば、データ構造を定義する database schema ファイルがある場合、CLAUDE.md に次を追加するとよい。

The database schema is defined in the @prisma/schema.prisma file. Reference it anytime you need to understand the structure of data stored in the database.

この方法でファイルに言及すると、その内容がすべての request に自動的に含まれるため、Claude は毎回 schema ファイルを探して読む必要なく、あなたのデータ構造に関する質問に即座に答えられる。

これは、別の tool 用の AGENTS.md ファイルがすでに repo にある場合にも有用である。指示を複製する必要はなく、CLAUDE.md の1行目に @AGENTS.md を追加すれば、Claude はまずそのファイルの内容を読み込む。その後、import の下に Claude 固有の指示を追加できる。

---

### レッスン 07: Making changes（changes を作る）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303236>  

Open in Claude

注意: 上の動画では、すでに効果のない古い「think harder」キーワードが映っている。/effort を使う以下のテキストに従うこと。

development environment で Claude を扱うとき、既存の project に変更を加える必要がよくある。このガイドは、スクリーンショットによる視覚的なコミュニケーションや Claude の高度な reasoning 能力の活用を含め、効果的に変更を実装する実践的なテクニックを扱う。

スクリーンショットによる正確なコミュニケーション

Claude とコミュニケーションする最も効果的な方法の1つはスクリーンショットである。インターフェースの特定の部分を変更したいとき、スクリーンショットを撮ることで、あなたが何を指しているのかを Claude が正確に理解できる。

スクリーンショットを Claude に貼り付けるには、Ctrl+V を使う(macOS でも Cmd+V ではない)。このキーボードショートカットは、チャットインターフェースにスクリーンショットを貼り付けるために特別に設計されている。画像を貼り付けたら、アプリケーションのその領域に特定の変更を加えるよう Claude に依頼できる。

Planning Mode（プランニングモード）

codebase 全体にわたる広範な調査を必要とする、より複雑な task のために、Planning Mode を有効にできる。この機能により、Claude は変更を実装する前に project の徹底的な探索を行う。

/plan と入力するか、Shift + Tab を2回押す(すでに edits を auto-accept している場合は1回)ことで Planning Mode を有効にする。このモードでは、Claude は次のことを行う。

project 内のより多くの files を読む
詳細な実装 plan を作成する
何をするつもりかを正確に示す
先に進む前にあなたの承認を待つ

これにより、plan をレビューし、Claude が重要な何かを見落としたり特定のシナリオを考慮しなかったりした場合に軌道修正する機会が得られる。

ヒント: plan をレビューするとき、Ctrl+G を押してテキストエディタで開ける。plan を承認する前に精密な編集を加えられ、Claude はあなたが submit した最終版を参照する。

Effort level: Claude がどれだけ深く考えるか

デフォルトでは、Claude は答える前に問題を reasoning する。動作中は「still thinking」のようなヒントが表示される。Claude の reasoning プロセスを見たい場合は、Ctrl+O を押して実際の reasoning ステップを展開する。

effort level を設定することで、Claude が問題をどう reasoning するかを制御できる。/effort を実行して現在のレベルを確認し、調整する。low はより速く安価で、max は難しい問題に対して最も長く reasoning する。デフォルトは model と plan に依存する — /effort が自分の値を表示する。

単一の prompt で Claude に追加の思考をさせたいと合図したい場合は、prompt 内で ultrathink というキーワードを使う。これは Claude にこのターンでより多く reasoning すべきだと合図するが、session の effort level は調整しない。

Planning と Effort をいつ使うか

これら2つの機能は、異なる種類の複雑さを扱う。

Planning Mode が最適なのは:

codebase の広範な理解を必要とする task
多段階の実装
複数の files やコンポーネントに影響する変更

より高い effort level への調整が最適なのは:

複雑なロジックの問題
難しい問題のデバッグ
アルゴリズム的な課題

幅と深さの両方を必要とする task では、両モードを組み合わせられる。ただし、どちらの機能も追加の tokens を消費するため、使用にはコストの考慮があることに留意すること。

---

### レッスン 08: Course satisfaction survey（コース満足度調査）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303701>  

Open in Claude
Loading...

---

### レッスン 09: Controlling context（context を control する）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303237>  

Open in Claude

注意: 上の動画では、memory を追加する古い # のショートカットが映っている。代わりに /memory を使う以下のテキストに従うこと。

複雑な task で Claude を扱うとき、会話を導いて集中的かつ生産的に保つ必要がよくある。会話の流れを制御し、Claude が軌道に乗り続けるのを助けるために使えるテクニックがいくつかある。

Escape で Claude を中断する

Claude が間違った方向に進み始めたり、一度に多くを扱おうとしたりすることがある。Escape キーを押すことで、応答の途中で Claude を止め、会話を軌道修正できる。

これは、Claude に複数のことを同時に処理させるのではなく、1つの特定の task に集中させたいときに特に有用である。たとえば、複数の関数のテストを書くよう Claude に頼んで、それがすべての関数についての包括的な plan を作り始めた場合、中断して一度に1つの関数に集中するよう頼める。

Escape と Memory を組み合わせる

escape テクニックの最も強力な応用の1つは、繰り返されるエラーの修正である。Claude が異なる会話をまたいで同じ間違いを繰り返すとき、次のことができる。

Escape を押して現在の応答を止める
/memory を実行する(または CLAUDE.md を直接編集する)ことで、正しいアプローチについてのメモを追加する
修正された情報とともに会話を続ける

これにより、その project に関する今後の会話で Claude が同じエラーを犯すのを防げる。

会話を巻き戻す

長い会話の間に、無関係になったり気を散らしたりする context が蓄積することがある。たとえば、Claude がエラーに遭遇してそのデバッグに時間を費やした場合、そのやり取りは次の task には有用でないかもしれない。

Escape を2回押すか /rewind と入力することで、会話を巻き戻せる。これはあなたが送ったすべての message を表示し、より早い時点に戻ってそこから続けられるようにする。このテクニックは次のことに役立つ。

価値ある context(Claude の codebase 理解など)を維持する
気を散らす、または無関係な会話履歴を取り除く
Claude を現在の task に集中させ続ける
Context 管理コマンド

Claude は会話の context を効果的に管理するためのいくつかの commands を提供する。

/compact

/compact コマンドは、Claude が学んだ重要な情報を保ちつつ、会話履歴全体を要約する。これは次のような場合に理想的である。

Claude が project について価値ある知識を得た
関連する task を続けたい
会話は長くなったが重要な context を含んでいる

Claude が現在の task について多くを学び、それが次の関連する task に移る際にもその知識を維持したいときに compact を使う。

/clear

/clear コマンドは、新鮮な context で新しい会話を開始する。これは次のような場合に最も有用である。

まったく異なる無関係な task に切り替える
現在の会話の context が新しい task で Claude を混乱させかねない
以前の context なしでやり直したい

後で /resume を使えば、以前の会話に戻ることもできる。/clear コマンドは、その会話を session 履歴から削除するわけではない。

これらのテクニックをいつ使うか

これらの会話制御テクニックは、特に次の場面で価値がある。

context が散らかりやすい長時間の会話
以前の context が気を散らしかねない task の切り替え
Claude が同じ間違いを繰り返す状況
特定のコンポーネントへの集中を維持する必要がある複雑な project

escape、escape の二度押し、/compact、/clear を戦略的に使うことで、development workflow を通じて Claude を集中的かつ生産的に保てる。これらは単なる便利機能ではなく、効果的な AI 支援開発 session を維持するための不可欠な tools である。

---

### レッスン 10: Custom commands（custom commands）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303234>  

Open in Claude

Claude Code には、スラッシュを入力してアクセスできる組み込みの commands が付属しているが、頻繁に実行する反復的な task を自動化するために、自分自身のカスタム commands を作成することもできる。

カスタム commands の作成

カスタム command を作成するには、project に特定のフォルダ構造を setup する必要がある。

project ディレクトリ内の .claude フォルダを見つける
その中に commands という新しいディレクトリを作成する
希望する command 名(audit.md など)で新しい markdown ファイルを作成する

ファイル名が command 名になる。つまり audit.md は /audit コマンドを作成する。

例: Audit コマンド

脆弱性について project の依存関係を監査するカスタム command の実用例を次に示す。

この audit コマンドは3つのことを行う。

npm audit を実行して脆弱な install 済みパッケージを見つける
npm audit fix を実行して更新を適用する
tests を実行して更新が何も壊していないことを検証する

command ファイルを作成すると、Claude Code は自動的にそれを認識する。再起動の必要はない。

引数付きの commands

カスタム commands は $ARGUMENTS プレースホルダーを使って引数を受け取れる。これにより、はるかに柔軟で再利用可能になる。

たとえば、write_tests.md コマンドは次のような内容を含むかもしれない。

Write comprehensive tests for: $ARGUMENTS

Testing conventions:
- Use Vitest with React Testing Library
- Place test files in a **tests** directory in the same folder as the source file
- Name test files as [filename].test.ts(x)
- Use @/ prefix for imports

Coverage:
- Test happy paths
- Test edge cases
- Test error states

その後、この command を file path とともに実行できる。

/write_tests the use-auth.ts file in the hooks directory

引数は file path である必要はなく、task に context と方向性を与えるために Claude へ渡したい任意の文字列にできる。

主な利点
自動化 - 反復的な workflow を単一の commands に変える
一貫性 - 毎回同じ手順が踏まれることを保証する
context - project 固有の指示や規約を Claude に提供する
柔軟性 - 引数を使って、異なる入力で commands を機能させる

カスタム commands は、test スイートの実行、code のデプロイ、チームの規約に従ったボイラープレートの生成といった、project 固有の workflow に特に有用である。

---

### レッスン 11: MCP servers with Claude Code（Claude Code と MCP servers）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303239>  

Open in Claude

MCP（Model Context Protocol）servers を追加することで、Claude Code の機能を拡張できる。これらの servers はリモートまたはあなたのマシン上でローカルに実行され、通常は持たない新しい tools と能力を Claude に提供する。

最も人気のある MCP servers の1つが Playwright で、Claude に web ブラウザを制御する能力を与える。これは web 開発 workflow に強力な可能性を開く。

Playwright MCP Server の install

Playwright server を Claude Code に追加するには、terminal で(Claude Code 内ではなく)次の command を実行する。

claude mcp add playwright npx @playwright/mcp@latest

この command は2つのことを行う。

MCP server に「playwright」という名前を付ける
あなたのマシン上でローカルに server を起動する command を提供する
permissions の管理

MCP server の tools を初めて使うとき、Claude は毎回 permission を求める。これらの permission プロンプトに疲れたら、設定を編集して server を事前承認できる。

.claude/settings.local.json ファイルを開き、server を allow 配列に追加する。

{
"permissions": {
"allow": ["mcp__playwright"],
"deny": []
}
}

mcp__playwright のダブルアンダースコアに注意すること。これにより、Claude は毎回 permission を求めることなく Playwright の tools を使える。

実用例: コンポーネント生成の改善

Playwright MCP server が開発 workflow をどう改善できるかの実世界の例を次に示す。手動で prompts をテストして調整する代わりに、Claude に次のことをさせられる。

ブラウザを開いてアプリケーションに移動する
テスト用コンポーネントを生成する
視覚的なスタイリングと code 品質を分析する
観察したことに基づいて生成 prompt を更新する
改善した prompt を新しいコンポーネントでテストする

たとえば、Claude に次のように依頼できる。

「localhost:3000 に移動し、基本的なコンポーネントを生成し、スタイリングをレビューし、今後より良いコンポーネントを生成するために @src/lib/prompts/generation.tsx の生成 prompt を更新せよ。」

Claude はブラウザの tools を使ってアプリと相互作用し、生成された出力を調べ、より独創的でクリエイティブなデザインを促すよう prompt ファイルを変更する。

結果と利点

実際には、このアプローチは著しく良い結果につながりうる。汎用的な紫から青へのグラデーションや標準的な Tailwind パターンの代わりに、Claude は次を促すよう prompts を更新するかもしれない。

暖かい夕焼けのグラデーション(オレンジからピンクから紫)
海の深みのテーマ(ティールからエメラルドからシアン)
非対称なデザインと重なり合う要素
クリエイティブな間隔と型破りなレイアウト

重要な利点は、Claude が code だけでなく実際の視覚的出力を見られることである。これにより、スタイリングの改善についてはるかに情報に基づいた判断ができる。

他の MCP servers を探る

Playwright は MCP servers で可能なことの一例にすぎない。エコシステムには次のための servers が含まれる。

database との相互作用
API のテストと監視
ファイルシステム操作
クラウドサービスの統合
開発 tool の自動化

自分の特定の開発ニーズに合致する MCP servers を探ることを検討すること。それらは Claude を、code assistant から、ツールチェーン全体と相互作用できる包括的な開発パートナーへと変えられる。

---

### レッスン 12: Github integration（GitHub integration）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303240>  

Open in Claude

Claude Code は、Claude を GitHub Actions 内で実行できる公式の GitHub integration を提供する。この integration は、issues と pull requests でのメンションサポートと、自動的な pull request レビューという、2つの主要な workflow を提供する。

integration の setup

始めるには、Claude で /install-github-app を実行する。この command は setup プロセスを案内する。

GitHub に Claude Code アプリを install する
API key を追加する
workflow ファイルを含む pull request を自動的に生成する

生成された pull request は、あなたの repository に2つの GitHub Actions を追加する。マージすると、.github/workflows ディレクトリに workflow ファイルが配置される。

デフォルトの GitHub Actions

この integration は2つの主要な workflow を提供する。

Mention Action（メンションアクション）

@claude を使って、任意の issue や pull request で Claude をメンションできる。メンションされると、Claude は次のことを行う。

request を分析して task plan を作成する
codebase へのフルアクセスで task を実行する
結果を issue や PR に直接返信する
Pull Request Action（プルリクエストアクション）

pull request を作成するたびに、Claude は自動的に次のことを行う。

提案された変更をレビューする
変更の影響を分析する
詳細なレポートを pull request に投稿する
workflow のカスタマイズ

最初の pull request をマージした後、project のニーズに合わせて workflow ファイルをカスタマイズできる。メンション workflow を強化する方法を次に示す。

Project Setup の追加

Claude が実行される前に、環境を準備するステップを追加できる。

- name: Project Setup
run: |
npm run setup
npm run dev:daemon
カスタム指示

project の setup についての context を Claude に提供する。

custom_instructions: |
The project is already set up with all dependencies installed.
The server is already running at localhost:3000. Logs from it
are being written to logs.txt. If needed, you can query the
db with the 'sqlite3' cli. If needed, use the mcp__playwright
set of tools to launch a browser and interact with the app.
MCP Server の設定

MCP servers を設定して、Claude に追加の能力を与えられる。

mcp_config: |
{
"mcpServers": {
"playwright": {
"command": "npx",
"args": [
"@playwright/mcp@latest",
"--allowed-origins",
"localhost:3000;cdn.tailwindcss.com;esm.sh"
]
}
}
}
Tool の permissions

GitHub Actions で Claude を実行するときは、許可されるすべての tools を明示的に列挙する必要がある。これは MCP servers を使う場合に特に重要である。

allowed_tools: "Bash(npm:*),Bash(sqlite3:*),mcp__playwright__browser_snapshot,mcp__playwright__browser_click,..."

ローカル開発とは異なり、GitHub Actions には permissions のショートカットがない。各 MCP server の各 tool を個別に列挙する必要がある。

ベストプラクティス

Claude の GitHub integration を setup するとき:

デフォルトの workflow から始めて、徐々にカスタマイズする
project 固有の context を提供するためにカスタム指示を使う
MCP servers を使うときは tool の permissions について明示的にする
複雑な task の前に簡単な task で workflow をテストする
追加ステップを設定する際は project の特定のニーズを考慮する

GitHub integration は、Claude を開発アシスタントから、GitHub workflow の中で直接 task を処理し、code をレビューし、洞察を提供できる自動化されたチームメンバーへと変える。

---

### レッスン 13: Introducing hooks（hooks の紹介）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312000>  

Open in Claude

Hooks を使うと、Claude が tool を実行しようとする前または後に commands を実行できる。これらは、ファイル編集後のコードフォーマッターの実行、ファイル変更時のテスト実行、特定ファイルへのアクセスのブロックといった自動化された workflow を実装するのに非常に有用である。

Hooks の仕組み

hooks を理解するために、まず Claude Code と相互作用するときの通常のフローを振り返ろう。Claude に何かを尋ねると、あなたのクエリは tool 定義とともに Claude model へ送られる。Claude はフォーマットされた応答を提供して tool を使うことを決めるかもしれず、その後 Claude Code はその tool を実行して結果を返す。

Hooks はこのプロセスに割り込み、tool の実行が起きる直前または直後に code を実行できるようにする。

最も一般的な hook の種類のうち2つを以下に示す(他の hooks は後のレッスンで見る)。

PreToolUse hooks - tool が呼ばれる前に実行される
PostToolUse hooks - tool が呼ばれた後に実行される
Hook の設定

Hooks は Claude の設定ファイルで定義される。次の場所に追加できる。

Global - ~/.claude/settings.json（すべての project に影響）
Project - .claude/settings.json（チームで共有）
Project（commit されない） - .claude/settings.local.json（個人設定）

これらのファイルに手で hooks を書くこともできるし、Claude Code 内で /hooks コマンドを使うこともできる。

設定構造には2つの主要なセクションが含まれる。

PreToolUse Hooks

PreToolUse hooks は tool が実行される前に実行される。どの tool 種別を対象にするかを指定する matcher を含む。

"PreToolUse": [
{
"matcher": "Read",
"hooks": [
{
"type": "command",
"command": "node /home/hooks/read_hook.js"
}
]
}
]

'Read' tool が実行される前に、この設定は指定された command を実行する。あなたの command は、Claude が行いたい tool 呼び出しについての詳細を受け取り、次のことができる。

操作を通常どおり進めさせる
tool 呼び出しをブロックし、Claude にエラーメッセージを返す
PostToolUse Hooks

PostToolUse hooks は tool が実行された後に実行される。write、edit、または multi-edit 操作の後にトリガーされる例を次に示す。

"PostToolUse": [
{
"matcher": "Write|Edit",
"hooks": [
{
"type": "command",
"command": "node /home/hooks/edit_hook.js"
}
]
}
]

tool 呼び出しはすでに発生しているため、PostToolUse hooks は操作をブロックできない。しかし、次のことができる。

フォローアップ操作を実行する(編集されたばかりのファイルをフォーマットするなど)
tool の使用について Claude に追加のフィードバックを提供する

実用的な応用

hooks を使う一般的な方法を次に示す。

コードフォーマット - Claude がファイルを編集した後に自動的にフォーマットする
テスト - ファイルが変更されたときに自動的に tests を実行する
アクセス制御 - 特定のファイルの読み取りや編集を Claude にブロックする
コード品質 - linters や type checkers を実行し、Claude にフィードバックを提供する
ロギング - Claude がアクセスまたは変更するファイルを追跡する
検証 - 命名規約やコーディング標準をチェックする

重要な洞察は、hooks を使えば、自分自身の tools やプロセスを workflow に統合することで Claude Code の機能を拡張できる、という点である。PreToolUse hooks は Claude ができることを制御し、PostToolUse hooks は Claude がやったことを強化できる。

---

### レッスン 14: Defining hooks（hooks を定義する）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312002>  

Open in Claude

Claude Code の hooks を使うと、tool 呼び出しが実行される前または後にそれを傍受し制御できる。これにより、Claude が development environment でできることとできないことに対する、きめ細かな制御が得られる。

Hook の構築

hook の作成は4つの主要なステップを含む。

PreToolUse か PostToolUse hook かを決める - PreToolUse hooks は tool 呼び出しの実行を防げるが、PostToolUse hooks は tool がすでに使われた後に実行される
どの種類の tool 呼び出しを監視したいかを決める - どの tools が hook をトリガーすべきかを正確に指定する必要がある
tool 呼び出しを受け取る command を書く - この command は、提案された tool 呼び出しについての JSON データを standard input 経由で受け取る
必要なら、command が Claude にフィードバックを提供する - command の exit code が、操作を許可するかブロックするかを Claude に伝える
利用可能な Tools

Claude Code は、hooks で監視できるいくつかの組み込み tools を提供する。

現在の setup で正確にどの tools が利用可能かを確認するには、Claude に直接リストを尋ねられる。利用可能な tools はカスタム MCP servers を追加すると変わりうるため、これは特に有用である。

Tool 呼び出しのデータ構造

hook command が実行されると、Claude は提案された tool 呼び出しの詳細を含む JSON データを standard input 経由で送る。

{
"session_id": "2d6a1e4d-6...",
"transcript_path": "/Users/sg/...",
"hook_event_name": "PreToolUse",
"tool_name": "Read",
"tool_input": {
"file_path": "/code/queries/.env"
}
}

あなたの command はこの JSON を standard input から読み、パースし、tool 名と入力パラメータに基づいて操作を許可するかブロックするかを決める。

Exit code と制御フロー

hook command は exit code を通じて Claude に伝え返す。

Exit Code 0 - すべて問題なし、tool 呼び出しを進めさせる
Exit Code 2 - tool 呼び出しをブロックする(PreToolUse hooks のみ)

PreToolUse hook で code 2 で終了すると、standard error に書いたエラーメッセージは、なぜ操作がブロックされたのかを説明するフィードバックとして Claude に送られる。

ユースケースの例

一般的なユースケースは、.env ファイルのような機密ファイルを Claude が読むのを防ぐことである。Read と Grep の両方の tools がファイル内容にアクセスできるため、両方の tool 種別を監視し、制限されたファイルパスにアクセスしようとしていないかをチェックしたいだろう。

このアプローチは、なぜ特定の操作が制限されるのかについての明確なフィードバックを提供しつつ、Claude のファイルシステムアクセスを完全に制御できるようにする。

Downloads
queries.zip
(opens in new tab)
queries_COMPLETED.zip
(opens in new tab)

---

### レッスン 15: Implementing a hook（hook を実装する）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312003>  

Open in Claude

注意: 上の動画では、Grep を含むこの演習の初期バージョンが映っている。現在のバージョンについては以下のテキストに従うこと。

Claude が機密ファイルを読むのを防ぐ hook を作ろう。これは、PreToolUse hook が tool 呼び出しを実行前に傍受する方法の実用的な例である。

この演習で扱う内容

Read tool が .env を開くのをブロックする hook を書く。これは session 中にあなたの環境変数を保護する。

この hook は Read のみをカバーすることに注意すること。Grep や Bash が同じファイルに到達するのをブロックするには、各 tool の入力の形を個別にチェックする必要がある。各 tool は異なるフィールドを送るからである。包括的なファイル保護のためには、hook を "Read(**/.env)" のような permissions.deny ルールと組み合わせること。より詳しい扱いは hooks ガイドを参照すること。

hook を設定する

.claude/settings.local.json を開き、Read tool にマッチする PreToolUse hook を追加する。

{
"hooks": {
"PreToolUse": [
{
"matcher": "Read",
"hooks": [
{ "type": "command", "command": "node $PWD/hooks/read_hook.js" }
]
}
]
}
}
hook スクリプトを書く

hooks/read_hook.js を作成する。

process.stdin.setEncoding("utf8");
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
const toolArgs = JSON.parse(input);
const readPath = toolArgs.tool_input?.file_path || "";
if (readPath.includes(".env")) {
console.error("You cannot read the .env file");
process.exit(2);
}
process.exit(0);
});

この hook は stdin から tool 呼び出しを JSON として読み、tool_input.file_path をチェックし、code 2 で終了して呼び出しをブロックする(stderr に書かれたものは Claude が見るメッセージになる)。

テストする

Claude Code session で、Claude にあなたの .env ファイルを読むよう頼む。次が表示されるはずである。

You cannot read the .env file

これが Read 呼び出しをブロックしている hook である。別のファイルを読むよう Claude に頼むと、通常どおり機能する。

なぜ Read のみか?

各 tool は異なる入力の形を送る。Read は {"file_path": "..."} を送り、Grep は {"pattern": "...", "path": "..."} を送る(path は検索ディレクトリであってファイルではない)。Bash は {"command": "..."} を送る。file_path のチェックは Read を捕捉するが、API_KEY をプロジェクト全体で grep することや Bash での cat .env は捕捉しない。それらをカバーするには、tool ごとに別々の matchers を書き、それぞれの固有のフィールドを検査するか、tools をまたいで一律に適用される permissions.deny ルールを使う。

---

### レッスン 16: Gotchas around hooks（hooks の注意点）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312423>  

Open in Claude

npm run setup コマンドを実行した後、.claude ディレクトリに2つの settings.json ファイルがあることに気づくかもしれない。そこで何が起きているのかを説明しよう。

Claude Code の documentation は、hooks のセキュリティに関するいくつかの推奨事項を挙げている。

推奨事項の1つは、スクリプトに(相対パスではなく)絶対パスを使うことである。これは path interception や binary planting 攻撃を緩和するのに役立つ。

この推奨事項はまた、settings.json ファイルの共有をはるかに難しくする。理由は単純で、あなたのマシン上の hook スクリプトへの絶対パスは、私のマシン上の絶対パスとはおそらく異なる。なぜなら、私たちはおそらく project を別々のディレクトリに置くからである。

この問題を解決するため、私たちの project には settings.example.json ファイルがある。その中で、スクリプト参照は $PWD プレースホルダーを含む。npm run setup を実行すると、いくつかの依存関係が install されるが、それは scripts ディレクトリに置かれた init-claude.js スクリプトも実行する。このスクリプトは、それらの $PWD プレースホルダーをあなたのマシン上の project への絶対パスに置き換え、settings.example.json ファイルをコピーして settings.local.json にリネームする。

このスクリプトにより、settings.json ファイルを共有しつつ、推奨される絶対パスを使えるようになる!

---

### レッスン 17: Useful hooks（便利な hooks）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312004>  

Open in Claude

Claude Code の hooks は、特に大規模な project で、AI 支援開発における一般的な弱点に対処するのに役立つ。これらの hooks は、Claude が code を変更したときに自動的に実行され、即座にフィードバックを提供して一般的な問題を防ぐ。

TypeScript 型チェック Hook

最も有用な hooks の1つは、根本的な問題に対処する。Claude が関数のシグネチャを変更するとき、その関数が呼ばれている project 全体のすべての箇所を更新しないことがよくある。

たとえば、schema.ts の関数に verbose パラメータを追加するよう Claude に頼むと、関数定義の更新には成功するが、main.ts の呼び出し箇所を見落とす。これは Claude が即座には捕捉しない型エラーを生む。

解決策は、すべてのファイル編集の後に TypeScript コンパイラを実行する post-tool-use hook である。

tsc --noEmit を実行して型エラーをチェックする
見つかったエラーを捕捉する
エラーを即座に Claude にフィードバックする
他のファイルの問題を修正するよう Claude を促す

この hook は、型チェッカーを実行できる任意の型付き言語で機能する。型なし言語では、代わりに自動テストを使って同様の機能を実装できる。

クエリ重複防止 Hook

多くの database クエリを持つ大規模な project では、Claude は既存の code を再利用する代わりに、重複した機能を作ることがある。これは、database 操作を1つのコンポーネントとして含む複雑な多段階 task を Claude に与えるときに特に問題となる。

それぞれが多くの SQL 関数を含む複数のクエリファイルを持つ project 構造を考えてみよう。「3日以上保留中の注文についてアラートを出す Slack 統合を作れ」と Claude に頼むと、既存の getPendingOrders() 関数を使う代わりに新しいクエリを書くかもしれない。

クエリ重複 hook は、レビュープロセスを実装することでこれに対処する。

その仕組みは次のとおりである。

Claude が ./queries ディレクトリ内のファイルを変更したときにトリガーされる
別の Claude Code インスタンスをプログラムから起動する
2番目のインスタンスに変更をレビューし、類似する既存クエリがないかチェックするよう頼む
重複が見つかった場合、元の Claude インスタンスにフィードバックを提供する
重複を削除して既存の機能を使うよう Claude を促す
実装上の考慮事項

両方の hooks は pre-tool-use または post-tool-use hook システムを使う。TypeScript hook は比較的軽量で素早く実行される。クエリ重複 hook は、各レビューのために別の Claude インスタンスを起動するため、より多くのリソースを必要とする。

クエリ hook については、次のトレードオフを考慮すること。

利点: 重複の少ないクリーンな codebase
コスト: 各クエリディレクトリ編集ごとの追加時間と API 使用量
推奨: オーバーヘッドを最小化するため、重要なディレクトリのみを監視する

これらの hooks は Claude の Agent SDK を使って AI とプログラムから相互作用する。これにより、ある Claude インスタンスが別のインスタンスの作業をレビューしフィードバックを提供できる、洗練された workflow を作れる。

これらの概念の拡張

これらの hooks は、自分自身の project に適用できるより広い原則を示している。

コンパイラ/linter の出力を使って即座にフィードバックを提供する
別の AI インスタンスを使ってコードレビュープロセスを実装する
一貫性が最も重要な高価値のディレクトリに監視を集中させる
自動化の利点とパフォーマンスのコストのバランスを取る

鍵となるのは、自分の development workflow における具体的な痛点を特定し、それらの問題に自動的に対処する的を絞った hooks を作ることである。

---

### レッスン 18: Another useful hook（もう一つの便利な hook）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312427>  

Open in Claude

この course で議論した PreToolUse と PostToolUse hooks 以外にも、さらに多くの hooks がある。次のものもある。

Notification - Claude Code が通知を送るときに実行される。これは Claude が tool を使う permission を必要とするとき、または Claude Code が60秒間アイドル状態だった後に起こる
Stop - Claude Code が応答を終えたときに実行される
SubagentStop - subagent(UI では「Task」として表示される)が終了したときに実行される
PreCompact - 手動または自動の compact 操作が起きる前に実行される
UserPromptSubmit - ユーザーが prompt を submit したとき、Claude が処理する前に実行される
SessionStart - session を開始または再開するときに実行される
SessionEnd - session が終了するときに実行される

ここが紛らわしい部分である。

あなたの commands への stdin 入力は、実行される hook の種類(PreToolUse、PostToolUse、Notification など)に基づいて変わる
その中に含まれる tool_input は、呼ばれた tool に基づいて異なる(PreToolUse と PostToolUse hooks の場合)

たとえば、TodoWrite tool の使用を監視していた PostToolUse である hook への stdin 入力のサンプルを次に示す。参考までに、それは Claude が to-do 項目を追跡するために使う tool である。

{
"session_id": "9ecf22fa-edf8-4332-ae85-b6d5456eda64",
"transcript_path": "<path_to_transcript>",
"hook_event_name": "PostToolUse",
"tool_name": "TodoWrite",
"tool_input": {
"todos": [{ "content": "write a readme", "status": "pending", "id": "1" }]
},
"tool_response": {
"oldTodos": [],
"newTodos": [{ "content": "write a readme", "status": "pending", "id": "1" }]
}
}

比較のため、Stop hook への入力の例を次に示す。

{
"session_id": "af9f50b6-f042-4773-b3e2-c3a4814765ce",
"transcript_path": "<path_to_transcript>",
"hook_event_name": "Stop",
"stop_hook_active": false
}

見てのとおり、あなたの command への stdin 入力は、hook(PreToolUse、PostToolUse、Stop など)と使われる matcher(PreToolUse と PostToolUse の場合)に基づいて大きく異なる。これは hooks の記述を難しくしうる。あなたの command への入力の正確な構造が分からないかもしれないのだ!

この課題に対処するため、次のようなヘルパー hook を作ってみるとよい。

"PostToolUse": [ // Or "PreToolUse" or "Stop", etc
{
"matcher": "*",
"hooks": [
{
"type": "command",
"command": "jq . > post-log.json"
}
]
},
]

提供された command に注目すること。これはこの hook への入力を post-log.json ファイルに書き込み、あなたの command に何が入力されたはずなのかを正確に検査できるようにする! これにより、あなたの command がどのデータを検査すべきかをはるかに簡単に理解できる。

---

### レッスン 19: The Claude Code SDK（Claude Code SDK）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312001>  

Open in Claude

注意: 上の動画では、もはや機能しない古いパッケージ名が使われている。現在のバージョンについては以下のテキストに従うこと。

Agent SDK を使うと、自分自身のアプリケーションやスクリプトから Claude Code をプログラムで実行できる。TypeScript と Python で利用可能で、CLI が使うのと同じ agent ループ(ファイルの読み取り、編集、tool の使用)をあなたの制御下で提供する。

Install

project 用のディレクトリを作成し、SDK パッケージを install する。

mkdir sdk-demo
cd sdk-demo
npm init -y
npm install @anthropic-ai/claude-agent-sdk

パッケージは @anthropic-ai/claude-agent-sdk である。(似た名前の @anthropic-ai/claude-code は CLI 自体であり、import できない。)

最小限の例

エディタを使って(または terminal で nano index.mjs として)index.mjs というファイルを作成し、次を貼り付ける。

import { query } from "@anthropic-ai/claude-agent-sdk";

const prompt = "List the files in the current directory";

for await (const message of query({ prompt })) {
console.log(JSON.stringify(message, null, 2));
}

実行する。

node index.mjs

JSON メッセージのストリームが表示される。これは CLI で見るのと同じ会話イベントで、tool 呼び出し、tool 結果、Claude のテキストを含む。

tools の制限

デフォルトでは、SDK は完全な tool セットにアクセスできる。それを絞るには、allowedTools を渡す。

for await (const message of query({
prompt,
options: { allowedTools: ["Read", "Glob"] },
})) {
// ...
}

これは CLI の --allowedTools フラグの SDK 版である。

次に進む先

SDK は CLI ができるすべてをサポートする。カスタム system prompts、MCP servers、hooks、subagents、session の再開などである。完全なリファレンスについては Agent SDK の documentation を参照すること。

---

### レッスン 20: Quiz on Claude Code（Claude Code に関するクイズ）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/308391>  

Open in Claude
Loading...

---

### レッスン 21: Summary and next steps（まとめと次のステップ）

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303238>  

Open in Claude

---
