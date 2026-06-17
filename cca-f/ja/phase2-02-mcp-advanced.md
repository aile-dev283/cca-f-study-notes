<!-- markdownlint-disable -->

# Model Context Protocol: Advanced Topics

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics>  
**所要時間:** 未記載  
**対象ドメイン:** D2  
**フェーズ:** Phase 2 - MCP & Agentic  

---

## カリキュラム

### レッスン 01: はじめに

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349>  

この course では、MCP の advanced topics として sampling、notifications、roots、JSON message types、transports、stateful StreamableHTTP を扱う。

### レッスン 02: Sampling

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296288>  

Sampling は、MCP server が client に対して LLM completion を依頼する仕組みである。server 自身が model provider の API key を持たずに、client 側の Claude access を通じて生成を行える。

使いどころ:

- server が data を整形したうえで Claude に判断を頼む。
- user の model access / policy を client 側で維持する。
- tool handler 内で AI-assisted processing を行う。

```python
# Call Claude using the Anthropic SDK
```

### レッスン 03: Sampling walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172>  

walkthrough では、server が sampling request を送り、client が Claude を呼び、結果を server に返す流れを確認する。server、client、model の責務を混同しないことが重要である。

### レッスン 04: log と progress notifications

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284>  

Notifications は、server から client へ state や progress を知らせる仕組みである。long-running tools では、進捗が見えることで user experience と debuggability が向上する。

種類:

- log notifications: debug、info、warning、error などの logs
- progress notifications: long task の進捗
- resource change notifications: resources の更新通知

### レッスン 05: Notifications walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036>  

walkthrough では、long-running operation の途中で progress notification を送り、client 側で表示する流れを確認する。notifications は result そのものではなく、進行状況を伝える補助情報である。

### レッスン 06: Roots

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296289>  

Roots は、client が server に対して「アクセスしてよい workspace の境界」を伝える仕組みである。file system や project scope を扱う server では、安全な access boundary として重要になる。

Roots を使うと、server は user が許可した directories や resources の範囲内で作業できる。

### レッスン 07: Roots walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839>  

walkthrough では、client が roots を提示し、server がそれを使って file operations の scope を制限する流れを確認する。

### レッスン 08: Survey

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/297276>  

course の満足度や理解度を確認する survey。

### レッスン 09: JSON message types

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296290>  

MCP は JSON-RPC style の message types を使う。request、response、notification の違いを理解することが重要である。

| type | 内容 |
|------|------|
| request | response が必要な呼び出し |
| response | request に対する結果または error |
| notification | response を要求しない一方向 message |

message id、method、params、result、error の扱いを正しく実装する。

### レッスン 10: STDIO transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291>  

STDIO transport は、client が local process と標準入出力で通信する方式である。local tools、developer workflows、Claude Code / Desktop の project integration に向く。

特徴:

- local process として簡単に起動できる。
- network server を立てなくてよい。
- user machine の環境や files に近い。
- process lifecycle の管理が必要。

### レッスン 11: StreamableHTTP transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287>  

StreamableHTTP transport は、HTTP を使って remote MCP server と通信する方式である。hosted services、shared team tools、cloud integrations に向く。

HTTP では authentication、authorization、network reliability、session handling が重要になる。

### レッスン 12: StreamableHTTP in depth

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286>  

StreamableHTTP では、request/response だけでなく streaming や long-running operations を扱う。server は client に incremental updates を返せる。

設計上は、timeouts、retries、idempotency、auth、rate limits を考慮する。

### レッスン 13: state と StreamableHTTP transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285>  

remote transport では state management が重要である。session id、connection lifecycle、in-flight operations、reconnection、resource changes などを設計する。

stateful な server は便利だが、scale と reliability の難しさが増える。必要な state を最小化し、復旧可能にする。

### レッスン 14: MCP concepts assessment

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301>  

sampling、notifications、roots、JSON message types、STDIO、StreamableHTTP、state management の理解を確認する assessment。

### レッスン 15: まとめ

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296350>  

Advanced MCP では、単純な tool integration を超えて、server が client に generation を依頼する sampling、進捗を伝える notifications、アクセス境界を示す roots、transport と state の設計を学んだ。production integration では、protocol の正しさだけでなく、security、observability、reliability が重要になる。
