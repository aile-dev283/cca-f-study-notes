# CCA-F 演習レポート — {DATE}

> セッション: 言語={LANGUAGE} / モード={MODE} / 問題数={COUNT}
> 出題シナリオ: {SCENARIOS}

## 1. サマリー

- **素点**: {RAW_CORRECT} / {COUNT}（{RAW_PCT}%）
- **スケールド推定**: 約 {SCALED_EST} / 1000 ＝ {PASS_OR_NOT}
  - ⚠️ **目安**です。実際の試験は難問が重み付けされるスケールドスコアで、720＝素点72%ではありません。
    自作問題での **素点 85〜90% を安全圏の目安**としてください（現在: {RAW_PCT}%）。
- ひとことコメント: {ONE_LINER}

## 2. ドメイン別正答率（ヒートマップ）

| ドメイン | 名称 | 重み | 正答/出題 | 正答率 | 判定 |
|---|---|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | {D1_C}/{D1_N} | {D1_PCT}% | {D1_FLAG} |
| D2 | Tool Design & MCP Integration | 18% | {D2_C}/{D2_N} | {D2_PCT}% | {D2_FLAG} |
| D3 | Claude Code Configuration & Workflows | 20% | {D3_C}/{D3_N} | {D3_PCT}% | {D3_FLAG} |
| D4 | Prompt Engineering & Structured Output | 20% | {D4_C}/{D4_N} | {D4_PCT}% | {D4_FLAG} |
| D5 | Context Management & Reliability | 15% | {D5_C}/{D5_N} | {D5_PCT}% | {D5_FLAG} |

（判定の目安: ✅ ≥85% / ⚠️ 60-84% / ❌ <60%）

## 3. 苦手サブドメイン ランキング

正答率の低いタスクステートメント順。復習はここから。

1. **{TS_RANK1}** — {TS_RANK1_NAME}（{TS_RANK1_RESULT}）
2. **{TS_RANK2}** — {TS_RANK2_NAME}（{TS_RANK2_RESULT}）
3. ...

## 4. 各問の解説

{各問について以下を列挙。設問・選択肢は出題時の全文（英語問題なら英語のまま）を載せ、後から振り返れるようにする。}

### Q{N}（{DOMAIN} / TS {TASK_STATEMENT} / {DIFFICULTY} / シナリオ {SCENARIO}）— {正解/不正解}

**Question（全文）:**
> {STEM 全文}

**Options（全文）:**
- **A.** {OPTION_A_TEXT}
- **B.** {OPTION_B_TEXT}
- **C.** {OPTION_C_TEXT}
- **D.** {OPTION_D_TEXT}

**あなたの回答**: {USER_CHOICE}（{USER_CHOICE_TEXT 要約}） ／ **正解**: {CORRECT}

- **なぜ正解か**: {正解の理由}
- **他がなぜアンチパターンか**:
  - {誤答キー}. {誤答1}: {why_wrong}
  - {誤答キー}. {誤答2}: {why_wrong}
  - {誤答キー}. {誤答3}: {why_wrong}
- **出典**: {citations のパス＋locator}

## 5. 弱点別の復習先（リポジトリ内パス）

{弱点ドメインごとに blueprint.yaml の review_links を提示}

### {弱点ドメイン}: {名称}（正答率 {PCT}%）
- 公式ブログ: {blog パス}
- docs: {docs パス}
- Skilljar: {skilljar パス}（対応フェーズ）
- 重点タスクステートメント: {弱点 TS のリスト}

## 6. 次回の推奨

- **推奨モード**: {例: D2 集中 10問 / 弱点復習 / フル模試}
- 理由: {弱点ドメインと素点状況から}
- 弱点復習モードで次回このレポートを入力にすると、出題が自動で弱点へ寄ります。
