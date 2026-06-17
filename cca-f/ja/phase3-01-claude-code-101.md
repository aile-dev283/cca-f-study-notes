<!-- markdownlint-disable -->

# Claude Code 101

**URL:** <https://anthropic.skilljar.com/claude-code-101>  
**所要時間:** 未記載  
**対象ドメイン:** D3  
**フェーズ:** Phase 3 - Claude Code  

---

## カリキュラム

### レッスン 01: Claude Code とは何か

**URL:** <https://anthropic.skilljar.com/claude-code-101/469788>  

Claude Code は terminal で動く agentic coding assistant である。repository を読み、files を編集し、commands を実行し、tests を確認し、git workflow を支援する。単なる code completion ではなく、codebase 全体を context として扱える。

### レッスン 02: Claude Code の仕組み

**URL:** <https://anthropic.skilljar.com/claude-code-101/469789>  

Claude Code は、project files、terminal output、git diff、instructions を読みながら作業する。必要に応じて search、read、edit、bash、git などの tools を使う。

人間は goal と constraints を与え、Claude は environment を探索し、plan を立て、実装し、verification を行う。

### レッスン 03: Claude Code の install

**URL:** <https://anthropic.skilljar.com/claude-code-101/469790>  

Claude Code を install し、terminal から project directory で起動する。初回は authentication、permissions、working directory を確認する。

一般的な準備:

- repository の git status を確認する。
- tests / lint commands を把握する。
- project instructions（CLAUDE.md）を用意する。
- secrets を repository に入れない。

### レッスン 04: 最初の prompt

**URL:** <https://anthropic.skilljar.com/claude-code-101/469791>  

最初の prompt では、何を達成したいか、どの範囲を触ってよいか、どの tests を使うかを伝える。曖昧な依頼より、goal、constraints、verification を含む依頼がよい。

例:

> Fix the failing validation for empty email addresses. Keep the change scoped to the form validator and run the existing unit tests.

### レッスン 05: explore -> plan -> code -> commit の流れ

**URL:** <https://anthropic.skilljar.com/claude-code-101/469792>  

Claude Code の基本 workflow は explore、plan、code、commit である。

1. Explore: files、tests、patterns を読む。
2. Plan: 変更方針と risk を整理する。
3. Code: scoped edits を行う。
4. Verify: tests、lint、diff review を行う。
5. Commit: 意図が分かる commit を作る。

大きな変更では plan mode、小さく明確な修正では direct execution が向く。

### レッスン 06: context management

**URL:** <https://anthropic.skilljar.com/claude-code-101/469793>  

Claude Code では、必要な files と terminal output を適切に context に入れることが重要である。無関係な logs や巨大 files を入れすぎると、判断が鈍る。

context を管理する方法:

- search で relevant files を探す。
- 変更前に local patterns を読む。
- 長い output は要点化する。
- session が長くなったら要約して整理する。

### レッスン 07: code review

**URL:** <https://anthropic.skilljar.com/claude-code-101/469794>  

Claude Code は code review にも使える。review では style よりも、bugs、behavioral regressions、missing tests、security、performance risk を優先する。

同じ session が自分の変更を review するより、独立した context で review した方が見落としを減らしやすい。

### レッスン 08: CLAUDE.md file

**URL:** <https://anthropic.skilljar.com/claude-code-101/469795>  

CLAUDE.md は project-specific instructions を置く場所である。commands、architecture、coding style、testing policy、review expectations などを書く。

例:

```markdown
# Project

This is a TypeScript React application.

# Commands

- npm test
- npm run lint

# Code Style

- Prefer existing patterns.
- Keep changes scoped.
```

#### README.md

README.md は人間向けの project overview、CLAUDE.md は Claude Code 向けの operational guidance と考えると分けやすい。

### レッスン 09: Subagents

**URL:** <https://anthropic.skilljar.com/claude-code-101/469796>  

Subagents は、research、review、specialized implementation などを別 context で実行するために使う。main session の context を守りつつ、複数観点を並行して扱える。

### レッスン 10: Skills

**URL:** <https://anthropic.skilljar.com/claude-code-101/469848>  

Skills は、特定作業の手順、templates、rules、reference files を Claude Code に与える。release notes、security review、migration、test generation などの定型作業に向く。

### レッスン 11: MCP

**URL:** <https://anthropic.skilljar.com/claude-code-101/469797>  

MCP により、Claude Code は external tools、docs、issue trackers、internal systems に接続できる。project-level `.mcp.json` は repository と一緒に共有でき、user-level config は個人環境に閉じる。

### レッスン 12: Hooks

**URL:** <https://anthropic.skilljar.com/claude-code-101/469798>  

Hooks は Claude Code の lifecycle に介入する仕組みである。tool use の前後、session events、notifications などで validation、logging、policy enforcement を行える。

prompt だけでルールを守らせるより、hook による programmatic enforcement の方が信頼性が高い場面がある。

### レッスン 13: course quiz

**URL:** <https://anthropic.skilljar.com/claude-code-101/469849>  

Claude Code の基本、workflow、context management、review、CLAUDE.md、subagents、skills、MCP、hooks の理解を確認する。
