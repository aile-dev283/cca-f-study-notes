<!-- markdownlint-disable -->

# Introduction to agent skills

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills>  
**所要時間:** 未記載  
**対象ドメイン:** D3  
**フェーズ:** Phase 3 - Claude Code  

---

## カリキュラム

### レッスン 01: skills とは何か

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434525>  

Skills は、Claude に特定の作業をうまく実行するための instructions、workflow、templates、reference files を渡す package である。人間が毎回説明していた手順を reusable にし、agent の振る舞いを安定させる。

skills が向く作業:

- 繰り返し発生する。
- 手順や品質基準がある。
- 出力形式が決まっている。
- domain-specific knowledge が必要。

### レッスン 02: 最初の skill を作る

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434527>  

skill は通常、`SKILL.md` を中心に構成する。frontmatter で description や metadata を定義し、本文で trigger、workflow、output format、examples を書く。

例:

```markdown
# PR Summary Skill

## What

Create concise pull request summaries.

## Why

Help reviewers understand intent, risk, and verification.

## Changes

- Summarize user-visible behavior.
- List tests run.
- Call out risks.
```

良い skill は、Claude がいつ使えばよいかを判断できる description を持つ。

### レッスン 03: configuration と multi-file skills

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434526>  

multi-file skill では、`SKILL.md` 以外に templates、examples、scripts、references を含められる。本文にすべてを詰め込むのではなく、必要なときに参照できる形にする。

configuration の観点:

- `allowed-tools` で skill が使える tools を制限する。
- `argument-hint` で入力の期待形を示す。
- 大きな reference は別 file に分ける。
- scripts がある場合は再利用する。

### レッスン 04: Skills と他の Claude Code features の違い

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434528>  

Skills、CLAUDE.md、slash commands、MCP、subagents は役割が異なる。

| feature | 主な用途 |
|---------|----------|
| CLAUDE.md | project 全体の恒久的 instructions |
| slash commands | 明示的に呼び出す短い workflow |
| skills | task に応じて呼び出される reusable expertise |
| MCP | external tools/resources/prompts への接続 |
| subagents | 別 context で専門 task を実行 |

skill は「Claude にやり方を教える」ための単位であり、tool connection や agent orchestration とは分けて考える。

### レッスン 05: skills を共有する

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434529>  

skills は team や projects で共有できる。共有前には、機密情報、個人情報、顧客固有情報が含まれていないか確認する。組織固有の手順は一般化し、必要な context は reference として整理する。

共有後は、実際の利用から feedback を集め、description、workflow、examples を改善する。

### レッスン 06: skills の troubleshooting

**URL:** <https://anthropic.skilljar.com/introduction-to-agent-skills/434530>  

skill が期待どおり使われない場合は、次を確認する。

- description が trigger として明確か。
- workflow が長すぎたり曖昧だったりしないか。
- output format が明示されているか。
- examples が task に合っているか。
- allowed tools が不足または過剰ではないか。
- reference files が必要なときに見つけやすいか。

skill は一度で完成するものではない。実際の tasks で試し、失敗例から instructions を改善する。
