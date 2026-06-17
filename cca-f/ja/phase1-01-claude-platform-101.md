<!-- markdownlint-disable -->

# Claude Platform 101

**URL:** <https://anthropic.skilljar.com/claude-platform-101>  
**所要時間:** 未記載  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** Phase 1 - 開発基盤  

---

## カリキュラム

### レッスン 01: Claude Developer Platform とは何か

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486250>  

Claude Developer Platform は、Claude を programmatically に組み込むための Anthropic の infrastructure である。browser で Claude と会話する代わりに、code から structured requests を送り、structured responses を受け取る。model、token budget、tools、system instructions まで制御できる。

platform は主に次の要素で構成される。

- 任意の language から呼び出せる REST API
- 複数 programming languages 向け SDK
- command line interfaces
- API keys、usage、managed agents、prompt testing を扱う console

platform は3層で理解できる。

| 層 | 内容 |
|----|------|
| Primitives | Messages API、tool use、files、web search、code execution、MCP servers、skills |
| Infrastructure | managed agents、retries、queues、observability |
| Controls | dashboards、evals、本番運用のための管理機能 |

要するに、primitives で build し、infrastructure で scale し、controls で run する。

help desk の返信 draft のような機能では、既存 product の button から ticket content を取り出し、`messages.create` に渡し、返ってきた draft を UI に表示する。Claude Platform は「Claude に質問する」から「Claude を product の一部にする」ための入口である。

### レッスン 02: 最初の API call

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486251>  

最初の実用的な API call では、Claude に意味のある入力を渡し、structured insight を受け取る。

準備:

- `platform.claude.com` で API key を取得する。
- key は `.env.local` などに保存し、version control に入れない。
- SDK を install する。

```bash
npm install @anthropic-ai/sdk
```

`messages.create` では、model、max tokens、messages を指定する。

```javascript
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
```

response content は string ではなく blocks の array である。通常の text response でも `type === "text"` を確認して処理する。tool calls や thinking など、複数 block が返る場合に備えるためである。

### レッスン 03: 適切な model を選ぶ

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486252>  

model choice は quality と cost に直結する。最も賢い model を常に使うと API bill が増え、最も安い model だけを使うと品質が足りない場合がある。

| model tier | 向いている用途 |
|------------|----------------|
| Claude Fable | 最難関の challenge。Opus より上の tier で cost も高い |
| Claude Opus | deep reasoning、complex analysis、multi-step coding、nuanced writing |
| Claude Sonnet | intelligence、speed、cost の balance が良く、多くの production work に向く |
| Claude Haiku | fast and low cost。classification、extraction、routing など high-volume / low-complexity work |

本番前には simple evaluation を作る。実際の workload から 20〜30 個の代表例を集め、各 model に通し、自分の use case における good output と照らして採点する。Haiku から試し、足りなければ Sonnet、必要な場合だけ Opus に上げる。

### レッスン 04: agent loop の説明

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486254>  

agent loop は、Claude が response を返し、tool use が必要なら tool を実行し、その結果を Claude に戻し、最終回答が出るまで繰り返す pattern である。

重要なのは `stop_reason` である。

- `"tool_use"`: Claude が tool を使いたがっている。tool call を実行し、result を messages に追加して loop を続ける。
- `"end_turn"`: Claude が最終回答を返した。loop を終了する。

tools array では、tool の `name`、`description`、input schema を定義する。description は Claude の tool selection に直接影響するため、曖昧にしない。

実アプリでは `run_tool` は database、API、internal service などに接続する。hardcoded lookup は学習用の単純化である。

### レッスン 05: tool use とは何か

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486255>  

Tool use により、Claude は外部 system に問い合わせたり、action を実行したりできる。Claude 自身は tool を直接実行せず、どの tool をどの arguments で呼ぶべきかを structured block として返す。developer 側がそれを実行し、結果を返す。

設計上の要点:

- tool name は短く明確にする。
- description は「いつ使うか」「何を返すか」「制約」を書く。
- input schema は required fields と types を明確にする。
- error は Claude が判断できる形で返す。

tool use は agentic system の基礎であり、後続の MCP、managed agents、workflows にもつながる。

### レッスン 06: thinking とは何か

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486256>  

Extended thinking は、Claude が複雑な問題をより慎重に解くための機能である。深い reasoning、multi-step planning、難しい coding、複雑な analysis で有効になる。

使いどころ:

- answer の正確性が重要な複雑問題
- 長い context を踏まえた判断
- 複数制約を同時に満たす設計
- agentic workflow の計画

単純な classification や short extraction には不要な場合が多い。latency と token cost を考え、task の難しさに応じて使う。

### レッスン 07: built-in tools

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486258>  

Claude Platform には、web search、code execution などの built-in tools がある。自前で tool server を作らなくても、Claude が検索や sandboxed code 実行を行える。

例:

- web search: 最新情報や外部情報に grounded な回答を作る。
- code execution: Python で計算、data analysis、file processing を行う。

tool use と同じく、どの tool を許可するか、どの task で使うか、結果をどう検証するかが重要である。

### レッスン 08: Skills

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486259>  

Skills は、Claude に特定作業の手順や domain knowledge を与えるための reusable instruction package である。workflow、templates、examples、reference files をまとめられる。

良い skill は次を含む。

- いつ使うべきかという trigger
- 入力と期待する output
- 手順
- 品質基準
- edge cases

Skills は agentic tasks の再現性を高める。特定のチームの作法や domain-specific process を Claude に渡すときに有効である。

### レッスン 09: MCP

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486260>  

Model Context Protocol（MCP）は、Claude と外部 tools / resources / prompts を接続する protocol である。Claude がさまざまな system と同じ形でやり取りできるようにする標準的な interface と考える。

MCP server は tools、resources、prompts を公開できる。Claude Code や Claude Desktop などの MCP client が server に接続し、必要な capability を利用する。

MCP は custom integration を再利用可能にし、agent workflows で外部 system を扱うための重要な土台になる。

### レッスン 10: context management

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486261>  

Context management は、Claude に何を見せ、何を見せないかを設計すること。context window は大きいが無限ではなく、不要な情報は cost と品質の両方を悪化させる。

主な戦略:

- 必要な部分だけ retrieve する。
- 長い文書は chunking / summarization する。
- intermediate state を compact に保持する。
- task ごとに context を分離する。
- 古い情報や矛盾する instructions を取り除く。

良い context design は、正確性、latency、cost、reliability を同時に改善する。

### レッスン 11: managed agents とは何か

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486263>  

Managed agents は、Claude Platform 上で agent を実行・管理するための infrastructure である。developer が loop、state、retries、tool calls、observability をすべて自前で持つ代わりに、platform 側の仕組みを使える。

prototype では単純な script で十分でも、production では reliability、monitoring、retry、session management が必要になる。managed agents はその段階で役立つ。

### レッスン 12: 最初の managed agent を作る

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486264>  

managed agent を作る流れは、agent definition を用意し、instructions、tools、permissions、runtime behavior を設定し、session を開始することから始まる。

実装時の注意:

- agent の goal と boundaries を明確にする。
- tools は必要最小限にする。
- tool results と agent state を観測できるようにする。
- human confirmation が必要な action を切り分ける。

### レッスン 13: Claude Code で build する

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486266>  

Claude Code は codebase 内で働く agentic coding assistant である。repository を読み、terminal や git を使い、変更を実装・検証できる。

Platform の観点では、Claude Code は Claude を developer workflow に統合する入口である。CLAUDE.md、MCP servers、skills、hooks、subagents などを組み合わせることで、チームの開発プロセスに合わせられる。

### レッスン 14: Claude Platform 101 quiz

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486268>  

この quiz では、Messages API、model selection、agent loop、tool use、thinking、built-in tools、skills、MCP、context management、managed agents、Claude Code の基礎を確認する。
