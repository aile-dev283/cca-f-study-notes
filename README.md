# CCA-F Study Notes

CCA-F（Claude Certified Architect – Foundations）試験対策のノートをまとめたリポジトリ。

[ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) をベースに、Anthropic Skilljar コースのノートと公式ブログの試験対策まとめを追加したもの。

---

## CCA-F 試験対策コンテンツ

**[`cca-f/`](cca-f/README.md)** を参照。

### 構成

| フェーズ | 内容 | 対象ドメイン |
|---------|------|------------|
| Phase 0–3 | Anthropic Skilljar コースノート（11コース・216レッスン）英語・日本語 | D1〜D5 全域 |
| Phase 4 | 公式エンジニアリングブログ補強（8記事）| D1〜D5 薄い領域を重点補強 |

### Phase 4 補強記事（公式ブログ）

| 優先度 | 記事 | ドメイン |
|--------|------|---------|
| S | Building Agents with Claude Agent SDK | D1/D3/D5 |
| S | Writing Effective Tools for AI Agents | D2/D4 |
| S | Code Execution with MCP + Advanced Tool Use | D2/D5 |
| S | Effective Context Engineering + Context Management | D5 |
| S | Claude Code 最新 Docs（Memory/Rules/Skills/Hooks） | D3/D1 |
| A | Auto Mode + How We Contain Claude | D3/D5 |
| A | Demystifying Evals for AI Agents | D4/D5 |
| A | Effective Harnesses for Long-Running Agents + Agent Skills | D1/D5/D3 |

### 試験概要

| 項目 | 内容 |
|------|------|
| 形式 | 60問・4択・120分・プロクター監視 |
| 合格ライン | 1000点満点中720点 |
| 受験料 | $99（Partner Network 割引あり） |
| 対象 | Anthropicパートナー企業の技術者 |

ドメイン構成：D1 Agentic Architecture（27%）/ D2 Tool Design & MCP（18%）/ D3 Claude Code（20%）/ D4 Prompt Engineering（20%）/ D5 Context Management（15%）

---

## Claude Code ドキュメントミラー

`docs/` には [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) 由来の Claude Code 公式ドキュメントミラーが含まれる。GitHub Actions で定期自動更新。

### upstream の更新を手動で取り込む

```bash
git fetch upstream
git merge upstream/main
git push
```

`cca-f/` は upstream に存在しないためコンフリクトは起きない。初回のみ `git remote add upstream https://github.com/ericbuess/claude-code-docs.git` が必要。

### `/docs` コマンドのインストール

```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```

インストール後、Claude Code で以下が使用可能：

```bash
/docs hooks       # hooks ドキュメントを参照
/docs mcp         # MCP ドキュメントを参照
/docs memory      # memory ドキュメントを参照
/docs -t          # 最終更新時刻を確認
/docs what's new  # 最近の更新差分を表示
/docs changelog   # Claude Code リリースノートを参照
```

インストール・アンインストールの詳細は [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) を参照。

---

## ライセンス

- `docs/` 内のドキュメントコンテンツは Anthropic に帰属
- ミラーツール部分（install.sh など）は [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) に帰属
- `cca-f/` の試験対策ノートは Anthropic Skilljar および Anthropic 公式ブログを出典とする
