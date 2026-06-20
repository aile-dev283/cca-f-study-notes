---
description: Refactor the specified code for clarity and maintainability, following team conventions
---

`$ARGUMENTS` で指定されたコード（指定なしの場合は現在のファイル）を対象に:

1. リファクタリング候補を上位3つ特定する（命名・重複・複雑度）
2. 変更内容と理由を説明し、**確認を取ってから**変更を適用する
3. 変更を1つずつ適用し、各変更後に `pytest -x` を実行する
4. 変更のサマリー（何を・なぜ変えたか）を出力する

CLAUDE.md のチーム規約に従うこと。公開 API のシグネチャは変更前に必ず報告すること。
