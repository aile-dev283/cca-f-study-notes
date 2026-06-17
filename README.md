# CCA-F Study Notes

CCA-F（Claude Certified Architect – Foundations）試験対策のノートをまとめたリポジトリ。

[ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) をベースに、Anthropic Skilljar コースのノートと公式ブログの試験対策まとめを追加したもの。

---

## 試験概要

**Claude Certified Architect – Foundations（CCA-F）**  
公式トップページ: <https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request>

| 項目 | 内容 |
|------|------|
| 対象 | Anthropicパートナー企業の技術者（〜301レベル） |
| 形式 | 60問・4択・120分・プロクター監視（ProctorFree） |
| 合格ライン | 1000点満点中720点（目安：Practice Exam で 900+/1000） |
| 受験料 | $99（Claude Partner Network 加盟企業は割引あり） |
| 結果通知 | 受験から2営業日以内（ドメイン別スコアレポート付き） |
| 合格特典 | CCA-Fバッジ（LinkedIn共有可） |
| 試験回数 | 1回のみ（再受験不可） |
| 受験登録 | パートナー企業のメールアドレスが必要 |

**前提条件（公式）:**

- Skilljar の 200 レベルコースをすべて完了していること
- Agent SDK・Claude Code・Anthropic API・MCP での実装経験があること

### ドメイン別出題割合

| ドメイン | 内容 | 割合 |
|---------|------|------|
| D1 | Agentic Architecture & Orchestration | **27%** |
| D2 | Tool Design & MCP Integration | **18%** |
| D3 | Claude Code Configuration & Workflows | **20%** |
| D4 | Prompt Engineering & Structured Output | **20%** |
| D5 | Context Management & Reliability | **15%** |

> ※公式ページ（2026年6月時点）より。

### 出題シナリオ（全6種・本番は4種をランダム抽出）

| # | シナリオ名 | 関連ドメイン |
|---|-----------|------------|
| 1 | Customer Support Resolution Agent | D1・D2・D5 |
| 2 | Code Generation with Claude Code | D3・D5 |
| 3 | Multi-Agent Research System | D1・D2・D5 |
| 4 | Developer Productivity with Claude | D2・D3・D1 |
| 5 | Claude Code for Continuous Integration | D3・D4 |
| 6 | Structured Data Extraction | D4・D5 |

> 詳細は公式 Exam Guide PDF（パートナー登録後にダウンロード可）を参照。

---

## 学習コンテンツ

詳細は **[`cca-f/`](cca-f/README.md)** を参照。

| フェーズ | 内容 | 学習時間 |
|---------|------|---------|
| Phase 0 | オリエンテーション（Claude 101 / Cowork） | 約 2h |
| Phase 1 | 開発基盤（Platform / AI Fluency / Claude API） | 約 12〜14h |
| Phase 2 | MCP & Agentic（MCP intro・advanced・Subagents） | 約 8〜10h |
| Phase 3 | Claude Code（101 / in Action / Agent Skills） | 約 3〜5h |
| Phase 4 | 公式ブログ補強（Agent SDK・Tool Design・Context Engineering・Security・Evals） | 約 8〜10h |

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
