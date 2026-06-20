---
description: Read and explain legacy code, producing a summary suitable for onboarding new team members
---

`$ARGUMENTS` で指定されたコードを対象に（**ファイルは変更しないこと**）:

1. 関連ファイルをすべて読む（推測せず Read ツールと Grep ツールを使うこと）
2. 以下を特定する: 目的・入出力・依存関係・副作用・既知の問題
3. 2段階の説明を書く:
   - **TL;DR**（新メンバー向け、1パラグラフ）
   - **技術詳細**（データフロー・主要アルゴリズム・統合ポイント）
4. 注意すべきコードの臭いや TODO をリストアップする

これは読み取り専用の分析。いかなるファイルも変更しないこと。
