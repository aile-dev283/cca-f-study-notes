<!-- markdownlint-disable -->

# Introduction to Model Context Protocol

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol>  
**所要時間:** 未記載  
**対象ドメイン:** D2  
**フェーズ:** Phase 2 - MCP & Agentic  

---

## カリキュラム

### レッスン 01: コースへようこそ

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/303756>  

この course では、Model Context Protocol（MCP）の基本を学ぶ。MCP は、Claude と external tools、resources、prompts を接続するための protocol であり、integration を標準化する。

### レッスン 02: MCP の紹介

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296689>  

MCP は、AI applications と外部 systems の間に共通 interface を提供する。従来は application ごとに custom integration が必要だったが、MCP server が capabilities を公開し、MCP client がそれを利用する形にできる。

MCP server は主に次を提供する。

- Tools: Claude が呼び出せる action
- Resources: Claude が参照できる content
- Prompts: 再利用可能な prompt templates

### レッスン 03: MCP clients

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690>  

MCP client は MCP server に接続し、公開された capabilities を Claude に渡す側である。Claude Desktop、Claude Code、自作 application などが client になれる。

client の役割:

- server connection を確立する。
- tools/resources/prompts の list を取得する。
- Claude の tool request を server に中継する。
- results や errors を Claude に返す。

### レッスン 04: project setup

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296694>  

MCP server project を作る。runtime、dependencies、server entrypoint、transport を準備し、local で実行できるようにする。

setup では、最小の server から始め、Inspector で capabilities を確認しながら増やすのが安全である。

### レッスン 05: MCP で tools を定義する

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296697>  

MCP tool は、Claude が外部 action を実行するための interface である。name、description、input schema、handler を定義する。

良い tool design:

- description に「いつ使うか」と「何を返すか」を書く。
- input schema は required fields と type を明確にする。
- error は structured に返す。
- side effect のある action は注意深く扱う。

### レッスン 06: server inspector

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296693>  

MCP Inspector は server を debug するための tool である。server が公開する tools、resources、prompts を確認し、arguments を入れて manual call できる。

Inspector で確認すべきこと:

- tool が期待どおり list されるか。
- schema が正しいか。
- valid input で期待した result が返るか。
- invalid input や permission error が分かりやすいか。

### レッスン 07: course satisfaction survey

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/297281>  

course の理解度や満足度を確認する survey。

### レッスン 08: client の実装

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696>  

client は MCP server に接続し、Claude からの tool calls を実行する。実装では、transport、lifecycle、capability discovery、error handling を扱う。

tool call の流れ:

1. client が server の tools を取得する。
2. Claude に tools を提示する。
3. Claude が tool_use を返す。
4. client が server の tool handler を呼ぶ。
5. result を Claude に返す。

### レッスン 09: resources を定義する

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296699>  

Resources は、Claude が参照できる content を catalog として公開する仕組みである。documents、database schema、API docs、configuration、reference data などを URI 付きで提供する。

resources は read-oriented な context 提供に向く。action が必要なら tool、定型 prompt が必要なら prompt を使う。

### レッスン 10: resources に access する

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296695>  

client は available resources を list し、必要な resource を read する。resource の metadata を分かりやすくすると、Claude が必要な context を見つけやすくなる。

大量の情報を tool call で探させるより、resources で catalog 化すると探索コストを下げられる。

### レッスン 11: prompts を定義する

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296698>  

MCP prompts は reusable prompt templates である。arguments を受け取り、特定の task に適した prompt を生成する。

prompts は、team の定型 workflow、review format、analysis template、report style を共有するのに向く。

### レッスン 12: client で prompts を使う

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296692>  

client は prompt template の list を取得し、arguments を渡して prompt を展開する。展開された prompt を Claude に送ることで、同じ workflow を再利用できる。

### レッスン 13: MCP final assessment

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/297196>  

MCP の client/server model、tools、resources、prompts、Inspector、error handling の理解を確認する assessment。

### レッスン 14: MCP review

**URL:** <https://anthropic.skilljar.com/introduction-to-model-context-protocol/296691>  

MCP は Claude と外部 systems を接続する標準 interface である。tools は action、resources は context、prompts は reusable instructions を担う。良い MCP integration は、明確な descriptions、structured schemas、分かりやすい errors、適切な scope を持つ。
