<!-- markdownlint-disable -->

# Claude Code in Action

**URL:** <https://anthropic.skilljar.com/claude-code-in-action>  
**所要時間:** 約1時間  
**対象ドメイン:** D3  
**フェーズ:** Phase 3 - Claude Code  

---

## カリキュラム

### レッスン 01: はじめに

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303233>  

この course では、Claude Code を実際の development workflow に組み込み、setup、context、changes、custom commands、MCP servers、GitHub integration、hooks、SDK を扱う。

### レッスン 02: coding assistant とは何か

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303235>  

coding assistant は、code を補完するだけでなく、repository を理解し、変更を計画し、tests を実行し、review を支援する collaborator である。Claude Code は terminal と git に近い場所で働くため、実際の engineering workflow に入りやすい。

### レッスン 03: Claude Code の実演

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303242>  

実演では、Claude Code が repository を探索し、問題を特定し、変更を加え、tests を実行し、diff を確認する一連の流れを見る。重要なのは、Claude が勝手にすべてを決めるのではなく、人間が goal と constraints を与えることである。

### レッスン 04: Claude Code の setup

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/301614>  

setup では install、authentication、project directory、permissions、terminal environment を確認する。初回は小さい task で動作確認する。

### レッスン 05: project setup

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/301615>  

project setup では、repository の structure、commands、test strategy、coding conventions を Claude に伝える。CLAUDE.md を整備すると、毎回の説明を減らせる。

### レッスン 06: context の追加

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303241>  

Claude Code は、files、terminal output、git diff、issues、docs などから context を得る。必要な context を絞って渡すと、変更の精度が上がる。

良い context:

- 変更対象の files
- 関連 tests
- error messages
- acceptance criteria
- 既存 patterns

### レッスン 07: changes を作る

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303236>  

changes を作るときは、scope を小さく保ち、既存 patterns に合わせ、verification を行う。Claude Code には、「どこまで触ってよいか」「どの tests を実行するか」を明示するとよい。

### レッスン 08: course satisfaction survey

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303701>  

course の満足度や理解度を確認する survey。

### レッスン 09: context を control する

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303237>  

context control は Claude Code の品質に直結する。大きな repository では、search、read、summarize を使い、必要な情報だけを active context に残す。

長い session では、途中で整理し、current objective、decisions、open questions、changed files をまとめるとよい。

### レッスン 10: custom commands

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303234>  

custom slash commands は、繰り返す workflow を短い command として定義する仕組みである。project scope の `.claude/commands/` と user scope の `~/.claude/commands/` を使い分ける。

例:

- `/review-pr`
- `/write-tests`
- `/summarize-issue`
- `/prepare-release-notes`

### レッスン 11: Claude Code と MCP servers

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303239>  

MCP servers を使うと、Claude Code に external capabilities を追加できる。GitHub、documentation、database schema、internal tools などを project workflow に統合できる。

project-level `.mcp.json` は team 共有に向く。secrets は `${ENV_VAR}` で参照し、commit しない。

### レッスン 12: GitHub integration

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303240>  

GitHub integration では、issues、pull requests、review comments、CI results を Claude Code の workflow に取り込む。PR の feedback を読み、修正し、tests を実行し、変更内容を説明できる。

重要なのは、review comments の意図を理解し、必要な変更だけを scoped に行うこと。

### レッスン 13: hooks の紹介

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312000>  

Hooks は Claude Code の events に反応して command や script を実行する仕組みである。policy enforcement、formatting、logging、notifications、safety checks に使える。

### レッスン 14: hooks を定義する

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312002>  

hook は event、matcher、command などを定義する。どの tool use や lifecycle event に反応するかを絞ることで、必要な場面だけ実行できる。

### レッスン 15: hook を実装する

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312003>  

実装では、hook script が input を受け取り、validation や logging を行い、必要なら operation を block する。error message は Claude と人間の両方が理解できるようにする。

### レッスン 16: hooks の注意点

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312423>  

hooks は強力だが、過剰に使うと workflow を遅くしたり、debug を難しくしたりする。side effects、performance、cross-platform compatibility、secret exposure に注意する。

### レッスン 17: 便利な hooks

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312004>  

便利な hooks の例:

- edit 後に formatter を実行する。
- sensitive files への write を block する。
- test command の前に environment を確認する。
- dangerous command に confirmation を要求する。

### レッスン 18: もう一つの便利な hook

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312427>  

別の例として、PR description や changelog の作成前に diff summary を生成する hook、または tool results を normalize する hook がある。hook は prompt instruction より確実に enforcement できる。

### レッスン 19: Claude Code SDK

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/312001>  

Claude Code SDK は、Claude Code の capabilities を programmatic workflow に組み込むための手段である。CI、automation、custom developer tools で Claude Code を非対話的に使える。

CI では `-p` / `--print`、structured output、JSON schema、exit codes を意識する。

### レッスン 20: Claude Code quiz

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/308391>  

setup、context、changes、custom commands、MCP、GitHub integration、hooks、SDK の理解を確認する。

### レッスン 21: まとめと次の steps

**URL:** <https://anthropic.skilljar.com/claude-code-in-action/303238>  

Claude Code は development workflow の中で Claude を使うための実践的な環境である。CLAUDE.md、commands、MCP、hooks、SDK を組み合わせることで、チームの開発プロセスに合わせた agentic workflow を作れる。
