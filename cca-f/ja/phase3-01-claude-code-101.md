<!-- markdownlint-disable -->

# Claude Code 101

**URL:** <https://anthropic.skilljar.com/claude-code-101>  
**所要時間:** 未記載  
**対象ドメイン:** D3  
**フェーズ:** Phase 3  

---

## カリキュラム

### レッスン 01: What is Claude Code?

**URL:** <https://anthropic.skilljar.com/claude-code-101/469788>  

Claude Code は agentic coding tool であり、あなたの codebase を理解し、files を編集し、commands を実行し、既存の developer tools と統合して、より速く物事を進める手助けをする。terminal、Visual Studio Code、Claude Desktop アプリ、web、そして JetBrains IDE で利用できる。

Claude Code は Claude と何が違うのか？

以前 Claude.ai を使ったことがあれば、Claude Code が何で違うのか疑問に思うかもしれない。Claude.ai と違い、Claude Code はあなたの files、terminal、そして codebase 全体に直接アクセスできる。code をあちこちにコピー&ペーストする代わりに、自分自身で中に入って作業を行う。

決定的な違いは、Claude Code が AI Agent として動作することにある。

Agent とは何か？

AI Agent とは、自身の環境と相互作用し、定義された目標を達成するためにアクションを実行できるソフトウェアである。その中核では、large language model がリアルタイムでループの中で動作することによって機能する。AI Agent は、目標に到達するのを助けるために、tools、external services、あるいは他の AI Agent にまでアクセスできる。

Claude Code は実際に何ができるのか？

実際の場面では次のようになる：

codebase を読み、理解する。Claude Code にある feature を説明してもらったり、code 全体にわたって bug を追跡してもらったりできる。
project 全体にわたって files を編集する。Claude Code はある function を refactor し、それを参照するすべての file を更新できる。
terminal commands を実行する。build script を実行し、tests を走らせ、packages をインストールし、その output を使って次に何をするかを決定できる。
web を検索する。documentation や最新の API references が必要なら、それを調べてくれる。

Claude Code を効果的に使う

Claude Code を効果的に使うには、次の3つの概念を念頭に置いておくこと：

context window。これは Claude の working memory（作業記憶）だと考えればよい。多くを保持できるが、すべてを一度には保持できない。ここで「agentic」な側面が出てくる ── Claude は codebase 全体を context に読み込むことなく、その中で答えを見つける戦略的な方法を探し出す。

許可を求める。デフォルトでは、Claude Code は commands を実行したり変更を加えたりする前にあなたに尋ねる。あなたが手を動かしたい派でも放任したい派でも、常にあなたが主導権を握っている。

間違いを犯すことがある。どんな tool もそうであるように、Claude Code は完璧ではない。あなたの意図を誤解したり、bug を混入させたり、解決策を過剰に作り込んだりするかもしれない。ループの中に留まることで、こうした問題を早期に発見できる。

まとめ

Claude Code は agentic coding tool である。codebase を読み、files を編集し、commands を実行し、external tools に接続して、より速く出荷する手助けをする。今すぐ terminal、VS Code、JetBrains、Claude Desktop アプリで使える。

---

### レッスン 02: How Claude Code works

**URL:** <https://anthropic.skilljar.com/claude-code-101/469789>  

Claude Code は典型的な chat アプリケーションとは異なる。その内部の仕組みを理解することで、より効果的に使えるようになる。

The Agentic Loop（エージェント的ループ）

Claude Code は agentic loop を通じて説明するのが最もよい：

Claude Code に prompt を入力する。
Claude は model とやり取りすることで必要な context を集め、model は text または Claude Code が実行できる tool call を返す。
アクションを起こす ── たとえば file を編集したり command を実行したりする。
結果を検証し、それがあなたの prompt が目指したことを達成しているかどうかを判断する。
達成していれば、Claude は終了して次の prompt を待つ。達成していなければ、ループに戻り、結果が完全で検証可能になるまで再試行する。

このループ全体を通して、あなたは context を追加したり、割り込んだり、model を誘導したりして、目標に向かわせる手助けができる。

Context

Claude は context window を持っており、これがあなたの会話、file の内容、command の output などをどれだけ保存・参照できるかを決定する。その上限に達すると、Claude Code は会話を compact する ── 何を削除または要約できるかを自動的に判断し、context window を使える大きさに戻す。

Tools

Tools は agent が機能する仕組みの背骨である。ほとんどの AI assistant は単に text を受け取って text を返すだけである。Tools は、Claude Code がタスク完了に近づくために code をいつ実行すべきかを判断できるようにする。これは file-reading tool、web search tool、あるいは他の数多くの capabilities でありうる。Claude Code は semantic understanding（意味的理解）を使って、いつ tool を呼ぶべきか、そしてその output をどう使うべきかを判断する。

Permissions

Claude Code にはいくつかの permission mode がある：

デフォルトの挙動: Claude は file を編集したり shell command を実行したりする前に、明示的な許可を求める。
Auto-accept: file は尋ねずに編集されるが、command は依然として承認が必要。
Plan mode: read-only tools を使って、作業を始める前に行動計画をまとめる。

これらはすべて settings file で設定できる。permissions をスキップする際は注意すること ── Claude Code に command を実行する自由を与えるということは、間違いが起きる前にそれを発見するのが難しくなることを意味する。

まとめ

Claude Code はいくつかの agentic な概念を組み合わせている：agentic loop、管理された context window、tools、そして設定可能な permissions ── これらすべてがあなたの terminal の中にある。codebase を読み、アクションを起こし、自分の作業を検証できる。これこそが、chat ウィンドウとは根本的に異なる点である。

---

### レッスン 03: Installing Claude Code

**URL:** <https://anthropic.skilljar.com/claude-code-101/469790>  

Claude Code は、terminal で使いたいときも、web で使いたいときも、IDE で使いたいときも、簡単にインストールできる。

Terminal

macOS、Linux、または WSL では、curl command を使えば一度にインストールできる。Homebrew が好みなら brew install も使えるが、この方法は auto-update をサポートしていない点に注意。

Windows では、いくつかの選択肢がある。PowerShell では Invoke-RestMethod command を使う。CMD では curl command を使う。winget command も利用できるが、Homebrew と同様、auto-update はされない。

インストール後は claude command を実行できるようになっているはずである。できない場合は terminal を再起動すること。project ディレクトリに移動して、次を実行する：

claude

color theme の選択や、Claude アカウント（Pro、Max、または Enterprise）でのサインイン、あるいは API key の使用といった初期セットアップの手順を進める。組織が Claude Enterprise アカウントを持っている場合は、必ずそのオプションを選択すること。

claude を実行したディレクトリがどこであれ、Claude Code はそのディレクトリとそのすべてのサブフォルダにアクセスできる。

Visual Studio Code

Extensions パネルを開き、「Claude Code」を検索する。青い verification check（認証チェック）のある Anthropic 製の extension を探す。install を押す。

インストール後、VS Code の再起動が必要な場合がある。起動したら、Ctrl/Cmd + Shift + P で command palette を開き、「Claude Code Open in New Tab」を検索する。sidebar に Claude のロゴが表示されていれば、それをクリックしてもよい。

VS Code extension は terminal とよく似た体験を提供する。settings で UI を使わず、terminal 体験を直接使うことを選ぶこともできる。

JetBrains

JetBrains Marketplace から Claude Code plugin をインストールする。インストール後、IDE を再起動する。再度開くと Claude のロゴが見える。それをクリックすると、editor と並んで動作する terminal 体験のペインが開く。

Desktop

Claude Desktop をインストールしてサインインすると、上部に「Code」というラベルの toggle が見える。見た目や使い心地は chat 側と似ているが、特定のフォルダ内で作業したり、permissions を変更したり、さらには cloud 環境で作業したりできる。

Web

web では、claude.ai/code にアクセスするか、chat アプリの sidebar にある「Code」ラベルをクリックすることで Claude Code にアクセスする。これは desktop アプリと似た動作をするが、GitHub repositories に限定される。

どれを使うべきか？

最先端に居たいなら、terminal が最良の選択肢である ── features はそこに最初に出荷される。IDE 統合は、Claude Code を code editor とより一体化させたい場合に、ほぼ同一の体験を提供する。

Desktop は、他のタスクをこなしている間に Claude をバックグラウンドで走らせておくのに最適である。

web 版の Claude Code は、GitHub repository を通じて project にリモートで作業したい場合の確かな選択肢である。

Claude Code をどう使うかはあなた次第である。

---

### レッスン 04: Your first prompt

**URL:** <https://anthropic.skilljar.com/claude-code-101/469791>  

Claude Code には、他の AI assistant と同じように話しかける。prompt を入力する際、あなたを守りつつ物事を楽にできる、考慮すべき点をいくつか挙げる。

Auto-Accept vs. Approval

Claude が提案するすべての file 変更を自動承認させるか、それとも毎回明示的な許可を求めさせるかを選べる。Shift + Tab を押すと mode を切り替えられる。

Approval mode: Claude は file を編集したり command を実行したりするたびに許可を求める。
Auto-accept mode: file 編集は自動的に承認されるが、command は依然としてあなたの許可が必要。

正解も不正解もない ── あなたが心地よいと感じるものでよい。

Plan Mode

Shift + Tab メニューの中に Plan Mode がある。Plan mode はあなたの prompt を受け取り、read-only tools を使って codebase を分析し、提案された実装を調査する。途中で明確化のための質問をしつつ、最後に実行可能な詳細な計画を返す。

Plan mode は、複雑な変更を計画したり、安全な code review を行ったりするのに最適である。多くの場合、ある feature に向けた multi-step の実装を Claude に任せることになるが、これはまさに Plan Mode が真価を発揮する場面である。

例: Dark Mode Toggle を追加する

例を一つ見ていこう。dark mode toggle が必要なアプリケーションがあるとする。project のルートディレクトリを開いて claude を実行する。Shift + Tab を数回押して Plan Mode に入り、次のような prompt を書く：

My app needs a dark mode implemented across the entire app. Can you create a toggle switch on the header that allows a user to toggle between light mode and dark mode? I need you to find a good contrast color that works based on my existing light theme.

Claude に計画を立てさせる。計画を確認して問題なければ、それを承認し、Claude に各ステップで承認を求めさせる。最後には、Claude が正確に何をしたか、どのようにその結論に至ったかを確認できる。

まとめ

Claude Code を使うときは、prompt をできるだけ具体的に書くようにすること。各ステップでループの中に留まりたければ、そうできる。実現したいことについて Claude にコードを実行する前に詳細を掘り下げさせるには、Plan Mode を使うこと。

---

### レッスン 05: The explore → plan → code → commit workflow

**URL:** <https://anthropic.skilljar.com/claude-code-101/469792>  

このコースから一つだけ持ち帰るとしたら、この workflow にしてほしい：Explore、Plan、Code、そして Commit。これがないと、ほとんどの人はいきなり Claude に code を書かせようとし ── それは後でより多くの軌道修正を招くことになる。

Explore and Plan

最初の2つのステップを最も速く処理する方法は Plan Mode を使うことである。plan mode では、Claude は file を編集できない ── 実装にどう取り組むかについての情報を集めるために file を読むだけである。

plan mode に入るには、text input の下に「Plan Mode」が見えるまで Shift + Tab を押す。それから次のような prompt を書く：

I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it.

Claude は関連する files を読み、いくつかの web 検索を実行し、行動計画を提示する。それを確認して、自分の基準を満たすか判断する。満たさなければ、特定の領域を修正するよう依頼する。

ここがコードを書く前なので、軌道修正をするのに最適な場所である。後で変更を加えるつもりがなく、codebase の概要だけが欲しい場合は、plan mode に入らずに explore subagent を実行することもできる。

Code

計画が良さそうに見えたら、「approve」を選択してそれを承認し、Claude にリスト項目を順に処理させる。Claude に file 編集を自動承認させるか、毎回尋ねさせるかを選べる。

Claude は計画を「完了」とみなす前に最善を尽くしてトラブルシューティングを行うが、時にはあなたが介入する必要がある。これが Plan Mode で作業することの利点である ── 実行後にも、どうやってその結果に至ったかという context が手元にあり、それが Claude の次の決定を導く助けになる。

coding フェーズをよりスムーズにするためのいくつかのコツ：

success criteria（成功基準）を定義する。Claude が結果に自信を持つには、「正しい」とは何かが明確である必要がある。計画を書くときにこれを明示すること。
tools を追加する。Claude の目標達成を助ける tools は、多くのやり取りを省いてくれる。たとえば web UI を構築しているなら、Claude in Chrome extension をインストールすれば、Claude Code が browser タブを制御して UI を直接テストできる。

test suite を含める。Claude が継続的に検証できる test suite を与える。Claude にテストを書かせることさえできる。これを引き渡す前に、false positive（偽陽性）を避けるため、テストが信頼できる真実の源であることを確認すること。

クイックヒント: Claude が同じ問題に繰り返しぶつかっていることに気づいたら、その解決策を CLAUDE.md file に保存するよう依頼するとよい。

Commit

自分自身で変更をテストして結果に満足したら、code を push する時である。commit する前に、subagent code reviewer を実行して自分の作業を見てもらう。subagent は codebase に新鮮な目を向ける ── セッション中に main agent が持ちうるバイアスを引きずらない。

それから Claude に、あなたのスタイルで commit message を生成させる。これを繰り返す。

まとめ

Claude Code を効果的に使うには、Explore、Plan、Code、Commit の workflow に従うこと：

Explore は project に必要な関連 context を Claude に与える。
Plan は Claude が成功を測るのに使う行動計画を作る。
Code は最終的な結果に落ち着くまでの、あなたと Claude の間のやり取りである。
Commit は code をレビューして push する手助けをし、次の feature に取りかかれるようにする。

---

### レッスン 06: Context management

**URL:** <https://anthropic.skilljar.com/claude-code-101/469793>  

Context は Claude の working memory（作業記憶）である。読むすべての file、実行するすべての command、送るすべての message ── それらすべてが context window の中で場所を取る。

Context Window とは何か？

context window は、Claude がメモリに保持できる空間の量だと考えればよい。prompt を入力したり、Claude が file を読んだり、tool call を実行したり、tool call の結果を受け取ったりするたびに、それらすべてが context window に追加されていく。空間は有限なので、その使い方を最適化することが重要になる。

Context がいっぱいになると何が起きるか

上限に近づくと、context window は自動的に compact される。compaction は重要な詳細を要約し、不要な tool call の結果を削除して空間を解放する。このプロセスでは詳細が失われる可能性がある点に注意。

Commands

/compact command で手動で compaction を実行できる。これはその時点までのすべてを compact する。以前作業した内容のメモリを保ちつつ、context 空間を解放したいときに便利である。

前のセッションのメモリを一切持たずに完全に最初からやり直したい場合は、/clear を実行する。これはすべてを削除する。

context の状態を確認するには、/context command を実行する。context のサイズの概要、最も空間を取っているカテゴリ、そして内訳を示す視覚的なグラフィックが得られる。

どちらをいつ使うか

一般的な目安：

特定の feature に取り組んでいて context の上限にぶつかっているが続ける必要があるときは /compact を使う。現在の feature に context を関連させ続けることが重要である。
新しい feature を始めたいときは /clear を使う。前の会話が新しいものにバイアスを持ち込むのを避けたいからである。セッションをまたいで Claude に覚えておいてほしいことは CLAUDE.md file に入れておけば、毎回ゼロから再発見する必要がなくなる。

Context 空間を節約するコツ

具体的にする。曖昧な prompt は一見小さく見えるが、長期的にはむしろ多くの context を消費する。明確な指示がないと、Claude は codebase をより多く探索し、自分で推論せざるを得なくなる ── これは詳細な prompt よりもはるかに多くの context 空間を取る。

MCP servers を管理する。MCP servers はデフォルトで、使っていなくても利用可能なすべての tools を context に読み込む。現在の project と無関係なことのために設定された servers があるなら、オフにすることを検討する。「Skills」も試せる。これは MCP servers と似た働きをするが、すべてを前もって context に読み込むことはしない。

subagents を使う。subagents は main agent と並行して動作するが、完全に独立した context window を持つ。「authentication endpoints はどこにあるか？」のように答えだけが必要なタスクでは、subagent が作業を行い、要約だけを main agent に返すので、主要な context をきれいに保てる。

まとめ

Claude Code 内で context を管理することは極めて重要である。長いセッションを要約するには /compact を、新たに始めるには /clear を使う。context window を効果的に使うには：prompt を具体的にし、現在の context が何を消費しているかを確認し、結果だけが必要なタスクを委譲するために subagents を使うこと。

---

### レッスン 07: Code review

**URL:** <https://anthropic.skilljar.com/claude-code-101/469794>  

Claude Code には git workflow を速くするいくつかの組み込み機能がある。それらを見ていこう。

Subagent でレビューする

PR を push する前に、Claude に subagent を使って変更をレビューするよう依頼する。subagent は新鮮な目で自身の context window の中で動作する ── セッションでちょうど code を書いた main agent のバイアスを引きずらない。

code-reviewer subagent を作るときは、read-only tools に制限すること。reviewer は問題を指摘すべきであって、file を編集すべきではない。チーム全員が同じ reviewer を使えるよう、subagent の設定を repo にチェックインしておく。

The /commit-push-pr Skill

/commit-push-pr skill は、commit、push、PR 作成をすべて一度のステップで処理する。それぞれを手動で行う代わりに、skill を実行するだけで Claude が引き受けてくれる。

CLAUDE.md に channels が記載された Slack MCP server を設定していれば、PR リンクを自動的にチームの channel に投稿してくれる。

--from-pr でのセッションリンク

Claude が gh pr create を通じて PR を作成すると、セッションは自動的にその PR にリンクされる。後で戻ってくる必要があるとき ── たとえば review コメントに対応したり、失敗した build を修正したりするとき ── は、次を実行する：

claude --from-pr <PR_NUMBER>

これで中断したところから正確に再開できる。

まとめ

push する前の偏りのない code review には subagent を使う。commit から PR までの全フローを一度のステップで処理するには /commit-push-pr を使う。そして後で PR の作業を再開するには --from-pr を使う。これらは小さな機能だが、日々の workflow から多くの摩擦を取り除いてくれる。

---

### レッスン 08: The CLAUDE.md file

**URL:** <https://anthropic.skilljar.com/claude-code-101/469795>  

Claude Code の最も有用な機能の一つが CLAUDE.md file である。これは Claude Code にあなたの project に関する持続的なメモリを与える。

それが解決する問題

CLAUDE.md file なしで Claude Code を開くと、毎回ゼロから始まる。codebase を再探索し、どんな dependencies が必要かを把握し、どの features がすでに実装されているかを理解しなければならない。時には思い込みをすることもあり、それが Claude を正しい方向へ導くのを難しくする。

CLAUDE.md はこれを解決する。これは project のルートに追加する Markdown file で、Claude Code はセッションを始めるたびに自動的にそれを読む。codebase 向けの onboarding スクリプトだと考えればよい。CLAUDE.md file の内容はあなたの prompt に追加される。

例

典型的な CLAUDE.md file は次のようになる：

# Project

This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands

- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style

- Use 2-space indentation
- Prefer named exports
- All API routes go in app/api/
- Use server actions instead of API routes where possible

これは分かりやすい。これで Claude Code に React component を作るよう頼めば、スタイリングに Tailwind を使うこと、そしてあなたの code 規約に従うことをすでに知っている。

CLAUDE.md はチームのためのもの

CLAUDE.md を version control に commit すれば（そしてそうすべきである）、チームもその恩恵を受けられる。誰のためのものかに応じて、実はメモリ file の階層がある：

Project レベルの CLAUDE.md は project のルートディレクトリに置かれる。チームと共有される。
User レベルの CLAUDE.md は設定フォルダに置かれる。これはあなただけのもので、すべての project に適用される。個人的な好みはここに入れる。

コツ

修正をメモリに保存する。Claude を繰り返し修正している自分に気づいたら ── たとえば API routes の代わりに常に server actions を使うように言っているなら ── そのルールをメモリに保存するよう Claude に明示的に依頼する。次に project を開いたときには、それを知っている。

project の docs を参照する。Claude に参照させたい documentation が project にあるなら、@ 記号と file path を使う：

## README.md

Please read if you need more info: @README.md

最初は CLAUDE.md なしで始める。CLAUDE.md file なしで project を始め、モデルをどこで絶えず軌道修正しなければならないかを見極めることを推奨する。こうすることで CLAUDE.md がコンパクトで、必要な情報だけに集中したものになる。準備ができたら /init を実行すれば、Claude が生成してくれる。

まとめ

Claude Code のセッションがフラストレーションになるか生産的になるかの違いは、しばしば context に行き着く ── そして CLAUDE.md file はその context を提供する手段である。あなたの技術スタック、好み、commands から始めて、進めながらそこに積み上げていく。

---

### レッスン 09: Subagents

**URL:** <https://anthropic.skilljar.com/claude-code-101/469796>  

Claude はタスクを subagents に委譲でき、subagents はそれを分解して構成タスクを並行して実行し、context 管理を改善する。各 subagent は自身の隔離された context window の中で動作する。

仕組み

Claude Code での context 管理は重要である。context window の多くは、codebase を探索する tool calls や調査のための web 検索の実行といったものに消費される。その探索中に Claude が発見することは、開発中の主要な feature に必ずしも関連しているわけではない。

ここで subagents の出番である。Claude は「この codebase を私のために探索してくれ」のようなタスクを処理するために subagent を生成する。subagent は自身の context window を持って並行して動作し、すべての探索作業を行い、終わったら発見した内容を要約してその要約を Claude に返す。

その結果：探していた答えが手に入り、そこに至るまでの道のり全体で主要な context が散らかることがない。

自分の Subagent を作る

Subagents は YAML frontmatter を持つ Markdown file で定義される。始める最も簡単な方法は、Claude に生成させることである。次を実行する：

/agents

そして「Create new agent」を選択する。agent のスコープを選び、目的を定義し、アクセスできる tools を選択し、さらには色を選ぶといった手順を進める。

Claude は subagent の名前、説明、prompt を生成する。これはまた、あなたが与える prompts に基づいて、いつ subagent を呼ぶべきかを Claude に伝える。

さらなるカスタマイズ

Subagents はさらにカスタマイズできる。いくつかのハイライト：

Persistent memory（持続的メモリ）は、subagent が会話をまたいでメモリを保持できるようにする。同じ project で一貫して使っている場合に最適である。
subagents に skills を preload するには、skill キーを追加して skills を名前で列挙する。main conversation の skills と違い、ここでは skill 全体が context に読み込まれる点に注意。

まとめ

context window をきれいに保つことは、Claude Code で生産的であり続ける最良の方法の一つである。subagents を使えば、agent をバックグラウンドで走らせて重労働を処理させ、答えだけを main context window に返すことができる。

もっと深く学びたい？専用コースをチェックしよう：Introduction to subagents

---

### レッスン 10: Skills

**URL:** <https://anthropic.skilljar.com/claude-code-101/469848>  

Video

Article

もっと深く学びたい？専用コースをチェックしよう：Introduction to agent skills

---

### レッスン 11: MCP

**URL:** <https://anthropic.skilljar.com/claude-code-101/469797>  

Model Context Protocol（MCP）は、Claude Code が external tools や data sources に接続できるようにするオープンな標準である。あなたが質問をすると、Claude はクエリをよりよく処理するためにいつそれらの tools を使うべきかを自動的に理解する。

あなたの context の多くは codebase の外にある ── databases、productivity アプリ、あるいは public repositories の中に。MCP はそのギャップを橋渡しする。

それで何ができるのか？

まず、agentic AI における「tools」の概念を理解することが重要である。Tools は、Claude Code のような agents に、タスクをより効果的に完了する助けとなるアクションを実行する能力を与える。これは、ただ text レスポンスが返ってくるだけの典型的な AI とは異なる。

たとえば、チームがプロジェクト管理に Linear を使っているなら、Linear MCP server を追加して特定の issues の詳細を取り込める。ある dependency の最新の documentation が必要なら、Context7 のような docs MCP server がそれを Claude Code に提供できる。

MCP Server を追加する

claude mcp add command で MCP servers を追加できる。主に2種類ある：

HTTP servers はリモートサービス用である。これらはサービス提供者によってホストされ、ネットワーク越しに接続する。
Stdio servers は、あなたのマシン上で動作するローカルプロセス用である。

Claude Code セッション内で /mcp を使えば servers を管理でき、何が接続されているかを確認し、status をチェックし、必要のない servers を無効化できる。

Server のスコープ設定

MCP servers は3つの方法でスコープを設定できる：

Local ── 現在の project でのみ、あなただけが利用できる。
User ── あなたのすべての project で利用できる。
Project ── version control にチェックインする .mcp.json file を使い、その codebase に関わる誰もがまったく同じ servers を自動的に得られる。

Context コスト

MCP servers は ── 積極的に使っていなくても ── context window に tool 定義を追加する。多くの servers を設定していると、これが利用可能な context を食いつぶす。/mcp を実行して何が接続されているかを確認し、積極的に使っていないものは無効化する。

ある tool に CLI の同等物がある場合（GitHub の gh や AWS の aws など）、CLI は持続的な tool 定義を追加しないので、より context 効率がよい。

代わりに Skill を使うことで利益を得られる場合もある。Skill は名前と説明が context に読み込まれ、Claude はそれを使う必要があると判断したときにだけ skill の全内容を読み込む。

MCP tools が context window の 10% を超えると、Claude Code は自動的に tool search mode に切り替わり、必要に応じて適切な tools を発見する ── ただしこれはそれほど確実には機能しないかもしれない。

まとめ

MCP は Claude Code を external tools や data sources に接続する。servers は claude mcp add で追加する。.mcp.json で project にスコープを設定すれば、チームが自動的にそれらを得られる。そして積極的に使っていない servers を無効化して context 使用量に目を配ること。

---

### レッスン 12: Hooks

**URL:** <https://anthropic.skilljar.com/claude-code-101/469798>  

Hooks は、Claude Code のライフサイクルの特定の時点で commands を実行できるようにする。hooks とこのコースで扱った他のすべてとの決定的な違いは、hooks は決定論的（deterministic）である ── 常に実行されるということである。

なぜ Hooks を使うのか

CLAUDE.md で Claude に、すべての file 編集の後に Prettier を実行するよう伝えることができる。たいていの場合は実行する。しかし時には実行しない。hook はそれを毎回、例外なく起こさせる。

よくあるユースケースには次のものがある：

file 編集後の自動フォーマット
コンプライアンスのための、実行されたすべての command のログ記録
production files の変更のような危険な操作のブロック
Claude がタスクを完了したときに自分に通知を送る

仕組み

Hooks は settings.json で設定する。イベントを選び、任意でどの tools に適用するかの matcher を設定し、実行する command を提供する。利用可能なイベントは：

PreToolUse ── tool call の前に実行
PostToolUse ── tool call の完了後に実行
UserPromptSubmit ── prompt を送信したとき、Claude が処理する前に実行
Stop ── Claude が応答を終えたときに実行
Notification ── Claude が通知を送るときに実行

これらは Claude Code 内の /hooks command を通じて、または settings.json を直接編集することで設定する。

実践的な例

最も一般的な hook：編集後の自動フォーマット。matcher を「Edit|MultiEdit|Write」とした PostToolUse hook を設定すれば、Claude が file を変更するたびに発火する。command は file 拡張子をチェックして適切な formatter を実行する ── TypeScript には Prettier、Go には gofmt、project が使うものは何でも。

PreToolUse でのブロック

PreToolUse hooks は、実行される前に tool calls をブロックできる。hook は tool 名と入力を JSON として stdin で受け取る。exit code が挙動を決定する：

Exit code 0 ── 通常通り進める。
Exit code 2 ── アクションをブロックする。stderr メッセージが feedback として Claude にフィードバックされ、Claude はなぜブロックされたかを知り、調整できる。
それ以外の exit code ── 非ブロッキングのエラーで、あなたに表示されるが何も止めない。

これがハードなルールを強制する方法である。production config ディレクトリへの書き込みをブロックする。rm -rf を含む bash commands をブロックする。main への commit をブロックする。チームが提案ではなく保証されるべきものは何でも。

チームと Hooks を共有する

.claude/settings.json で設定された hooks は project レベルであり、repo にチェックインできる。これにより、チーム全員が同じ hooks を自動的に得られる。command 内で CLAUDE_PROJECT_DIR 環境変数を使って project に保存されたスクリプトを参照すれば、Claude の現在の作業ディレクトリに関係なく機能する。

まとめ

Hooks は Claude Code の挙動に対する決定論的な制御を与える。自動フォーマットやログ記録には PostToolUse を使う。危険な操作のブロックには PreToolUse を使う。/hooks または settings.json で設定する。そしてチームも得られるよう repo にチェックインする。

何かが毎回必ず起こる必要があるなら、それを prompt に入れてはいけない。hook に入れること。

---

### レッスン 13: Course quiz

**URL:** <https://anthropic.skilljar.com/claude-code-101/469849>  

Loading...

---
