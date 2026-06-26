# CCA-F 試験頻出 一般英語語彙集

> CCA-F 試験の問題文・選択肢・教材本文に頻出する一般英語語彙をまとめたリスト。
> 技術用語（MCP、agentic loop 等）は対象外。試験問題を読む際に詰まりやすい表現を優先して収録。

---

## Section 1: 動詞・動詞句（最重要）

試験の設問文や選択肢の解説に繰り返し登場する動詞。意味を知らないと選択肢の意図が読み取れない。

| 英語 | 日本語 | 試験文脈での例 | 例文の日本語訳 |
|------|--------|--------------|--------------|
| leverage | 活用する、最大限に利用する | "leverage existing tool descriptions" | 既存のツール説明を活用する |
| validate | 検証する、妥当性を確認する | "validate output against the schema" | スキーマに照らして出力を検証する |
| mitigate | 軽減する、緩和する | "mitigate the risk of hallucination" | 幻覚のリスクを軽減する |
| enforce | 強制する、徹底させる | "enforce compliance rules deterministically" | コンプライアンスルールを決定論的に強制する |
| decompose | 分解する | "decompose a complex request into subtasks" | 複雑なリクエストをサブタスクに分解する |
| synthesize | 統合する、まとめる | "synthesize findings from multiple subagents" | 複数のサブエージェントの調査結果を統合する |
| aggregate | 集約する | "aggregate results from each specialist" | 各専門エージェントの結果を集約する |
| propagate | 伝播させる、広げる | "errors propagate through the pipeline" | エラーがパイプライン全体に伝播する |
| disambiguate | 曖昧さを取り除く | "disambiguate similar tool descriptions" | 類似したツール説明の曖昧さを取り除く |
| consolidate | 統合する、一本化する | "consolidate related tools into one" | 関連するツールを1つに統合する |
| calibrate | 調整する、最適化する | "calibrate review thresholds based on data" | データに基づいてレビューのしきい値を調整する |
| preserve | 保持する、維持する | "preserve source attribution during synthesis" | 統合時に出典の帰属を保持する |
| prioritize | 優先順位をつける | "prioritize high-severity findings" | 重大度の高い問題を優先する |
| demonstrate | 実証する、示す | "demonstrate practical judgment in context" | 文脈の中で実践的な判断力を示す |
| route | 振り向ける、転送する | "route requests through the coordinator" | リクエストをコーディネーター経由で転送する |
| eliminate | 排除する、なくす | "eliminate false positives" | 誤検知をなくす |
| differentiate | 区別する、差別化する | "differentiate each tool's purpose clearly" | 各ツールの目的を明確に区別する |
| truncate / trim | 削減する、切り詰める | "trim verbose tool outputs before passing" | 渡す前に冗長なツール出力を削減する |
| grounded in | 〜に根ざす、〜に基づく | "questions grounded in realistic scenarios" | 現実的なシナリオに根ざした設問 |
| handle gracefully | 適切に・うまく対処する | "handle edge cases gracefully" | エッジケースを適切に処理する |
| put in place | 導入する、設ける | "put safeguards in place" | 安全策を導入する |
| rule out | 排除する、否定する | "rule out unfeasible approaches first" | まず実現不可能なアプローチを排除する |
| work around | 回避する | "work around context window limitations" | コンテキストウィンドウの制限を回避する |
| weigh | 比較検討する | "weigh tradeoffs between speed and accuracy" | 速度と精度のトレードオフを比較検討する |
| shed light on | 明らかにする | "shed light on the root cause" | 根本原因を明らかにする |
| fall back to | 〜にフォールバックする | "fall back to a simpler strategy" | よりシンプルな戦略にフォールバックする |
| delegate | 委任する、任せる | "delegate subtasks to subagents" | サブタスクをサブエージェントに委任する |
| spawn | 生成する、起動する | "spawn a new subagent for each domain" | 各ドメインに新しいサブエージェントを生成する |
| infer | 推測する、推論する | "infer user intent from context" | コンテキストからユーザーの意図を推測する |

---

## Section 2: 形容詞・副詞

選択肢の修飾語として登場し、正誤の判断に影響する。

| 英語 | 日本語 | 試験文脈での例 | 例文の日本語訳 |
|------|--------|--------------|--------------|
| deterministic | 決定論的な（必ず同じ結果が出る） | "deterministic enforcement via hooks" | フック経由での決定論的な強制 |
| non-deterministic | 非決定論的な（結果が毎回変わりうる） | "non-deterministic systems like LLMs" | LLMのような非決定論的なシステム |
| ambiguous | 曖昧な | "ambiguous or high-stakes requests" | 曖昧または重要度の高いリクエスト |
| robust | 堅牢な、頑健な | "a more robust architecture" | より堅牢なアーキテクチャ |
| granular | 粒度の細かい、詳細な | "granular control over tool access" | ツールアクセスに対するきめ細かい制御 |
| actionable | 実行可能な、具体的に役立つ | "actionable feedback with clear criteria" | 明確な基準を持つ実行可能なフィードバック |
| transient | 一時的な | "transient errors such as timeouts" | タイムアウトなどの一時的なエラー |
| explicit | 明示的な（はっきり書かれている） | "explicit criteria in the prompt" | プロンプト内の明示的な基準 |
| implicit | 暗黙的な（書かれていないが前提とされる） | "implicit assumptions in the design" | 設計における暗黙の前提 |
| probabilistic | 確率的な | "probabilistic compliance is insufficient" | 確率的なコンプライアンス遵守では不十分 |
| scalable | スケーラブルな（規模拡大に対応できる） | "a scalable multi-agent architecture" | スケーラブルなマルチエージェントアーキテクチャ |
| erroneous | 誤った | "erroneous inferences from the model" | モデルによる誤った推論 |
| exhaustive | 徹底的な、網羅的な | "exhaustive validation is not always feasible" | 網羅的な検証が常に実現可能とは限らない |
| comprehensive | 包括的な | "a comprehensive understanding of the system" | システムの包括的な理解 |
| proportionate | 相応しい、釣り合いの取れた | "a proportionate first response" | 状況に見合った最初の対応 |
| superficial | 表面的な | "superficial comments that miss root causes" | 根本原因を見逃す表面的なコメント |
| consistent | 一貫した | "consistent output across repeated calls" | 繰り返し呼び出しにわたる一貫した出力 |
| inconsistent | 不一貫な | "inconsistent results in production" | 本番環境での不一貫な結果 |
| semantic | 意味的な（形式でなく内容に関する） | "semantic errors survive schema validation" | 意味的なエラーはスキーマ検証をすり抜ける |
| heterogeneous | 異種混在の、バラバラの | "heterogeneous document formats" | 異種混在のドキュメント形式 |
| empirical | 実証的な（データに基づく） | "empirical evaluation of the approach" | そのアプローチの実証的な評価 |
| optimal | 最適な | "the optimal strategy given constraints" | 制約を踏まえた最適な戦略 |
| reliable | 信頼できる、安定した | "reliable structured output" | 信頼できる構造化された出力 |
| idempotent | 冪等な（何度実行しても同じ結果） | "ensure the operation is idempotent" | 操作が冪等であることを保証する |
| retriable | 再試行可能な | "mark transient errors as retriable" | 一時的なエラーを再試行可能としてマークする |
| scoped | スコープ限定の、範囲を絞った | "scoped tool access per agent" | エージェントごとにスコープを絞ったツールアクセス |
| verbose | 冗長な、詳細すぎる | "trim verbose tool outputs" | 冗長なツール出力を削減する |

---

## Section 3: 一般名詞

ドメイン固有でない名詞で、試験文中に自然に登場するもの。

| 英語 | 日本語 | 試験文脈での例 | 例文の日本語訳 |
|------|--------|--------------|--------------|
| tradeoff | トレードオフ（一方を得るともう一方を失う関係） | "weigh the tradeoffs between cost and accuracy" | コストと精度のトレードオフを比較検討する |
| overhead | オーバーヘッド（余分なコスト・負担） | "reduce computational overhead" | 計算上のオーバーヘッドを削減する |
| bottleneck | ボトルネック（全体の速度を制限する箇所） | "the coordinator becomes a bottleneck" | コーディネーターがボトルネックになる |
| latency | レイテンシ、遅延 | "minimize end-to-end latency" | エンドツーエンドのレイテンシを最小化する |
| throughput | スループット（単位時間当たりの処理量） | "improve throughput with batching" | バッチ処理でスループットを改善する |
| coverage | カバレッジ、対象範囲 | "expand test coverage across document types" | ドキュメント種類全体でテストカバレッジを拡大する |
| precision | 精度（取得したもののうち正しい割合） | "precision over recall in this scenario" | このシナリオではリコールよりも精度を優先する |
| accuracy | 正確さ（全体として正しい割合） | "measure overall accuracy" | 全体の正確さを測定する |
| confidence | 信頼度、確信度 | "low-confidence extractions" | 信頼度の低い抽出結果 |
| bias | バイアス、偏り | "selection bias in training examples" | 学習例における選択バイアス |
| iteration | イテレーション、反復 | "each iteration of the agentic loop" | エージェントループの各反復 |
| pipeline | パイプライン（一連の処理フロー） | "a multi-stage processing pipeline" | 多段階の処理パイプライン |
| payload | ペイロード（送受信されるデータ本体） | "the request payload to the API" | APIへのリクエストペイロード |
| constraint | 制約 | "given business constraints" | ビジネス上の制約を踏まえると |
| boundary | 境界、境界線 | "define clear tool boundaries" | 明確なツールの境界を定義する |
| heuristic | ヒューリスティック、経験則 | "a heuristic for tool selection" | ツール選択のための経験則 |
| edge case | エッジケース、例外的な入力 | "handle edge cases gracefully" | エッジケースを適切に処理する |
| gap | ギャップ、欠如 | "identify gaps in policy coverage" | ポリシーカバレッジのギャップを特定する |
| variance | 分散、ばらつき | "high variance across repeated runs" | 繰り返し実行にわたるばらつきが大きい |
| precedent | 先例、前例 | "there is no clear precedent for this case" | このケースには明確な先例がない |
| symptom | 症状、表面に現れた問題 | "address the symptom rather than the root cause" | 根本原因でなく症状に対処する |
| root cause | 根本原因 | "identify the root cause of the failure" | 障害の根本原因を特定する |
| criterion / criteria | 基準（単数 / 複数） | "explicit criteria for escalation" | エスカレーションのための明示的な基準 |
| threshold | しきい値、閾値 | "set a confidence threshold" | 信頼度のしきい値を設定する |
| footprint | 影響範囲 | "minimize the agent's footprint" | エージェントの影響範囲を最小化する |

---

## Section 4: 熟語・慣用表現

複数の単語からなるフレーズで、個々の単語から意味を推測しにくいもの。

| 英語 | 日本語 | 試験文脈での例 | 例文の日本語訳 |
|------|--------|--------------|--------------|
| at the expense of | 〜を犠牲にして | "improves speed at the expense of accuracy" | 精度を犠牲にして速度を向上させる |
| out of scope | 範囲外 | "this request is out of scope for the agent" | このリクエストはエージェントの範囲外だ |
| trade off X for Y | YのためにXを犠牲にする | "trade off precision for higher recall" | より高いリコールのために精度を犠牲にする |
| given that | 〜を考えると、〜を前提として | "given that the task is well-defined" | タスクが明確に定義されているという前提で |
| in the absence of | 〜がない場合は | "in the absence of explicit instructions" | 明示的な指示がない場合は |
| over the course of | 〜の間に、〜を通じて | "context degrades over the course of a session" | セッションが続く間にコンテキストが劣化する |
| in lieu of | 〜の代わりに | "use caching in lieu of repeated API calls" | APIの繰り返し呼び出しの代わりにキャッシュを使う |
| come into play | 重要になる、関係してくる | "context limits come into play for long tasks" | 長いタスクではコンテキストの制限が関係してくる |
| put in place | 導入する、設ける | "put validation checks in place" | バリデーションチェックを導入する |
| fall short of | 〜に達していない | "the output falls short of the required quality" | 出力が求められる品質に達していない |
| as such | したがって、そういうわけで | "the model is non-deterministic; as such, hooks are needed" | モデルは非決定論的だ。したがってフックが必要になる |
| by and large | 概ね、大体において | "by and large, the approach is effective" | 概ね、そのアプローチは効果的だ |
| bring to bear | 適用する、持ち出す | "bring domain expertise to bear on the problem" | ドメインの専門知識を問題に適用する |
| work around | 回避する | "work around the limitation using caching" | キャッシュを使って制限を回避する |
| rule out | 排除する、ないと判断する | "rule out network errors first" | まずネットワークエラーの可能性を排除する |
| on a per-X basis | Xごとに | "validate on a per-document basis" | ドキュメントごとに検証する |
| rather than | 〜するのではなく | "addresses a symptom rather than the root cause" | 根本原因でなく症状に対処する |
| in isolation | 単独で、他と切り離して | "the option is correct in isolation but..." | その選択肢は単独では正しいが… |
| at scale | 大規模に、スケールした状態で | "this approach fails at scale" | このアプローチは大規模になると破綻する |
| in practice | 実際には | "in practice, this creates new problems" | 実際には、これは新たな問題を生む |

---

## Section 5: 試験問題特有の定型パターン

設問文・選択肢に繰り返し現れる定型フレーズ。パターンを知っていると読解速度が上がる。

### 設問文パターン

| パターン | 意味・読み方のコツ |
|---------|-----------------|
| Which of the following **best** addresses... | 「最も適切に対処する」選択肢を選ぶ。完全正解でなくても「最善」を選ぶ |
| What is the **most effective** first step to... | 複数手順があるとき、最初にすべき最善策を選ぶ |
| A developer **needs to**... What should they do? | 要件が与えられ、それを満たす手段を選ぶ |
| Production logs **show that**... What is the **root cause**? | 症状から原因を特定する問題 |
| What change would **most effectively** address... | 現状を改善する変更を選ぶ |
| Which approach **minimizes** X while maintaining Y? | XとYのトレードオフを正しく理解しているか問う |
| The team wants to **ensure** that... | 保証・強制の手段を選ぶ問題 |

### 選択肢の解説で使われるパターン

| パターン | 意味 |
|---------|------|
| Option X **incorrectly assumes** that... | この選択肢は誤った前提に立っている |
| Option Y **addresses a symptom rather than the root cause** | 根本原因でなく表面的な症状に対処している |
| Option Z is **over-engineered** for this scenario | このシナリオには不必要に複雑すぎる |
| This option **would work but is less effective than** [correct answer] | 機能はするが最善ではない |
| This option **conflates** X with Y | XとYを混同している |
| This option is **correct in isolation but** fails to... | 単体では正しいが、全体では問題がある |
| This option **solves a different problem** | 問われている問題とは別の問題を解いている |

---

## Section 6: 否定・逆接・比較の表現

設問の罠になりやすい表現。読み飛ばすと意味が逆になる。

| 英語 | 日本語 | 注意点 |
|------|--------|--------|
| rather than | 〜するのではなく | "X rather than Y" → X が正しく Y が間違い |
| instead of | 〜の代わりに | 代替手段を示す |
| despite | 〜にもかかわらず | 逆接。直後の内容が主張 |
| even though | 〜であるにもかかわらず | 強い逆接 |
| unless | 〜でない限り | 否定条件 |
| at the cost of | 〜を犠牲にして | "at the expense of" と同義 |
| however | しかし | 前の文の内容が否定・転換される |
| while | 〜ではあるが / 〜している間 | 文脈によって逆接か時間か変わる |
| not only ... but also | 〜だけでなく〜も | 追加の条件 |
| neither ... nor | 〜も〜もない | 両方否定 |
| in contrast to | 〜とは対照的に | 比較で差異を強調 |
| as opposed to | 〜ではなく（対比） | "X as opposed to Y" → X を推奨 |
| compared to | 〜と比較して | 相対的な評価 |
