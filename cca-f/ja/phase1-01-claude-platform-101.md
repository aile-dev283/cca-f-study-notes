<!-- markdownlint-disable -->

# Claude Platform 101

**URL:** <https://anthropic.skilljar.com/claude-platform-101>  
**所要時間:** 未記載  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** API・開発基盤  

---

## カリキュラム

### レッスン 01: What is the Claude Developer Platform?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486250>  

Claude Developer Platform は、Claude を使って programmatically に構築するための Anthropic の infrastructure である。browser で Claude とチャットする代わりに、自分の code から structured requests を送り、structured responses を受け取る。そして、どの model を使うか、何 tokens を消費するか、Claude がどの tools を使えるか、どの system instructions に従うか、といったあらゆる細部を制御できる。

具体的には、platform はいくつかの要素で構成される。

任意の language から呼び出せる REST API
さまざまな programming language 向けの SDK
command line interfaces
API keys を管理し、usage を監視し、managed agents を deploy し、prompts を test する console
platform の3つの layer

platform を捉えるのに有用な見方は、互いに積み重なった3つの layer として描くことである。

Primitives — Claude に最適化された API の building blocks。これは Messages API、tool use、files、web search、code execution、MCP servers、skills である。これらは実際に自分の code から呼び出す部品である。
Infrastructure — agentic systems を prototype を越えて build し scale するために必要なもの。managed agents、retries、queues、observability — 1つの Claude call が1000になっても物事を動かし続ける配管である。
Controls — それらの system を production で運用するための tools。dashboards や evals などである。これらは、稼働後にチームが使う dials である。

略語的に言えば、build with primitives, scale on infrastructure, run with control（primitives で build し、infrastructure で scale し、control で run する）。

この構造は Claude Console 自体にも反映されている。そこは infrastructure layer と control layer が存在する場所であり、build、agents の管理、analytics のための section がある。

実例: help desk の返信を draft する

ある基本的な help desk アプリを管理していて、機能を追加するよう依頼されたとしよう。チケットの内容に基づいて、チームの tone と guidelines に従って返信を draft するという機能である。これを UI 上の button に紐づけたい。

これは Messages API にぴったりの use case である。flow は次のようになる。

client を定義する
chat が参照している ticket を取得する
messages.create を呼ぶ
button が render するために response を返す
client = anthropic.Anthropic()

response = client.messages.create(
model="claude-haiku-4-5",   # Haiku: a good fit for a simple drafting task
max_tokens=1024,
system=TONE_AND_GUIDELINES,
messages=[
{"role": "user", "content": ticket_content}
],
)

draft = response.content

各 parameter は特定の役割を果たす。

model — どの model が request を処理するか。ここでは Haiku である。返信を draft するのは単純な task だからである。
max_tokens — Claude の response の長さの上限を決める。
system — system prompt であり、Claude が演じる role を定義する場所。関連する tone と guidelines はここに入る。
messages — objects の array。user role は Claude にこれが user 入力であることを伝える。ticket content はそこに入る。

その後、response を取得し、button が render するために返す。完了である。

「Claude に質問する」から「Claude が自分の product の一部になる」へ

その例で何が起きたかに注目してほしい。chatbot を一から build しているのではない。すでに存在する product に Claude を追加しており、API がそれを結線する手段なのである。

それが核となる考え方である。Claude Platform は、Claude の models、tools、infrastructure への API レベルのアクセスである。これが、ask Claude a question（Claude に質問する）から Claude is part of my product（Claude が自分の product の一部になる）へと進む方法である。

そして product に agents が必要になったとき、platform は単に model を渡すだけではない。managed agents によって、platform があなたの代わりにそれらを実行する。

まとめ
Claude Developer Platform は、Claude を使って programmatically に構築するための Anthropic の infrastructure である。REST API、SDK、CLI、そして keys、usage、managed agents、prompt testing のための console から成る。
3つの layer として考える。primitives（Messages API、tool use、files、web search、code execution、MCP servers、skills）、infrastructure（managed agents、retries、queues、observability）、controls（dashboards、evals）。
略語: build with primitives, scale on infrastructure, run with control。
1つの messages.create call で、model、response の長さ、system prompt、user 入力を完全に制御できる。help desk の返信 draft のような既存機能に Claude を結線するのに十分である。
platform は、Claude に質問することから Claude を product の一部にすることへとあなたを導く。そして managed agents により、あなたの agents を実行することもできる。

---

### レッスン 02: Your first API call

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486251>  

Claude に「hi」と言うのは心温まるかもしれないが、実際にはあまり役に立たない。このレッスンでは、20行に満たない code で、Claude に本物の入力を送り、structured insight を受け取る。

準備する

まず、platform.claude.com から API key を取得する。事前に credits を購入しておく必要がある。

API key を取得したら、version control の外に保つために `.env.local` ファイルに保存する。source files に key を hardcode すると、それが GitHub に漏洩することになる。代わりに environment files に保管すること。

次に、SDK を install する。

npm install @anthropic-ai/sdk
request の構造（anatomy）

すべての API call は messages.create function を通る。3つのものを指定する。

model — どの Claude model が request を処理するか
max tokens limit — response の長さの上限
messages の list — user または assistant role を持つ objects で、他の場所で Claude と会話するときと同様に構造化されている

最も基本的な形は次のとおりである。

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const msg = await client.messages.create({
model: "claude-opus-4-7",
max_tokens: 1024,
messages: [{
role: "user",
content: "Hello, Claude",
}],
});

実例: バグのある code を review する

「hello」よりも少し面白いものを Claude に与えてみよう。バグのある code を指し示し、review を依頼する。これが全体である。1ファイル、約20行の code である。

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const buggyCode = `
function add(a, b) {
return a - b;
}
`;

const response = await client.messages.create({
model: "claude-opus-4-8",
max_tokens: 1024,
system: "You are a terse senior code reviewer. Give feedback in one paragraph.",
messages: [
{ role: "user", content: `Review this code:\n${buggyCode}` },
],
});

for (const block of response.content) {
if (block.type === "text") {
console.log(block.text);
}
}

ここで注目すべき2点。

system prompt は persona を形作る場所である。私はおしゃべりではなく簡潔な senior reviewer がほしいので、そう言うだけである。
response の message.content は string ではなく blocks の array である。基本的な text reply では通常 type text の block が1つだけだが、Claude は複数の block — text、tool calls、thinking — を返すことがあるので、常に loop して type を確認する。

実行すると、Claude は add が減算していることを見抜き、1段落でそれを伝える。それだけである。それが API call の全体である。

script から product へ

実際の product では、この同じ messages.create の形が、summarize endpoint のようなものの engine になる。database から meeting transcript を取り出し、「extract insights and risks（洞察とリスクを抽出せよ）」という system prompt とともに Claude に渡し、結果を row に保存し直し、UI に返す。同じ call を route handler でラップしただけである。

まとめ
最初の API call は、model、token limit、messages を持つ messages.create function である。
API key は `.env.local` ファイルに保存して version control の外に保つ。
Claude の振る舞いを形作るために system prompt を追加する。
response content は blocks の array である。各 block の type を loop して確認する。
ここから先、すべてはこの pattern の上に積み上がる。

---

### レッスン 03: Choosing the right model

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486252>  

Claude を使ったアプリを出荷するとする。どの model を選ぶか。最も賢いものを default にすると、API bill に驚くことになる。最も安いものを選ぶと、output が持ちこたえないかもしれない。各 model には異なる trade-off があり、適切なものを選ぶことは quality と cost の両方に影響する。

model の tiers

Anthropic は現在4つの model tier を提供しており、API call の model parameter で選択する。

このコースの時点では Claude Fable は generally available ではなく、上の video には反映されていない点に注意。Claude Fable と Claude Mythos についてはこちらで詳しく学べる。

Claude Fable は、これまでで最も capable な model である。Opus の上に位置する新しい tier で、最も困難な challenge のために作られている。Opus より大幅にコストが高いので、その追加の能力に見合うだけの価値がある仕事のために取っておくこと。
Claude Opus は3つの core model family のうち最も capable だが、3つの中で最も遅く、最もコストが高い。deep reasoning、complex analysis、multi-step coding、nuanced writing に使う。
Claude Haiku は最も速く、最も低コストで、最大の知能ではなく speed と cost 効率に最適化されている。classification、extraction、routing のような high-volume・low-complexity の仕事に使う。
Claude Sonnet はちょうど良い位置にある。intelligence、speed、cost のバランスが取れた組み合わせで、ほとんどの production work でうまく機能する。
まず simple evaluation から始める

production code を書く前に、simple evaluation を設定する。example inputs の集合を各 model に通し、自分の use case にとって good output が何を意味するかと照らして採点する。凝ったものは要らない。実際の workload からの代表的な example を20〜30個あれば始めるのに十分である。

そして tier を上に向かって進む。

まず Haiku で example を通す。quality が持ちこたえれば完了で、大量のお金を節約したことになる。
持ちこたえなければ、Sonnet に上げる。
task が必要とするときだけ Opus に手を伸ばす。
tier を横並びで比較する

tier 間の違いを、話すだけでなく実際に見てみよう。同じ prompt を3つの model すべてに送り、latency と token counts を観察する。

models = ["claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-7"]

for model in models:
response = client.messages.create(
model=model,
max_tokens=300,
messages=[{"role": "user", "content": prompt}],
)
print(model, response.usage)

ここで起きていることは2つ。

loop は各 request で model フィールドを入れ替える。同じ prompt、同じ max tokens で、変わるのは model だけである。
response.usage は input と output の tokens を API から直接返す。これがあなたの bill が計算される基になる。

実行すると、3つの model と3組の数字が見える。Opus は最も時間がかかり、最も洗練された読み心地だが、2文の定義に対してはその洗練さは無駄である。Sonnet は書き方を少し締める。そして Haiku は、しばしば1秒未満で、非常に有能な2文の答えを返してくる。この種の場面には正直完璧である。

そしてそれこそが要点である。適切な model は、その output を実際に出荷できる中で最も安いものである。定義に対しては Haiku で十分である。規制対応の draft に対しては、同じ比較を行い、おそらく Opus に行き着くだろう。eval は毎回まったく同じ形である。

異なる仕事を異なる model に振り分ける

実際のアプリでは、同じ endpoint の中で異なる種類の仕事を異なる model に振り分ける。document processing route を持つ operations dashboard を考えてみよう。

入ってくるすべての file は Haiku で classify される。
client updates は Sonnet で draft される。
RFP responses だけが Opus に手を伸ばす。

1つの queue、3つの model、task ごとに選択。

まとめ
Anthropic は3つの model tier を提供する。難しい問題には Opus、日常の仕事には Sonnet、量には Haiku。
production code を書く前に simple evaluation を設定する。実際の workload からの代表例を20〜30個。
eval は Haiku から上に向かって実行し、その output を実際に出荷できる中で最も安い model で止める。
response.usage は input と output の tokens を報告する。これがあなたの bill の基になる。
production では、すべてに1つの model を選ぶのではなく、同じ endpoint の中で異なる task を異なる model に振り分ける。

---

### レッスン 04: The agent loop explained

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486254>  

API calls はしてきたが、単一の call は1つの response を返すだけである。workflow を automate したいなら、Claude は行動し、結果を見て、次に何をするかを決め、続行する必要がある。その pattern こそが、人々が agentic workflows と言うときに意味するものである。

agent とは実際に何か

agent は、Claude の autonomous な version であり、人間を間に挟まずに messaging loop の両側を実行する。agent は task を受け取り、tool を選び、Claude がその task が完了したと判断するまで loop の中で code を実行する。

agent loop を実装する最も簡単な方法は次のようになる。

利用可能な tools とともに Claude に message を送る。
Claude は、最終回答か、あなたが定義した tool を使うリクエストのいずれかで応答する。
あなたの code がその tool を実行する。
結果を Claude に送り返す。
stop reason が end_turn になるまで繰り返す。

turn が交互になる会話だと考えるとよい。user が口火を切り、agent が tool を呼び、tool が結果を返し、agent は答えを得るまで続行する。

最小の動作例

database や UI を引き込まずにこの loop が end to end で動くのを見るために、get_weather という偽の tool を結線し、Claude に「今日の Austin で何を着るべきか」を尋ねる。Claude は自力で天気を知る術がないので、tool を呼び、結果を読み、それから答えを返さなければならない。

これがその script の全体である。

import anthropic

client = anthropic.Anthropic()

# The tools array tells Claude what's available

# a name, a description, and a JSON schema for the inputs

tools = [
{
"name": "get_weather",
"description": "Get the current weather for a city.",
"input_schema": {
"type": "object",
"properties": {
"city": {
"type": "string",
"description": "The city to get weather for",
}
},
"required": ["city"],
},
}
]

# run_tool is just a hardcoded lookup

# In a real app, this would hit your database, an API, whatever

def run_tool(name, tool_input):
if name == "get_weather":
return f"Weather in {tool_input['city']}: 95F, sunny"
raise ValueError(f"Unknown tool: {name}")

messages = [
{"role": "user", "content": "What should I wear in Austin today?"}
]

# The agent loop. Each iteration sends messages to Claude

# and switches on the response's stop reason

while True:
response = client.messages.create(
model="claude-sonnet-4-6",
max_tokens=1024,
tools=tools,
messages=messages,
)

if response.stop_reason == "end_turn":

# Claude is done. Print the final text and break

for block in response.content:
if block.type == "text":
print(block.text)
break

if response.stop_reason == "tool_use":

# Find the tool use blocks in the response and run each one

tool_results = []
for block in response.content:
if block.type == "tool_use":
result = run_tool(block.name, block.input)
tool_results.append(
{
"type": "tool_result",
"tool_use_id": block.id,
"content": result,
}
)

# Push the assistant's response and our tool results

# back into messages, then loop again so Claude can answer

messages.append({"role": "assistant", "content": response.content})
messages.append({"role": "user", "content": tool_results})

注目すべき3つの部分。

tools array は Claude に何が利用可能かを伝える。name、description、inputs の JSON schema である。
run_tool は単なる hardcoded lookup である。実際のアプリでは、これは database、API、何であれそれにアクセスする。
loop が agent loop である。各 iteration は messages を Claude に送り、response の stop reason で分岐する。end_turn では Claude が完了している。最終 text を print して break する。tool_use では tool use blocks を見つけ、それぞれを実行し、assistant の response と自分の tool results を messages に戻して、Claude が答えられるよう再度 loop する。
実行する

script を実行すると、2つの turn が見える。

turn 1: stop reason は tool_use。Claude は Austin に対して get_weather をリクエストし、あなたの code は気温と状況を返す。
turn 2: stop reason は end_turn で、Claude は軽くて通気性のあるものを着るよう伝える。

2つの API call、1つの tool 実行、1つの最終回答。それが loop の全体である。Claude API で build するものすべては、これに似たものになる。

production での同じ loop

実際の環境では、この同じ loop が auto-review endpoint のようなものを動かす。構造報告書を読み、tool 経由で関連する building codes を参照し、作業しながら risk findings を1つずつ database に書き戻す compliance agent である。

loop の形は、あなたが今実行したものとまったく同じである。違いは次のとおり。

mock の weather loo の代わりに本物の tools

---

### レッスン 05: What is tool use?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486255>  

あなたの既存の workflow は、project management software、databases、files など多くの異なる technology に依存している。Claude はそれらを自分で勝手に確認することはできない。代わりに tools に依存する。tools は Claude に外部 data と action へのアクセスを与える。

tool とは何か

簡単に言えば、tool はあなたが定義し Claude に公開する function である。何をするか、どんな inputs を取るかを記述すると、Claude がそれをいつ呼ぶかを決める。

内面化すべき重要な点はこれである。Claude は tool を実行しない。あなたの code が実行する。flow は次のようになる。

Claude が tool call をリクエストする。
あなたの code が function を実行する。
結果が Claude に戻り、Claude は続行する。
tool はどのように定義されるか

tools は3つの部分を持つ JSON schemas である。name、description、input schema。これらを request body の tools array として Claude に渡す。

description は、Claude がその tool を呼ぶかどうかを決めるために読むものである。曖昧な description を書くと、tool use が悪くなる。これは agents が誤作動したり、利用可能な tools をつかまない最大の理由である。具体的に書くこと。

tool definition は次のようになる。

{
"name": "lookup_building_code",
"description": "Look up a specific building code section by its identifier. Returns the full text of that code section.",
"input_schema": {
"type": "object",
"properties": {
"section": {
"type": "string",
"description": "The building code section to look up"
}
},
"required": ["section"]
}
}

では、これを使うと何が起きるか。agent に compliance report を送ったとしよう。最初の turn で、Claude は stop_reason: "tool_use" を返してくる。それが私たちの signal である。その response は次のようになる。

私たちの loop は Claude がリクエストした parameter で lookup_building_code を呼び、その結果を tool result として戻す。tool call の id に紐づいた tool_result block を含む user message である。

そして Claude は続行する。その時点で、Claude が必要とするものを得るまで、tools を呼び結果を Claude に返し続けられる。

複数の tools: Claude に選ばせる

1つの tool は有用だが、興味深いのは Claude に複数の tools を与えて、どれをどの順で使うかを選ぶのを見ることである。

この場面を想像してほしい。Denver への3日間の旅行の荷造りをしていて、今日の天気と今後数日の forecast の両方がほしい。そこで、1つではなく2つの tools を宣言する。

const tools = [
{
name: "get_weather",
description: "Get today's current weather for a city.",
input_schema: {
type: "object",
properties: {
city: { type: "string", description: "The city to check" }
},
required: ["city"]
}
},
{
name: "get_forecast",
description: "Get the weather forecast for the next few days for a city.",
input_schema: {
type: "object",
properties: {
city: { type: "string", description: "The city to check" }
},
required: ["city"]
}
}
];

loop は、すでに見てきた agent loop とまったく同じである。唯一新しい部分は、switch 文で tool name に応じて dispatch する runTool function である。この code の block は、あなたの code が実際に実行される場所にすぎない。

function runTool(name, input) {
switch (name) {
case "get_weather":
return getWeather(input.city);
case "get_forecast":
return getForecast(input.city);
}
}

while (true) {
const response = await client.messages.create({
model: "claude-sonnet-4-6",
max_tokens: 1024,
messages,
tools,
});

if (response.stop_reason !== "tool_use") {
// Claude is done — this is the final answer
break;
}

messages.push({ role: "assistant", content: response.content });

const toolResults = response.content
.filter((block) => block.type === "tool_use")
.map((block) => ({
type: "tool_result",
tool_use_id: block.id,
content: runTool(block.name, block.input),
}));

messages.push({ role: "user", content: toolResults });
}

そしてそれが pattern の全体である。3つ目の tool がほしい？ array に追加し、switch に case を追加すれば完了である。

これを実行すると、Claude が get_weather を呼び、それから get_forecast を呼ぶのが見える。同じ turn の中のこともあれば、1つずつのこともある。それから答える。重ね着を荷造りせよ、今日は snow flurries を見込め、週を通して暖かくなる、と。

ここで Claude がどう選んだかに注目してほしい。description を読み、あなたの prompt を「今日の天気」と「今後数日」にマッピングし、それぞれに適切な tool を選んだ。だからこそ tool descriptions が本当に重要なのである。

tool runner: ボイラープレートを省く

今書いたものに、すでに2つの red flag に気づいているだろう。

2つの単純な lookup にしては code が多すぎる。
実際の codebase では、自分が持つすべての function に対して手で JSON schemas を書きたくない。code を二度書くようなものである。

そこで tool runner の出番である。これは TypeScript、Python、Ruby 用の Claude SDK に同梱されている。runner はあなたの実際の functions を取り、types と docs を読んで schema を構築し、tool 全体を処理する

---

### レッスン 06: What is thinking?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486256>  

一部の task は、素早い答え以上のものを必要とする。Claude は応答する前に問題を解き進めることができる。extended thinking と呼ばれる機能である。このレッスンでは、thinking とは何か、どう有効にするか、そしていつ実際に役立つかを見る。

避けようとしている failure mode はこれである。multi-step の質問を model に尋ねて即座に答えさせると、自信満々に間違えることがある。

extended thinking とは何か

extended thinking は、Claude が最終的な response を生成する前に step by step で reason することを可能にする。有効にすると、Claude は internal reasoning tokens — しばしば chain of thought と呼ばれる — を生成し、それから答えを届ける。reasoning は隠されていない。最終 text と並んで response の中に見ることができる。

Opus 4.7 での adaptive thinking

Opus 4.7 では、thinking は adaptive である。token budget を選ばない。単に有効にするだけで、Claude がいつ・どれだけ think するかを動的に決める。

Claude がどれだけ think するかを制御するには、effort parameter を使う。1つの落とし穴: それは thinking block の隣ではなく output_config の中に入る。levels は次のとおり。

low
medium
high (default)
xhigh (extra high)
max
いつ使うか（そしていつ省くか）

extended thinking が役立つのは:

数学と multi-step logic
code debugging
規制分析
trade-offs や選択肢の比較を伴うもの

単純な classification、extraction、ボイラープレートには省くこと。それらの task では、結果を実際に改善せずに latency と cost を追加するだけである。

thinking の実演

動くのを見てみよう。これは1つの weather tool を持つ agent loop で、Claude に San Francisco を起点とする road trip を計画するよう尋ねる。2か所の立ち寄り先で、天気と運転時間を比較考量する。これは本物の trade-off であり、thinking がその価値を発揮する種類の質問である。

import anthropic

client = anthropic.Anthropic()

weather_tool = {
"name": "get_weather",
"description": "Get the current weather for a city.",
"input_schema": {
"type": "object",
"properties": {
"city": {"type": "string", "description": "City name"}
},
"required": ["city"],
},
}

response = client.messages.create(
model="claude-opus-4-7",
max_tokens=16000,
thinking={"type": "adaptive"},
output_config={"effort": "high"},  # low | medium | high | xhigh | max
tools=[weather_tool],
messages=[
{
"role": "user",
"content": "Plan a road trip out of San Francisco with two stops, "
"weighing weather and drive time.",
}
],
)

これを実行すると、output は通常より興味深い。Claude が trade-offs を解き進める thinking blocks が見え、続いて各都市を確認する tool calls、そして最後に実際の推奨を含む text block が見える。

reasoning は可視である。それこそが要点である。

なぜ production で重要なのか

production アプリでは、これは問題を1つずつ見つける agent と、それらを結びつける agent との違いである。compliance review アプリを考えてみよう。auto-review call で adaptive thinking を有効にすると、agent は report の section をまたいで reason できる。section 3 の wind load 仕様が、文書の他の場所の material 仕様と矛盾しているといったことを捉えられる。

まとめ
extended thinking は、Claude が答える前に reason する余地を与え、その reasoning は response の中に可視である。
Opus 4.7 では、thinking: {"type": "adaptive"} で有効にする。token budget は不要で、Claude がいつ・どれだけ think するかを決める。
深さは output_config 内の effort parameter で調整する。low、medium、high（default）、xhigh、max。
難しく trade-off の多い問題に使う。単純なものには省く。そこでは latency と tokens を費やすだけである。

---

### レッスン 07: Built-in tools

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486258>  

独自の custom tools を build できるが、一部の能力はありふれているので Anthropic が事前構築済みで提供している。code を書かない。sandbox を host しない。ただ tool を宣言するだけで、Anthropic がそれを実行する。

Server tools: あなたが宣言し、Anthropic が実行する

Anthropic は、自社の infrastructure 上で動く server tools を提供する。これらをあなたが実行するのではない。Anthropic が実行する。つまり、これらの call には agent loop が不要である。Claude が自分で tools を呼び、結果は同じ response の中に返ってくる。

主なものは:

Web search — インターネットを検索し、citations 付きの結果を返す
Code execution — sandbox の中で Python を書いて実行する
Web fetch — URL から full content を取得する
1ファイルの中の2つの server tools

大きなものをいくつか1ファイルで見てみよう。2つの messages.create call で、1つは web search、もう1つは code execution である。

import anthropic

client = anthropic.Anthropic()

# Call 1: web search — Anthropic runs the search server-side

search_response = client.messages.create(
model="claude-opus-4-8",
max_tokens=1024,
tools=[{"type": "web_search_20260209", "name": "web_search"}],
messages=[
{"role": "user", "content": "What is Anthropic's latest model release? Answer in one sentence."}
],
)

for block in search_response.content:
if block.type == "server_tool_use":
print(f"Tool call: {block.name} — {block.input}")
elif block.type == "text":
print(block.text)

# Call 2: code execution — Claude writes and runs Python in a sandbox

code_response = client.messages.create(
model="claude-opus-4-8",
max_tokens=1024,
tools=[{"type": "code_execution_20260120", "name": "code_execution"}],
messages=[
{"role": "user", "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"}
],
)

for block in code_response.content:
if block.type == "server_tool_use":
print(f"Tool call: {block.name} — {block.input}")
elif block.type == "bash_code_execution_tool_result":
print(f"stdout: {block.content.stdout}")
elif block.type == "text":
print(block.text)

注目すべき2点。

ここには agent loop がない。stop_reason で分岐しない。tool results を戻さない。Anthropic が server-side で tool を実行し、response はすでに結果を含んでいる。
response には新しい block types がある。tool call のための server_tool_use block、output のための code execution tool result block、そして通常の text blocks である。
実行する

web search では、Claude の tool call が print され、続いて最新の model release についての1文の答えが、search citations を折り込んで表示される。

code execution では、Claude が書いた実際の Python、それを実行した sandbox の stdout、そして最後の text 答えが見える。

search crawler を立ち上げる必要はなかった。Python sandbox を実行する必要もなかった。2つの tools を宣言して、両方を無料で得た。

もう1つのカテゴリ: client tools

もう1つのカテゴリが存在することを知っておく価値がある。client tools はあなたの code が動く場所で動く。Claude SDK に同梱されているので、自分で schema を定義する必要はない。2つの例:

Memory — Claude が session をまたいで memory を読み書きする
Bash — Claude が commands を実行できる persistent な bash shell

これらは custom tool と同じ形を持つが、SDK が schema と妥当な runner を提供する。

なぜ production で重要なのか

production アプリでは、これは本来なら数週間かかる機能への最短経路である。web search は、draft 内のすべての数値的・規制的主張を live な web に照らして検証する fact-check endpoint を動かせる。

ただし1つの注意点。インターネット上で検証されたからといって、それが真実とは限らない。常に Claude の作業を再確認すること。

まとめ
Server tools — web search、code execution、web fetch — は tools array で宣言する。Anthropic が実行する。
結果は同じ response の中で得られ、agent loop は不要である。通常の text blocks と並んで server_tool_use と tool result blocks を探す。
memory や bash のような client tools はあなたの code が動く場所で動くが、SDK が schema と runner を提供する。
「Anthropic によって host される」という考えは最後まで scale する。managed agents はそれを1つの tool ではなく agent 全体に適用する。

---

### レッスン 08: Skills

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486259>  

Skills は、Claude が専門的な task でのパフォーマンスを向上させるために動的に読み込む、instructions、scripts、resources のフォルダである。すべての Skill の核には SKILL.md ファイルがある。一度 upload して、それから任意の messages.create call に attach する、パッケージ化された instructions の集合である。あなたは Claude に、あなたのやり方を教えている。status report の format、review checklist、release notes などである。Claude は Skill を読み、手順に従い、あなたの形で output を生成する。

Skills と tools

両者は異なる問題を解くので、違いを明確にしておく価値がある。

Tools は Claude を data と action に接続する。「このコード section を調べる」「このメールを送る」— Claude が tool を呼び、何か別のものが実行する。
Skills は Claude に手順を教える。「このテンプレートに従って daily status report を生成する」— Claude が読んで従う playbook であり、ときには同梱された scripts を自分で実行することも意味する。

覚えやすい言い方: tools は Claude が何をできるか、Skills はあなたがどうやってほしいか、についてである。

もう1つ知っておく価値があること。Skills は起動時に context へ完全には load されない。最初は name と description だけが load される。agent が Skill が関連すると判断したとき、完全な Skill を context に load する。これにより、多くの Skills が利用可能でも context を lean に保てる。

Skill を upload する

Skills は workspace に一度 upload し、その後 ID で参照する。Claude Platform 上で直接 upload することも、programmatically に行うこともできる。

skill = client.beta.skills.create(
display_title="Status Report Generator",
files=files_from_dir("status-report-skill"),  # folder containing SKILL.md
)

print(skill.id)  # reference this ID in future requests

この例では、status report generator がほしい。良い status report を構成するすべてのルール — sections、tone、要約の仕方、blockers の扱い方 — は事前にパッケージ化された Skill の中にある。activity log そのものは、request 時に渡される単なる string である。

Skill を request に attach する

Skills は container configuration を通じて request に attach される。container の中の skills array であり、各 entry が skill_id と version を指定する。status report generator のための full call を示す。

response = client.beta.messages.create(
model="claude-sonnet-4-5",
max_tokens=4096,
betas=["skills-2025-10-02", "code-execution-2025-08-25"],
container={
"skills": [
{
"type": "custom",
"skill_id": skill.id,
"version": "latest",
}
]
},
tools=[
{
"type": "code_execution_20250825",
"name": "code_execution",
}
],
messages=[
{
"role": "user",
"content": f"Generate the daily status report from this activity log:\n\n{activity_log}",
}
],
)

指摘しておく価値のある点がいくつか。

標準のものではなく client.beta.messages.create を呼んでおり、skills 機能を beta header 経由で渡している。この video の時点では、Skills はまだ beta 機能である。
container.skills は Skill が attach される場所である。list なので、1つの call に複数の Skills を重ねられる。
ここでは code execution も有効にしている。Skills はしばしば code execution とよく組み合わさる。Skill の手順が、terminal で scripts を実行するような実際の作業を行えるからである。
実行する

output は、Skill が指定したとおりにきっかり format された status report である。sections、tone、blocker の扱い — そのすべては、あなたが upload した SKILL.md ファイルから来る。user prompt は1行で、手順は Skill の中にある。

production アプリでは、これはチームが機能全体で output を標準化する方法である。この daily status report endpoint では、すべての PM が同じ構造、同じ tone、同じ sections を、同じ順序で得る。誰も template を prompt にコピペすることなく。

まとめ
Skills はあなたの手順をパッケージ化する。SKILL.md ファイル（と任意の scripts や resources）が、あなたがどうしてほしいかを Claude に教える。
Tools と Skills: tools は Claude が何をできるか、Skills はあなたがどうしてほしいか、についてである。
Skills は段階的に load される。起動時には name と description だけが load され、agent が使うと判断したとき完全な Skill が context に load される。
client.beta.skills.create で一度 upload し、任意の messages.create call で container.skills を使って attach する。list なので複数の Skills を重ねられる。
Skill の手順が実際の作業を行う必要があるときは code execution と組み合わせる。
how が what と同じくらい重要なときに Skill に手を伸ばす。

---

### レッスン 09: MCP

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486260>  

tools、skills、connectors がある。ではなぜ MCP が存在するのか。一見すると、API の上に積み重ねられた2つ目の API のように見える。もっともな疑問である。そして答えは、integration code を誰が maintain するかに帰着する。

maintenance の問題

あなたの agent が、Asana から tasks を引き出し、Google Calendar を確認し、Slack を検索する必要があるとしよう。すべて一度に。custom tools では、3つの integration を書かなければならない。その部分は実行可能である。痛みを伴うのはその後である。それらの service が API を変更するたびに、それらの integration を maintain しなければならない。それは頻繁に起きる。おめでとう、あなたは今や third-party API wrappers の山を maintain している。

MCP はその maintenance を service provider に移す。Asana が MCP server を公開する。Slack が公開する。Google が公開する。各 server は、descriptions、schemas、authentication とともに、自身の tools を標準的な protocol を通じて公開する。彼らの API が変わると、彼らが自分の server を更新する。あなたは何も変えない。

tools と skills と MCP

これら3つの機能は異なる仕事をする。

Tools は Claude をあなたの internal systems に接続する。あなたの database、project tracker、proprietary API。code はあなたが所有するので、maintenance もあなたが所有する。
Skills は Claude に手順を教える。あなたの report テンプレート、review checklist。Skills は instructions であり、必ずしも integration ではない。
MCP は Claude を third-party services に接続し、そこでは service provider が integration を maintain する。あなたが Asana wrapper を書くのではない。Asana が書いた。

短い言い方: tools はあなたのもの、skills はあなたのプロセス、MCP は他のみんなのもの、のためである。

MCP server に接続する

MCP の感覚をつかむ最もきれいな方法は、Claude を任意の MCP server に向け、そこに何があるかを発見させることである。この例では、Linear MCP server を使う。接続詳細と auth token は .env ファイルに保存する。

request の中で2つの部分が連携する。mcp_servers key は接続を宣言する。type、URL、参照用の name、そして任意で auth token である。次に、type mcp_toolset の tool が、その server から Claude が使える tools を構成する。default はすべてだが、絞り込みたい場合はここで行う。

import os
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
model="claude-opus-4-8",
max_tokens=1000,
messages=[
{"role": "user", "content": "What tools do you have available?"}
],
mcp_servers=[
{
"type": "url",
"url": "https://mcp.linear.app/mcp",
"name": "linear",
"authorization_token": os.environ["LINEAR_MCP_TOKEN"],
}
],
tools=[
{
"type": "mcp_toolset",
"mcp_server_name": "linear",
}
],
betas=["mcp-client-2025-11-20"],
)

print(response)

tool schema を1つも書いていないことに注目してほしい。Claude が server を introspect し、tools とその schemas の list を取得し、prompt に適切なものを選ぶ。このレッスンの時点では、MCP connector は beta である。request 内の beta header に注意。

実行して、あなたの MCP URL が Linear の MCP endpoint を指していれば、Claude は Linear の tools を列挙し、それから1つを呼ぶ。同じことが基本的にあらゆる準拠 server で機能する。私たちは tool を1つも定義しなかった。Linear client を書かなかった。Linear がそれを maintain している。

Claude が使える tools を絞り込む

MCP servers はしばしば非常に多くの tools を公開する。そして Claude にそのすべてを使わせたいとは限らない。write 権限を持たせたくないかもしれないし、それらすべての tool definitions が context を占めるのが嫌かもしれない。

対処法: default ですべて無効にし、それからほしい特定の tools だけを有効にする。Slack MCP server でのその pattern を示す。

tools=[
{
"type": "mcp_toolset",
"mcp_server_name": "slack",
"default_config": {
"enabled": False,
},
"configs": {
"search_messages": {"enabled": True},
"list_channels": {"enabled": True},
},
}
]

これで Claude は Slack を検索し channels を列挙できるが、投稿や削除はできない。read については service を信頼するが、Claude にあなたの代わりに誤って書き込ませたくないときに有用である。

まとめ
MCP が存在するのは、誰かがすでに build した integration を maintain しなくて済むようにするためである。service provider が MCP server を公開し最新に保つ。彼らの API が変わってもあなたは何も変えない。
仕事に適した機能を選ぶ。あなたの data には tools、あなたのプロセスには skills、third-party services には MCP。
接続は mcp_servers で宣言し（type、URL、name、任意の auth token）、tools の中の mcp_toolset entry でアクセスを付与する。Claude が server を introspect して tools を自分で発見する。書くべき schemas はない。
default_config: {"enabled": False} を設定し、configs で特定の tools を有効にしてアクセスを絞り込む。server を read-only に保つのに便利。
MCP connector は現在 beta なので、request に beta header を含める。
modelcontextprotocol.io で詳細を確認できる

---

### レッスン 10: Context management

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486261>  

Claude に送るすべての request には context window がある。100万 tokens は多く聞こえるが、実際の agent を出荷し始めると、思ったより速く尽きる。そこで context management の出番である。これは、重要なものを失わずに window の中に留まる方法である。

context として数えられるもの

context は、与えられた turn で Claude が見るすべてである。

system prompt
message history
tool definitions と tool results
attached files と skills
thinking blocks

それはすべての API call への input である。入るときに支払い、出るときに支払う。そして一度 window が満杯になると、request は失敗する。

だから目標は、すべてを詰め込むことではない。目標は、適切なものを詰め込むことである。

Anthropic は、long-running agents で context を管理するための4つの pattern を公開している。3つは first-class な API 機能で、1つは design pattern である。

Pattern 1: Just-in-time context

すべてを前もって load しない。agent が今必要とするものを load し、求めたときに tools 経由でさらに引き込ませる。

compliance review agent を考えてみよう。building code book 全体を system prompt に詰め込まれるのではない。特定の section が必要なときに lookup_building_code tool を呼ぶ。これは4つのうち design pattern である。API には特別なものはなく、何をいつ load するかについての意図的な選択にすぎない。

Pattern 2: Server-side compaction

会話が長くなると、Anthropic の server-side compaction が古い turn を1つの block に要約する。request に context_management key を追加し、type を持つ edit を保持することで opt-in する。

response = client.messages.create(
model="claude-sonnet-4-5",
max_tokens=1024,
context_management={
"edits": [
{"type": "compact"}
]
},
messages=messages,
)

API は input が trigger threshold を越えたとき自動的に要約する。会話の長さを自分で追跡する必要はない。

Pattern 3: Prompt caching

Prompt caching は、request の安定した部分 — system prompt、tool definitions、長い文書 — をマークし、call をまたいで一部のコストで再利用できるようにする。

数学が見た目以上に重要である。system prompt が4,000 tokens で、1時間に100回呼ぶなら、caching は使える bill と finance からの電話との違いになる。

Pattern 4: The memory tool

一部の context は session をまたいで生き残る必要がある。user preferences、agent の進行中のメモ、先週決まったこと。これに推奨される primitive は memory tool である。

仕組みは次のとおり。

Claude が tool calls を通じて memory directory を読み書きする。
あなたが storage backend を client-side で実装する。file system、database、encrypted store、何でもよい。
Anthropic が、作業開始前に memory directory を確認するよう Claude に伝える system instruction を自動注入する。
pattern を重ねる

production アプリでは、通常4つすべてを一度に重ねる。compliance review agent は system prompt と tool definitions を cache し、building code sections を lookup_building_code 経由で just in time に引き込む。

各 pattern は異なる failure mode を扱う。cost、window size、statelessness である。あなたにとって壊れているものに合うものを選ぶ。

まとめ
context は turn で Claude が見るすべてであり、無料でも無限でもない。一度 window が満杯になると、request は失敗する。
Just-in-time context: 今必要なものを load し、残りは tools に引き込ませる。これは4つのうち design pattern である。
Server-side compaction: context_management key を追加すると、input が trigger threshold を越えたとき API が古い turn を自動的に要約する。
Prompt caching: request の安定した部分をマークし、call をまたいで一部のコストで再利用する。
memory tool: Claude が tool calls 経由で memory directory を読み書きする。storage backend はあなたが所有するので、context は session をまたいで生き残る。
4つの pattern、1つの目標。手で結線するか、caching と compaction が default で有効な Claude managed agents を使う。

---

### レッスン 11: What are managed agents?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486263>  

Claude Managed Agents は、agents を at scale で build し deploy するための API のスイートである。特定の tools、personas、capabilities を持つ agents を定義する。適切な packages と network controls を備えた sandbox environments を構成する。それから、自分のアプリケーションから sessions を発射し、Claude が isolated container の中で作業する。full file system access、bash execution、web search を備えている。

agent loop を、あなたの代わりに host する

内部では、これは agent loop である。Claude が reason し、tool を呼び、結果を読み、仕事が完了するまで繰り返す。以前 agents を build したことがあれば、おそらくこの種の loop を自分で書いたことがあるだろう。managed agents はその同じ loop を取り、Anthropic の infrastructure 上で host するので、あなたがそれを実行する必要がない。

Managed Agents は Claude Console の独自の section にある。

これが何を解き放つかを理解する最良の方法は、いくつかの例を辿ることである。

例1: 作業を行う Kanban board

managed agents の上に乗った Kanban board を想像してほしい。チケットを「in progress」列にドラッグすると、自動的に session が発射される。チケットに「optimize website performance」と書かれているとしよう。何が起きるか。

あなたの back end が session を作る。
session は、Lighthouse と Puppeteer がプリインストールされた、あなたが構成した environment を指す。
あなたの GitHub repo が container にマウントされる。

これで Claude は codebase、tools、そして done が何を意味するかを定義する rubric を持つ。

Lighthouse score が90以上
render-blocking resources なし
すべての images が lazy load される

Claude は audit を実行し、それから images を圧縮し、CSS を inline 化し、scripts を defer し始める。すべての tool call が event stream を通じてリアルタイムで board にストリームバックされるので、作業をその場で見られる。

それから rubric が作動する。別個の grader が、自身の context window で実行され、output をあなたの criteria に照らして評価する。Claude はそのフィードバックを読み、戻って見落としを修正し、再提出する。デモでは、その loop が Lighthouse score を96まで上げる。

もう1つ。最初のが実行中でも、2つ目のチケットをドラッグして渡せる。2つの session、2つの container、2つの別々の task が並行して実行される。

例2: memory を持つ定期 research agent

別の形の agent がここにある。会社が支払うすべての SaaS tool の価格と plan の変更を追跡し、stand-up の前に report を用意することが仕事のものである。

各実行で、agent は:

現在の価格ページを web で検索し、plan tier の変更を確認し、契約に影響しそうな新機能をフラグする
sandbox の中で Python で cost analysis を実行する
Excel spreadsheet skill を使い、executive summary を書く
Slack にリンクを投稿し、Asana に review task を作る。両方とも MCP servers 経由

agent は memory store からの読み取りと書き込みも行う。始める前に先週見つけたものを確認する。終えた後、変わったものを保存する。だから来週の月曜の report は、毎回同じ静的な価格データを列挙する代わりに、「compute costs are 15% lower since last week（compute コストが先週より15%低い）」と言える。

例3: 複数 agent による incident response

monitoring stack からアラートが発火したと想像してほしい。あなたの back end の custom tool がアラートの payload を受け取り、それを tool result として新しい session に送り込む。この session は multi-agent coordination を使う。

coordinator agent がアラートを受け取り、3人の specialist に委任する。
各 specialist は、同じ共有 file system 上で自身の context window で実行される。
specialist が報告し、coordinator がその findings を1つの incident summary に統合する。

summary が Slack に行く前に、permissions policy が発火する。draft が画面に表示され、あなたが承認し、message が送信される。sensitive な action は人間を待つ。

memory がこのすべてを結びつける。coordinator が memory store 内の過去の incident を確認し、パターンをフラグする。「これは2週間前の DNS resolution issue に似ている。misconfigured TTL が原因だった」。次に似たアラートが発火したとき、agent は一から診断する代わりにその context から始める。

building blocks

これらの例を通じて、managed agents は developer に、次の上に構築された fully managed で stateful な agent experience を提供する tools を与える。

Agents — 特定の tools、personas、capabilities を持つ definitions
Sessions — 自分のアプリケーションから発射する個々の実行
Environments — 適切な packages と network controls を備えた sandbox
Tools — あなたの back end の custom tools を含む
MCP — Slack や Asana のような service への接続
Memory — agent が開始前に読み、完了時に書き込む store
Outcomes — done が何かを定義し確認する rubrics と graders
Multi-agent coordination — specialist に委任する coordinator
まとめ
Claude Managed Agents は、agents を at scale で build し deploy するための API のスイートであり、Anthropic の infrastructure 上で host される。
おなじみの agent loop — reason、tool を呼ぶ、結果を読む、繰り返す — を、file system access、b を備えた isolated container の中で実行する

---

### レッスン 12: Building your first managed agent

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486264>  

agent loop を手で build したことがあれば、その流れを知っているだろう。while loop、stop reason の分岐、tool 実行。それは機能するし、多くの機能ではそれが実際に正しい形である。だがときには、その loop が非常に長く実行されることがある。数分、ことによると数時間。多くの tool にまたがり、保持すべき state があり、書くべき files があり、network のしゃっくりの後に再開すべき作業がある。その時点で、あなたは自分の server で loop を実行したくない。委任したい。それが managed agents である。

managed agent とは何か

managed agent は、あなたのではなく Anthropic の infrastructure 上で実行される agent loop である。agent を一度記述し、作業する environment を与え、session を開始する。Anthropic が loop を実行し、あなたは作業の進行に応じて events をストリームアウトするだけである。

managed agents はすべての API account で default で有効である。特別なアクセスは不要。

4つの primitives

4つの primitives があり、順番に来る。

Agent — persona: model、system prompt、toolset。これは多くの実行をまたいで再利用可能である。
Environment — agent が実行される場所: cloud か local、networking 構成など。
Session — 特定の environment 内での agent の単一の実行。session は作業の単位である。
Events — 出入りする messages: agent の actions、tool calls、results、replies。

部品がどう組み合わさるか。あなたのアプリが session と対話し、session が environment 内で作業を駆動し、起こるすべてが event stream を通じて流れ出る。

ここでの転換に注目してほしい。あなたは while loop を実行していない。events を送り、events を読んでいる。

可能な限り最小の managed agent

何か役に立つことをする、最小の managed agent を build しよう。temp drive にファイルを作り、その行数を数え、報告し返す。

tools には、agent toolset を使う。Anthropic のバンドル済みの file、bash、web tools である。この task にはそれで十分に機能するので、自分で tools を定義する必要はない。

Step 1: agent を作る

まず agent を作る。tools array の中にすぐ定義された agent toolset に注意。それがバンドル済みの toolset である。

import anthropic

client = anthropic.Anthropic()

agent = client.beta.agents.create(
name="Line Counter",
model="claude-opus-4-8",
system="You are a helpful agent that completes small file tasks.",
tools=[
{"type": "agent_toolset_20260401", "default_config": {"enabled": True}}
],
)

覚えておく: agent は再利用可能である。一度作り、多くの session をまたいで実行する。

Step 2: environment を作る

次に environment。これは container template を立ち上げる。cloud で、unrestricted networking。これがファイルが実際に書かれる sandbox である。

environment = client.beta.environments.create(
name="line-counter-env",
config={
"type": "cloud",
"networking": {"type": "unrestricted"},
},
)

Step 3: session を作る

それから、agent と environment、そして任意の title を持つ session を作る。session は作業の単位である。

session = client.beta.sessions.create(
agent=agent.id,
environment_id=environment.id,
title="Count lines demo",
)

Step 4: stream を開き、それから kickoff を送る

ここで event stream を開く。これを最初に行うことに注目。stream は開いた後に発生する events だけを届けるので、kickoff message を送る前に必ず開くこと。それから、live な stream に user message を送る。

with client.beta.sessions.events.stream(session_id=session.id) as stream:

# Stream is open — now send the kickoff

client.beta.sessions.events.send(
session_id=session.id,
events=[
{
"type": "user.message",
"content": [
{
"type": "text",
"text": "Create a file in the temp directory, "
"count its lines, and report back.",
}
],
}
],
)

events — 複数形であることに注目。events は、この API ですべてが流れる方法である。

Step 5: stream を消費する

最後に、stream を消費する。このデモで重要な event type は3つ。

agent.message — Claude の text
agent.tool_use — Claude が選んだ tool
session.status_idle — agent が完了した
for event in stream:
if event.type == "agent.message":
for block in event.content:
if block.type == "text":
print(block.text, end="", flush=True)
elif event.type == "agent.tool_use":
print(f"\n[tool] {event.name}")
elif event.type == "session.status_idle":
print("\n--- Agent done ---")
break

実行すると、output は agent が声に出して reason する様子である。実際の text、選ぶ tools、そして最後の答え。そのすべてが、あなたのではなく Anthropic の container の中で実行される。

トレードオフ

通常 agents では、すべてを制御しなければならない自分の loop を持つ。managed agents では、その l を委任する

---

### レッスン 13: Building with Claude Code

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486266>  

Claude API を手で呼ぶ code を書くのはうまく機能するが、さらに速い経路がある。Claude にそれを書かせるのである。このレッスンでは、Claude Code を使って、スタブ化されたファイルから API integration を埋める。このコースを通じて学んだのと同じ primitives を使う。

stub から始める

project は単純である。天気を取得する TypeScript ファイルである。2つの stub を含む。

getWeather — city を受け取り、気温と状況を返す。
run — tool runner と Claude TypeScript SDK を使うべき function。

tool runner は、tool calling と agent loop をあなたの代わりに処理する部品なので、それを手で結線する必要はない。

Claude API skill

Claude Code には Claude API という built-in skill が付属している。/claude-api で直接呼び出せるし、TypeScript SDK を使っていることを検出すると Claude Code が自動的に呼び出す。

skill が見当たらない場合は、marketplace から追加できる。

/plugin marketplace add AnthropicsSkills

Anthropics の末尾の s に注意。見落としやすい。

1つの prompt、動く code

terminal で project フォルダを開き、Claude Code を起動する。

そこからは、1つの prompt で済む。良い prompt は3つのことをする。

変更したいファイルを指名する。
使ってほしい pattern を指名する。
期待する end state を指名する。

すると Claude Code は、types に対して getWeather と run を埋め、ファイルの末尾に call を追加し、script を実行し、output を報告する。何かエラーが出たら、エラーメッセージを読み、その場で code をパッチする。

Claude Code が生成したもの

この実行では、Claude Code は input をパースし city type に基づいて output を返す Zod tool を作った。私たちが依頼した tool runner と run function も作り、agent loop の最終結果を print した。

覚えておくべき pattern

Claude API に対して書くもののほとんどは、おなじみの形を持つ。

tool を定義する。
runner に渡す。
結果を返す。

毎回それを記憶から打ち込む必要はない。代わりに、ファイルをスタブ化し、Claude Code に渡し、diff を review するだけである。

まとめ
Claude Code は、terminal の中でファイルを編集し commands を実行する agent である。
built-in の Claude API skill は、Claude Code が TypeScript SDK を検出したとき自動的に load されるか、/claude-api で呼び出せる。
ファイル、pattern、end state を指名する prompt を与える。code を書き、実行し、その場でエラーを修正する。
Claude API code はおなじみの形に従う。tool を定義し、runner に渡し、結果を返す。スタブ化し、委任し、diff を review する。

---

### レッスン 14: Claude Platform 101 Quiz

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486268>  

Loading...

---
