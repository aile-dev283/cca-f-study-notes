<!-- markdownlint-disable -->

# Claude 101

**URL:** <https://anthropic.skilljar.com/claude-101>  
**所要時間:** 約1時間  
**対象ドメイン:** D4  
**フェーズ:** Phase 0 - オリエンテーション  

---

## カリキュラム

### レッスン 01: Claude とは何か

**URL:** <https://anthropic.skilljar.com/claude-101/383389>  

**推定時間:** 15分

**学習目標**

このレッスンを終えると、次のことができるようになる。

- Claude とは何か、そして Claude の設計を導く原則を説明する。
- Claude の主要な能力と、単なるチャットボットとの違いを説明する。
- Claude にアクセスする方法（web、desktop、mobile）を識別する。

Claude は単なるチャットボットではなく、思考のパートナーとして設計された AI assistant である。このレッスンでは、Claude が他の AI tools とどう違うのか、仕事上のさまざまなタスクをどう支援できるのかを学ぶ。

**重要ポイント**

- Claude は helpful、harmless、honest であることを重視して設計されている。Constitutional AI により、人間の価値観に沿い、透明性を保って動作するよう訓練されている。
- Claude は要約、検索、創造的な執筆、共同執筆、Q&A、coding など、幅広い会話・テキスト処理タスクに対応できる。
- Claude は steerable で collaborative である。personality、tone、behavior を指示でき、望む出力に近づけるための会話がしやすい。
- Claude apps は Free、Pro、Max、Team、Enterprise の各 plan で利用でき、サインインしていれば conversations、projects、memory、preferences がデバイス間で同期される。

Claude は、writing and content creation、research and analysis、coding assistance、problem-solving and reasoning、learning new things を支援できる。大きな context window により長い文書を一度に扱え、Opus 4.7 などのモデルでは複雑な reasoning や coding にも強い。

### レッスン 02: Claude との最初の会話

**URL:** <https://anthropic.skilljar.com/claude-101/383390>  

**推定時間:** 20分

**学習目標**

- Claude で新しい会話を開始し、interface を操作する。
- 明確で具体的な言葉を使って効果的な prompt を書く。
- files や images を upload し、Claude に追加 context を与える。
- follow-up messages で Claude の response を反復改善する。

**重要ポイント**

- Claude は強力で知的な collaborator であり、仕事全体の能力を拡張する。Claude は AI intelligence を持ち、利用者は context と expertise を持ち込む。
- Claude に話しかける最善の方法は、同僚に話すように自然で簡潔な会話をすること。
- 次の会話の前に、setting the stage（役割・目的・背景）、defining the task（Claude にしてほしい行動）、specifying rules（style、tone、examples）を考える。
- 関連文書や背景情報を chat に upload すると、Claude はそれを response に反映する。
- Claude の力は一回きりの prompt ではなく、継続的で頻繁なやり取りによって発揮される。

例:

> "I'm the marketing lead at an indie streaming startup, and we're preparing an investor pitch deck for Series A investors. Can you research the current state of the independent film streaming market and identify key trends, competitor positioning, and growth opportunities? Use current web research with citations and structure it as a professional report of up to 5 pages, with an executive summary, market analysis, competitive landscape, and growth opportunities."

この prompt では、役割と目的を示し、具体的な調査タスクを依頼し、citations と report structure というルールを指定している。

Claude は PDF、DOCX、CSV、TXT、PNG、JPEG などの file types を扱える。documents の要約、images の説明、spreadsheets の trend analysis、code の説明や bug finding などに使える。

### レッスン 03: より良い結果を得る

**URL:** <https://anthropic.skilljar.com/claude-101/383392>  

**推定時間:** 15分

**学習目標**

- AI を使い始めたときのよくある課題を認識し、troubleshooting techniques で解決する。
- AI Fluency を定義し、より fluent に AI と働くための学習先を知る。
- 自分の workflow で Claude がどの程度機能するかを理解するために evals を設計する。

| 課題 | 起きていること | 試すこと |
|------|----------------|----------|
| Claude の response が一般的すぎる | prompt に自分の状況の context が足りない | audience、role、constraints を追加する |
| response が長すぎる、または短すぎる | Claude が適切な長さを推測している | 「2段落」「100 words 未満」など明示する |
| format に従わない | 内容は伝わっているが提示形式が曖昧 | 例を示す、または structure を明示する |
| もっともらしいが誤った情報が出る | Claude は特に具体的事実や niche topics で誤ることがある | 重要事項は独立に検証し、sources や confidence を求める |
| tone が合わない | Claude は helpful and professional に寄りやすい | desired tone を平易な言葉で説明し、例を示す |

最初の prompt が完璧な結果を生むことは少ない。初回出力を draft として扱い、具体的な feedback を与え、必要なら新しい chat でやり直す。

AI Fluency は、AI tools と効果的に協働する能力である。4D Framework は Delegation、Description、Discernment、Diligence の4つの力で構成される。

### レッスン 04: Claude desktop app: Chat, Cowork, Code

**URL:** <https://anthropic.skilljar.com/claude-101/440908>  

**推定時間:** 6分

Claude desktop app には Chat、Cowork、Code の3つの mode がある。Chat は claude.ai と同じ会話体験に quick entry、screenshots、dictation、connectors を加えたもの。Cowork は目標を渡すと tools and resources を使って作業を進める agentic tool。Code は software を作るための environment で、writing、testing、deployment まで扱う。

Cowork と Code は同じ engine、つまり Claude Code を土台にしている。どちらも local machine 上で動き、sub-agents を起動し、長い task を継続できる。

| mode | 向いている作業 |
|------|----------------|
| Chat | quick questions、brainstorming、drafting、bounded exchange |
| Cowork | multi-step research、tool use、finished deliverables |
| Code | codebase 内の development、terminal、git、software delivery |

### レッスン 05: projects 入門

**URL:** <https://anthropic.skilljar.com/claude-101/383393>  

Projects は、関連する conversations、knowledge、instructions をまとめる workspace である。繰り返し扱う context を project knowledge として置くことで、毎回同じ説明を貼り直さずに Claude と作業できる。

Projects は team での共有にも向く。資料、方針、style guide、過去の成果物を集約し、Claude が一貫した前提で応答できるようにする。

### レッスン 06: artifacts で作る

**URL:** <https://anthropic.skilljar.com/claude-101/383394>  

Artifacts は、Claude が作成する documents、code、web pages、visualizations などを conversation の横に表示して編集できる機能である。長い文章、HTML、React component、diagram、analysis など、単なる chat response では扱いにくい成果物に向く。

Artifacts を使うと、Claude と対話しながら成果物を段階的に改善できる。初稿を作り、style を直し、内容を追加し、format を調整するという流れを自然に行える。

### レッスン 07: skills を使う

**URL:** <https://anthropic.skilljar.com/claude-101/383396>  

Skills は、特定の作業の進め方、rules、templates、examples を Claude に教えるための仕組みである。組織固有の writing style、analysis workflow、file format、review checklist などを再利用可能な形にできる。

良い skill は、何をすべきかだけでなく、いつ使うか、どの順序で進めるか、どの出力形式にするかを明確にする。

### レッスン 08: tools を接続する

**URL:** <https://anthropic.skilljar.com/claude-101/383397>  

Connectors により、Claude は email、calendar、cloud storage、team messaging、project tools など、仕事が存在する場所にアクセスできる。これにより、資料を手で貼り付けなくても context を取得できる。

接続時は、アクセス範囲と権限を確認する。Claude が read only なのか、create/update までできるのかは connector によって異なる。

### レッスン 09: Enterprise search

**URL:** <https://anthropic.skilljar.com/claude-101/383398>  

Enterprise search は、組織内の documents、messages、knowledge bases から関連情報を見つけるための機能である。Claude は質問に答えるだけでなく、関連する社内資料を探し、要約し、比較できる。

有効に使うには、検索対象、判断基準、期待する出力を prompt で明確にする。

### レッスン 10: 深掘りのための research mode

**URL:** <https://anthropic.skilljar.com/claude-101/383399>  

Research mode は、より深い調査、source gathering、比較分析、synthesis に向いている。単発の質問よりも、複数の sources を確認し、論点を整理し、引用付きで結論をまとめる作業に適する。

調査では、scope、must-have sources、exclusions、出力 format を指定すると品質が安定する。

### レッスン 11: Claude in action: role 別ユースケース

**URL:** <https://anthropic.skilljar.com/claude-101/383401>  

Claude は role によって使い方が変わる。marketing では campaign planning や copy writing、sales では account research や follow-up drafting、engineering では code explanation や debugging、operations では process documentation や reporting に使える。

重要なのは、Claude に任せる task と、人間が判断する部分を切り分けることである。

### レッスン 12: Claude と働くその他の方法

**URL:** <https://anthropic.skilljar.com/claude-101/383402>  

Claude は web app、desktop app、mobile app、API、Claude Code、Cowork など複数の入口から使える。quick chat、deep work、software development、automation など、作業の形に応じて適切な入口を選ぶ。

### レッスン 13: 次に学ぶこと

**URL:** <https://anthropic.skilljar.com/claude-101/385338>  

次の学習では、AI Fluency、Claude Platform、Claude Code、MCP、agentic workflows へ進む。Claude をうまく使うには、単に prompt を書く力だけでなく、task design、context design、evaluation、responsible use が必要になる。

### レッスン 14: 修了証

**URL:** <https://anthropic.skilljar.com/claude-101/385349>  

このコースの完了により、Claude の基本的な使い方、主な機能、良い prompt の考え方、次に深めるべき学習領域を確認できる。
