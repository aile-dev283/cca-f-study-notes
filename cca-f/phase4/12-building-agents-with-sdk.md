<!-- markdownlint-disable -->

# Building Agents with the Claude Agent SDK

**URL:** <https://claude.com/blog/building-agents-with-the-claude-agent-sdk>  
**対応ドメイン:** D1 / D3 / D5  
**優先度:** S

---

## 概要

Claude Agent SDK（旧Claude Code SDK）は、Claudeにコンピュータ的な能力（ファイル操作・コマンド実行・反復的問題解決）を与える自律エージェント構築フレームワーク。「Claudeにコンピュータへのアクセスを与えることで、プログラマーのようにコードを書けるようになる」という設計思想に基づき、コーディングを超えた汎用エージェント構築を可能にする。

---

## エージェントフィードバックループ（4ステップ）

| ステップ | 内容 |
|---------|------|
| 1. Gather Context | 関連情報の取得・理解 |
| 2. Take Action | ツールを使ったタスク実行 |
| 3. Verify Work | 出力の評価・エラー検出 |
| 4. Repeat | 目標達成まで反復 |

---

## コンテキスト取得手法

### Agentic Search / File System
- bash コマンド（grep、tail など）でフォルダ構造から情報を知的にロード
- ディレクトリ構造自体が「一種のコンテキストエンジニアリング」

### Semantic Search
- ベクトル検索は「精度が低く、保守が難しく、透明性が低い」
- 推奨：まず agentic search から始める

### Subagents
- 並列化とコンテキスト分離を実現
- 複数 subagent が異なるタスクを同時処理し、関連抜粋のみを返す（全コンテキストではない）

### Compaction
- 長時間 agent 実行中のコンテキストウィンドウ枯渇を防ぐ自動要約

---

## アクション実行手法

| 手法 | 説明 |
|------|------|
| Tools | 主要構成要素。頻繁・意図的なエージェントアクションを表す。カスタムツールで効率最大化 |
| Bash / Scripts | PDF ダウンロード、フォーマット変換、コンテンツ検索などの汎用コンピュータアクセス |
| Code Generation | 「コードは精密・合成可能・無限再利用可能」。複雑で信頼性の高い操作に最適 |
| MCPs | Slack、GitHub、Asana などの認証・API 管理を自動処理する標準化統合 |

---

## 成果物検証手法

| 手法 | 特徴 |
|------|------|
| Rules-Based Feedback | 明示的な出力ルール定義。TypeScript lint は JS より多層バリデーション |
| Visual Feedback | スクリーンショット・レンダリングでレイアウト・スタイル・コンテンツ階層・レスポンシブを評価 |
| LLM as Judge | セカンダリ LLM がファジー基準で出力評価。レイテンシトレードオフと堅牢性の限界あり |

---

## 試験対策：重要ポイント

| 論点 | 正解寄り | 罠 |
|------|---------|-----|
| コンテキスト取得 | ディレクトリ構造・agentic search を活用 | 全ファイルを一括コンテキストに投入 |
| Subagent 活用 | 必要な抜粋のみ返す、並列処理 | 全履歴・全ツールを渡す |
| 成果物検証 | lint・visual・LLM judge を組み合わせ | Claude の自己申告 confidence だけ信じる |
| 長期タスク | Compaction + structured notes + artifacts | 1つの長大プロンプトでやらせる |

---

## 実用ユースケース

- Finance agent：ポートフォリオ分析・投資評価
- Personal assistant：カレンダー管理・旅行予約
- Customer support：高曖昧性チケット対応
- Research agent：ドキュメント分析・統合
