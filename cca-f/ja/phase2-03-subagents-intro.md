<!-- markdownlint-disable -->

# Introduction to subagents

**URL:** <https://anthropic.skilljar.com/introduction-to-subagents>  
**所要時間:** 未記載  
**対象ドメイン:** D1  
**フェーズ:** Phase 2 - MCP & Agentic  

---

## カリキュラム

### レッスン 01: subagents とは何か

**URL:** <https://anthropic.skilljar.com/introduction-to-subagents/450698>  

Subagents は、main agent から特定 task を委任される specialized agents である。大きな問題を分解し、それぞれの subagent に役割、instructions、tools、context を与えて並列または段階的に進められる。

subagent が有効な場面:

- research、coding、review など専門性の違う作業を分けたい。
- main context を汚さず探索したい。
- 複数の観点で独立に analysis したい。
- coordinator が全体を管理し、subagents に部分 task を委任したい。

重要なのは、subagent は coordinator の context を自動的にすべて継承しないこと。必要な context は prompt で明示的に渡す。

### レッスン 02: subagent を作成する

**URL:** <https://anthropic.skilljar.com/introduction-to-subagents/450699>  

subagent は、name、description、system prompt、allowed tools などで定義する。description は coordinator がいつ呼ぶべきかを判断する材料になる。

良い subagent definition:

- 役割が明確である。
- 入力として必要な context が分かる。
- output format が明確である。
- allowed tools が task に必要な範囲に絞られている。
- 失敗時の扱いが書かれている。

`Task` tool は subagent を起動するための入口である。coordinator の `allowedTools` に `"Task"` が必要になる。

### レッスン 03: 効果的な subagents を設計する

**URL:** <https://anthropic.skilljar.com/introduction-to-subagents/450700>  

効果的な subagents は、分担が重複しすぎず、責務が狭く、必要な tools だけを持つ。1つの subagent に多すぎる役割や tools を与えると、判断が曖昧になり reliability が下がる。

設計の観点:

- decomposition: 大きな task をどう分けるか。
- context passing: subagent に何を渡すか。
- output contract: coordinator が統合しやすい形にする。
- error handling: subagent が失敗したときの escalation。
- isolation: main session を守るために探索を分離する。

### レッスン 04: subagents を効果的に使う

**URL:** <https://anthropic.skilljar.com/introduction-to-subagents/450701>  

subagents は、hub-and-spoke pattern で使うと整理しやすい。coordinator が task を分解し、subagents に依頼し、結果を集約し、最終判断を行う。

使い分け:

- parallel research: 複数観点を同時に調査する。
- independent review: 別 context で code や plan を確認する。
- specialist delegation: security、performance、UX など専門観点を分ける。
- exploration isolation: main context に不要な探索を持ち込まない。

subagent には必要な context、明確な task、出力形式、制約を渡す。曖昧な依頼は coordinator 側の統合負荷を上げる。
