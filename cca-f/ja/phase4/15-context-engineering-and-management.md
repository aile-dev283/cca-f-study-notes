<!-- markdownlint-disable -->

# Effective Context Engineering + Context Management

**URL（前半）:** <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>  
**URL（後半）:** <https://anthropic.com/news/context-management>  
**対応ドメイン:** D5  
**優先度:** S

---

## Part 1: Effective Context Engineering for AI Agents

### Context Engineering とは

「推論時のトークン全体（システム指示・ツール・メッセージ履歴・外部データ）を動的に管理し、LLM の出力を最適化する実践」。プロンプトエンジニアリングの進化形。

- **プロンプトエンジニアリング**：効果的なプロンプト文の作成に焦点
- **コンテキストエンジニアリング**：推論時のトークン全体を動的に管理

設計原則：**「最小限で高信号なトークンセットを見つけ、所望の結果確率を最大化する」**

### Context Rot（コンテキスト劣化）

コンテキストサイズが増加するにつれ、LLM の情報正確想起能力が低下する。トランスフォーマーの n² 個のペアワイズ関係による設計的制約。

→「コンテキストを増やせばよい」ではなく「**何を残し、何を捨て、何を外部化するか**」がポイント。

### 効果的なコンテキストの設計

#### システムプロンプト
- 過度に複雑な硬直ロジックと曖昧さの間の適切な高度（altitude）
- 構造化セクション（背景情報・指示・ツール使用法など）を活用

#### ツール設計
- ツールセットが膨れ上がり、曖昧な判断を招くことを避ける
- 最小限で明確な機能性を保つ

#### Few-shot 例
- 数千語の説明より、多様で代表的な例の方が有効

### 長期タスクの高度技法

#### 1. Compaction（圧縮）
会話をまとめて要約し、新しいコンテキストウィンドウで再開する手法。

Claude Code の実装：
- **保持**：アーキテクチャ的決定・未解決バグ・実装詳細
- **破棄**：冗長なツール出力

> **注意**：Compaction だけでは不十分。構造的指示と環境設計が必須。

#### 2. Structured Note-taking（構造化記録）
エージェントがコンテキストウィンドウ外のメモリに定期的に記録を保持する方法。

実績：Pokémon をプレイする Claude が数千ステップにわたって目標追跡・戦略を維持。

#### 3. Sub-agent Architectures（サブエージェント設計）
複数の専門化エージェントが並行して探索し、数千トークン使用後に **1,000〜2,000 トークンの要約**を返す構造。単一エージェント方式より複雑な研究タスクで大幅改善。

---

## Part 2: Managing Context on the Claude Developer Platform

### 2つの新機能（2025年、Public Beta）

#### Context Editing
「コンテキストウィンドウがトークン限界に近づいた際、古いツール呼び出しと結果を自動的にクリア」。関連性のないコンテンツを除去しながら会話フローを保持し、手動介入なしでエージェント動作期間を延長。

#### Memory Tool
「ファイルベースのシステムを通じてコンテキストウィンドウ外に情報を保存・参照」。エージェントは専用メモリディレクトリに CRUD 操作可能 → アクティブコンテキストを増やさずセッションをまたいだ知識ベース構築。

### 改善数値

| 手法 | 改善内容 |
|------|---------|
| Memory tool + Context editing（組み合わせ） | **39% パフォーマンス向上** |
| Context editing 単独 | **29% 向上** |
| 100 ターン web search eval | **84% トークン消費削減**（失敗していたタスクが完了可能に） |

### 対象ユースケース

| ユースケース | 活用方法 |
|------------|---------|
| コーディング | 大規模コードベース管理・デバッグ洞察の保持 |
| リサーチ | 知識ベース構築・古い検索結果の除去 |
| データ処理 | トークン限界を超えるワークフロー処理 |

---

## 試験対策：判断軸

| 状況 | 正解寄り | 罠 |
|------|---------|-----|
| 長い agent session | Compaction + structured notes + artifacts | コンテキストウィンドウ拡大だけで解決 |
| 大量ツール結果 | Stale tool result clearing / context editing | 全ツール結果を保持 |
| 複数セッション継続 | Memory tool + file artifacts + TODO + decision log | 前セッションの自然文要約だけに頼る |
| 重要根拠の保持 | Citation / provenance / timestamp | 「たぶん正しい」summary |
| 失敗処理 | 構造化エラー + retryability + partial result | 空配列を成功扱い |
| 長期開発 | 小さな incremental task + handoff artifact | 「アプリ全部作って」と一発依頼 |

---

## 主要論点まとめ

- context engineering = 何を context に入れるかの戦略的設計
- context rot を避けるため、重要情報は先頭に置き、冗長な tool output は除去する
- compaction は必要だが十分ではない。memory + structured notes + subagent architecture を組み合わせる
- context editing でコンテキストウィンドウを擬似的に延長できる（84% トークン削減の実績）
- memory tool はコンテキスト外の永続ストレージ。長期エージェントには必須
