# S3: Multi-Agent Research System (D1)

オーケストレーター + サブエージェントのパターンを2つの方法で学ぶ。

## 実行

```bash
# sandbox/ から実行
uv run python s3-multi-agent/coordinator.py

# Claude Code native subagent を使う場合（Claude Code CLI が必要）:
# s3-multi-agent/ ディレクトリ内で claude を起動し、
# 「MCP Sampling について3エージェントで調査して」と指示する
```

## 2つの実装アプローチ

### coordinator.py（Pure API）
複数の `client.messages.create()` 呼び出しをコーディネーターが順番/並列に実行。

```
coordinator.py
├── call_sub_agent(system=SEARCH_SYSTEM, ...)    → Haiku
├── call_sub_agent(system=ANALYSIS_SYSTEM, ...)  → Haiku
└── call_sub_agent(system=REPORT_SYSTEM, ...)    → Sonnet ← 高品質モデルを選択
```

### .claude/agents/（Claude Code Native）
`.claude/agents/*.md` で定義したサブエージェントを Claude Code が自動的に使う。
Agent SDK のネイティブ機能であり、コンテキスト分離が自動で行われる。

## 試験で問われる設計判断

| 判断 | 選択肢 | 正解の理由 |
|------|--------|----------|
| サブエージェント使うべきか | はい | コンテキスト汚染を防ぐ |
| 並列 vs シーケンシャル | 依存関係次第 | 独立タスクは並列、依存あれば直列 |
| モデル選択 | タスクで使い分け | 検索=Haiku（速い）、レポート=Sonnet（高品質） |
| サブエージェントへの情報渡し | 必要なものだけ | 過剰なコンテキストはノイズになる |
