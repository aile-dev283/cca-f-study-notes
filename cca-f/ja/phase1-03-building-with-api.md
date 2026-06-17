<!-- markdownlint-disable -->

# Building with the Claude API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api>  
**所要時間:** 約8.1時間  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** Phase 1 - 開発基盤  

---

## カリキュラム

### レッスン 01: コースへようこそ

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287818>  

この course では、Claude API を使って applications、tools、agents、evaluations を構築する方法を学ぶ。中心になるのは Messages API、system prompts、streaming、structured data、evals、prompt engineering、tool use、RAG、advanced features、MCP、Claude Code、agents and workflows である。

### レッスン 02: Claude models の概要

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287722>  

Claude models は speed、cost、capability の trade-off によって選ぶ。Haiku は高速・低コスト、Sonnet は balance、Opus は複雑な reasoning や coding、Fable はさらに難しい task 向けの tier として理解する。

### レッスン 03: API への access

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287726>  

API を使うには、Anthropic Console で account を作り、billing を設定し、API key を発行する。key は environment variable や `.env.local` に保存し、repository に commit しない。

SDK を使うと request の組み立てと response handling が簡単になる。

```bash
npm install @anthropic-ai/sdk
```

### レッスン 04: API key の取得

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/296766>  

API key は秘密情報である。source code に hardcode せず、local environment、secret manager、CI secrets などで管理する。漏えいした場合はすぐに revoke して再発行する。

### レッスン 05: request を送る

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287725>  

Claude API の基本形は `messages.create` である。最低限、`model`、`max_tokens`、`messages` を指定する。

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Explain prompt caching in one paragraph." }],
});
```

response は content blocks として返るため、text block を確認して取り出す。

### レッスン 06: multi-turn conversations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735>  

multi-turn では、conversation history を `messages` array に保持する。user message と assistant response を順に追加し、follow-up question では過去の context を含めて送る。

```javascript
const messages = [];

messages.push({ role: "user", content: "What is RAG?" });
const first = await client.messages.create({ model, max_tokens: 1024, messages });
messages.push({ role: "assistant", content: first.content });

messages.push({ role: "user", content: "When should I use it?" });
const second = await client.messages.create({ model, max_tokens: 1024, messages });
```

context は便利だが長くなりすぎると cost と品質に影響するため、必要に応じて要約・圧縮する。

### レッスン 07: chat 演習

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287727>  

exercise では、basic chat application を作り、message history、user input、assistant output の扱いを確認する。conversation state をどこに保存するかを意識する。

### レッスン 08: system prompts

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287733>  

system prompt は Claude の role、tone、rules、boundaries を定義する場所である。user message は task の入力、system prompt はその task をどう実行するかの前提として扱う。

```javascript
const withoutSystem = await client.messages.create({
  model,
  max_tokens: 1024,
  messages: [{ role: "user", content: "Review this pull request." }],
});

const withSystem = await client.messages.create({
  model,
  max_tokens: 1024,
  system: "You are a terse senior code reviewer. Focus on correctness and risk.",
  messages: [{ role: "user", content: "Review this pull request." }],
});
```

### レッスン 09: system prompts 演習

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287724>  

system prompt の違いが output にどう影響するかを比較する。role、style、format、criteria を変えながら、task に適した instruction を探る。

### レッスン 10: temperature

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287728>  

`temperature` は output の variation を調整する parameter である。低い temperature はより predictable、高い temperature はより creative になりやすい。

```javascript
// Low temperature - more predictable
temperature: 0.2

// High temperature - more creative
temperature: 0.9
```

production の classification や extraction では低め、ideation や creative writing では高めが向くことが多い。

### レッスン 11: course satisfaction survey

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/297284>  

course の理解度と満足度を確認する survey。

### レッスン 12: response streaming

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734>  

streaming は長い response を少しずつ client に返す機能である。user experience を改善し、待ち時間を短く感じさせられる。

実装では chunk を client に送りつつ、complete message を database 保存用に保持する。

```javascript
// Send each chunk to your client
// Get the complete message for database storage
```

### レッスン 13: structured data

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287732>  

structured data では、Claude に JSON など parse 可能な形式で output させる。schema、examples、validation、retry を組み合わせると安定する。

注意点:

- JSON のみを返すよう明示する。
- required fields を定義する。
- invalid JSON の fallback を用意する。
- parser と validator で確認する。

### レッスン 14: structured data exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287729>  

exercise では、unstructured text から structured fields を抽出し、JSON parse と validation を行う。

### レッスン 15: API access quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289117>  

Messages API、API key、multi-turn、system prompts、temperature、streaming、structured data の基礎を確認する。

### レッスン 16: prompt evaluation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287731>  

prompt evaluation は、prompt が実際の use case でどれだけ良い output を出すかを測る手法である。少数の例で感覚的に判断するのではなく、representative examples と scoring criteria を用意する。

eval は model selection、prompt improvement、regression detection に役立つ。

### レッスン 17: typical eval workflow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287736>  

典型的な eval workflow:

1. task を定義する。
2. representative dataset を集める。
3. good output の criteria を決める。
4. prompt / model candidates を実行する。
5. outputs を grade する。
6. results を比較し、改善する。

### レッスン 18: test datasets の生成

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287739>  

test dataset は、実際の workload を反映している必要がある。easy cases だけでなく、edge cases、ambiguous inputs、failure-prone examples を含める。

AI で synthetic examples を作ることもできるが、production data や domain expert review と組み合わせると良い。

### レッスン 19: eval を実行する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287743>  

eval runner は、dataset の各 input を candidate prompt/model に通し、output と metadata を保存する。latency、token usage、error rate も併せて記録すると比較しやすい。

```javascript
// 原文コード例は抽出時に省略。ここでは eval runner の役割のみを要約する。
```

### レッスン 20: model based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287742>  

model based grading は、別の model に output を評価させる方法である。rubric を明確にし、score と explanation を structured output で返させる。

```javascript
// Create evaluation prompt
// Grade the output
```

採点 model も誤る可能性があるため、human spot check と calibration が必要である。

### レッスン 21: code based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287737>  

code based grading は、deterministic checks で output を評価する方法である。JSON validity、required fields、exact match、regex、unit tests、schema validation などに向く。

creative writing や nuanced judgment には不十分な場合があるため、model based grading や human review と組み合わせる。

### レッスン 22: prompt evals exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287738>  

exercise では、prompt candidate を複数用意し、dataset に対する output を比較して改善する。

### レッスン 23: prompt evaluation quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289118>  

eval dataset、rubric、model based grading、code based grading、regression testing の理解を確認する。

### レッスン 24: prompt engineering

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287745>  

prompt engineering は、Claude に task を正確に理解させ、望む output を安定して得るための設計である。明確さ、具体性、structure、examples、constraints が中心になる。

### レッスン 25: clear and direct に書く

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287744>  

曖昧な依頼は曖昧な output につながる。何をしてほしいか、何をしないでほしいか、どの形式で返すかを直接書く。

悪い例: "Analyze this."  
良い例: "Extract the top 5 risks, explain each in one sentence, and rank them by severity."

### レッスン 26: specific にする

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287740>  

audience、purpose、constraints、examples、edge cases を具体化すると output が安定する。特に extraction や classification では inclusion / exclusion criteria が重要である。

### レッスン 27: XML tags で structure を作る

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287741>  

XML tags は prompt の section を分けるのに便利である。

```xml
<instructions>
Summarize the document for an executive audience.
</instructions>
<document>
...
</document>
```

instructions、context、examples、output format を分けると Claude が解釈しやすくなる。

### レッスン 28: examples を与える

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287746>  

few-shot examples は output style、format、classification criteria を示すのに有効である。良い例だけでなく、境界例や悪い例を含めると判断が安定する。

### レッスン 29: prompting exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287748>  

exercise では、曖昧な prompt を clear、specific、structured、example-rich な prompt に改善する。

### レッスン 30: prompt engineering techniques quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289121>  

clear/direct、specificity、XML tags、examples、constraints の理解を確認する。

### レッスン 31: tool use 入門

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287747>  

Tool use は、Claude に外部 function を呼ばせる仕組みである。Claude は tool call を提案し、application が実行し、tool result を Claude に戻す。

### レッスン 32: project overview

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287751>  

tool use の project では、time、weather、database lookup などの tool functions を定義し、Claude がどの tool をいつ使うかを学ぶ。

### レッスン 33: tool functions

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287756>  

tool function は application 側で実行される通常の code である。Claude に渡すのは function そのものではなく、name、description、input schema である。

```python
# Default format: "2024-01-15 14:30:25"
# Just hour and minute: "14:30"
```

### レッスン 34: tool schemas

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753>  

tool schema は JSON Schema で入力形式を定義する。required fields、types、enum、description を正しく書くと、Claude が valid な arguments を作りやすくなる。

```javascript
// 原文コード例は抽出時に省略。ここでは schema 設計の要点のみを要約する。
```

### レッスン 35: message blocks の handling

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287757>  

Claude response は text blocks、tool_use blocks など複数の block を含む。block type を確認し、text は表示、tool_use は実行に回す。

### レッスン 36: tool results を送る

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287752>  

tool result は `tool_result` block として user message に含め、対応する `tool_use_id` を指定して Claude に返す。Claude は result を使って最終回答を作る。

### レッスン 37: tools 付き multi-turn conversations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287750>  

tools を使う会話では、conversation history に assistant の tool_use と user の tool_result を正しい順序で保持する。順序が崩れると context が壊れる。

```python
# 原文コード例は抽出時に省略。ここでは tool_use と tool_result の順序管理を要約する。
```

### レッスン 38: multiple turns の実装

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287758>  

agent loop では、Claude response を受け取り、tool_use があれば実行し、tool_result を追加して再度 Claude に送る。`stop_reason` が `end_turn` になるまで繰り返す。

```javascript
// Process each tool request...
// Add more tools as needed
```

### レッスン 39: multiple tools を使う

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287749>  

複数 tools を与えると Claude は task に応じて選択できる。ただし tool が多すぎると選択が不安定になる。agent ごとに必要な tool だけを渡す。

### レッスン 40: fine grained tool calling

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/313160>  

fine grained tool calling では、partial JSON chunks や incremental tool arguments を扱う。streaming 中の incomplete JSON に注意し、complete snapshot または validation できる単位で処理する。

```javascript
// Process the partial JSON chunk
// Or use the complete snapshot so far
// Handle invalid JSON appropriately
```

### レッスン 41: text edit tool

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287760>  

text edit tool は、既存 text に対して targeted edits を行うための tool pattern である。search/replace、patch、diff などの形式を使い、変更範囲を明確にする。

### レッスン 42: web search tool

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287755>  

web search tool は、最新情報や外部 sources が必要な task で使う。Claude の知識だけで答えると古い可能性がある場合、search によって grounded response を作る。

### レッスン 43: tool use quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289122>  

tool schema、tool_use block、tool_result、agent loop、multiple tools、built-in tools の理解を確認する。

### レッスン 44: Retrieval Augmented Generation 入門

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287763>  

RAG は、外部 knowledge base から relevant context を retrieval し、その context を使って Claude に回答させる pattern である。model の内部知識に頼らず、最新・固有・大量の情報を扱える。

### レッスン 45: text chunking strategies

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287776>  

chunking は long documents を検索しやすい単位に分けること。section、paragraph、token count、semantic boundaries を考慮する。chunk が小さすぎると context が不足し、大きすぎると retrieval 精度が落ちる。

### レッスン 46: text embeddings

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287759>  

embeddings は text を vector に変換し、semantic similarity search を可能にする。query と document chunks の embeddings を比較し、関連性の高い chunk を取り出す。

### レッスン 47: full RAG flow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287764>  

RAG flow:

1. documents を chunk する。
2. chunks の embeddings を作る。
3. vector store に保存する。
4. query を embedding する。
5. relevant chunks を retrieve する。
6. retrieved context を prompt に入れる。
7. Claude が grounded answer を生成する。

**Section 2: Software Engineering**

### レッスン 48: RAG flow の実装

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287761>  

実装では ingestion pipeline、indexing、retrieval、prompt assembly、answer generation を分ける。retrieved context には source metadata を付け、回答で citations を返せるようにする。

### レッスン 49: BM25 lexical search

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287767>  

BM25 は lexical search の代表的手法で、keyword match に強い。semantic search では拾いにくい exact terms、IDs、固有名詞に有効である。

```python
# 1. Chunk your text by sections
# 2. Create a BM25 store and add documents
# 3. Search the store
# Print results
```

### レッスン 50: Multi-Index RAG pipeline

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287766>  

Multi-Index RAG は、vector search、BM25、metadata filters など複数 index の結果を統合する。Reciprocal Rank Fusion（RRF）などで順位を統合すると、異なる検索方式の強みを組み合わせられる。

```python
# Get results from all indexes
# Track document ranks across indexes
# Apply RRF scoring formula
# Return merged and sorted results
```

### レッスン 51: extended thinking

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287773>  

Extended thinking は複雑な reasoning のための機能である。難しい analysis、multi-step coding、計画、数学的推論などで有効。cost と latency が増えるため、task に応じて使い分ける。

### レッスン 52: image support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287778>  

Claude は images を input として扱える。image block と text block を組み合わせ、画像の説明、表や chart の読み取り、UI screenshot の分析などに使う。

```javascript
// Image Block
// Text Block
```

### レッスン 53: PDF support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287768>  

PDF support により、text と visual layout を含む documents を扱える。long PDFs では page selection、chunking、summarization、citation が重要になる。

### レッスン 54: citations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287771>  

citations は、回答がどの source に基づくかを示すために使う。RAG、PDF analysis、web search では、source metadata を保持し、answer と一緒に参照を返す設計が重要である。

### レッスン 55: prompt caching

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287772>  

prompt caching は、繰り返し使う長い prompt prefix を cache し、latency と cost を下げる機能である。large system prompt、long documents、shared context を何度も使う場合に有効。

### レッスン 56: prompt caching の rules

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287770>  

cache される部分は安定している必要がある。頻繁に変わる content を cache prefix に入れると効果が下がる。static context と dynamic user query を分ける。

### レッスン 57: prompt caching in action

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287774>  

実装では、長い instructions や reference material を cacheable block として渡し、user query だけを毎回変える。usage metadata を見て cache hit を確認する。

### レッスン 58: code execution と Files API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287777>  

code execution は sandbox 内で Python を実行し、data analysis や file processing を行う機能である。Files API と組み合わせると、input files を渡し、生成物を回収できる。

### レッスン 59: Claude features quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289124>  

extended thinking、image/PDF support、citations、prompt caching、code execution、Files API の理解を確認する。

### レッスン 60: MCP 入門

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287780>  

MCP は、Claude と外部 tools / resources / prompts をつなぐ protocol である。standard interface により integration を再利用できる。

### レッスン 61: MCP clients

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287775>  

MCP client は MCP server に接続し、公開された capabilities を Claude に渡す。Claude Desktop、Claude Code、自作 application などが client になり得る。

### レッスン 62: project setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287785>  

MCP server の project を作成し、dependencies を install する。

```bash
# If using UV (recommended)
uv init

# If using standard Python
python -m venv .venv
```

### レッスン 63: MCP tools の定義

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287797>  

MCP tool は name、description、input schema、handler で構成される。tool descriptions は Claude の選択に影響するため、具体的に書く。

### レッスン 64: server inspector

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287781>  

MCP Inspector を使うと、server が公開する tools、resources、prompts を確認し、手動で呼び出して debug できる。

### レッスン 65: client の実装

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287793>  

client は server に接続し、capabilities を取得し、Claude の tool calls を server に中継する。transport、session lifecycle、errors を扱う。

### レッスン 66: resources の定義

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287782>  

Resources は、Claude に見せられる content catalog である。documents、schemas、configs、reference material などを URI 付きで公開する。

### レッスン 67: resources への access

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287783>  

client は resource list を取得し、必要な resource を read する。resources を使うと、探索的な tool calls を減らし、必要な context を明示しやすい。

### レッスン 68: prompts の定義

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287784>  

MCP prompts は reusable prompt templates である。arguments を取り、特定 workflow の instruction を生成できる。

### レッスン 69: client で prompts を使う

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287786>  

client は prompt template に arguments を渡し、生成された prompt を Claude に送る。

```python
# The doc_id gets interpolated into the prompt
```

### レッスン 70: MCP review

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287790>  

MCP の tools、resources、prompts、client/server architecture、debugging の要点を復習する。

### レッスン 71: MCP quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289126>  

MCP concepts、tools、resources、prompts、clients、transports の理解を確認する。

### レッスン 72: Anthropic apps

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287787>  

Anthropic apps は、Claude を日常の作業や development workflow に接続する入口である。Claude.ai、Desktop、Claude Code、Console などを task に応じて使い分ける。

### レッスン 73: Claude Code setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287788>  

Claude Code を install し、project repository で起動する。permissions、CLAUDE.md、tool access、git 状態を確認する。

### レッスン 74: Claude Code in action

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287805>  

Claude Code は repository を探索し、変更方針を立て、files を編集し、tests を実行し、diff を確認する。大きな作業では explore -> plan -> code -> test -> commit の流れが有効である。

```text
# - Adds notes to your CLAUDE.md file
```

### レッスン 75: MCP servers による enhancements

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287792>  

Claude Code に MCP servers を追加すると、GitHub、docs、internal systems などへの access を拡張できる。project-level `.mcp.json` と user-level config の scope を使い分ける。

### レッスン 76: agents and workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287796>  

workflows は事前に定義された steps、agents は環境を観察しながら動的に判断する systems である。task の予測可能性と必要な autonomy に応じて選ぶ。

### レッスン 77: parallelization workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287804>  

parallelization は、独立した subtasks を同時に実行し、最後に統合する pattern である。複数 reviewers、複数 search queries、複数 extraction units などに向く。

### レッスン 78: chaining workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287800>  

chaining は、前の step の output を次の step の input にする pattern である。outline -> draft -> review -> revise のような段階的作業に向く。

### レッスン 79: routing workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287801>  

routing は、input の種類に応じて別の path、prompt、model、agent に振り分ける pattern である。support ticket classification や task triage に有効。

### レッスン 80: agents and tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287803>  

agent は tools を使って環境に作用する。tool selection、error handling、state management、human approval が reliability の鍵になる。

### レッスン 81: environment inspection

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287798>  

agent は作業前に environment を観察する必要がある。files、configs、available tools、current state を確認し、assumptions を減らす。

### レッスン 82: workflows vs agents

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287794>  

workflow は predictability と control に強く、agent は flexibility と autonomy に強い。固定された手順で十分なら workflow、状況に応じた判断が必要なら agent を選ぶ。

### レッスン 83: agents and workflows quiz

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289130>  

parallelization、chaining、routing、agent/tool design、environment inspection、workflow vs agent の理解を確認する。

### レッスン 84: final assessment

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/290899>  

course 全体の理解を確認する final assessment。

### レッスン 85: course wrap up

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287802>  

この course では、Claude API の基本から、evals、prompt engineering、tool use、RAG、advanced features、MCP、Claude Code、agents and workflows までを学んだ。実務では、小さく eval を作り、model と prompt を比較し、tool/context/reliability を設計しながら本番化する。
