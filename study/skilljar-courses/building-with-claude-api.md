<!-- markdownlint-disable -->

# Claude API で構築する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api>  
**所要時間:** 約8.1時間  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** Phase 1  

---

## カリキュラム

### レッスン 01: コースへようこそ

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287818>  

Open in Claude
0 seconds of 2 minutes, 14 secondsVolume 90%

---

### レッスン 02: Claude モデルの概要

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287722>  

Open in Claude

---

### レッスン 03: API へのアクセス

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287726>  

Open in Claude
0 seconds of 5 minutes, 18 secondsVolume 90%
00:00
05:18

Claude でアプリケーションを構築するとき、リクエストのライフサイクル全体を理解しておくと、より良いアーキテクチャ上の判断ができ、問題のデバッグもより効果的になります。ユーザーがチャットインターフェースで「send」をクリックした瞬間から、Claude のレスポンスが画面に表示されるまでに何が起こるのかを順に見ていきましょう。

#### 5 ステップのリクエストフロー

Claude とのすべてのやり取りは、サーバーへのリクエスト、Anthropic API へのリクエスト、モデル処理、サーバーへのレスポンス、クライアントへのレスポンスという、5 つの明確なフェーズを持つ予測可能なパターンに従います。

#### サーバーが必要な理由

クライアントサイドのコードから Anthropic API に直接リクエストを送ってはいけません。理由は次のとおりです。

- API リクエストには認証用の秘密 API キーが必要です
- このキーをクライアントコード内で公開すると、重大なセキュリティ脆弱性になります
- 誰でもキーを抽出し、不正なリクエストを行える可能性があります

代わりに、Web アプリやモバイルアプリは自分のサーバーにリクエストを送り、そのサーバーが安全に保存されたキーを使って Anthropic API と通信します。

#### API リクエストを行う

サーバーが Anthropic API にアクセスするときは、公式 SDK を使うことも、通常の HTTP リクエストを行うこともできます。Anthropic は Python、TypeScript、JavaScript、Go、Ruby 向けの SDK を提供しています。

すべてのリクエストには、次の必須フィールドを含める必要があります。

- API Key - Anthropic に対してリクエストを識別します
- Model - 使用するモデルの名前（"claude-3-sonnet" など）
- Messages - ユーザーの入力テキストを含むリスト
- Max Tokens - Claude が生成できるトークン数の上限

#### Claude の処理の内部

Anthropic がリクエストを受け取ると、Claude は tokenization、embedding、contextualization、generation という 4 つの主な段階で処理します。

##### Tokenization

Claude はまず、入力テキストを token と呼ばれる小さなまとまりに分割します。これは単語全体、単語の一部、スペース、記号などです。単純化して、各単語が 1 つの token だと考えてください。

##### Embedding

各 token は embedding に変換されます。これは、その単語が持ちうるすべての意味を表す長い数値のリストです。embedding は、意味的な関係を捉える数値的な定義のようなものだと考えてください。

単語には複数の意味があることがよくあります。たとえば、"quantum" は次のものを指す可能性があります。

- 物理量の離散的な単位（物理学）
- 量子力学または量子物理学の概念
- 非常に小さいもの、または亜原子レベルのもの
- 量子コンピューティングの応用

##### Contextualization

Claude は周囲の単語に基づいて各 embedding を精緻化し、文脈上もっとも可能性の高い意味を判断します。このプロセスでは、適切な定義が強調されるように数値表現が調整されます。

##### Generation

contextualized embeddings は出力層を通過し、次に来る可能性のある各単語の確率が計算されます。Claude は常に最高確率の単語を選ぶわけではありません。確率と制御されたランダム性を組み合わせて、自然で多様なレスポンスを作成します。

各単語を選択した後、Claude はそれをシーケンスに追加し、次の単語について同じプロセス全体を繰り返します。

#### Claude が生成を停止するとき

各 token の後、Claude は続行するかどうかを判断するためにいくつかの条件を確認します。

- Max tokens reached - 指定した上限に達しましたか？
- Natural ending - end-of-sequence token を生成しましたか？
- Stop sequence - 事前定義された停止フレーズに遭遇しましたか？

#### API レスポンス

生成が完了すると、API は次を含む構造化レスポンスを返します。

- Message - 生成されたテキスト
- Usage - 入力 token と出力 token の数
- Stop Reason - 生成が終了した理由

サーバーはこのレスポンスを受け取り、生成されたテキストをクライアントアプリケーションに転送します。そこでユーザーインターフェースに表示されます。

#### 重要なポイント

この流れを理解すると、次のことに役立ちます。

- API キーを保護する安全なアーキテクチャを設計する
- ユースケースに適した token 上限を設定する
- アプリケーションロジックでさまざまな stop reason を処理する
- パイプラインのどこで問題が発生しうるかを理解してデバッグする

すべての詳細を暗記する必要はありません。目的は、Claude の API を扱うときに出会う用語と全体的なプロセスに慣れることです。

---

### レッスン 04: API キーを取得する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/296766>  

Open in Claude

次の動画では Anthropic API にリクエストを送ります。そのためには、秘密 API キーが必要です。このガイドでは、API キーを作成する手順を説明します。

1. **ステップ 1: Anthropic API Console に移動する**

ブラウザで https://console.anthropic.com/ に移動し、Anthropic アカウントにログインします。すると、次のようなページが表示されます。

2. **ステップ 2: 'Get API Keys' ボタンをクリックする**

このボタンは、メインダッシュボードページの右上付近にあります。

3. **ステップ 3: 'Create Key' ボタンをクリックする**

ページ右上にある 'Create Key' ボタンを見つけてクリックします。

4. **ステップ 4: キーの workspace と名前を入力する**

workspace 'Default' にキーを作成し、キーの名前を入力します。この名前は、生成したキーを識別するために使われます。ここでは 'Anthropic Course' という名前を使いましょう。

5. **ステップ 5: キーをコピーする**

API キーがポップアップウィンドウに表示されます。このキーをコピーして保管してください。次の動画で使用します。このキーは一度しか表示されないため、必ずコピーしてください。

誤ってウィンドウを閉じてしまった場合は、古いキーを削除して再生成してください。

---

### レッスン 05: リクエストを行う

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287725>  

Open in Claude

基本的なセットアップと構造を理解すれば、Anthropic API への最初のリクエストは簡単です。このガイドでは、Python を使って Claude にプロンプトへ応答させるための基本手順を説明します。

#### 環境をセットアップする

API 呼び出しを行う前に、必要なパッケージをインストールし、API キーを安全に設定する必要があります。

まず、Jupyter notebook で必要な依存関係をインストールします。

```bash
%pip install anthropic python-dotenv
```

次に、notebook と同じディレクトリに .env ファイルを作成し、API キーを安全に保存します。

```bash
ANTHROPIC_API_KEY="your-api-key-here"
```

この方法により、API キーをコードの外に置き、誤ってバージョン管理にコミットすることを防げます。必ず .env を .gitignore ファイルに追加してください。

環境変数を読み込み、API client を作成します。

```python
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
```

#### Create 関数

API リクエストの中心となるのは client.messages.create() 関数です。この関数には 3 つの重要なパラメータが必要です。

- model - 使用したい Claude モデルの名前
- max_tokens - レスポンス長の安全上限（目標値ではありません）
- messages - Claude に送信する会話履歴

max_tokens パラメータは安全機構として機能します。1000 に設定すると、Claude はまだ話すことがあっても 1000 tokens 後に生成を停止します。Claude はこの上限に到達しようとするわけではありません。適切だと思う内容を書き、最大値に達した場合に停止するだけです。

#### Messages を理解する

Messages は、チャットアプリケーションに似た、あなたと Claude の会話を表します。message には 2 種類あります。

- User messages - Claude に送信したい内容（人間が書いたもの）
- Assistant messages - Claude が生成したレスポンス

各 message は、role（"user" または "assistant"）と content（実際のテキスト）を持つ dictionary です。

#### 最初のリクエストを行う

Claude にリクエストを行う完全な例を示します。

```python
message = client.messages.create(
model=model,
max_tokens=1000,
messages=[
{
"role": "user",
"content": "What is quantum computing? Answer in one sentence"
}
]
)
```

このコードを実行すると、Claude はリクエストを処理し、生成されたテキストとリクエストに関する metadata を含む response object を返します。

#### レスポンスを取り出す

response object には多くの情報が含まれますが、通常は生成されたテキストだけが必要です。次のようにアクセスします。

```python
message.content[0].text
```

これにより、次のような読みやすい出力が得られます: "Quantum computing is a type of computation that leverages quantum mechanics principles like superposition and entanglement to process information using quantum bits (qubits), potentially solving certain complex problems exponentially faster than classical computers."

これらの基本が整えば、さまざまなプロンプトを試し、Claude とのより複雑なやり取りを構築し始めることができます。

---

### レッスン 06: マルチターン会話

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735>  

Open in Claude

Anthropic API と Claude を扱うとき、理解しておくべき重要な概念があります。Claude は会話履歴を一切保存しません。あなたが行う各リクエストは完全に独立しており、以前のやり取りの記憶はありません。

つまり、Claude が以前の messages の文脈を覚えている multi-turn conversation をしたい場合は、conversation state を自分で管理する必要があります。

#### ステートレスな会話の問題

Claude に "What is quantum computing?" と尋ねて良いレスポンスを得たとします。その後で "Write another sentence" と続けても、Claude は何について言っているのか分かりません。量子コンピューティングの話題を記憶していないため、まったくランダムな内容について文を書いてしまいます。

#### Multi-Turn Conversations の仕組み

会話の文脈を維持するには、次の 2 つを行う必要があります。

- コード内ですべての messages のリストを手動で管理する
- 毎回のリクエストで完全な message history を送信する

実際に機能する流れは次のとおりです。

1. 最初の user message を Claude に送信する
2. Claude のレスポンスを取得し、assistant message として message list に追加する
3. フォローアップ質問を別の user message として追加する
4. 会話履歴全体を Claude に送信する

#### Helper Functions を作成する

会話管理を簡単にするために、3 つの helper functions を作成できます。

```python
def add_user_message(messages, text):
user_message = {"role": "user", "content": text}
messages.append(user_message)

def add_assistant_message(messages, text):
assistant_message = {"role": "assistant", "content": text}
messages.append(assistant_message)

def chat(messages):
message = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
)
return message.content[0].text
```

#### すべてを組み合わせる

これらの関数を使って会話を維持する方法は次のとおりです。

```python
# Start with an empty message list

messages = []

# Add the initial user question

add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response

answer = chat(messages)

# Add Claude's response to the conversation history

add_assistant_message(messages, answer)

# Add a follow-up question

add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context

final_answer = chat(messages)
```

これで Claude は、完全な会話コンテキストが提供されているため、"Write another sentence" が量子コンピューティングの定義を拡張することを指していると理解します。

これらの helper functions は、Claude を使った作業全体で役立ち、複数のやり取りにわたって意味のある会話を維持できるアプリケーションをはるかに簡単に構築できます。

---

### レッスン 07: チャット演習

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287727>  

Open in Claude

---

### レッスン 08: System prompts

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287733>  

Open in Claude
0 seconds of 6 minutes, 20 secondsVolume 90%

System prompts は、Claude がユーザー入力にどう応答するかをカスタマイズする強力な方法です。汎用的な回答を得る代わりに、Claude のトーン、スタイル、アプローチを特定のユースケースに合わせて形作ることができます。

#### System Prompts が重要な理由

数学チューターの chatbot を構築する場合を考えてみましょう。生徒が "How do I solve 5x + 2 = 3 for x?" と尋ねたとき、Claude には答えをただ吐き出すのではなく、本物のチューターのように振る舞ってほしいはずです。優れた数学チューターは次のようにするべきです。

- 最初から完全な解答ではなくヒントを与える
- 問題を段階的に、生徒に寄り添って進める
- 類似問題の解法を例として示す

Claude に絶対してほしくないことは次のとおりです。

- すぐに直接の答えを与える
- 電卓を使えばよいとだけ生徒に言う

#### System Prompts の仕組み

System prompts は、Claude がどう応答するかについての guidance を提供します。これらは plain strings として定義し、create function call に渡します。主な利点は次のとおりです。

- System prompts は Claude に応答方法の guidance を提供する
- Claude は指定された role の人物が応答するような方法で応答しようとする
- Claude をタスクに集中させるのに役立つ

基本構造は次のとおりです。

```python
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
model=model,
messages=messages,
max_tokens=1000,
system=system_prompt
)
```

#### 違いを見る

system prompt がない場合、Claude はすぐに完全な step-by-step solution を提示します。これは役に立つかもしれませんが、生徒が自分で問題を考え抜くことを促しません。

数学チューターの system prompt を使うと、Claude のレスポンスは大きく変わります。完全な解法を提供する代わりに、Claude は "What do you think would be a good first step to isolate x? Consider what operation we might need to perform on both sides to start moving terms around." のような導く質問をします。

#### 柔軟な Chat Function を構築する

system prompts をハードコードする代わりに、system prompts をパラメータとして受け取ることで chat function をより再利用しやすくできます。

```python
def chat(messages, system=None):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
}

if system:
params["system"] = system

message = client.messages.create(**params)
return message.content[0].text
```

この方法は重要な細部を扱っています。Claude の API は system=None を受け付けないため、system parameter は提供された場合にだけ条件付きで含める必要があります。

これで、system prompt ありでもなしでも chat function を呼び出せます。

```python
# Without system prompt

answer = chat(messages)

# With system prompt

system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)
```

System prompts は、意図した目的に対して一貫して適切に振る舞う AI アプリケーションを作成するために不可欠です。汎用的な AI レスポンスを、専門化された role に適したやり取りへと変換します。

---

### レッスン 09: System prompts 演習

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287724>  

Open in Claude

---

### レッスン 10: Temperature

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287728>  

Open in Claude
0 seconds of 6 minutes, 7 secondsVolume 90%

Temperature は、Claude のレスポンスがどれだけ予測可能または創造的になるかを制御する強力なパラメータです。効果的な使い方を理解すると、AI アプリケーションを大きく改善できます。

#### Claude がテキストを生成する仕組み

temperature に入る前に、Claude の text generation process を理解しておくと役立ちます。Claude に "What do you think?" のような prompt を送ると、3 つの重要なステップを通ります。

1. Tokenization - 入力を小さなまとまりに分割する
2. Prediction - 次に来る可能性のある単語の確率を計算する
3. Sampling - それらの確率に基づいて token を選ぶ

この例では、Claude は "about" に 30%、"would" に 20%、"of" に 10% といった確率を割り当てるかもしれません。モデルは 1 つの token を選択し、このプロセス全体を繰り返して完全な文を作ります。

#### Temperature の役割

Temperature は 0 から 1 の間の小数値で、これらの選択確率に直接影響します。Claude のレスポンスにおける「創造性ダイヤル」を調整するようなものです。

低い temperature（0 に近い）では、Claude は非常に deterministic になり、ほぼ常に最高確率の token を選びます。高い temperature（1 に近い）では、Claude は選択肢全体に確率をより均等に分散し、より多様で創造的な出力になります。

#### Interactive Temperature Demo

Claude の interactive demo で temperature の動作を確認できます。temperature slider を調整すると、確率分布がどのように変わるかを見てください。

temperature 0.0 では、"about" が 100% の確率になり、完全に deterministic です。temperature 1.0 では、確率がすべての可能な tokens により均等に広がり、ランダム性と創造性が導入されます。

#### 適切な Temperature を選ぶ

タスクによって適した temperature range は異なります。

| Temperature range | 用途 |
|------|------|
| Low Temperature (0.0 - 0.3) | 事実に基づくレスポンス / Coding assistance / Data extraction / Content moderation |
| Medium Temperature (0.4 - 0.7) | Summarization / Educational content / Problem-solving / 制約のある Creative writing |
| High Temperature (0.8 - 1.0) | Brainstorming / Creative writing / Marketing content / Joke generation |

#### コードで Temperature を実装する

chat function に temperature support を追加するのは簡単です。既存の関数を次のように修正します。

```python
def chat(messages, system=None, temperature=1.0):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature
}

if system:
params["system"] = system

message = client.messages.create(**params)
return message.content[0].text
```

主な変更点は、temperature=1.0 をパラメータとして追加し、params dictionary に "temperature": temperature を含めることです。

#### Temperature の効果をテストする

temperature の動作を見るには、異なる設定で映画のアイデアを生成してみてください。

```python
# Low temperature - more predictable

answer = chat(messages, temperature=0.0)

# High temperature - more creative

answer = chat(messages, temperature=1.0)
```

temperature 0.0 では、"A time-traveling archaeologist must prevent ancient artifacts from being stolen." のようなレスポンスが一貫して得られるかもしれません。temperature 1.0 では、テーマ、キャラクター、プロット要素にずっと多くのバリエーションが見られます。

#### 重要なポイント

temperature は異なる出力を保証するものではなく、それらが得られる確率を変えるだけだということを覚えておいてください。高い temperature でも、Claude が時々似たレスポンスを生成することがあります。重要なのは、temperature の選択を特定のユースケースに合わせることです。

- 一貫した事実に基づくレスポンスが必要ですか？ low temperature を使う
- 創造的な brainstorming が欲しいですか？ temperature を上げる
- その中間ですか？ medium temperatures はほとんどの一般的なタスクにうまく機能する

Temperature は、特定のニーズに合わせて Claude の挙動を fine-tune するために調整できる、もっとも実用的なパラメータの 1 つです。

---

### レッスン 11: コース満足度アンケート

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/297284>  

Open in Claude
Loading...

---

### レッスン 12: Response streaming

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734>  

Open in Claude

Claude でチャットアプリケーションを構築するとき、大きなユーザー体験上の課題があります。レスポンス生成に 10〜30 秒かかることがあり、その間ユーザーは loading spinner を見続けることになります。解決策は response streaming です。これは Claude が生成するにつれてテキストを chunk ごとに表示できるようにし、ずっと反応の良い感覚を作ります。

#### 標準レスポンスの問題

一般的なチャット設定では、サーバーは user message を Claude に送り、完全なレスポンスを待ってからクライアントに何かを返します。これにより、ユーザーには何が起きているのかフィードバックがない気まずい遅延が生まれます。

#### Streaming の仕組み

streaming を有効にすると、Claude はリクエストを受け取りテキスト生成を開始していることを示す初期レスポンスをすぐに返します。その後、一連の events を受け取り、それぞれに全体レスポンスの小さな一部が含まれます。

サーバーは、これらの text chunks が到着するたびにクライアントアプリケーションへ転送でき、ユーザーはレスポンスが単語ごとに組み上がっていくのを見ることができます。これらすべての events は、Claude への単一のリクエストの一部です。

#### Stream Events を理解する

streaming を有効にすると、Claude はいくつかの種類の events を返します。

- MessageStart - 新しい message が送信されている
- ContentBlockStart - text、tool use、その他の content を含む新しい block の開始
- ContentBlockDelta - 実際に生成された text の chunks
- ContentBlockStop - 現在の content block が完了した
- MessageDelta - 現在の message が完了した
- MessageStop - 現在の message に関する情報の終了

ContentBlockDelta events には、ユーザーに表示したい実際の生成テキストが含まれます。

#### 基本的な Streaming 実装

streaming を有効にするには、messages.create call に stream=True を追加します。

```python
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
stream=True
)

for event in stream:
print(event)
```

#### 簡略化された Text Streaming

events を手動で解析する代わりに、SDK の簡略化された streaming interface を使って text content だけを抽出できます。

```python
with client.messages.stream(
model=model,
max_tokens=1000,
messages=messages
) as stream:
for text in stream.text_stream:
print(text, end="")
```

この方法は、実際の text content 以外を自動的にフィルタします。通常、ユーザーにレスポンスを表示するために必要なのはこれです。

#### 完全な Message を取得する

個々の chunks を streaming するのはユーザー体験に優れていますが、保存や追加処理のために complete message が必要になることもよくあります。streaming が完了した後、組み立てられた final message を取得できます。

```python
with client.messages.stream(
model=model,
max_tokens=1000,
messages=messages
) as stream:
for text in stream.text_stream:

# Send each chunk to your client

pass

# Get the complete message for database storage

final_message = stream.get_final_message()
```

これにより、ユーザー向けの real-time streaming と、アプリケーションロジック用の complete message object の両方を得られます。

---

### レッスン 13: Structured data

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287732>  

Open in Claude
0 seconds of 5 minutes, 59 secondsVolume 90%

Claude に JSON、Python code、bulleted lists のような structured data を生成させる必要がある場合、よくある問題に遭遇します。Claude は役に立とうとして、コンテンツの周りに説明文を追加したがります。通常これは素晴らしいことですが、ときには余計なもののない raw data だけが必要です。

AWS EventBridge rules を生成する Web アプリを構築する場合を考えてみましょう。ユーザーは説明を入力し、generate をクリックし、すぐにコピーして使える clean JSON を期待します。Claude が JSON を markdown code blocks と説明文で囲んで返すと、ユーザーはレスポンス全体を単純にコピーできません。JSON 部分だけを手動で選択する必要があります。

デフォルトレスポンスの問題

デフォルトでは、Claude に JSON を生成するよう頼むと、次のようなものが返ってくることがあります。

```json
{
"source": ["aws.ec2"],
"detail-type": ["EC2 Instance State-change Notification"],
"detail": {
"state": ["running"]
}
}
```

この rule は、instances が running を開始したときの EC2 instance state changes を捕捉します。

JSON は正しいですが、markdown formatting で囲まれ、説明文が含まれています。ユーザーが raw JSON をコピーする必要がある Web アプリでは、これはユーザー体験に friction を生みます。

#### 解決策: Assistant Message Prefilling + Stop Sequences

assistant message prefilling と stop sequences を組み合わせることで、欲しい content を正確に得られます。仕組みは次のとおりです。

```python
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
```

この technique は次のように機能します。

- user message が Claude に何を生成するかを伝える
- prefilled assistant message により、Claude はすでに markdown code block を開始していると考える
- Claude は続けて JSON content だけを書く
- Claude が code block を ``` で閉じようとすると、stop sequence により generation が即座に終了する

結果は、余計な formatting のない clean JSON です。

```json
{
"source": ["aws.ec2"],
"detail-type": ["EC2 Instance State-change Notification"],
"detail": {
"state": ["running"]
}
}
```

#### レスポンスを処理する

レスポンスに余分な newline characters が含まれることに気づくかもしれません。これは簡単に処理できます。

```python
import json

# Clean up and parse the JSON

clean_json = json.loads(text.strip())
```

#### JSON 以外にも

この technique は JSON generation に限定されません。commentary なしで structured data が必要なときはいつでも使えます。

- Python code snippets
- Bulleted lists
- CSV data
- 説明ではなく content だけが欲しい、任意の formatted content

重要なのは、Claude が自然に content を何で囲みたがるかを特定し、それを prefill と stop sequence として使うことです。code では通常 markdown code blocks です。lists では別の formatting markers かもしれません。

この方法により、Claude の output format を正確に制御でき、clean structured data が不可欠なアプリケーションに AI-generated content を統合しやすくなります。

---

### レッスン 14: Structured data 演習

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287729>  

Open in Claude

---

### レッスン 15: API で Claude にアクセスするクイズ

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289117>  

Open in Claude
Loading...

---

### レッスン 16: Prompt evaluation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287731>  

Open in Claude

Claude を扱うとき、良い prompt を書くことは始まりにすぎません。信頼できる AI アプリケーションを構築するには、prompt engineering と prompt evaluation という 2 つの重要な概念を理解する必要があります。Prompt engineering はより良い prompts を書くための techniques を提供し、prompt evaluation はそれらの prompts が実際にどれだけうまく機能するかを測定するのに役立ちます。

#### Prompt Engineering vs Prompt Evaluation

Prompt engineering は、効果的な prompts を作るための toolkit です。次のような techniques が含まれます。

- Multishot prompting
- XML tags による構造化
- その他多くの best practices

これらの techniques は、Claude があなたの依頼内容と、どのように応答してほしいかを正確に理解するのに役立ちます。

Prompt evaluation は別のアプローチを取ります。prompts の書き方に焦点を当てるのではなく、automated testing を通じてその有効性を測定します。次のことができます。

- expected answers に対してテストする
- 同じ prompt の異なる versions を比較する
- outputs に errors がないか review する

#### Prompt を書いた後の 3 つの道

prompt の下書きができたら、通常、次に何をするかについて 3 つの選択肢があります。

Option 1: prompt を一度だけテストし、十分良いと判断する。これは、ユーザーが予期しない inputs を提供したときに production で壊れる大きなリスクを伴います。

Option 2: prompt を数回テストし、corner case を 1 つか 2 つ処理できるように調整する。option 1 よりは良いものの、ユーザーはあなたが考慮していない非常に予期しない outputs を提供することがよくあります。

Option 3: prompt を evaluation pipeline に通して score を付け、objective metrics に基づいて prompt を反復改善する。このアプローチにはより多くの作業とコストが必要ですが、prompt の reliability に対してはるかに高い confidence が得られます。

#### 多くのエンジニアが Testing Traps に陥る理由

Options 1 と 2 は、私自身も含め、すべてのエンジニアが陥る一般的な traps です。重要なアプリケーション向けの prompt を書いても、十分に徹底してテストしないのは自然なことです。私たちは、実際のユーザーが遭遇する edge cases の多さを過小評価しがちです。

現実には、prompt を production にデプロイすると、ユーザーはあなたが予想もしなかった方法でそれとやり取りします。限られたテストでは堅牢に見えた prompt も、現実世界の入力の多様性に直面するとすぐに破綻することがあります。

#### Evaluation-First Approach

Option 3 は、prompt development に対するより体系的なアプローチです。prompt を evaluation pipeline に通すことで、より広範な test cases における performance について objective metrics を得られます。この data-driven approach により、次のことができます。

- production issues になる前に弱点を特定する
- 異なる prompt versions を客観的に比較する
- 測定可能な改善に基づいて confidence を持って反復する
- より信頼できる AI アプリケーションを構築する

このアプローチは、時間と testing infrastructure への upfront investment をより多く必要としますが、最終的なアプリケーションの reliability と robustness に大きな見返りをもたらします。目標は、ユーザーが問題に遭遇した後ではなく、development 中に問題を捕まえることです。

---

### レッスン 17: 典型的な eval workflow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287736>  

Open in Claude

典型的な prompt evaluation workflow は、objective measurement を通じて prompts を体系的に改善するための 5 つの主要ステップに従います。これらの workflows を組み立てる方法は多数あり、さまざまな open source や paid tools もありますが、core process を理解すると、小さく始めて必要に応じて scale up できます。

#### Step 1: Prompt を下書きする

まず、改善したい initial prompt を書きます。この例では、単純な prompt を使います。

```python
prompt = f"""
Please answer the user's question:

{question}
"""
```

この basic prompt が、testing と improvement の baseline になります。

#### Step 2: Eval Dataset を作成する

evaluation dataset には、prompt が production で扱う質問やリクエストの種類を代表する sample inputs が含まれます。dataset には、prompt template に interpolation される questions を含める必要があります。

この例では、dataset には 3 つの questions が含まれます。

- "What's 2+2?"
- "How do I make oatmeal?"
- "How far away is the Moon?"

実世界の evaluations では、数十、数百、あるいは数千の records があるかもしれません。これらの datasets は手作業で組み立てることも、Claude を使って生成することもできます。

#### Step 3: Claude に通す

dataset から各 question を取り出し、prompt template と結合して complete prompts を作成します。その後、それぞれを Claude に送信して responses を取得します。

たとえば、最初の question は次のようになります。

```
Please answer the user's question:
What's 2+2?
```

Claude は数学の question に対して "2 + 2 = 4" と応答し、2 番目の question には oatmeal の調理手順を示し、3 番目には Moon までの距離を答えるかもしれません。

#### Step 4: Grader に通す

grader は、original question と Claude の answer の両方を調べて、Claude の responses の quality を評価します。このステップは objective scoring を提供し、通常は 1 から 10 の scale で、10 が perfect answer、低い scores は改善の余地を示します。

この例では、grader は次のように割り当てるかもしれません。

- Math question: 10（perfect answer）
- Oatmeal question: 4（needs improvement）
- Moon question: 9（very good answer）

すべての questions の average score により、objective measurement が得られます: (10 + 4 + 9) ÷ 3 = 7.66

#### Step 5: Prompt を変更して繰り返す

baseline score が得られたら、prompt を修正し、プロセス全体を再実行して変更が performance を改善したかを確認できます。

たとえば、prompt により多くの guidance を追加するかもしれません。

```python
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

この improved prompt を同じ evaluation process に通した後、average score が 8.7 に上がるかもしれません。これは追加 instruction が Claude のより良い responses に役立ったことを示します。

#### Prompt Scoring

この workflow の主な利点は、prompt performance の objective measurements を得られることです。次のことができます。

- 異なる prompt versions を数値で比較する
- もっとも score の良い version を使う
- さらに良いアプローチを見つけるために反復を続ける

この体系的なアプローチにより、prompt engineering から当て推量を取り除き、変更が単なる別 variation ではなく実際に improvement であるという confidence が得られます。

---

### レッスン 18: Test datasets を生成する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287739>  

Open in Claude

custom prompt evaluation workflow の構築は、しっかりした prompt を作成し、それがどれだけうまく機能するかを見るための test data を生成することから始まります。AWS-specific code を書くユーザーを支援する prompt の evaluation system をセットアップする手順を見ていきましょう。

#### Goal を設定する

私たちの prompt は、AWS use cases 向けに次の 3 種類の output を書くユーザーを支援する必要があります。

- Python code
- JSON configuration files
- Regular expressions

重要な要件は、ユーザーが task の支援を依頼したとき、余計な explanations、headers、footers なしで、これらの formats のいずれかで clean output を返すことです。

開始時の prompt（version 1）は次のとおりです。

```python
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

#### Evaluation Dataset を作成する

evaluation dataset には、prompt に入力する inputs が含まれます。prompt と input の各組み合わせについて、prompt を実行し、results を分析します。

dataset は JSON objects の array になります。各 object には、Claude に達成してほしい内容を説明する "task" property が含まれます。この dataset は手作業で作成することも、Claude を使って自動生成することもできます。

test data を生成しているので、full Claude model ではなく Haiku のような faster model を使う絶好の機会です。

#### コードで Test Data を生成する

test dataset を自動生成する関数を作成しましょう。まず、Claude を扱うための helper functions が必要です。

```python
def add_user_message(messages, text):
user_message = {"role": "user", "content": text}
messages.append(user_message)

def add_assistant_message(messages, text):
assistant_message = {"role": "assistant", "content": text}
messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature
}
if system:
params["system"] = system
if stop_sequences:
params["stop_sequences"] = stop_sequences

response = client.messages.create(**params)
return response.content[0].text
```

次に dataset generation function を作成します。

````python
def generate_dataset():
prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:

```json
[
{
"task": "Description of task",
},
...additional
]
```

- Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
- Focus on tasks that do not require writing much code

Please generate 3 objects.
"""
````

JSON response を適切に parse するために、prefilling と stop sequences を使います。

```python
messages = []
add_user_message(messages, prompt)
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
return json.loads(text)
```

#### Dataset Generation をテストする

関数を実行して、どのような test cases が得られるか見てみましょう。

```python
dataset = generate_dataset()
print(dataset)
```

これにより、target outputs である Python functions、JSON configurations、AWS-specific tasks の regular expressions をカバーする 3 つの異なる test cases が返るはずです。

#### Dataset を保存する

dataset ができたら、evaluation 中に後で簡単に読み込めるように file に保存します。

```python
with open('dataset.json', 'w') as f:
json.dump(dataset, f, indent=2)
```

これにより、notebook と同じ directory に dataset.json file が作成され、prompt evaluation の準備ができた tasks の list が含まれます。

この foundation が整うと、AWS-related coding tasks のさまざまな種類に対して prompts がどれだけうまく機能するかを評価するための test data を体系的に生成できるようになります。

Downloads
001_prompt_evals.ipynb
(opens in new tab)

---

### レッスン 19: Eval を実行する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287743>  

Open in Claude

evaluation dataset の準備ができたので、core evaluation pipeline を構築します。これには、各 test case を取り出し、prompt と結合し、Claude に渡し、その results を grading することが含まれます。

evaluation process は明確な workflow に従います。test cases の dataset を取り、各 case を prompt template と組み合わせ、処理のため Claude に送信し、grader system を使って output を評価します。

#### Core Functions を構築する

evaluation pipeline は、それぞれ特定の責務を持つ 3 つの main functions で構成されます。もっとも単純なもの、individual prompts を扱う関数から始めましょう。

#### run_prompt Function

この関数は test case を受け取り、prompt template と結合します。

```python
def run_prompt(test_case):
"""Merges the prompt and test case input, then returns the result"""
prompt = f"""
Please solve the following task:

{test_case["task"]}
"""

messages = []
add_user_message(messages, prompt)
output = chat(messages)
return output
```

現時点では、prompt を非常に単純にしています。formatting instructions を一切含めていないため、Claude はおそらく必要以上に verbose な output を返すでしょう。prompt design を反復する中で、後ほどこれを refine します。

#### run_test_case Function

この関数は、単一の test case を実行し、result を grading する流れを調整します。

```python
def run_test_case(test_case):
"""Calls run_prompt, then grades the result"""
output = run_prompt(test_case)

# TODO - Grading

score = 10

return {
"output": output,
"test_case": test_case,
"score": score
}
```

今のところ、hardcoded score of 10 を使っています。grading logic は今後の sections で多くの時間をかける部分ですが、この placeholder により全体 pipeline をテストできます。

#### run_eval Function

この関数は evaluation process 全体を調整します。

```python
def run_eval(dataset):
"""Loads the dataset and calls run_test_case with each case"""
results = []

for test_case in dataset:
result = run_test_case(test_case)
results.append(result)

return results
```

この関数は dataset 内のすべての test case を処理し、すべての results を単一の list に集めます。

#### Evaluation を実行する

evaluation pipeline を実行するには、dataset を読み込み、functions に通します。

```python
with open("dataset.json", "r") as f:
dataset = json.load(f)

results = run_eval(dataset)
```

これを初めて実行するときは、ある程度時間がかかることを想定してください。Claude Haiku でも、full dataset の処理に約 30 seconds かかることがあります。optimization techniques については後で扱います。

#### Results を確認する

evaluation は、各 object が 1 つの test case result を表す structured JSON array を返します。

```python
print(json.dumps(results, indent=2))
```

各 result には 3 つの重要な情報が含まれます。

- output: Claude からの complete response
- test_case: 処理された original test case
- score: evaluation score（現在は hardcoded）

output を見ると分かるように、まだ specific formatting instructions を提供していないため、Claude はかなり verbose な responses を生成します。これは、prompts を refine する中で対処するまさにその種の問題です。

#### 達成したこと

この時点で、core evaluation pipeline の構築に成功しました。dataset を取り、Claude に通して処理し、structured results を収集できます。大きく欠けている部分は grading system です。hardcoded score of 10 は、actual evaluation logic に置き換える必要があります。

この pipeline は、ほとんどの AI evaluation systems の foundation を表しています。単純に見えるかもしれませんが、eval pipeline が実際に行うことの大部分をすでに構築したことになります。複雑さは details にあります。より良い prompts、sophisticated grading、performance optimizations です。

次に、graders という重要なトピックに入ります。これにより、hardcoded scores が Claude の performance に対する meaningful evaluations へと変わります。

---

### レッスン 20: Model based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287742>  

Open in Claude

prompt evaluation workflows を構築するとき、grading systems は output quality について objective signals を提供します。grader は model output を受け取り、何らかの measurable feedback を返します。通常は 1 から 10 の number で、10 は high quality、1 は poor quality を表します。

#### Graders の種類

model outputs を grading する主なアプローチは 3 つあります。

- Code graders - custom logic を使って programmatically に outputs を評価する
- Model graders - 別の AI model を使って quality を評価する
- Human graders - 人間が手動で outputs を review して score を付ける

#### Code Graders

Code graders では、想像できるあらゆる programmatic check を実装できます。一般的な用途には次のものがあります。

- output length の確認
- output に特定の words がある/ないことの検証
- JSON、Python、regex の syntax validation
- Readability scores

唯一の要件は、code が何らかの usable signal を返すことです。通常は 1 から 10 の number です。

#### Model Graders

Model graders は、original output を別の API call に渡して評価します。このアプローチは、次の評価に非常に高い柔軟性を提供します。

- Response quality
- Quality of instruction following
- Completeness
- Helpfulness
- Safety

#### Human Graders

Human graders はもっとも柔軟ですが、時間がかかり退屈です。次の評価に役立ちます。

- General response quality
- Comprehensiveness
- Depth
- Conciseness
- Relevance

#### Evaluation Criteria を定義する

grader を実装する前に、clear evaluation criteria が必要です。code generation prompt では、次に焦点を当てるかもしれません。

- Format - explanation なしで Python、JSON、Regex のみを返すべき
- Valid Syntax - 生成された code は valid syntax を持つべき
- Task Following - response は accurate code でユーザーの task に直接対応すべき

最初の 2 つの criteria は code graders と相性がよく、task following は model graders の柔軟性のため、model graders により適しています。

#### Model Grader を実装する

model grader function を構築する方法は次のとおりです。

```python
def grade_by_model(test_case, output):

# Create evaluation prompt

eval_prompt = """
You are an expert code reviewer. Evaluate this AI-generated solution.

Task: {task}
Solution: {solution}

Provide your evaluation as a structured JSON object with:

- "strengths": An array of 1-3 key strengths
- "weaknesses": An array of 1-3 key areas for improvement
- "reasoning": A concise explanation of your assessment
- "score": A number between 1-10
"""

messages = []
add_user_message(messages, eval_prompt)
add_assistant_message(messages, "```json")

eval_text = chat(messages, stop_sequences=["```"])
return json.loads(eval_text)
```

重要な insight は、score とあわせて strengths、weaknesses、reasoning を求めることです。この context がないと、models は 6 前後の middling scores に default しがちです。

#### Workflow に Grading を統合する

test case runner を更新して grader を呼び出します。

```python
def run_test_case(test_case):
output = run_prompt(test_case)

# Grade the output

model_grade = grade_by_model(test_case, output)
score = model_grade["score"]
reasoning = model_grade["reasoning"]

return {
"output": output,
"test_case": test_case,
"score": score,
"reasoning": reasoning
}
```

最後に、すべての test cases にわたる average score を計算します。

```python
from statistics import mean

def run_eval(dataset):
results = []

for test_case in dataset:
result = run_test_case(test_case)
results.append(result)

average_score = mean([result["score"] for result in results])
print(f"Average score: {average_score}")

return results
```

これにより、prompt を反復する際に追跡できる objective metric が得られます。model graders はやや capricious であることがありますが、improvements を測定するための consistent baseline を提供します。

Downloads
001_prompt_evals_grader.ipynb
(opens in new tab)

---
### レッスン 21: Code based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287737>  

Open in Claude

コードを生成するAIモデルを評価するときは、レスポンスが意味をなしているかを確認するだけでは不十分です。生成されたコードが実際に有効な構文を持ち、正しい形式に従っていることも検証する必要があります。ここで code-based grading が役立ちます。

#### Code Grading の仕組み

Code grading は、AIが生成したレスポンスの2つの重要な側面を検証します。

- 形式 - レスポンスは、説明なしで要求されたコードタイプ（Python、JSON、Regex）のみを返す必要があります
- 有効な構文 - 生成されたコードは、意図された言語として実際に正しく解析できる必要があります
- タスクへの準拠 - レスポンスは、求められた内容に直接対応し、正確である必要があります

最初の2つの基準は code grader によって処理され、タスクへの準拠は model grader によって評価されます。これらを組み合わせることで、包括的な評価が可能になります。

#### 構文検証関数

生成されたコードが有効な構文を持つか確認するには、出力の解析を試みる3つのヘルパー関数を作成できます。

```python
def validate_json(text):
try:
json.loads(text.strip())
return 10
except json.JSONDecodeError:
return 0

def validate_python(text):
try:
ast.parse(text.strip())
return 10
except SyntaxError:
return 0

def validate_regex(text):
try:
re.compile(text.strip())
return 10
except re.error:
return 0
```

各関数は、テキストをそれぞれの形式として解析しようとします。解析に成功した場合は満点の10を返します。エラーで失敗した場合、その構文は無効であり、0を返します。

#### データセット形式の要件

code grader がどの validator を使うべきか判断できるように、テストケースでは期待される出力形式を指定する必要があります。

```json
{
"task": "Create a Python function to validate an AWS IAM username",
"format": "python"
}
```

データセット生成プロンプトの出力例構造にこの format フィールドを追加することで、自動的に含めるよう更新できます。

#### プロンプトの明確さを改善する

AIモデルからより良い結果を得るには、期待する出力形式についてプロンプトの指示をより具体的にします。

- Python、JSON、またはプレーンな Regex のみで応答する
- コメント、解説、説明を一切追加しない

事前入力済みの assistant message とコードブロックを使って、モデルが生のコードだけを返すよう促すこともできます。

````python
add_assistant_message(messages, "```code")
````

これにより、Claude は事前に Python、JSON、Regex のどれかを指定しなくても、コード内容の生成を開始するようになります。

#### スコアの組み合わせ

最後のステップは、model grader のスコアと code grader のスコアを統合することです。単純な方法は平均を取ることです。

```python
model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2
```

これにより、コンテンツ品質と技術的な正しさの両方に同じ重みを与えます。特定のユースケースで何がより重要かに応じて、これらの重みを調整してもよいでしょう。

#### 実装のテスト

code grading を実装したら、評価を実行してベースラインスコアを取得します。スコアそのものに本質的な良し悪しはありません。重要なのは、プロンプトを改善することでスコアを向上できるかどうかです。これにより、主観的な評価に頼るのではなく、prompt engineering の進捗を定量的に測定できます。

Downloads
001_prompt_evals_fns.ipynb
(opens in new tab)

---

### レッスン 22: Exercise on prompt evals

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287738>  

Open in Claude
Downloads
001_prompt_evals_complete.ipynb
(opens in new tab)

---

### レッスン 23: Quiz on prompt evaluation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289118>  

Open in Claude
Loading...

---

### レッスン 24: Prompt engineering

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287745>  

Open in Claude

Prompt engineering とは、自分が書いたプロンプトを取り上げ、より信頼性が高く高品質な出力を得るために改善することです。このプロセスでは、基本的なプロンプトから始め、その性能を評価し、体系的に engineering 技法を適用して改善していく反復的な改善を行います。

#### 反復的な改善プロセス

このアプローチは、望む結果が得られるまで繰り返せる明確なサイクルに従います。

1. 目標を設定する - プロンプトに何を達成させたいかを定義する
2. 初期プロンプトを書く - 基本的な最初の試みを作成する
3. プロンプトを評価する - 基準に照らしてテストする
4. prompt engineering 技法を適用する - 性能を改善するための具体的な方法を使う
5. 再評価する - 変更によって実際に結果が改善したことを確認する

性能に満足するまで、最後の2ステップを繰り返します。各反復では、評価スコアに測定可能な改善が見られるべきです。

#### 評価パイプラインのセットアップ

このプロセスを示すために、実践的な例として、アスリート向けの1日分の食事プランを生成するプロンプトを作成します。このプロンプトでは、アスリートの身長、体重、目標、食事制限を考慮し、包括的な食事プランを作成する必要があります。

評価セットアップでは、データセット生成と model grading を処理する PromptEvaluator class を使います。evaluator インスタンスを作成するときは、max_concurrent_tasks parameter で並行数を制御できます。

```python
evaluator = PromptEvaluator(max_concurrent_tasks=5)
```

レート制限エラーを避けるため、最初は低い並行数（3など）から始めます。API quota がより高速な処理を許す場合は、増やすことができます。

#### テストデータの生成

評価システムは、プロンプトの要件に基づいてテストケースを自動生成できます。プロンプトに必要な入力を定義します。

```python
dataset = evaluator.generate_dataset(
task_description="Write a compact, concise 1 day meal plan for a single athlete",
prompt_inputs_spec={
"height": "Athlete's height in cm",
"weight": "Athlete's weight in kg",
"goal": "Goal of the athlete",
"restrictions": "Dietary restrictions of the athlete"
},
output_file="dataset.json",
num_cases=3
)
```

開発中は反復サイクルを速めるため、テストケース数を少なく（2〜3）保ちます。最終検証では増やしてもかまいません。

#### 初期プロンプトを書く

ベースラインを確立するために、シンプルで素朴なプロンプトから始めます。以下は、意図的に基本的な最初の試みの例です。

```python
def run_prompt(prompt_inputs):
prompt = f"""
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
"""

messages = []
add_user_message(messages, prompt)
return chat(messages)
```

この基本的なプロンプトはおそらく低品質な結果を出しますが、改善を測定するための出発点になります。

#### 評価基準を追加する

評価を実行するとき、grading model が考慮すべき追加基準を指定できます。

```python
results = evaluator.run_evaluation(
run_prompt_function=run_prompt,
dataset_file="dataset.json",
extra_criteria="""
The output should include:

- Daily caloric total
- Macronutrient breakdown
- Meals with exact foods, portions, and timing
"""
)
```

これにより、ユースケースにとって重要な具体的要件に照らしてプロンプトが評価されるようになります。

#### 結果の分析

評価を実行すると、数値スコアと詳細な HTML レポートの両方が得られます。レポートでは、各テストケースの結果と、それぞれのスコアに対するモデルの reasoning を正確に確認できます。

初期スコアが低くても落ち込む必要はありません。最初の試みでは10点中2.3点程度は典型的です。目標は、engineering 技法を適用するにつれて一貫した改善を見ることです。

詳細な評価レポートは、プロンプトがどこで失敗しているか、どの改善が必要かを正確に理解するのに役立ちます。このフィードバックを次の反復の指針にします。

#### 次のステップ

ベースラインが確立できたら、具体的な prompt engineering 技法の適用を開始できます。学ぶ各技法は評価スコアの測定可能な改善につながり、基本的なプロンプトを信頼性の高い高性能なツールへと徐々に変えていくはずです。

prompt engineering は反復的なプロセスであることを覚えておいてください。重要なのは、一度に1つの変更を加え、その影響を評価し、うまくいくものを積み重ねることです。この体系的なアプローチにより、特定のユースケースに最も価値をもたらす技法を理解できます。

Downloads
001_prompting.ipynb
(opens in new tab)
002_prompting_completed.ipynb
(opens in new tab)

---

### レッスン 25: Being clear and direct

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287744>  

Open in Claude

プロンプトの最初の1行は、リクエスト全体の中で最も重要な部分です。ここで以降すべての土台を作ります。ここを正しく書くことで、結果を大きく改善できます。

#### 明確かつ直接的であること

重要な最初の1行を作るときは、明確さと直接性という2つの原則に集中します。つまり、Claude に何をしてほしいのかについて曖昧さが残らない、シンプルな言葉を使うということです。

#### 明確なコミュニケーション

「明確」であるとは、次のことを意味します。

- 誰にでも理解できるシンプルな言葉を使う
- 遠回しにせず、望むことを正確に述べる
- Claude のタスクを率直に述べることから始める

「I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called」のような曖昧な表現ではなく、直接的に「Write three paragraphs about how solar panels work.」と書きます。

#### 直接的な指示

「直接的」であることは、リクエストの構造に関係します。

- 質問ではなく指示を使う
- 「Write」「Create」「Generate」のような直接的な動作動詞で始める

「I was reading about renewable energy and geothermal energy sounds neat. What countries use it?」と尋ねる代わりに、「Identify three countries that use geothermal energy. Include generation stats for each.」とします。

#### 実践してみる

この技法の実例を見てみましょう。単に「What should this person eat?」と尋ねる弱いプロンプトから始め、明確で直接的なアプローチを適用できます。

改善版は次のようになります。Generate a one-day meal plan for an athlete that meets their dietary restrictions.

この修正により、Claude にはすぐに次のことが伝わります。

- 取るべき行動（generate）
- 作成するもの（meal plan）
- 主要な制約（one day、for an athlete、meeting dietary restrictions）

#### 結果は重要です

この単純な変更でも、性能に大きな影響を与える可能性があります。この例では、評価スコアが2.32から3.92へ上がりました。冒頭の1行を再構成しただけで、かなりの改善です。

重要なポイントは、Claude は、こちらの意図を推測しなければならない相手としてではなく、明確な指示を必要とする有能なアシスタントとして扱うと最もよく応答するということです。直接的な動作動詞で力強く始め、タスクを具体的にすれば、すぐにより良い結果が得られます。

---

### レッスン 26: Being specific

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287740>  

Open in Claude

Claude を使うとき、結果を改善する最も効果的な方法の1つは、望む内容を具体的に示すことです。すべてをモデルの解釈に任せるのではなく、Claude を求める出力へ導く明確なガイドラインや手順を提供できます。

こう考えてみてください。Claude に「隠れた才能を発見する登場人物について短編を書いて」と頼むと、Claude は無数の方向に進めます。物語は200語かもしれませんし、2,000語かもしれません。登場人物は1人かもしれませんし、5人かもしれません。どんな才能発見のシナリオにも焦点を当てられます。

具体的なガイドラインを追加することで、Claude により明確な目標を与えられます。これにより、出力の一貫性と品質の両方が大きく改善します。

#### 2種類のガイドライン

プロンプトで具体的にする方法には主に2つあり、プロフェッショナルなアプリケーションでは両方が一緒に使われることもよくあります。

#### 出力品質ガイドライン

1つ目のタイプは、出力が備えるべき品質を列挙することに焦点を当てます。これらのガイドラインは次の制御に役立ちます。

- レスポンスの長さ
- 構造と形式
- 含めるべき具体的な属性や要素
- トーンやスタイルの要件

たとえば、物語は1,000語未満であること、登場人物の才能を明らかにする明確な行動を含むこと、少なくとも1人の脇役を登場させることを指定できます。

#### プロセス手順

2つ目のタイプは、Claude が従うべき具体的な手順を提供します。このアプローチは、Claude に問題を体系的に考えさせたい場合や、最終回答に到達する前に複数の観点を検討させたい場合に特に有用です。

いきなり執筆に入るのではなく、Claude に次のように依頼できます。

1. 劇的な緊張を生む才能を3つブレインストーミングする
2. 最も面白い才能を選ぶ
3. その才能を明らかにする重要なシーンをアウトライン化する
4. インパクトを高められる脇役タイプをブレインストーミングする

#### 実際の影響

具体性がもたらす違いは劇的です。食事プランニングのプロンプトをテストしたところ、ガイドラインを追加することで評価スコアは3.92から7.86に改善しました。Claude に含めるべき要素を正確に伝えただけで、出力品質が2倍以上になったのです。

ガイドライン:

1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned

#### 各アプローチを使うタイミング

どの種類の具体性をいつ使うべきかについて、実践的なガイドを示します。

#### 出力ガイドラインは常に使う

ほぼすべてのプロンプトに品質ガイドラインを含めるべきです。これは、一貫して有用な結果を得るための安全網です。

#### 複雑な問題にはプロセス手順を使う

次のような場合は、ステップごとの指示を追加します。

- 複雑な問題のトラブルシューティング
- 意思決定シナリオ
- 批判的思考タスク
- Claude に複数の角度を検討させたいあらゆる状況

たとえば、営業チームの成績が下がった理由を Claude に分析させる場合、1つの潜在的な原因だけに注目させるのではなく、市場指標、業界の変化、個人のパフォーマンス、組織の変化、顧客フィードバックを検討するよう導くべきです。

#### 両方のアプローチを組み合わせる

プロフェッショナルな prompting では、両方の技法が一緒に使われることがよくあります。出力の形式と内容を制御するガイドラインに加えて、Claude が応答前に問題を十分に考え抜くことを保証する手順を含めることができます。

この組み合わせにより、結果の一貫性と、Claude が結論に至る際に重要な要素をすべて考慮したという確信の両方が得られます。

---

### レッスン 27: Structure with XML tags

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287741>  

Open in Claude
0 seconds of 4 minutes, 0Volume 90%

多くのコンテンツを含むプロンプトを作成するとき、Claude はどのテキスト片が一緒に属しているのか、あるいは異なるセクションが何を表しているのかを理解するのに苦労することがあります。XML タグは、特に大量のデータを補間するときに、プロンプトへ構造と明確さを追加するシンプルな方法です。

#### 構造が重要な理由

20ページ分の売上記録を分析する必要があるプロンプトを考えてみましょう。明確な境界がなければ、Claude はあなたの指示と、分析してほしい実際のデータを区別するのに苦労する可能性があります。

上の例は、不明確な境界が Claude に意図を解析させるうえでどれほど難しくするかを示しています。売上記録を <sales_records> と </sales_records> のような XML タグで囲むことで、Claude がプロンプトの構造を理解しやすくなる明確な区切りを作れます。

#### 実践例: コードとドキュメント

XML タグが重要な理由を示す、よりはっきりした例を見てみましょう。提供されたドキュメントを使って Claude にコードのデバッグを依頼する場合、すべてを混ぜ合わせると混乱が生じます。

「Not Great」版では、何がコードで何がドキュメントなのかを見分けるのがほぼ不可能です。「Better」版では、<my_code> と <docs> タグを使って明確な境界を作っています。

#### カスタムタグ名

公式の XML タグを使う必要はありません。内容に合った説明的な名前を作成してください。

- <sales_records> は <data> より優れています
- <athlete_information> はユーザー詳細を明確に識別します
- <my_code> と <docs> は異なる種類のコンテンツを分離します

タグ名が具体的で説明的であるほど、Claude は各セクションの目的をよりよく理解できます。

#### XML タグを使うタイミング

XML タグは次の場合に最も有用です。

- 大量のコンテキストやデータを含める場合
- 異なる種類のコンテンツ（コード、ドキュメント、データ）を混在させる場合
- コンテンツの境界を特に明確にしたい場合
- 複数の変数を補間する複雑なプロンプトを扱う場合

短いコンテンツでも、XML タグはプロンプト構造を Claude にとってより明白にする区切りとして役立ちます。

#### 実際の応用

実際には、次のようにプロンプトを構造化できます。

```
<athlete_information>

- Height: 6'2"
- Weight: 180 lbs
- Goal: Build muscle
- Dietary restrictions: Vegetarian
</athlete_information>

上記の athlete information に基づいて meal plan を生成してください。
```

これにより、身長、体重、目標、制限がすべて関連する athlete data であり、食事プランを生成するときに一緒に考慮すべきであることが非常に明確になります。

単純なプロンプトでは劇的な改善が見られないかもしれませんが、プロンプトがより複雑になり、多様なコンテンツを大量に含むようになるほど、XML タグの価値は高まります。

---

### レッスン 28: Providing examples

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287746>  

Open in Claude

プロンプトに例を提供することは、使用する prompt engineering 技法の中でも最も効果的なものの1つです。このアプローチは「one-shot」または「multi-shot」 prompting と呼ばれ、Claude の応答を導くためにサンプルの input/output ペアを与えるものです。

#### 例の仕組み

感情分析の例を見てみましょう。Claude に tweet がポジティブかネガティブかを分類させたいとします。

ここでの課題は皮肉です。「Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'」のような tweet は表面的にはポジティブに見えますが、実際には皮肉でネガティブです（Plan 9 は史上最悪の映画の1つとして有名です）。

#### コーナーケースを扱うために例を追加する

これを解決するには、扱いにくいケースを Claude に示す例を追加できます。

改善されたプロンプトには次が含まれます。

- 明確なポジティブ例: "Great game tonight!" → "Positive"
- 皮肉の例: "Oh yeah, I really needed a flight delay tonight! Excellent!" → "Negative"
- 皮肉を慎重に扱うべき理由を説明するコンテキスト

例が <sample_input> や <ideal_output> のような XML タグで囲まれている点に注目してください。この構造により、各部分が何を表しているのかが Claude にとって非常に明確になります。

#### 例を使うタイミング

例は特に次の場合に役立ちます。

- コーナーケースやエッジシナリオを捉える
- 複雑な出力形式（特定の JSON 構造など）を定義する
- 望む正確なスタイルやトーンを示す
- 曖昧な入力をどう扱うかを示す

#### One-Shot と Multi-Shot

One-Shot: パターンを確立するために1つの例を提供する

Multi-Shot: 複数のシナリオをカバーするために複数の例を提供する

さまざまなエッジケースを処理する必要がある場合や、有効な応答の異なるタイプを示したい場合は multi-shot を使います。

#### 評価から良い例を見つける

prompt evaluation を実行するときは、最も高得点だった出力を例として使うことを検討します。

スコア10（または利用可能な最高スコア）を取ったレスポンスを見つけ、その input/output ペアをプロンプト内の例として使います。これにより、Claude は特定のユースケースにおける「完璧な」出力がどのようなものかを理解できます。

#### 例にコンテキストを追加する

input/output ペアだけを提供するのではなく、なぜその出力が良いのかを説明します。

```
<ideal_output>
[Your example output here]
</ideal_output>

この例は構造が優れており、食品の選択と量に関する詳細な情報を提供し、アスリートの目標と制限に合致しています。
```

この追加コンテキストにより、Claude は良いレスポンスの形式だけでなく、その背後にある reasoning も理解できます。

#### ベストプラクティス

- 例を明確に構造化するため、常に XML タグを使う
- 何を示しているのかを明示する: 「Here is an example input with an ideal response」
- 最も一般的な失敗ケースに対応する例を含める
- 例の出力が理想的と見なされる理由を説明する
- 例は特定のタスクに関連したものに保つ

例が特に強力なのは、説明するのではなく見せるからです。望む内容を言葉で正確に説明しようとする代わりに、直接示します。これによりプロンプトの信頼性が大幅に高まり、指示だけでは表現しにくい微妙な要件を Claude が理解しやすくなります。

---

### レッスン 29: Exercise on prompting

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287748>  

Open in Claude

---

### レッスン 30: Quiz on prompt engineering techniques

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289121>  

Open in Claude
Loading...

---

### レッスン 31: Introducing tool use

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287747>  

Open in Claude

Tools により、Claude は外部世界の情報にアクセスでき、学習時に得た知識を超えて能力を拡張できます。デフォルトでは、Claude は学習データに含まれる情報しか知らず、現在の出来事、リアルタイムデータ、外部システムにはアクセスできません。tool use は、Claude が新しい情報を要求して受け取るための構造化された方法を作ることで、この制限を解決します。

#### Tools がない場合の問題

ユーザーが Claude に現在の情報を尋ねると、Claude は壁にぶつかります。たとえば、誰かが「What's the weather in San Francisco, California?」と尋ねた場合、Claude は「I'm sorry, but I don't have access to up-to-date weather information.」のように応答せざるを得ません。

これは、Claude が現在の情報にアクセスできさえすれば理論上は手助けできるリアルタイムデータを人々が必要としている場合に、もどかしいユーザー体験を生みます。

#### Tool Use の仕組み

tool use は、アプリケーションと Claude の間の特定の往復パターンに従います。完全な flow は次のとおりです。

1. 初期リクエスト: 外部ソースから追加データを取得する方法の指示とともに、Claude に質問を送る
2. Tool Request: Claude が質問を分析し、追加情報が必要だと判断して、必要なデータの具体的な詳細を要求する
3. データ取得: サーバーがコードを実行し、外部 API やデータベースから要求された情報を取得する
4. 最終レスポンス: 取得したデータを Claude に返し、Claude が元の質問と新しいデータの両方を使って完全なレスポンスを生成する

#### 実践での天気の例

天気の質問でこれがどのように機能するか見てみましょう。プロセスははるかに具体的になります。

ユーザーが現在の天気について尋ねたら、天気データを取得する方法に関する指示をプロンプトに含めます。Claude は現在の情報が必要だと認識し、特定の場所の天気データを要求します。次にサーバーが weather API を呼び出してリアルタイムの状況を取得し、そのデータを Claude に返します。最後に Claude は、新しい天気データとユーザーの質問を組み合わせ、正確で現在のレスポンスを提供します。

#### 主な利点

- リアルタイム情報: Claude の学習時には利用できなかった現在のデータにアクセスできる
- 外部システム統合: Claude をデータベース、API、その他のサービスに接続できる
- 動的なレスポンス: 利用可能な最新情報に基づいて回答できる
- 構造化されたインタラクション: Claude がどの情報を必要とし、それをどう求めるべきかを正確に把握できる

tool use は、Claude を静的な知識ベースから、ライブデータを扱える動的なアシスタントへ変えます。これにより、天気データ、株価、データベースクエリ、その他ユーザーが必要とするあらゆるリアルタイム情報など、現在の情報を必要とするアプリケーションを構築する可能性が広がります。

---

### レッスン 32: Project overview

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287751>  

Open in Claude

これから、Claude に将来の日付のリマインダーを設定する方法を教える実践的なプロジェクトを構築します。一見単純に聞こえるかもしれませんが、custom tools を使って解決するいくつかの興味深い課題が明らかになります。

目標は単純です。Claude に「Set a reminder for my doctor's appointment. It's a week from Thursday」と伝えると、Claude が「OK, I will remind you.」と応答できるようにしたいのです。しかしこれを機能させるには、Claude の時間とリマインダーの扱いに関するいくつかの制限に対処する必要があります。

#### これが難しい理由

Claude は現在の日付を知っていますが、解決すべき具体的な問題が3つあります。

- 限定的な時間認識: Claude は現在の日付を知っているかもしれませんが、正確な時刻までは知らない可能性があります
- 日付計算の問題: Claude は、特に将来の多くの日数を扱うとき、時間ベースの加算を常にうまく処理できるわけではありません
- リマインダー機能がない: Claude はリマインダーの設定方法を知りません。このための組み込みメカニズムはありません

これらの制限はそれぞれ、Claude が自然にできることと、リマインダーシステムに必要なことの間にあるギャップを表しています。Tools は、これらのギャップを埋める方法です。

#### 必要な Tools

各課題に対応するため、3つの別々の tools を作成します。

- 現在の date time を取得する: Claude は現在の日付と時刻を正確に知る必要があります
- date time に duration を加算する: Claude は date time の加算が完璧ではないため、信頼できる tool を与えます
- リマインダーを設定する: システム内で実際にリマインダーを設定する方法が必要です

これらの tools を、最も単純なものから順に1つずつ実装します。このアプローチにより、より複雑な機能を構築する前に、tool calling がどのように機能するかを理解できます。最終的に Claude は、「remind me in a week」のような自然言語リクエストを、これらの tools を組み合わせて正確な時刻を計算し、リマインダーを設定することで処理できるようになります。

このプロジェクトは、AI を扱う上での重要な原則を示しています。モデルに制限がある場合、プロンプトでその制限を回避しようとするのではなく、tools によって能力を拡張するのです。

---

### レッスン 33: Tool functions

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287756>  

Open in Claude

Claude を使って AI アプリケーションを構築するとき、リアルタイム情報へのアクセスやアクション実行能力を与える必要がよくあります。ここで tool functions が登場します。これは、Claude がユーザーを助けるために追加データを必要としたときに呼び出せる Python functions です。

上の画像は、実装する3つの重要な tools を示しています。現在の date/time の取得、日付への duration の加算、リマインダーの設定です。最初のものから始めましょう。

#### Tool Functions とは何か

tool function は、Claude がユーザーを助けるために追加情報が必要だと判断したときに自動実行される通常の Python function です。たとえば、誰かが「What time is it?」と尋ねたら、Claude は現在時刻を取得するために date/time tool を呼び出します。

以下は weather tool function の例です。入力を検証し、明確なエラーメッセージを提供している点に注目してください。これらは重要なベストプラクティスです。

#### Tool Functions のベストプラクティス

tool functions を書くときは、次のガイドラインに従います。

- 説明的な名前を使う: function name と parameter name の両方が目的を明確に示すべきです
- 入力を検証する: 必須 parameters が空または無効でないことを確認し、そうであればエラーを発生させます
- 意味のあるエラーメッセージを提供する: Claude はエラーメッセージを見ることができ、修正した parameters で function call を再試行する可能性があります

検証は特に重要です。Claude はエラーから学習するからです。「Location cannot be empty」のような明確なエラーを発生させると、Claude は適切な location value で再度 function を呼び出そうとするかもしれません。

#### 最初の Tool Function を作る

現在の日付と時刻を取得する function を作成しましょう。この function は date format parameter を受け取り、Claude が異なる形式で時刻を要求できるようにします。

```python
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
if not date_format:
raise ValueError("date_format cannot be empty")
return datetime.now().strftime(date_format)
```

この function は Python の datetime module を使って現在時刻を取得し、指定された format string に従って整形します。デフォルト形式では year-month-day hour:minute:second が得られます。

異なる形式でテストできます。

```python
# Default format: "2024-01-15 14:30:25"

get_current_datetime()

# Just hour and minute: "14:30"

get_current_datetime("%H:%M")
```

検証チェックにより、Claude が date format に空文字列を渡せないようにします。この特定のエラーが起きる可能性は低いですが、入力を検証し、Claude が学べる役立つエラーメッセージを提供するパターンを示しています。

#### 次のステップ

function の作成は最初のステップにすぎません。次に、Claude に function を説明する JSON schema を書き、それを chat system に統合する必要があります。この tool function アプローチにより、コードを整理し保守しやすく保ちながら、Claude に強力な能力を与えられます。

Downloads
001_tools.ipynb
(opens in new tab)

---

### レッスン 34: Tool schemas

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753>  

Open in Claude

tool function を書いた後の次のステップは、function が期待する arguments とその使い方を Claude に伝える JSON schema を作成することです。この schema は、Claude が tools をいつ、どのように呼び出すかを理解するために読むドキュメントとして機能します。

#### JSON Schema を理解する

JSON Schema は AI や tool calling 固有のものではありません。長年使われている広く普及したデータ検証仕様です。AI コミュニティがこれを採用したのは、function parameters を記述し、データを検証する便利な方法だからです。

完全な tool specification には、主に3つの部分があります。

- name - tool の明確で説明的な名前（"get_weather" など）
- description - tool が何をするか、いつ使うか、何を返すか
- input_schema - function の arguments を記述する実際の JSON schema

#### 効果的な Description を書く

tool description は、Claude が function をいつ使うべきか理解するために非常に重要です。ベストプラクティスは次のとおりです。

- tool が何をするかを3〜4文で説明することを目指す
- Claude がいつ使うべきかを説明する
- どのようなデータを返すかを説明する
- 各 argument について詳細な説明を提供する

#### Schemas を生成する簡単な方法

JSON schemas をゼロから書く代わりに、Claude 自身に生成させることができます。手順は次のとおりです。

1. tool function code をコピーする
2. Claude に行き、tool calling 用の JSON schema を書くよう依頼する
3. tool use に関する Anthropic documentation をコンテキストとして含める
4. Claude に、ベストプラクティスに従った正しい形式の schema を生成させる

プロンプトは次のようなものにします。「Write a valid JSON schema spec for the purposes of tool calling for this function. Follow the best practices listed in the attached documentation.」

#### コードへの Schema 実装

Claude が schema を生成したら、コードファイルにコピーします。従うとよい命名パターンは次のとおりです。

```python
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
if not date_format:
raise ValueError("date_format cannot be empty")
return datetime.now().strftime(date_format)

get_current_datetime_schema = {
"name": "get_current_datetime",
"description": "Returns the current date and time formatted according to the specified format",
"input_schema": {
"type": "object",
"properties": {
"date_format": {
"type": "string",
"description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
"default": "%Y-%m-%d %H:%M:%S"
}
},
"required": []
}
}
```

schemas を整理し、それぞれ対応する functions と照合しやすくするため、function_name に function_name_schema を続けるパターンを使います。

#### 型安全性を追加する

型チェックを改善するには、Anthropic library から ToolParam type を import して使います。

```python
from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
"name": "get_current_datetime",
"description": "Returns the current date and time formatted according to the specified format",

# ... rest of schema

})
```

機能上は厳密には必須ではありませんが、Claude の API で schema を使うときの型エラーを防ぎ、コードをより堅牢にします。

---

### レッスン 35: Handling message blocks

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287757>  

Open in Claude

Claude の tool 機能を扱うとき、これまで見てきた単純なテキストレスポンスとは異なる新しい種類のレスポンス構造に出会います。単一の text block が返るだけではなく、Claude は text と tool usage information の両方を含む multi-block messages を返せるようになります。

#### Tool 対応の API Calls を行う

Claude が tools を使えるようにするには、API call に tools parameter を含める必要があります。リクエストの構造は次のようにします。

```python
messages = []
messages.append({
"role": "user",
"content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
tools=[get_current_datetime_schema],
)
```

tools parameter は、Claude が呼び出せる利用可能な functions を記述する JSON schemas の list を受け取ります。

#### Multi-Block Messages を理解する

Claude が tool を使うと決めたとき、content list に複数の blocks を持つ assistant message を返します。これは、これまで扱ってきた単純な text-only responses からの大きな変化です。

multi-block message には通常、次が含まれます。

- Text Block - Claude が何をしているかを説明する人間が読めるテキスト（例: "I can help you find out the current time. Let me find that information for you"）
- ToolUse Block - どの tool を呼び出し、どの parameters を使うべきかについてのコード向け指示

ToolUse block には次が含まれます。

- tool call を追跡するための ID
- 呼び出す function の名前（"get_current_datetime" など）
- dictionary として整形された input parameters
- type designation "tool_use"

#### Multi-Block Messages で会話履歴を管理する

Claude は会話履歴を保存しないことを覚えておいてください。手動で管理する必要があります。tool responses を扱うときは、すべての blocks を含む content structure 全体を保持しなければなりません。

multi-block assistant message を会話履歴に正しく追加する方法は次のとおりです。

```python
messages.append({
"role": "assistant",
"content": response.content
})
```

これにより、text block と tool use block の両方が保持されます。これは、後続の API calls を行うときに会話コンテキストを維持するために非常に重要です。

#### 完全な Tool Usage Flow

tool usage process は次のパターンに従います。

1. tool schema とともに user message を Claude に送る
2. text block と tool use block を含む assistant message を受け取る
3. tool information を抽出し、実際の function を実行する
4. 完全な会話履歴とともに tool result を Claude に返す
5. Claude から最終レスポンスを受け取る

各ステップでは、Claude が正確なレスポンスを提供するために必要な完全なコンテキストを持てるよう、message structure を慎重に扱う必要があります。

#### Helper Functions の更新

add_user_message() や add_assistant_message() のような helper functions を使っている場合は、multi-block content を処理できるよう更新する必要があります。現在のバージョンは単一の text blocks だけをサポートしている可能性がありますが、これからは tool use blocks を含むより複雑な content structures に対応する必要があります。

この multi-block message handling は、Claude の tool capabilities をシームレスに統合しつつ、適切な会話 flow を維持できる堅牢なアプリケーションを構築するために不可欠です。

---

### レッスン 36: Sending tool results

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287752>  

Open in Claude

Claude が tool call を要求した後、function を実行し、その結果を返す必要があります。これにより、Claude が要求した情報を提供して tool use workflow が完了します。

#### Tool Function を実行する

Claude が tool use block で応答したら、input parameters を抽出して function を呼び出します。tool parameters へのアクセス方法は次のとおりです。

```python
response.content[1].input
```

これにより、Claude が function に渡したい arguments の dictionary が得られます。function は dictionary ではなく keyword arguments を期待しているため、Python の unpacking syntax を使います。

```python
get_current_datetime(**response.content[1].input)
```

#### Tool Result Block

tool function を実行した後、tool result block を使って結果を Claude に返す必要があります。この block は user message の中に入り、tool を実行したときに何が起きたかを Claude に伝えます。

tool result block にはいくつかの重要な properties があります。

- tool_use_id - この ToolResult が対応する ToolUse block の id と一致している必要があります
- content - tool の実行結果を string として serialized したもの
- is_error - エラーが発生した場合は True

#### 複数の Tool Calls を処理する

Claude は1つのレスポンスで複数の tool calls を要求できます。たとえば、ユーザーが「What's 10 + 10 and what's 30 + 30?」と尋ねると、Claude は2つの別々の ToolUse blocks で応答するかもしれません。

各 tool call には一意の ID が付与され、結果を返すときはこれらの ID を一致させる必要があります。これにより、結果が異なる順序で到着したとしても、Claude はどの結果がどの要求に対応するかを把握できます。

#### フォローアップリクエストを構築する

Claude へのフォローアップリクエストには、完全な会話履歴に加えて新しい tool result を含める必要があります。構造は次のとおりです。

```python
messages.append({
"role": "user",
"content": [{
"type": "tool_result",
"tool_use_id": response.content[1].id,
"content": "15:04:22",
"is_error": False
}]
})
```

完全な message history には、これで次が含まれます。

- 元の user message
- tool use block を含む assistant message
- tool result block を含む user message

#### 最終リクエストを行う

フォローアップリクエストを送るとき、Claude に別の tool call を期待していなくても、tool schema を引き続き含める必要があります。Claude は会話履歴内の tool references を理解するために schema を必要とします。

```python
client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
tools=[get_current_datetime_schema]
)
```

Claude はその後、tool results をユーザー向けの自然なレスポンスに組み込んだ最終メッセージで応答します。これで tool use workflow は完了です。custom function を通じて Claude がリアルタイム情報にアクセスできるようにすることに成功しました。

---

### レッスン 37: Multi-turn conversations with tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287750>  

Open in Claude

複数の tools を持つアプリケーションを構築するとき、Claude が1つのユーザー質問に答えるために複数の tools を順番に呼び出す必要があるシナリオを扱う必要があります。たとえば、ユーザーが「What day is 103 days from today?」と尋ねた場合、Claude はまず現在の日付を取得し、それから103日を加算する必要があります。

これにより、Claude が最終回答を提供する前に複数の tool requests を行う multi-turn conversation pattern が生まれます。アプリケーションはこれを自動的に処理する必要があります。

#### Multi-Turn Tool Pattern

Claude が複数の tools を必要とするとき、裏側では次のことが起こります。

1. ユーザーが尋ねる: "What day is 103 days from today?"
2. Claude が get_current_datetime を要求する tool use block で応答する
3. サーバーが function を呼び出し、結果を返す
4. Claude がさらに情報が必要だと気づき、add_duration_to_datetime を要求する
5. サーバーがその function を呼び出し、結果を返す
6. Claude が最終回答を提供するのに十分な情報を得る

#### Conversation Loop を構築する

このパターンを扱うには、Claude が tools の要求をやめるまで続く conversation loop が必要です。

```python
def run_conversation(messages):
while True:
response = chat(messages)

add_assistant_message(messages, response)

# Pseudo code

if response isn't asking for a tool:
break

tool_result_blocks = run_tools(response)
add_user_message(messages, tool_result_blocks)

return messages
```

#### Helper Functions のリファクタリング

conversation loop を実装する前に、複数の message blocks を適切に処理できるよう helper functions を更新する必要があります。

#### Message Handlers の更新

add_user_message と add_assistant_message functions は現在、常に plain text を扱うと仮定しています。full message objects を扱えるよう更新します。

```python
from anthropic.types import Message

def add_user_message(messages, message):
user_message = {
"role": "user",
"content": message.content if isinstance(message, Message) else message
}
messages.append(user_message)
```

これにより、string、blocks の list、または完全な message object のいずれも渡せるようになります。

#### Chat Function の更新

chat function を修正し、tools の list を受け取り、text だけでなく full message を返すようにします。

```python
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature,
"stop_sequences": stop_sequences,
}

if tools:
params["tools"] = tools

if system:
params["system"] = system

message = client.messages.create(**params)
return message
```

#### Messages から Text を抽出する

これで full message objects を返すようになったため、必要なときに text を抽出する helper を作成します。

```python
def text_from_message(message):
return "\n".join(
[block.text for block in message.content if block.type == "text"]
)
```

この function は message 内のすべての text blocks を見つけて結合します。ユーザーに最終レスポンスを表示する必要があるときに便利です。

#### 主な改善点

これらのリファクタリング手順により、堅牢な tool handling の準備が整います。

- 柔軟な message handling - helper functions が異なる message formats を扱えるようになります
- chat での tool support - chat function が tool schemas を受け取り、渡せるようになります
- full message returns - text だけでなく complete message objects を取得し、すべての blocks を保持できます
- text extraction utility - 複雑な messages から readable text を簡単に取得できます

これらの基盤が整えば、複数の tool calls を自動処理する conversation loop を実装する準備ができます。これにより、Claude がユーザー質問に答えるために必要な数だけ tools を使える、シームレスな体験を作れます。

Downloads
001_tools_007.ipynb
(opens in new tab)

---

### レッスン 38: Implementing multiple turns

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287758>  

Open in Claude

tools を使う会話システムを構築するには、Claude が tool usage の要求をやめるまで Claude を呼び続ける loop を実装する必要があります。Claude が tools を要求しなくなったら、ユーザーに返す最終レスポンスの準備ができたという合図です。

#### Tool Requests を検出する

Claude が tool を使いたがっているかどうかを知る鍵は、response message の stop_reason field にあります。Claude が tool を呼び出す必要があると判断すると、この field は "tool_use" に設定されます。これにより、conversation loop を続ける必要があるかをきれいに確認できます。

```python
if response.stop_reason != "tool_use":
break  # Claude is done, no more tools needed
```

#### Conversation Loop

メインの conversation function は単純なパターンに従います。

```python
def run_conversation(messages):
while True:
response = chat(messages, tools=[get_current_datetime_schema])
add_assistant_message(messages, response)
print(text_from_message(response))

if response.stop_reason != "tool_use":
break

tool_results = run_tools(response)
add_user_message(messages, tool_results)

return messages
```

この loop は、Claude が tools を要求せずに最終回答を提供するまで続きます。

#### 複数の Tool Calls を処理する

Claude は1つのレスポンスで複数の tools を要求できます。message content には blocks の list が含まれ、各 tool use block を個別に処理する必要があります。

run_tools function は、tool use blocks をフィルタリングしてそれぞれを処理します。

```python
def run_tools(message):
tool_requests = [
block for block in message.content if block.type == "tool_use"
]
tool_result_blocks = []

for tool_request in tool_requests:

# Process each tool request
```

#### Tool Result Blocks

各 tool use block には、対応する tool result block で応答する必要があります。それらの接続は、ID の一致によって維持されます。

tool result block の構造は次のとおりです。

```python
tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": json.dumps(tool_output),
"is_error": False
}
```

#### エラーハンドリング

堅牢な tool execution には、潜在的なエラーの処理が必要です。tool が失敗した場合でも、Claude に result block を提供する必要があります。

```python
try:
tool_output = run_tool(tool_request.name, tool_request.input)
tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": json.dumps(tool_output),
"is_error": False
}
except Exception as e:
tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": f"Error: {e}",
"is_error": True
}
```

#### スケーラブルな Tool Routing

複数の tools をサポートするには、tool names をその実装にマッピングする routing function を作成します。

```python
def run_tool(tool_name, tool_input):
if tool_name == "get_current_datetime":
return get_current_datetime(**tool_input)
elif tool_name == "another_tool":
return another_tool(**tool_input)

# Add more tools as needed
```

このアプローチにより、core conversation logic を変更せずに新しい tools を簡単に追加できます。

#### 完全な Workflow

完全な multi-turn conversation は次のように機能します。

1. 利用可能な tools とともに user message を Claude に送る
2. Claude が text や tool requests で応答する
3. 要求されたすべての tools を実行し、result blocks を作成する
4. tool results を user message として返す
5. Claude が最終回答を提供するまで繰り返す

これにより、Claude が複雑なユーザーリクエストに完全に答えるため、複数の turns にわたって複数の tools を使えるシームレスな体験が作られます。会話履歴は完全なコンテキストを保持し、Claude が以前の tool results を基に包括的なレスポンスを提供できるようにします。

Downloads
001_tools_008.ipynb
(opens in new tab)

---

### レッスン 39: Using multiple tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287749>  

Open in Claude

core tool-handling infrastructure が整っていれば、Claude 実装に複数の tools を追加するのは簡単です。このチュートリアルでは、シンプルなパターンに従って追加の tools を統合する方法を示します。

#### 追加する Tools

リマインダーシステムには、主に3つの機能が必要です。

- 現在の date time を取得する - Claude は現在の日付と時刻を知る必要があります
- date time に duration を加算する - Claude は date time addition が完璧ではありません
- リマインダーを設定する - リマインダーを設定する方法が必要です

良い知らせは、実装作業の大半はすでに完了していることです。add_duration_to_datetime function と set_reminder function は、それぞれ対応する schemas とともに提供されています。

#### Conversation に Tools を追加する

まず、run_conversation function を更新し、tools list に新しい tool schemas を含めます。

```python
response = chat(messages, tools=[
get_current_datetime_schema,
add_duration_to_datetime_schema,
set_reminder_schema
])
```

これにより、Claude に会話中に使える3つの tools すべてを知らせます。

#### Tool Router の更新

次に、run_tool function を修正して新しい tool calls を処理します。各 new tool に対して elif cases を追加します。

```python
def run_tool(tool_name, tool_input):
if tool_name == "get_current_datetime":
return get_current_datetime(**tool_input)
elif tool_name == "add_duration_to_datetime":
return add_duration_to_datetime(**tool_input)
elif tool_name == "set_reminder":
return set_reminder(**tool_input)
```

パターンは単純です。tool name を確認し、対応する function を提供された input で呼び出し、結果を返します。

#### 複数 Tool Usage のテスト

システムをテストするには、複数の tools を必要とするリクエストを試します。「Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050.」

このリクエストは Claude に次を強制します。

- 日付を計算する（add_duration_to_datetime を使用）
- リマインダーを設定する（set_reminder を使用）

Claude は、まず何をする必要があるかを説明し、それから適切な tool calls を順番に実行することでこれを処理します。会話では、Claude が目標日を June 27, 2050 と計算し、その日付にリマインダーを設定する様子が示されます。

#### Message Flow を理解する

会話履歴を確認すると、完全な message structure が見えます。

- リクエストを含む user message
- text と tool use blocks の両方を含む assistant message
- Tool result messages
- Follow-up assistant messages

これは、Claude が単一の message に複数の blocks を含められることを示しています。説明テキストと tool usage requests を組み合わせられるのです。

#### Tools を追加するためのシンプルなパターン

core tool infrastructure が整っていれば、新しい tools の追加は次のパターンに従います。

1. tool function implementation を作成する
2. tool schema を定義する
3. run_conversation の tools list に schema を追加する
4. run_tool にその tool の case を追加する

このモジュール式アプローチにより、既存コードを再構成せずに AI assistant の capabilities を簡単に拡張できます。各 new tool は、既存の conversation flow と tool-handling logic にシームレスに統合されます。

Downloads
001_tools_009.ipynb
(opens in new tab)

---

### レッスン 40: Fine grained tool calling

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/313160>  

Open in Claude

Claude で tool use と streaming を組み合わせると、AI が tool arguments を生成するにつれてリアルタイム更新を受け取れます。これにより、より応答性の高いユーザー体験が生まれますが、裏側でどのように機能するかについて理解すべき重要な詳細がいくつかあります。

#### 基本的な Tool Streaming

streaming を有効にすると、Claude はリクエストを処理しながらさまざまな種類の events を返します。通常の text generation で使われる ContentBlockDelta のような events にはすでに馴染みがあるでしょう。tool use では、InputJsonEvent という新しい event type も処理する必要があります。

各 InputJsonEvent には、2つの重要な properties が含まれます。

- partial_json - tool arguments の一部を表す JSON の chunk
- snapshot - これまで受け取ったすべての chunks から構築された累積 JSON

streaming pipeline でこれらの events を処理する方法は次のとおりです。

```python
for chunk in stream:
if chunk.type == "input_json":

# Process the partial JSON chunk

print(chunk.partial_json)

# Or use the complete snapshot so far

current_args = chunk.snapshot
```

#### JSON Validation の仕組み

ここが興味深い点です。Anthropic API は、Claude が生成したすべての chunk をすぐに送信するわけではありません。代わりに、chunks をバッファリングし、先に検証します。

API は、完全な top-level key-value pairs が揃うまで何も送信しません。たとえば、tool が次の構造を期待している場合です。

```json
{
"abstract": "This paper presents a novel...",
"meta": {
"word_count": 847,
"review": "This paper introduces QuanNet..."
}
}
```

API は次を行います。

1. abstract value 全体が完了するまで待つ
2. その key-value pair を schema に照らして検証する
3. abstract 用にバッファリングされたすべての chunks を一度に送信する
4. meta object について同じ処理を繰り返す

この検証プロセスにより、streaming が有効でも、遅延の後に text がまとめて流れてくる理由が説明できます。chunks は、完全で有効な top-level key-value pair が準備できるまで保持されているのです。

#### Fine-Grained Tool Calling

より速く、より細かい streaming が必要な場合、たとえばユーザーに即時更新を表示したい場合や、partial results の処理をすばやく開始したい場合は、fine-grained tool calling を有効にできます。

fine-grained tool calling が主に行うことは1つです。API 側の JSON validation を無効にします。つまり、次のようになります。

- Claude が生成するとすぐに chunks を受け取れる
- top-level keys 間のバッファリング遅延がない
- より伝統的な streaming behavior
- 重要: JSON validation が無効になるため、コード側で invalid JSON を処理する必要があります

API call に fine_grained=True を追加して有効にします。

```python
run_conversation(
messages,
tools=[save_article_schema],
fine_grained=True
)
```

fine-grained tool calling を使うと、meta object 全体の完了を待たずに、word_count value を stream のかなり早い段階で受け取れる可能性があります。

#### Invalid JSON の処理

fine-grained tool calling を使う場合、Claude は適切な number ではなく "word_count": undefined のような invalid JSON を生成する可能性があります。アプリケーションはこれらのケースを適切に処理する必要があります。

```python
try:
parsed_args = json.loads(chunk.snapshot)
except json.JSONDecodeError:

# Handle invalid JSON appropriately

print("Received invalid JSON, continuing...")
```

fine-grained tool calling を使わない場合、API の validation がこのエラーを検出し、問題のある values を strings で包む可能性があります。ただし、それが期待する schema と一致しないこともあります。

#### Fine-Grained Tool Calling を使うタイミング

次の場合は fine-grained tool calling の有効化を検討します。

- tool argument generation のリアルタイム進捗をユーザーに表示する必要がある
- partial tool results の処理をできるだけ早く開始したい
- バッファリング遅延がユーザー体験に悪影響を与える
- 堅牢な JSON error handling を実装する準備がある

ほとんどのアプリケーションでは、validation 付きのデフォルト動作で十分です。しかし、追加の応答性が必要な場合、fine-grained tool calling により、Claude が生成できる速度で chunks を取得する制御が得られます。

Downloads
003_tool_streaming.ipynb
(opens in new tab)
003_tool_streaming_completed.ipynb
(opens in new tab)

---
### レッスン 41: テキスト編集ツール

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287760>  

Open in Claude
0 seconds of 8 minutes, 41 secondsVolume 90%

重要な注記: すべてのモデルバージョンに対応するツールのバージョン文字列は、こちらで確認できます: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool

Claude には、ゼロから作成する必要のない組み込みツールが 1 つあります。それがテキスト編集ツールです。このツールにより、Claude は標準的なテキストエディタと同じようにファイルやディレクトリを扱えるようになります。

#### テキスト編集ツールでできること

テキスト編集ツールは、Claude に包括的なファイル操作機能を提供します。

- ファイルまたはディレクトリの内容を表示する
- ファイル内の特定の行範囲を表示する
- ファイル内のテキストを置換する
- 新しいファイルを作成する
- ファイル内の特定の行にテキストを挿入する
- ファイルへの最近の編集を取り消す

これにより Claude の能力は大きく拡張され、最初からソフトウェアエンジニアのように振る舞う力を実質的に得られます。

#### 実装要件を理解する

ここが少し混乱しやすい点です。ツール schema は Claude に組み込まれていますが、実際の実装は依然として提供する必要があります。つまり、Claude はファイル操作を依頼する方法を知っていますが、その操作を実際に実行するコードはあなたが書く必要があります。

他のツールを使う場合は、JSON schema と関数実装の両方を書きます。テキスト編集ツールでは、Claude が schema の知識を提供しますが、ファイル作成、ディレクトリ読み取り、テキスト置換などに関する Claude のリクエストを処理する関数はあなたが書く必要があります。

#### Schema バージョン

主要な schema は Claude に組み込まれていますが、リクエストを行う際には小さな schema スタブを含める必要があります。正確な schema は、使用している Claude モデルによって異なります。

```python
def get_text_edit_schema(model):
if model.startswith("claude-3-7-sonnet"):
return {
"type": "text_editor_20250124",
"name": "str_replace_editor",
}
elif model.startswith("claude-3-5-sonnet"):
return {
"type": "text_editor_20241022",
"name": "str_replace_editor",
}
```

Claude はこの小さな schema を見て、背後で自動的に完全なテキスト編集ツール仕様へ展開します。

#### 実践例

テキスト編集ツールが実際にどのように動くか見てみましょう。Claude にファイルを扱うよう依頼すると、必要に応じてツールを使ってファイルを読み取り、変更し、作成します。

たとえば、Claude に「Open the ./main.py file and summarize its contents」と依頼すると、Claude は次のことを行います。

1. テキスト編集ツールを使ってファイルを表示する
2. 内容を読み取る
3. 要約を提供する

さらに進めて、Claude にファイルの変更を依頼することもできます。たとえば、「Open the ./main.py file and write out a function to calculate pi to the 5th digit. Then create a ./test.py file to test your implementation.」のように依頼します。

Claude は次のことを行います。

1. 既存の main.py ファイルを表示する
2. 円周率計算関数を含む新しい実装で内容を置換する
3. 適切な unit tests を含む新しい test.py ファイルを作成する

#### なぜテキスト編集ツールを使うのか？

現代のコードエディタにはすでに AI アシスタントが組み込まれているのに、なぜこのツールが存在するのか疑問に思うかもしれません。テキスト編集ツールは、次のような場面で価値を発揮します。

- プログラムからファイルを編集する必要があるアプリケーションを構築している
- 高機能なコードエディタにアクセスできない環境で作業している
- Claude 搭載アプリケーションにファイル編集機能を直接統合したい

要するに、テキスト編集ツールを使うと、高機能な AI 搭載コードエディタの機能の多くを自分のアプリケーション内で再現でき、Claude がファイルシステムとどうやり取りするかを細かく制御できます。

Downloads
005_text_editor_tool.ipynb
(opens in new tab)

---

### レッスン 42: Web search ツール

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287755>  

Open in Claude

重要な注記: Web Search ツールを使用する前に、組織で settings console から有効化する必要があります。この設定はこちらで確認できます: https://console.anthropic.com/settings/privacy

Claude には、ユーザーの質問に答えるために最新情報や専門的な情報をインターネットで検索できる組み込みの web search ツールが含まれています。実装を提供する必要がある他のツールとは異なり、Claude が検索プロセス全体を自動的に処理します。あなたが行う必要があるのは、有効化のためのシンプルな schema を提供することだけです。

#### Web Search ツールの設定

web search ツールを使うには、次の必須フィールドを持つ schema オブジェクトを作成します。

```json
web_search_schema = {
"type": "web_search_20250305",
"name": "web_search",
"max_uses": 5
}
```

max_uses フィールドは、Claude が実行できる検索回数を制限します。Claude は初期結果に基づいて追加検索を行う場合があるため、これにより過剰な API 呼び出しを防げます。1 回の検索で複数の結果が返りますが、Claude は追加検索が必要だと判断することがあります。

#### レスポンスの仕組み

Claude が web search ツールを使用すると、レスポンスには複数種類のブロックが含まれます。

- Text blocks - Claude が何をしているかの説明
- ServerToolUseBlock - Claude が使用した正確な検索クエリを示す
- WebSearchToolResultBlock - 検索結果を含む
- WebSearchResultBlock - タイトルと URL を持つ個別の検索結果
- Citation blocks - Claude の記述を裏付けるテキスト

このレスポンス構造により、Claude が何を検索し、どのソースを見つけたかを正確に確認できます。Citations には、Claude が回答の根拠として使用した具体的なテキストと、そのソース URL が含まれます。

#### 検索ドメインを制限する

allowed_domains フィールドを使うと、検索を特定のドメインに制限できます。これは、信頼できる権威あるソースが欲しい場合に特に有用です。

```json
web_search_schema = {
"type": "web_search_20250305",
"name": "web_search",
"max_uses": 5,
"allowed_domains": ["nih.gov"]
}
```

たとえば、医療や運動に関するアドバイスについて尋ねる場合、PubMed (nih.gov) のようなドメインに制限すると、ランダムなブログ記事ではなく、エビデンスに基づく情報を得られます。

#### 検索結果のレンダリング

レスポンス内の異なるブロックタイプは、特定の UI レンダリング向けに設計されています。

- text blocks を通常のコンテンツとしてレンダリングする
- web search results を上部にソース一覧として表示する
- citations を本文中にインライン表示し、ソースドメイン、ページタイトル、URL、引用テキストを含める

この構造は、Claude がどのように回答に到達したかをユーザーが理解する助けになり、使用されているソースについて透明性を提供します。citation 形式により、どの具体的な情報がどのソースから来たのかが明確になり、AI の回答への信頼を高めます。

#### 実践的な使い方

web search ツールが最も効果的なのは次の用途です。

- 時事問題や最近の動向
- Claude の training data に含まれていない専門情報
- ファクトチェックと権威あるソースの発見
- 最新情報を必要とするリサーチタスク

API 呼び出し時に tools array に schema を含めるだけで、Claude はユーザーの質問に答えるために web search が役立つかどうかを自動的に判断します。

Downloads
006_web_search.ipynb
(opens in new tab)
006_web_search_complete.ipynb
(opens in new tab)

---

### レッスン 43: Claude による tool use のクイズ

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289122>  

Open in Claude
Loading...

---

### レッスン 44: Retrieval Augmented Generation の紹介

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287763>  

Open in Claude

Retrieval Augmented Generation (RAG) は、単一の prompt に収まりきらない大きなドキュメントを扱うための手法です。すべてを巨大な prompt に詰め込むのではなく、RAG はドキュメントを chunk に分割し、質問に答える際に最も関連性の高い部分だけを含めます。

#### 大きなドキュメントの問題

800 ページの財務文書があり、Claude に「この会社にはどのようなリスク要因がありますか？」のような具体的な質問をしたいと想像してください。ドキュメント内の関連情報を何らかの方法で Claude に渡す必要がありますが、prompt に含められるテキスト量には制限があります。

#### 選択肢 1: すべてを Prompt に含める

最初のアプローチは単純です。ドキュメントからすべてのテキストを抽出し、ユーザーの質問と一緒に prompt に詰め込みます。prompt は次のようになります。

```
Answer the user's question about the financial document.

<user_question>
{user_question}
</user_question>

<financial_document>
{financial_document}
</financial_document>
```

このアプローチには重大な制限があります。

- prompt 長には厳しい上限があり、ドキュメントが長すぎる可能性がある
- 非常に長い prompt では Claude の有効性が下がる
- 大きな prompt は処理コストが高くなる
- 大きな prompt は処理に時間がかかる

#### 選択肢 2: ドキュメントを Chunk に分割する

RAG はより賢いアプローチを取ります。まず、前処理ステップでドキュメントを小さな chunk に分割します。その後、ユーザーが質問したら、その質問に最も関連する chunk を見つけ、その chunk だけを prompt に含めます。

仕組みはこうです。「この会社はどのようなリスクに直面していますか？」と誰かが尋ねた場合、chunk を検索し、「Risk Factors」セクションを見つけ、その関連 chunk だけを prompt に含めます。

#### RAG の利点

- Claude が最も関連性の高いコンテンツだけに集中できる
- 非常に大きなドキュメントまでスケールできる
- 複数のドキュメントに対応できる
- 小さな prompt はコストが低く、実行も速い

#### RAG の課題

- ドキュメントを chunk 化する前処理ステップが必要
- 「関連する」chunk を見つける検索メカニズムが必要
- 含めた chunk に Claude が必要とするすべての context が含まれていない可能性がある
- テキストを chunk 化する方法は多数あり、どのアプローチが最善か？

たとえば、ドキュメントを同じサイズの部分に分割することも、見出しやセクションなどのドキュメント構造に基づいて chunk を作成することもできます。それぞれのアプローチにはトレードオフがあり、特定のユースケースに合わせて評価する必要があります。

#### RAG を使うべき場合

RAG には多くの技術的判断が伴い、単にすべてを prompt に含めるよりも多くの作業が必要です。特定のアプリケーションにおいて、利点が複雑さを上回るかどうかを分析する必要があります。非常に大きなドキュメント、複数のドキュメントを扱う場合、またはコストとパフォーマンスを最適化する必要がある場合に特に価値があります。

重要な洞察は、RAG がシンプルさと引き換えにスケーラビリティと効率を得るということです。適切に実装するには事前作業が多く必要ですが、単純な prompt stuffing では扱えないドキュメントコレクションを扱えるようになります。

---

### レッスン 45: テキスト chunking 戦略

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287776>  

Open in Claude

Text chunking は、RAG (Retrieval Augmented Generation) pipeline を構築するうえで最も重要なステップの 1 つです。ドキュメントをどのように分割するかは、システム全体の品質に直接影響します。不適切な chunking 戦略では、無関係な context が prompt に挿入され、AI が完全に誤った回答をする原因になります。

次の例を考えてみてください。医療研究とソフトウェアエンジニアリングに関するセクションを持つドキュメントがあるとします。chunking が不適切だと、ユーザーが「今年、エンジニアはいくつの bug を修正しましたか？」と尋ねたときに、ソフトウェアエンジニアリングではなく医療研究に関する情報を得てしまうかもしれません。単に医療セクションに別の文脈で「bug」という単語が含まれていたからです。

だからこそ、適切な chunking 戦略を選ぶことが非常に重要です。主な 3 つのアプローチを見ていきましょう。

#### サイズベースの Chunking

サイズベースの chunking は最も単純なアプローチで、テキストを同じ長さの文字列に分割します。325 文字のドキュメントがある場合、おおよそ 108 文字ずつの 3 つの chunk に分割するかもしれません。

この方法は実装が簡単で、どの種類のドキュメントにも使えますが、明確な欠点があります。

- 単語が文の途中で切れる
- chunk が周辺テキストからの重要な context を失う
- セクション見出しが内容から切り離される可能性がある

これらの問題に対処するため、chunk 間に overlap を追加できます。つまり、各 chunk に隣接 chunk の一部の文字を含めることで、より良い context を提供し、完全な単語や文を確保します。

基本的な実装は次のとおりです。

```python
def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
chunks = []
start_idx = 0

while start_idx < len(text):
end_idx = min(start_idx + chunk_size, len(text))
chunk_text = text[start_idx:end_idx]
chunks.append(chunk_text)

start_idx = (
end_idx - chunk_overlap if end_idx < len(text) else len(text)
)

return chunks
```

#### 構造ベースの Chunking

構造ベースの chunking は、見出し、段落、セクションといったドキュメントの自然な構造に基づいてテキストを分割します。Markdown ファイルのような整形済みドキュメントでは非常に効果的です。

Markdown ドキュメントでは、見出しマーカーで分割できます。

```python
def chunk_by_section(document_text):
pattern = r"\n## "
return re.split(pattern, document_text)
```

このアプローチは、各 chunk が完全なセクションを表すため、最もクリーンで意味のある chunk を得られます。ただし、ドキュメント構造について保証がある場合にしか機能しません。現実世界の多くのドキュメントは、明確な構造マーカーのないプレーンテキストや PDF です。

#### 意味ベースの Chunking

意味ベースの chunking は最も高度なアプローチです。テキストを文に分割し、自然言語処理を使って連続する文同士がどれだけ関連しているかを判断します。関連する文のグループから chunk を構築します。

この方法は計算コストが高いですが、最も関連性の高い chunk を生成します。個々の文の意味を理解する必要があり、他の戦略より実装が複雑です。

#### 文ベースの Chunking

実用的な中間案は、文単位で chunk 化することです。正規表現を使ってテキストを個々の文に分割し、必要に応じて overlap を付けながら chunk にまとめます。

```python
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
sentences = re.split(r"(?<=[.!?])\s+", text)

chunks = []
start_idx = 0

while start_idx < len(sentences):
end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
current_chunk = sentences[start_idx:end_idx]
chunks.append(" ".join(current_chunk))

start_idx += max_sentences_per_chunk - overlap_sentences

if start_idx < 0:
start_idx = 0

return chunks
```

#### 戦略の選び方

選択は完全にユースケースとドキュメントに関する保証に依存します。

- 構造ベース: ドキュメントの形式を制御できる場合に最良の結果が得られる（社内レポートなど）
- 文ベース: ほとんどのテキストドキュメントに対する良い中間案
- サイズベース: コードを含むあらゆるコンテンツタイプで機能する、最も信頼できる fallback

overlap 付きのサイズベース chunking は、シンプルで信頼性があり、あらゆるドキュメントタイプに対応できるため、本番環境でよく選ばれます。完璧な結果は得られないかもしれませんが、pipeline を壊さない妥当な chunk を一貫して生成します。

覚えておいてください。単一の「最良」の chunking 戦略はありません。適切なアプローチは、具体的なドキュメント、ユースケース、そして実装の複雑さと chunk 品質の間でどのトレードオフを受け入れるかによって決まります。

Downloads
001_chunking.ipynb
(opens in new tab)
report.md
(opens in new tab)

---

### レッスン 46: Text embeddings

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287759>  

Open in Claude

ドキュメントを chunk に分割した後、RAG pipeline の次のステップは、ユーザーの質問に最も関連する chunk を見つけることです。これは本質的には検索問題です。すべての text chunks を調べ、ユーザーが尋ねている内容に関連するものを特定する必要があります。

#### Semantic Search

関連する chunk を見つける最も一般的なアプローチは semantic search です。正確な単語一致を探す keyword-based search とは異なり、semantic search は text embeddings を使って、ユーザーの質問と各 text chunk の意味と context を理解します。

#### Text Embeddings

text embedding は、あるテキストに含まれる意味の数値表現です。単語や文を、コンピュータが数学的に扱える形式に変換するものだと考えてください。

プロセスは次のように動きます。

1. テキストを embedding model に入力する
2. モデルが長い数値リスト（embedding）を出力する
3. 各数値は -1 から +1 の範囲になる
4. これらの数値は、入力テキストの異なる性質や特徴を表す

#### 数値を理解する

embedding 内の各数値は、本質的には入力テキストの何らかの性質に対する「score」です。ただし、重要な注意点があります。それぞれの数値が何を表しているのか、私たちには正確には分かりません。

ある数値が「テキストがどれだけ幸せか」や「テキストがどれだけ海について話しているか」を表すと想像すると分かりやすいですが、これらは概念的な例にすぎません。各次元の実際の意味は、training 中にモデルが学習したものであり、人間が直接解釈できるものではありません。

#### Embeddings 用の VoyageAI

Anthropic は現在 embedding 生成を提供していないため、推奨プロバイダーは VoyageAI です。次のことが必要です。

- 別途 VoyageAI アカウントに登録する
- API key を取得する（無料で開始可能）
- key を環境変数に追加する

.env ファイルに次を追加します。

```bash
VOYAGE_API_KEY="your_key_here"
```

#### 実装

まず、VoyageAI ライブラリをインストールします。

```bash
%pip install voyageai
```

次に client をセットアップし、embeddings を生成する関数を作成します。

```python
from dotenv import load_dotenv
import voyageai

load_dotenv()
client = voyageai.Client()

def generate_embedding(text, model="voyage-3-large", input_type="query"):
result = client.embed([text], model=model, input_type=input_type)
return result.embeddings[0]
```

この関数を text chunk に対して実行すると、embedding を表す浮動小数点数のリストが返されます。プロセスは高速で単純です。本当の課題は、RAG pipeline で最も関連性の高いコンテンツを見つけるために、これらの embeddings をどう効果的に使うかを理解することです。

次のステップは、embeddings を比較して、どの chunk がユーザーの質問に最も似ているかを判断する方法を学ぶことです。これは semantic search プロセスの中核を形成します。

Downloads
002_embeddings.ipynb
(opens in new tab)
VoyageAI API Key Directions.pdf
(opens in new tab)

---

### レッスン 47: 完全な RAG flow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287764>  

Open in Claude

ここまで RAG、text chunking、embeddings の基本を扱ってきたので、完全な RAG pipeline をステップごとに見ていきましょう。この例では、これらの要素がどのように連携して関連情報を取得し、レスポンスを生成するかを正確に示します。

#### Step 1: ソーステキストを Chunk 化する

まず、ソースドキュメントを扱いやすい chunk に分割します。この例では、2 つのシンプルなテキストセクションを使います。

- Section 1: Medical Research - "This year saw significant strides in our understanding of XDR-47, a 'bug' we have not seen before."
- Section 2: Software Engineering - "This division dedicated significant effort to studying various infection vectors in our distributed systems"

#### Step 2: Embeddings を生成する

次に、embedding model を使って各 text chunk を数値 embeddings に変換します。理解しやすくするため、常に正確に 2 つの数値を返し、それぞれの数値が何を表すか分かっている完璧な embedding model があると想像しましょう。

私たちの架空のモデルでは次のとおりです。

- 1 つ目の数値は、テキストが医療分野についてどれだけ話しているかを表す
- 2 つ目の数値は、テキストがソフトウェアエンジニアリングについてどれだけ話しているかを表す

医療研究セクションでは、[0.97, 0.34] が得られるかもしれません。これは非常に医療寄りですが、「bug」という単語により一部ソフトウェア要素も含みます。ソフトウェアエンジニアリングセクションでは、[0.30, 0.97] が得られます。これは大きくソフトウェア寄りですが、「infection vectors」によって医療的な含みもあります。

#### Normalization

embedding API は通常、各ベクトルの大きさを 1.0 にスケールする normalization ステップを実行します。ここで数学を心配する必要はありません。自動的に処理されます。これにより、[0.944, 0.331] や [0.295, 0.955] のような正規化ベクトルが得られます。

これらの embeddings は単位円上に可視化できます。各点は text chunk の 1 つを表します。

#### Step 3: Vector Database に保存する

これらの embeddings を vector database に保存します。これは、embeddings のような長い数値リストを保存、比較、検索するために最適化された特殊なデータベースです。

この時点で一旦止まります。ここまでの作業はすべて、事前に行われる preprocessing です。次に、ユーザーが query を送信するのを待ちます。

#### Step 4: ユーザー Query を処理する

ユーザーが「I'm curious about the company. In particular, what did the software engineering dept do this year?」のような質問をしたら、その query を同じ embedding model に通します。

この query は [0.1, 0.89] のように embedding されます。医療 score は低く、ソフトウェアエンジニアリング score は高い値です。normalization 後は [0.112, 0.993] になります。

#### Step 5: 類似 Embeddings を見つける

ユーザーの query embedding を vector database に送り、保存済み embeddings の中から最も類似したものを見つけるよう依頼します。

データベースは、ユーザーの質問内容に最も近い一致であるソフトウェアエンジニアリングセクションを返します。

#### Similarity の仕組み: Cosine Similarity

vector database は cosine similarity を使って、どの embeddings が最も似ているかを判断します。これは 2 つのベクトル間の角度の cosine を測定します。

cosine similarity に関する重要点:

- 結果は -1 から 1 の範囲になる
- 1 に近い値は高い類似性を意味する
- -1 に近い値は非常に異なることを意味する
- 0 は直交（関係なし）を意味する

この例では、ユーザー query とソフトウェアエンジニアリング chunk の cosine similarity は 0.983 で、非常に高い類似性です。医療研究 chunk との類似性は 0.398 にすぎず、かなり低い値です。

#### Cosine Distance

vector database のドキュメントでは、「cosine distance」をよく目にします。これは単純に (1 - cosine similarity) として計算されます。cosine distance では次のようになります。

- 0 に近い値は高い類似性を意味する
- 大きい値は類似性が低いことを意味する

この調整により、多くの文脈で数値を解釈しやすくなります。

#### Step 6: 最終 Prompt を作成する

最後に、ユーザーの質問と見つけた最も関連性の高い text chunk を組み合わせて prompt を作成し、Claude に送信してレスポンスを得ます。

prompt は次のようになります。

```
Answer the user's question about the financial document.

<user_question>
How many bugs did engineers fix this year?
</user_question>

<report>
## Section 2: Software Engineering
This division dedicated significant effort to studying various infection vectors in our distributed systems
</report>
```

これが完全な RAG pipeline です。システムは semantic similarity に基づいて最も関連性の高い情報を正常に取得し、正確なレスポンスを生成するための context として提供しました。

---

### レッスン 48: RAG flow の実装

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287761>  

Open in Claude

RAG flow を概念的に理解したので、ステップごとに実装してみましょう。テキストを chunk 化し、embeddings を生成し、vector database に保存し、similarity search を実行する方法を示す完全な例を見ていきます。

#### 5 ステップの RAG 実装

実装は、前に説明した同じ 5 つのステップに従います。

1. テキストをセクションごとに chunk 化する
2. 各 chunk の embeddings を生成する
3. vector store を作成し、各 embedding を追加する
4. ユーザーの質問の embedding を生成する
5. store を検索して最も関連性の高い chunk を見つける

この図は、ユーザー query を embeddings に変換し、vector database を検索して最も関連性の高いコンテンツを見つける方法を示しています。

#### Step 1: テキストの Chunking

まず、ドキュメントを読み込み、扱いやすいセクションに分割します。

```python
with open("./report.md", "r") as f:
text = f.read()

chunks = chunk_by_section(text)
chunks[2]  # Test to see the table of contents
```

以前と同じ chunk_by_section 関数を使って、ドキュメントを論理的なセクションに分割します。

#### Step 2: Embeddings を生成する

次に、すべての chunk の embeddings を一度に作成します。

```python
embeddings = generate_embedding(chunks)
```

embedding 関数は、単一の文字列と文字列リストの両方を扱えるよう更新されており、batch processing でより効率的になっています。

#### Step 3: Vector Database に保存する

次に vector store を作成し、embeddings と関連するテキストを追加します。

```python
store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
store.add_vector(embedding, {"content": chunk})
```

embedding と元のテキスト content の両方を保存している点に注目してください。後で検索するときに、数値の embedding 値だけでなく実際のテキストを返す必要があるため、これは極めて重要です。

#### 元のテキストを保存する理由

vector database に query したとき、embedding の数値だけが返ってきても役に立ちません。その embeddings を生成するために使われた実際のテキストが必要です。だからこそ、各 embedding と一緒に元の chunk テキスト（または少なくともそれへの参照）をデータベースに含めます。

#### Step 4: ユーザー Query を処理する

ユーザーが質問したら、その query の embedding を生成します。

```python
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

#### Step 5: 関連コンテンツを見つける

最後に、vector store を検索して最も類似した chunk を見つけます。

```python
results = store.search(user_embedding, 2)

for doc, distance in results:
print(distance, "\n", doc["content"][0:200], "\n")
```

この検索は、2 つの最も関連性の高い chunk と、それぞれの similarity scores（cosine distances）を返します。

検索結果は、ユーザーの質問に最も関連するドキュメントのセクションと similarity scores を示します。

#### 結果を理解する

ソフトウェアエンジニアリング部門に関する例の query を実行すると、次が返ります。

- Section 2: Software Engineering、distance は 0.71（最も近い一致）
- Methodology セクション、distance は 0.72（2 番目に近い）

distance 値が低いほど類似性が高いことを示すため、Section 2 が query に最も関連しています。

#### 次は何か？

この実装は基本的なケースではうまく機能しますが、期待どおりに動かないシナリオもあります。次のセクションでは、RAG システムをより堅牢で正確にするための改善点を探ります。

重要なポイントは、RAG が根本的にはテキストを数値（embeddings）に変換し、それらの数値を効率的に保存し、ユーザーが質問したときに数学的な類似性を使って関連コンテンツを見つけることだという点です。

Downloads
003_vectordb.ipynb
(opens in new tab)

---

### レッスン 49: BM25 lexical search

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287767>  

Open in Claude

RAG pipelines を構築していると、semantic search だけでは常に最良の結果が返るわけではないことにすぐ気づきます。semantic search が見落とす可能性のある正確な用語一致が必要になる場合があります。解決策は、BM25 と呼ばれる手法を使って semantic search と lexical search を組み合わせることです。

#### Semantic Search だけの問題

たとえば、ドキュメント内で "INC-2023-Q4-011" のような特定の incident ID を検索しているとします。semantic search は context や意味を理解することに優れていますが、探している正確な用語を実際には含んでいない、意味的に関連するセクションを返すことがあります。

上の例では、semantic search は incident ID を含む cybersecurity セクションを返しましたが、その incident にはまったく言及していない financial analysis セクションも返しました。これは、semantic search が正確な用語一致ではなく概念的な類似性に注目するために起こります。

#### Hybrid Search 戦略

解決策は、semantic search と lexical search の両方を並行して実行し、その結果を merge することです。これにより両方の長所を得られます。

- Semantic search は embeddings を使って概念的に関連するコンテンツを見つける
- Lexical search は古典的なテキスト検索を使って正確な用語一致を見つける
- Merged results は両方のアプローチを組み合わせて精度を高める

#### BM25 の仕組み

BM25 (Best Match 25) は、RAG systems における lexical search の一般的なアルゴリズムです。検索 query を次のように処理します。

1. **Step 1: query を token 化する**
ユーザーの質問を個々の term に分解します。たとえば、"a INC-2023-Q4-011" は ["a", "INC-2023-Q4-011"] になります。

2. **Step 2: term frequency を数える**
各 term がすべてのドキュメント全体でどれだけ頻繁に現れるかを確認します。"a" のような一般的な単語は 5 回現れるかもしれませんが、"INC-2023-Q4-011" のような特定の term は 1 回しか現れないかもしれません。

3. **Step 3: 重要度で term に重み付けする**
出現頻度の低い term ほど高い重要度 score を得ます。"a" は一般的なので重要度が低く、"INC-2023-Q4-011" は珍しいので重要度が高くなります。

4. **Step 4: 最良の一致を見つける**
重みの高い term をより多く含むドキュメントを返します。

#### BM25 Search の実装

基本的な BM25 search システムの設定方法は次のとおりです。

```python
# 1. Chunk your text by sections

chunks = chunk_by_section(text)

# 2. Create a BM25 store and add documents

store = BM25Index()
for chunk in chunks:
store.add_document({"content": chunk})

# 3. Search the store

results = store.search("What happened with INC-2023-Q4-011?", 3)

# Print results

for doc, distance in results:
print(distance, "\n", doc["content"][:200], "\n----\n")
```

この検索を実行すると、semantic search 単体よりもはるかに良い結果が得られます。BM25 アルゴリズムは、特に incident IDs のような珍しい term について、具体的な検索 term を実際に含むセクションを優先します。

結果が、Software Engineering セクションと Cybersecurity セクションを適切に優先している点に注目してください。どちらも、検索している incident ID を実際に含んでいます。

#### なぜこれがより良く機能するのか

BM25 は正確な一致の発見に優れています。理由は次のとおりです。

- 珍しい具体的な term に高い重みを与える
- 検索価値を加えない一般的な単語を無視する
- 意味ではなく term frequency に注目する
- 技術用語、ID、特定の phrase に特に適している

重要な洞察は、2 つの検索方法には相補的な強みがあるということです。semantic search は context と意味を理解し、lexical search は正確な term 一致を見逃さないようにします。組み合わせることで、概念的な query と具体的な lookup の両方を効果的に扱う、より堅牢な検索システムを作成できます。

次のステップでは、両方の検索システムからの結果を merge して、統一された hybrid search 体験を作る方法を学びます。

Downloads
004_bm25.ipynb
(opens in new tab)

---

### レッスン 50: Multi-Index RAG pipeline

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287766>  

Open in Claude

semantic search（vector embeddings を使用）と lexical search（BM25 を使用）の個別実装を構築しました。次は、それらを統合された検索 pipeline に組み合わせ、両方のアプローチの強みを活用します。

Multi-Index アーキテクチャ

VectorIndex クラスと BM25Index クラスは、どちらもほぼ同一の API を共有しています。どちらにも add_document() と search() methods があります。この一貫性により、それらを Retriever という新しいクラスでまとめることが簡単になります。

Retriever は、ユーザー query を両方の indexes に転送し、結果を収集し、reciprocal rank fusion という手法を使って merge する調整役として機能します。

#### Reciprocal Rank Fusion を理解する

異なる検索方法からの結果を merge することは、単にリストを連結するほど単純ではありません。各方法は異なる scoring systems を使うため、rankings を公平に正規化して組み合わせる方法が必要です。

reciprocal rank fusion がどのように機能するか、例で見てみましょう。"INC-2023-Q4-011" に関する情報を検索し、次の結果が得られたとします。

- VectorIndex returns: Section 2 (rank 1), Section 7 (rank 2), Section 6 (rank 3)
- BM25Index returns: Section 6 (rank 1), Section 2 (rank 2), Section 7 (rank 3)

これらを単一の表にまとめ、各 text chunk の両 indexes における rank を示してから、RRF formula を適用します。

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

ここで k は定数（多くの場合 60 ですが、ここでは結果を分かりやすくするため 1 を使います）、rank_i(d) は i 番目の ranking における document d の rank です。

この例では次のようになります。

- Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
- Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
- Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

最終 ranking は Section 2 (0.833), Section 6 (0.75), Section 7 (0.583) になります。これは直感的にも妥当です。Section 2 は両方の indexes で良い成績だったため、最上位に上がります。

#### 実装の詳細

Retriever クラスは複数の search indexes をラップし、統一された interface を提供します。

```python
class Retriever:
def **init**(self, *indexes: SearchIndex):
if len(indexes) == 0:
raise ValueError("At least one index must be provided")
self._indexes = list(indexes)

def add_document(self, document: Dict[str, Any]):
for index in self._indexes:
index.add_document(document)

def search(self, query_text: str, k: int = 1, k_rrf: int = 60):

# Get results from all indexes

all_results = []
for idx, results in enumerate(all_results):
for rank, (doc, _) in enumerate(results):

# Track document ranks across indexes

# Apply RRF scoring formula

# Return merged and sorted results
```

重要な洞察は、異なる検索実装間で一貫した API を維持することで、密結合なしに簡単に組み合わせられるという点です。

#### Hybrid アプローチのテスト

以前の問題を覚えていますか？"what happened with INC-2023-Q4-011?" を検索したとき、vector-only アプローチでは予期しない結果が返りました。cybersecurity incident（Section 10）が最初に来ましたが、より関連性の高い software engineering セクションではなく financial analysis（Section 3）が 2 番目に来ました。

hybrid retriever を使うと、はるかに良い結果が得られます。

- Section 10: Cybersecurity Analysis - Incident Response Report（最も関連性が高い）
- Section 2: Software Engineering - Project Phoenix Stability Enhancements（2 番目に関連性が高い）
- Section 5: Legal Developments（3 番目）

これは、semantic search と lexical search を組み合わせることで、どちらか一方だけを使った場合の制限を克服できることを示しています。

#### 拡張性

このアーキテクチャの美しさは拡張性にあります。すべての indexes が add_document() と search() methods を持つ同じ SearchIndex protocol を実装しているため、新しい検索方法を簡単に追加できます。

keyword-based index を追加したいですか？graph-based search は？専門ドメイン向け index は？同じ interface を実装するだけで、Retriever が自動的に fusion プロセスに組み込みます。

この modular アプローチにより、各検索実装を focused かつ testable に保ちながら、最終システムでそれらの強みを組み合わせるクリーンな方法を提供できます。

Downloads
005_hybrid.ipynb
(opens in new tab)

---

### レッスン 51: Extended thinking

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287773>  

Open in Claude

重要な注記: Extended Thinking は、特に message pre-filling や temperature など、一部の機能と互換性がありません。制限の完全な一覧はこちらを参照してください: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#feature-compatibility

Extended thinking は、最終レスポンスを生成する前に、Claude が複雑な問題をじっくり考え抜く時間を与える高度な reasoning 機能です。Claude の「scratch paper」のようなものだと考えてください。答えに至る reasoning プロセスを見ることができ、透明性が高まり、多くの場合より高品質なレスポンスにつながります。

#### Extended Thinking の仕組み

extended thinking を有効にすると、Claude のレスポンスは単純な text block から、2 つの部分を含む構造化レスポンスに変わります。

thinking を有効にすると、reasoning プロセスと最終回答の両方を取得できます。

主な利点は次のとおりです。

- 複雑なタスクに対する reasoning capabilities の向上
- 難しい問題での accuracy 向上
- Claude の thought process に対する透明性

ただし、重要なトレードオフがあります。

- コストが高くなる（thinking tokens に料金がかかる）
- latency が増える（thinking には時間がかかる）
- コード内での response handling がより複雑になる

#### Extended Thinking を使うべき場合

判断は明快です。prompt evaluations を使ってください。まず thinking なしで prompts を実行し、すでに prompt を最適化した後でも accuracy が要件を満たさない場合に、extended thinking の有効化を検討します。これは、標準的な prompting ではあと一歩届かないときのためのツールです。

#### Response Structure と Security

Extended thinking のレスポンスには、security のための特別な signature system が含まれます。

signature は、thinking text が改変されていないことを保証する cryptographic token です。これにより、開発者が Claude の reasoning process を改ざんすることを防ぎます。改ざんは、潜在的にモデルを安全でない方向に導く可能性があります。

#### Redacted Thinking

読み取り可能な reasoning text の代わりに、redacted thinking block を受け取ることがあります。

これは、Claude の thinking process が内部 safety systems によって flagged された場合に起こります。redacted content には実際の thinking が encrypted form で含まれており、今後の会話で context を失うことなく完全な message を Claude に返すことができます。

#### 実装

コードで extended thinking を有効にするには、chat 関数に 2 つのパラメータを追加する必要があります。

```python
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024
):
```

thinking budget は、Claude が reasoning に使用できる最大 tokens を設定します。最小値は 1024 tokens で、max_tokens parameter は thinking budget より大きくなければなりません。

API parameters に thinking configuration を追加します。

```python
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget": thinking_budget
    }
```

次に、thinking を有効にして呼び出します。

```python
chat(messages, thinking=True)
```

#### Redacted Responses のテスト

テスト目的では、特別な trigger string を送信することで、Claude に redacted thinking block を返すよう強制できます。これにより、アプリケーションが redacted responses を crash せずに適切に処理できることを確認できます。

Extended thinking は、Claude に複雑な reasoning tasks に取り組ませる必要がある場合に強力な機能ですが、コストと latency の影響を考慮して慎重に使ってください。標準的な prompting から始め、十分に最適化し、それでも追加の reasoning capability が必要な場合に thinking を追加します。

Downloads
001_thinking_complete.ipynb
(opens in new tab)
001_thinking.ipynb
(opens in new tab)

---

### レッスン 52: Image support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287778>  

Open in Claude

Claude の vision capabilities により、messages に画像を含めて、Claude に無数の方法で分析させることができます。画像の内容説明、複数画像の比較、物体の数え上げ、複雑な visual analysis tasks の実行などを依頼できます。

#### Image Handling の基本

画像を扱う際には、覚えておくべき重要な制限がいくつかあります。

- 単一リクエスト内のすべての messages で最大 100 images
- 1 画像あたり最大 5MB
- 1 枚の画像を送信する場合: 最大 height/width は 8000px
- 複数画像を送信する場合: 最大 height/width は 2000px
- 画像は base64 encoding または画像への URL として含められる
- 各画像は寸法に基づいて tokens として数えられる: tokens = (width px × height px) / 750

Claude に画像を送るには、user message の中に text blocks と並べて image block を含めます。構造は次のとおりです。

```python
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])
```

#### Message Flow

会話は text-only interactions と同じように機能します。サーバーは image blocks と text blocks の両方を含む user message を Claude に送り、Claude は分析を含む text block で応答します。

#### Prompting Techniques

画像で良い結果を得る鍵は、テキストで使うのと同じ prompting engineering techniques を適用することです。単純な prompts は不十分な結果につながることがよくあります。たとえば、「How many marbles are in this image?」と尋ねると、誤った数が返るかもしれません。

Claude の accuracy は、次の方法で大きく改善できます。

- 詳細なガイドラインと分析手順を提供する
- one-shot または multi-shot examples を使う
- 複雑なタスクを小さなステップに分解する

#### Step-by-Step Analysis

単純な質問ではなく、Claude に method を提供します。

```
Analyze this image of marbles and determine the exact count using this methodology:

1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```

#### One-Shot Examples

message 内に examples を提供することでも accuracy を改善できます。既知の数を持つ画像を含め、正しい答えを示したうえで、対象画像について尋ねます。これにより、Claude は求められている分析タイプの reference point を得られます。

#### 実世界の例: 火災リスク評価

実践的な応用例として、住宅保険の火災リスク評価の自動化があります。すべての物件に inspector を送る代わりに、保険会社は satellite imagery と Claude の分析を利用できます。

システムは satellite images を分析して次を特定します。

- 住宅の近くに密集した close-packed trees があるか
- 緊急サービスの access routes が困難か
- 住宅に覆いかぶさる branches があるか

「provide a fire risk score」のような単純な prompt ではなく、よく構造化された prompt は分析を具体的なステップに分解します。

```
Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:

- The largest roofed structure
- Typical residential features (driveway connection, regular geometry)
- Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:

- Identify any trees whose canopy extends directly over any portion of the roof
- Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
- Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:

- Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
- Proximity to chimneys, vents, or other roof openings if visible
- Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:

- Identify if trees connect to form a continuous canopy over or near the home
- Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:

- Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around the home
- Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
- Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple vulnerability points
- Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item
```

---

### レッスン 53: PDF support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287768>  

Open in Claude

Claude は PDF ファイルを直接読み取り、分析できます。そのため document processing の強力なツールになります。この機能は image processing と似ていますが、コードの構造にいくつか重要な違いがあります。

#### PDF Processing の設定

Claude で PDF ファイルを処理するには、画像で使うコードとほぼ同じコードを使用します。主な違いは、ファイルタイプの指定と、分かりやすさのための変数名です。

既存の image processing コードを PDF 用に変更する方法は次のとおりです。

```python
with open("earth.pdf", "rb") as f:
    file_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

messages = []

add_user_message(
    messages,
    [
        {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": file_bytes,
            },
        },
        {"type": "text", "text": "Summarize the document in one sentence"},
    ],
)

chat(messages)
```

#### Image Processing からの主な変更点

image processing コードを PDF に適用する際は、いくつかの要素を更新する必要があります。

- ファイル拡張子を .png から .pdf に変更する
- 分かりやすさのため、変数名を image_bytes から file_bytes に更新する
- type を "image" ではなく "document" に設定する
- media type を "image/png" ではなく "application/pdf" に変更する

#### Claude が PDF から抽出できるもの

Claude の PDF processing capabilities は、単純なテキスト抽出を超えています。次を分析し、理解できます。

- ドキュメント全体の text content
- PDF に埋め込まれた images と charts
- tables とその data relationships
- document structure と formatting

これにより Claude は、summaries、data analysis、specific content extraction のいずれが必要な場合でも、PDF documents からあらゆる種類の情報を抽出する one-stop solution のように機能します。

上の例では、PDF として保存された Earth に関する Wikipedia 記事を Claude が正常に処理しており、複雑な document content を 1 文で理解し要約できることを示しています。

Downloads
earth.pdf
(opens in new tab)

---

### レッスン 54: Citations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287771>  

Open in Claude

あなたが提供したドキュメントに基づいて Claude が質問に答えるとき、ユーザーはそれが単に training data から引き出されていると思うかもしれません。しかし、Claude が具体的な情報をどこで見つけたかを正確に示せるとしたらどうでしょうか？そこで citations が登場します。これは Claude が source documents の特定部分を参照し、各情報がどこから来たのかをユーザーに正確に示せる強力な機能です。

#### Citations が重要な理由

Claude に地球の大気がどのように形成されたかを尋ね、詳細な回答を得る場面を想像してください。citations がなければ、ユーザーは情報を検証する方法も、Claude が実際にはあなたが提供した特定のドキュメントを参照していることを理解する方法もありません。citations は、Claude のレスポンスから source material へ戻る明確な trail を作ることで、この透明性の問題を解決します。

#### Citations を有効にする

citations を有効にするには、document message structure を変更する必要があります。document block に 2 つの新しい fields を追加します。

```json
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": file_bytes,
    },
    "title": "earth.pdf",
    "citations": { "enabled": True }
}
```

title field はドキュメントに読みやすい名前を付け、citations: {"enabled": True} は Claude に情報を見つけた場所を追跡するよう指示します。

#### Citation Structure を理解する

citations が有効になると、Claude のレスポンスはより複雑になります。単純なテキストではなく、各 claim の citation information を含む structured data が返ります。

各 citation には、いくつかの重要な情報が含まれます。

- cited_text - Claude の記述を裏付ける、ドキュメント内の正確なテキスト
- document_index - Claude が参照しているドキュメント（複数ドキュメントを提供する場合に有用）
- document_title - あなたがドキュメントに割り当てた title
- start_page_number - cited text が始まる位置
- end_page_number - cited text が終わる位置

#### Citations を使った User Interfaces の構築

citations の本当の力は、この情報にアクセスしやすくする user interfaces を構築することで発揮されます。ユーザーが citation markers に hover すると、情報がどこから来たかを正確に確認できる interactive elements を作成できます。

これにより、ユーザーは次のことができる透明な体験を得られます。

- Claude の回答が実際の source material に根拠づけられていることを確認する
- 元のドキュメントを確認して情報を検証する
- 引用された各情報の周辺 context を理解する

#### Plain Text での Citations

citations は PDF documents に限定されません。plain text sources でも使用できます。テキストを扱う場合は、document structure を次のように変更します。

```json
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": article_text,
    },
    "title": "earth_article",
    "citations": { "enabled": True }
}
```

plain text sources では、page numbers の代わりに character positions が返り、Claude が各情報をテキスト内のどこで見つけたかを正確に示します。

#### Citations を使うべき場合

citations は特に次の場合に価値があります。

- ユーザーが情報の正確性を検証する必要がある
- ユーザーが参照できるべき権威あるドキュメントを扱っている
- 情報ソースについての透明性がアプリケーションにとって重要である
- ユーザーが特定の事実の broader context を探りたい可能性がある

citations を実装することで、Claude は回答を提供する「black box」から、自分の work を示す透明な research assistant へと変わります。これによりユーザーの信頼が高まり、必要に応じて source materials をさらに深掘りできるようになります。

Downloads
002_citations_complete.ipynb
(opens in new tab)
earth.pdf
(opens in new tab)

---

### レッスン 55: Prompt caching

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287772>  

Open in Claude

Prompt caching は、以前のリクエストの計算作業を再利用することで、Claude のレスポンスを高速化し、text generation のコストを削減する機能です。各リクエスト後にすべての処理作業を捨てるのではなく、Claude は似た content が再度送られてきたときに、それを保存して再利用できます。

#### Claude が通常リクエストを処理する方法

prompt caching を理解するために、まず caching が有効でない通常のリクエストで何が起こるかを見てみましょう。

Claude に message を送信すると、Claude はすぐにレスポンス生成を始めるわけではありません。代わりに、入力に対して膨大な preprocessing work を行います。

1. prompt を小さな pieces に tokenize する
2. 各 token の embeddings を作成する
3. 周辺テキストに基づいて context を追加する
4. その後でようやく実際の output text を生成する

レスポンスを送信した後、Claude はこの computational work をすべて捨てます。tokenization、embeddings、context analysis はすべて破棄されます。

#### 作業を破棄することの問題

これは、同じ content を含む follow-up requests を行う場合に非効率になります。たとえば、同じ長いテキストの summary を refinement するよう Claude に依頼している会話では次のようになります。

Claude は、つい先ほど分析した content に対して、同じ preprocessing work を繰り返さなければなりません。Claude は心の中でこう思うかもしれません。「I just processed that message and threw away all the work I did - I could have reused it!」

#### Prompt Caching がこれをどう解決するか

Prompt caching は、preprocessing work を破棄する代わりに保存することで、この workflow を変えます。

初回リクエスト時、Claude は通常どおりすべての preprocessing を実行しますが、その結果を捨てずに cache に保存します。cache は、「この message を再び見たら、すでに行ったこの work を再利用する」という lookup table のように機能します。

#### 主な利点と制限

Prompt caching にはいくつかの利点があります。

- より速いレスポンス: cached content を使うリクエストはより速く実行される
- 低コスト: リクエストの cached 部分について支払いが少なくなる
- 自動最適化: 初回リクエストは cache に書き込み、follow-up requests はそこから読み取る

ただし、覚えておくべき重要な制限もあります。

- Cache duration: cached content は 1 時間しか保持されない
- Limited use cases: 同じ content を繰り返し送信する場合にのみ有益
- High frequency requirement: 同じ content がリクエスト内に非常に頻繁に現れる場合に最も効果的

Prompt caching は、同じ大きなドキュメントについて複数の質問をする document analysis workflows や、base content は一定のまま特定の側面を refine する iterative editing tasks のようなシナリオで最も効果的です。

---

### レッスン 56: Prompt caching のルール

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287770>  

Open in Claude

Claude の prompt caching は、messages に対して行われた computational work を保存し、follow-up requests で再利用できるようにすることで機能します。これにより後続リクエストはより速く、より安く実行できますが、同一の content を繰り返し送信している場合に限られます。

プロセスは単純です。初回リクエストで processing work を cache に書き込み、follow-up requests は同じ content を再処理する代わりにその cache から読み取ることができます。cache は 1 時間保持されるため、この機能は、その時間枠内で同じ content を繰り返し送信する場合にのみ有用です。

#### Cache Breakpoints

caching は自動的には有効になりません。messages 内の特定の blocks に cache breakpoints を手動で追加する必要があります。仕組みは次のとおりです。

- messages に対して行われた work は自動的には cache されない
- block に 'cache breakpoint' を手動で追加する必要がある
- breakpoint より前のすべてに対して行われた work が cache される
- follow-up requests で cache が使われるのは、breakpoint まで（breakpoint を含む）の content が同一の場合のみ

cache breakpoint を追加するには、テキスト blocks を書く際に shorthand 形式ではなく longhand 形式を使う必要があります。

shorthand 形式には cache control field を追加する場所がないため、cache_control field を {"type": "ephemeral"} に設定した expanded format を使う必要があります。

#### Cache Breakpoints の仕組み

message に cache breakpoint を配置すると、Claude はその breakpoint まで（breakpoint を含む）のすべての processing work を cache します。breakpoint より後の content は通常どおり caching なしで処理されます。

follow-up requests で cache を有効に使うには、breakpoint までの content が同一でなければなりません。"please" という単語を追加するような小さな変更でさえ cache を無効化し、Claude にすべてを再処理させます。

#### Cross-Message Caching

Cache breakpoints は複数の messages や message types をまたぐことができます。後の message に breakpoint を置くと、それ以前のすべての messages（user、assistant など）が cached content に含まれます。

これは、会話の context 全体をある時点まで cache したい場合に特に便利です。

#### System Prompts と Tools

text blocks に限定されるわけではありません。cache breakpoints は次にも追加できます。

- System prompts
- Tool definitions
- Image blocks
- Tool use and tool result blocks

System prompts と tool definitions は、リクエスト間でほとんど変わらないため、caching の優れた候補です。多くの場合、prompt caching の恩恵を最も得られるのはここです。

#### Cache Ordering

背後では、Claude はリクエスト components を特定の順序で処理します。tools が最初、次に system prompt、最後に messages です。この順序を理解すると、breakpoints を効果的に配置できます。

合計で最大 4 つの cache breakpoints を追加できます。たとえば、tools を cache し、その後 conversation history の途中に別の breakpoint を追加できます。これにより、リクエストの異なる部分が変化したときに、何を cache するか柔軟に制御できます。

#### Minimum Content Length

caching には最小しきい値があります。cache されるには content が少なくとも 1024 tokens である必要があります。これは、cache しようとしているすべての messages と blocks の合計であり、個々の block の長さではありません。

単純な "Hi there!" message はこのしきい値に達しませんが、その content を 500 回複製する（または本当に長い prompt を持つ）場合、1024 tokens を超えて caching の対象になります。

効果的な prompt caching の鍵は、リクエストのどの部分が複数回の calls で一貫しているかを特定し、再利用を最大化しつつ cache invalidation を最小化するよう breakpoints を戦略的に配置することです。

---

### レッスン 57: Prompt caching の実践

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287774>  

Open in Claude

Prompt caching は、同じ content を Claude に繰り返し送信しているときに、API requests をより速く、より安くする強力な optimization 機能です。アプリケーションで効果的に実装する方法を見ていきましょう。

#### Prompt Caching の仕組み

prompt caching を有効にすると、最初のリクエストは content を 1 時間保持される cache に書き込みます。follow-up requests は同じ content を再処理する代わりに、この cache から読み取ることができます。これは、次のようなものを送信している場合に特に価値があります。

- 大きな system prompts（6K token の coding assistant prompt など）
- 複雑な tool schemas（複数 tools で約 1.7K tokens）
- 繰り返される message content

重要な洞察は、caching は同一 content を繰り返し送信する場合にのみ役立つということです。ただし、多くのアプリケーションでは、これは非常に頻繁に起こります。

#### Tool Schema Caching の設定

tool schemas を cache するには、list 内の最後の tool に cache control field を追加する必要があります。元の tool definitions を変更せずに行う正しい方法は次のとおりです。

```python
if tools:
    tools_clone = tools.copy()
    last_tool = tools_clone[-1].copy()
    last_tool["cache_control"] = {"type": "ephemeral"}
    tools_clone[-1] = last_tool
    params["tools"] = tools_clone
```

このアプローチでは、cache control field を追加する前に、tools list と最後の tool schema の両方のコピーを作成します。tools[-1]["cache_control"] を直接変更することもできますが、コピーする方法は後で tools の順序を変えた場合の問題を防ぎます。

#### System Prompt Caching

system prompts では、cache control を持つ text block として構造化する必要があります。

```python
if system:
    params["system"] = [
        {
            "type": "text",
            "text": system,
            "cache_control": {"type": "ephemeral"}
        }
    ]
```

これにより、system prompt が単純な string から caching をサポートする structured format に変換されます。

#### Cache Behavior を理解する

caching を有効にして requests を実行すると、レスポンス内に異なる usage patterns が表示されます。

- First request: cache_creation_input_tokens=1772 - Claude writes to cache
- Follow-up requests: cache_read_input_tokens=1772 - Claude reads from cache
- Changed content: New cache creation tokens appear

cache は非常に敏感です。tools や system prompt の中の 1 文字を変更しただけでも、その component の cache 全体が無効になります。

#### Cache Ordering と Breakpoints

単一リクエストに複数の cache breakpoints を設定できます。順序が重要です。

1. Tools (if provided)
2. System prompt (if provided)
3. Messages

system prompt を変更して tools は同じままにすると、partial cache read（tools 用）と cache write（新しい system prompt 用）が表示されます。この granular caching により、実際に変更された部分の processing に対してのみ支払うことになります。

#### 実践上の考慮事項

Prompt caching が最も効果的なのは、次のものがある場合です。

- requests 間で一貫した tool schemas
- 安定した system prompts
- 似た context で複数 requests を行うアプリケーション

cache は 1 時間しか持たないことを覚えておいてください。そのため、長期保存ではなく、比較的頻繁に API を使用するアプリケーション向けに設計されています。

Downloads
003_caching.ipynb
(opens in new tab)

---

### レッスン 58: Code execution と Files API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287777>  

Open in Claude

Anthropic API は、組み合わせると非常にうまく機能する 2 つの強力な機能を提供します。Files API と Code Execution です。一見すると別々のものに見えるかもしれませんが、組み合わせることで、複雑なタスクを Claude に委任する非常に興味深い可能性が開けます。

#### Files API

Files API は、ファイルアップロードを扱う代替手段を提供します。画像や PDF を base64 data として messages に直接エンコードする代わりに、事前にファイルをアップロードし、後で参照できます。

仕組みは次のとおりです。

1. ファイル（image、PDF、text など）を別の API call で Claude にアップロードする
2. 一意の file ID を含む file metadata object を受け取る
3. 将来の messages で raw file data を含める代わりに、その file ID を参照する

このアプローチは、同じファイルを複数回参照したい場合や、毎回のリクエストに含めるには扱いにくい大きなファイルを扱う場合に特に有用です。

#### Code Execution Tool

code execution は server-based tool であり、実装を提供する必要はありません。リクエストに事前定義された tool schema を含めるだけで、Claude は隔離された Docker container 内で必要に応じて Python code を実行できます。

code execution environment の主な特徴:

- 隔離された Docker container 内で実行される
- network access はない（外部 API calls はできない）
- Claude は 1 回の会話中に複数回 code を実行できる
- 結果は Claude によって取得、解釈され、final response に反映される

#### Files API と Code Execution を組み合わせる

真の力は、これらの機能を組み合わせることで発揮されます。Docker containers には network access がないため、Files API が execution environment に data を出し入れする主要な方法になります。

典型的な workflow は次のとおりです。

1. Files API を使って data file（CSV など）をアップロードする
2. message に file ID を持つ container upload block を含める
3. Claude に data の分析を依頼する
4. Claude が file を処理する code を書いて実行する
5. Claude が download 可能な outputs（plots など）を生成できる

#### 実践例

streaming service data を使った実例を見てみましょう。CSV ファイルには、subscription tiers、viewing habits、churn（subscription を解約したか）などの user information が含まれています。

まず、helper function を使って file をアップロードします。

```python
file_metadata = upload('streaming.csv')
```

次に、アップロード済み file と分析リクエストの両方を含む message を作成します。

```python
messages = []
add_user_message(
    messages,
    [
        {
            "type": "text",
            "text": """Run a detailed analysis to determine major drivers of churn.
Your final output should include at least one detailed plot summarizing your findings."""
        },
        {"type": "container_upload", "file_id": file_metadata.id},
    ],
)

chat(
    messages,
    tools=[{"type": "code_execution_20250522", "name": "code_execution"}]
)
```

#### Response を理解する

Claude が code execution を使うと、レスポンスには複数種類の blocks が含まれます。

- Text blocks - Claude の分析と説明
- Server tool use blocks - Claude が実行することを決めた実際の code
- Code execution tool result blocks - code 実行の output

Claude は単一のレスポンス中に複数回 code を実行し、反復的に分析を組み立てることがあります。各 execution cycle には code とその results が含まれます。

#### 生成された Files を Download する

最も強力な機能の 1 つは、Claude が files（plots や reports など）を生成し、それらを download 可能にできることです。Claude が visualization を作成すると、それは container に保存され、Files API を使って download できます。

レスポンス内で type: "code_execution_output" の blocks を探してください。これらには生成された content の file IDs が含まれます。

```python
download_file("file_id_from_response")
```

その結果、手作業で書くにはかなりの coding が必要だった、professional visualizations を含む包括的な分析が得られます。

#### Data Analysis を超えて

data analysis は自然な用途ですが、Files API と code execution の組み合わせは多くの可能性を開きます。

- Image processing と manipulation
- Document parsing と transformation
- Mathematical computations と modeling
- custom formatting を伴う report generation

重要なのは、Files API を通じて inputs と outputs を制御しながら、複雑で computational なタスクを Claude に委任できるということです。これにより、Claude が実際に solutions を実行して反復できる coding assistant になる強力な workflow が生まれます。

Downloads
streaming.csv
(opens in new tab)
005_code_execution.ipynb
(opens in new tab)

---

### レッスン 59: Claude の features に関するクイズ

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289124>  

Open in Claude
Loading...

---
### レッスン 60: MCP の紹介

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287780>  

Open in Claude

Model Context Protocol (MCP) は、退屈な統合コードを大量に書かなくても、Claude にコンテキストとツールを提供できる通信レイヤーです。ツール定義と実行の負担を、あなたのサーバーから専用の MCP サーバーへ移す仕組みだと考えてください。

MCP に初めて触れると、基本アーキテクチャを示す図を見ることになります。つまり、MCP Client（あなたのサーバー）が、ツール、プロンプト、リソースを含む MCP Servers に接続する構成です。各 MCP server は、何らかの外部サービスへのインターフェースとして機能します。

#### 実例で MCP を理解する

ユーザーが GitHub データについて Claude に質問できるチャットインターフェースを作っているとしましょう。ユーザーは「自分の全リポジトリでオープンな pull request は何がありますか？」と尋ねるかもしれません。これに答えるには、Claude が GitHub の API にアクセスするためのツールが必要です。

MCP がなければ、GitHub 統合ツールをすべて自分で作成する必要があります。つまり、サポートしたい GitHub 機能のすべてについて、schema と function を書く必要があるということです。

#### Tool Function の問題

GitHub には、リポジトリ、pull request、issue、project など、非常に多くの機能があります。完全な GitHub chatbot を作るには、驚くほど多くのツールを作成しなければなりません。

各ツールには、schema definition と function implementation の両方が必要です。これは開発者として書き、テストし、保守しなければならない大量のコードを意味します。

#### MCP がこれをどう解決するか

MCP は、ツール定義と実行の負担を、あなたのサーバーから MCP servers へ移します。あなたがそれらすべての GitHub ツールを書く代わりに、それらは専用の MCP server 内で作成され、実行されます。

MCP server は GitHub の機能を包む wrapper として機能し、自分で実装しなくても使える事前構築済みのツールを提供します。

MCP servers は、外部サービスによって実装されたデータや機能へのアクセスを提供します。複雑な統合を再利用可能なコンポーネントとしてパッケージ化し、どのアプリケーションからでも接続できるようにします。

#### MCP に関するよくある質問

##### MCP Servers は誰が作成するのか？

誰でも MCP server implementation を作成できます。多くの場合、サービス提供者自身が公式の MCP implementation を作成します。たとえば AWS は、さまざまなサービス用のツールを備えた公式 MCP server を公開するかもしれません。

##### MCP は直接 API 呼び出しとどう違うのか？

MCP servers は、tool schemas と functions をあらかじめ定義済みの形で提供します。API を直接呼び出す場合、それらの tool definitions を自分で作成する責任があります。MCP はその実装作業を省いてくれます。

##### MCP は単なる tool use ではないのか？

これはよくある誤解です。MCP servers と tool use は補完的ですが、異なる概念です。MCP は、ツールの作成と保守の作業を誰が行うかに関するものです。MCP では、誰かがすでに tool functions と schemas を書いており、それらが MCP server の中にパッケージされています。

重要なポイントは、MCP servers が tool schemas と functions をあらかじめ定義済みで提供し、複雑な統合を自分で構築・保守する必要をなくしてくれることです。

---

### レッスン 61: MCP clients

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287775>  

Open in Claude

MCP client は、あなたのサーバーと MCP servers の間の通信ブリッジとして機能します。MCP server が提供するすべてのツールへのアクセスポイントだと考えてください。外部ツールやサービスを使う必要があるとき、client がメッセージの受け渡しとプロトコルの詳細をすべて処理します。

#### Transport に依存しない通信

MCP の主要な強みの 1 つは transport agnostic であることです。これは、client と server が異なる通信方式でやり取りできる、という少し専門的な言い方です。最も一般的な構成では、MCP client と server の両方を同じマシン上で実行し、標準入力/出力を通じて通信します。

ただし、その方法に限定されるわけではありません。MCP clients と servers は次の方法でも接続できます。

- HTTP
- WebSockets
- その他さまざまなネットワークプロトコル

#### メッセージタイプ

接続されると、client と server は MCP specification で定義された特定のメッセージタイプを交換します。主に扱うメッセージタイプは次のとおりです。

- ListToolsRequest/ListToolsResult: client が server に「どのツールを提供していますか？」と尋ね、利用可能なツール一覧を受け取ります。
- CallToolRequest/CallToolResult: client が server に特定の引数で特定のツールを実行するよう依頼し、その結果を受け取ります。

#### 完全なフローの例

実際のシナリオで、すべての要素がどのように連携するかを見てみましょう。ユーザーが「自分にはどんなリポジトリがありますか？」と尋ねたとします。完全な通信フローは次のようになります。

ユーザーがあなたのサーバーに query を送信するとプロセスが始まります。あなたのサーバーは、リクエストを行う前に Claude に利用可能なツール一覧を提供する必要があると判断します。

あなたのサーバーは MCP client にツールを問い合わせます。MCP client は MCP server に ListToolsRequest を送り、ListToolsResult を受け取ります。

これであなたのサーバーは、Claude への最初のリクエストに必要なものをすべて持っています。つまり、ユーザーの質問と利用可能なツールの両方です。

Claude はツールを確認し、質問に答えるにはそのうちの 1 つを呼び出す必要があると判断します。Claude は tool use request で応答します。

あなたのサーバーは、Claude が要求したツールを実行するよう MCP client に依頼します。MCP client は MCP server に CallToolRequest を送り、MCP server が実際に GitHub へのリクエストを行います。

GitHub はリポジトリデータを返します。そのデータは MCP server から CallToolResult として戻り、MCP client を経由し、最終的にあなたのサーバーへ届きます。

あなたのサーバーは follow-up message で tool results を Claude に送り返します。Claude は完全な応答を作成するために必要な情報をすべて手に入れます。

最後に Claude が整形された答えを返し、あなたのサーバーがそれをユーザーへ渡します。

はい、このフローには多くのステップがありますが、各コンポーネントには明確な責任があります。MCP client は server communication の複雑さを抽象化し、あなたがアプリケーションロジックの構築に集中できるようにします。これから自分たちの MCP client と server を実装していく中で、各要素が実際にどのように組み合わさるかが見えてくるでしょう。

---

### レッスン 62: Project setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287785>  

Open in Claude

MCP clients と servers がどのように連携するかをよりよく理解するために、CLI ベースの chatbot を作ります。このハンズオンプロジェクトにより、MCP アーキテクチャの両側を実践的に体験できます。

#### 作るもの

この chatbot では、ユーザーが command-line interface を通じてドキュメントのコレクションと対話できます。システムは 2 つの主要コンポーネントで構成されます。

- ユーザー操作を処理する MCP client
- ドキュメント操作を管理するカスタム MCP server

server は 2 つの重要なツールを提供します。1 つはドキュメント内容を読むためのもの、もう 1 つはそれを更新するためのものです。単純化のため、すべてのドキュメントはメモリ内に保存します。データベースは不要です。

#### 重要なアーキテクチャ上の注意

実際のプロジェクトでは、通常 MCP client か MCP server のどちらか一方を実装し、両方は実装しません。たとえば次のようなものを作ることがあります。

- 自分のサービスを他の開発者に公開するための MCP server
- 既存の MCP servers に接続するための MCP client

このプロジェクトで両方のコンポーネントを作るのは、純粋に学習目的です。両者がどのように通信し、連携するかを理解するためです。

#### Project Setup

このレッスンに添付されている cli_project.zip ファイルをダウンロードし、好みの開発ディレクトリに展開してください。project folder をコードエディタで開きます。

このプロジェクトには、セットアップ手順を含む包括的な README ファイルが含まれています。次の手順に従ってください。

1. Anthropic API key を .env ファイルに追加する
2. UV（推奨）または pip を使って dependencies をインストールする
3. starter application を実行して、すべてが動作することを確認する

#### アプリケーションの実行

terminal で project directory に移動します。main.py、mcp_client.py、mcp_server.py などの主要な project files が見えるはずです。

アプリケーションを開始するには、次のいずれかのコマンドを使います。

```bash
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
```

アプリケーションが正常に起動すると、chat prompt が表示されます。「what's 1+1?」のような簡単な質問でテストしてください。Claude から短い応答が返るはずです。

基本セットアップが完了したので、MCP features の実装を始め、clients と servers が Model Control Protocol を通じてどのように通信するかを探っていく準備ができました。

Downloads
cli_project.zip
(opens in new tab)
cli_project_COMPLETE.zip
(opens in new tab)

---

### レッスン 63: MCP でツールを定義する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287797>  

Open in Claude

公式 Python SDK を使うと、MCP server の構築はずっと簡単になります。ツール用の複雑な JSON schemas を手作業で書く代わりに、SDK が decorators と type hints によってその複雑さをすべて処理してくれます。

この例では、メモリ内に保存されたドキュメントを管理する MCP server を作成します。server は 2 つの重要なツールを提供します。1 つはドキュメント内容を読むためのもの、もう 1 つは find-and-replace operations によって更新するためのものです。

#### MCP Server のセットアップ

Python MCP SDK により、server 作成は非常に簡単になります。わずか 1 行で完全な MCP server を初期化できます。

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

この実装では、documents は単純な Python dictionary に保存されます。keys は document IDs、values には document content が入ります。

```python
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditure",
    "outlook.pdf": "This document presents the projected future performance of the",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}
```

#### Decorators による Tool Definition

SDK は、冗長なツール作成プロセスを、きれいで読みやすいものに変えてくれます。長い JSON schemas を書く代わりに、Python decorators と type hints を使います。

#### Document Reader Tool の作成

最初のツールでは、Claude が ID によって任意のドキュメントを読めるようにします。完全な実装は次のとおりです。

```python
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")

    return docs[doc_id]
```

@mcp.tool decorator は、Claude に必要な JSON schema を自動的に生成します。Pydantic の Field class は parameter descriptions を提供し、Claude が各 argument に何が期待されているかを理解する助けになります。

#### Document Editor Tool の構築

2 つ目のツールは、ドキュメントに対して単純な find-and-replace operations を実行します。

```python
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")

    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

このツールは 3 つの parameters を取ります。document ID、検索する text、replacement text です。実装では単純化のため、Python 組み込みの string replace() method を使っています。

#### Error Handling

どちらのツールにも、Claude が存在しないドキュメントを要求した場合を処理する基本的な error handling が含まれています。無効な document ID が提供されると、ツールは Claude が理解し、場合によっては対応できる説明的な message を含む ValueError を発生させます。

#### SDK アプローチの主な利点

- Python type hints からの自動 JSON schema generation
- 保守しやすい、きれいで読みやすいコード
- Pydantic による組み込みの parameter validation
- 手作業で schema を書く場合と比べた boilerplate の削減
- 開発時の type safety と IDE support

MCP Python SDK は、かつて複雑だった tool definitions の作成プロセスを、Python 開発者にとって自然に感じられるものへ変えてくれます。あなたは business logic に集中し、SDK が protocol details を処理します。

---

### レッスン 64: The server inspector

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287781>  

Open in Claude

MCP servers を構築するときは、完全なアプリケーションに接続しなくても機能をテストできる方法が必要です。Python MCP SDK には、server をリアルタイムでデバッグおよびテストできる、browser-based inspector が組み込まれています。

#### Inspector の起動

まず、Python environment が有効化されていることを確認します（正確なコマンドはプロジェクトの README を確認してください）。次に、次のコマンドで inspector を実行します。

```bash
mcp dev mcp_server.py
```

これにより port 6277 で development server が起動し、ブラウザで開くための local URL が表示されます。inspector interface が読み込まれ、MCP Inspector dashboard が表示されます。

#### Interface に関する重要な注意

MCP inspector は現在も活発に開発されているため、表示される interface は現在のスクリーンショットとは異なる場合があります。ただし、tools、resources、prompts をテストするための core functionality は同様のままであるはずです。

#### 接続とツールのテスト

左側の "Connect" button をクリックして MCP server を開始します。接続されると、Resources、Prompts、Tools、その他の機能の sections を含む navigation bar が表示されます。

ツールをテストするには、次の手順を実行します。

1. Tools section に移動する
2. "List Tools" をクリックして利用可能なすべてのツールを表示する
3. ツールを選択して testing interface を開く
4. 必要な parameters を入力する
5. "Run Tool" をクリックして実行し、結果を見る

#### ドキュメント操作のテスト

たとえば、document reading tool をテストするには、document ID（"deposition.md" など）を入力してツールを実行します。inspector には、返された content や success messages などの結果が表示されます。

操作を連鎖させて機能を確認することもできます。たとえば、text を置換してドキュメントを編集した後、すぐに read tool を再実行して、変更が正しく適用されたことを確認できます。

#### Development Workflow

inspector は効率的な development loop を作ります。

1. MCP server code に変更を加える
2. inspector を通じて個別のツールをテストする
3. 完全な application setup なしで結果を確認する
4. 問題を分離してデバッグする

このツールは、より複雑な MCP servers を構築するにつれて不可欠になります。基本機能をテストするためだけに server を Claude や別のアプリケーションへ接続する必要がなくなり、開発が大幅に速く、集中しやすくなります。

---

### レッスン 65: client を実装する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287793>  

Open in Claude

MCP server が動作するようになったので、次は client 側を構築します。client によって、私たちのアプリケーションは MCP server と通信し、その機能へアクセスできるようになります。

#### Client Architecture を理解する

ほとんどの実際のプロジェクトでは、MCP client または MCP server のどちらか一方を実装します。両方ではありません。このプロジェクトで両方を作るのは、それらがどのように連携するかを見るためです。

MCP client は 2 つの主要コンポーネントで構成されます。

- MCP Client - session を使いやすくするために作成する custom class
- Client Session - server への実際の接続（MCP Python SDK の一部）

client session は、使い終わった後に適切な resource cleanup を必要とします。そのため、custom MCP Client class で包み、cleanup を自動的に処理します。

#### Client がアプリケーションにどう組み込まれるか

私たちの application flow を思い出してください。CLI code は MCP server に対して 2 つの主要なことを行う必要があります。

- Claude に送るための利用可能なツール一覧を取得する
- Claude が要求したときにツールを実行する

MCP client は、アプリケーションコードが使える単純な method calls を通じて、これらの機能を提供します。

#### Core Methods の実装

client に 2 つの重要な methods、list_tools() と call_tool() を実装する必要があります。

#### List Tools Method

この method は server からすべての利用可能なツールを取得します。

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

これは単純です。session（server への接続）にアクセスし、組み込みの list_tools() function を呼び出し、result から tools を返します。

#### Call Tool Method

この method は server 上の特定のツールを実行します。

```python
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

tool name と input parameters（Claude によって提供されるもの）を server に渡し、result を返します。

#### Client のテスト

実装をテストするために、client を直接実行できます。このファイルには、MCP server に接続して methods を呼び出す testing harness が含まれています。

```python
async with MCPClient(
    command="uv", args=["run", "mcp_server.py"]
) as client:
    result = await client.list_tools()
    print(result)
```

このテストを実行すると、以前作成した read_doc_contents と edit_document tools を含む tool definitions が出力されるはずです。

#### すべてを組み合わせる

client が tools を list し、それらを call できるようになったので、完全な flow をテストできます。main application を実行し、Claude にドキュメントについて質問すると、次のようになります。

1. コードが client を使って利用可能なツールを取得する
2. それらのツールがユーザーの質問とともに Claude に送られる
3. Claude が read_doc_contents tool を使うと決める
4. コードが client を使ってそのツールを実行する
5. 結果が Claude に送り返され、Claude がユーザーに応答する

たとえば、「What is the contents of the report.pdf document?」と尋ねると、Claude は document reading tool を使い、server に設定した 20m condenser tower document についての情報が返ってきます。

client はアプリケーションロジックと MCP server の間のブリッジとして機能し、基盤となる接続の詳細を気にせずに server functionality へ簡単にアクセスできるようにします。

---

### レッスン 66: resources を定義する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287782>  

Open in Claude

MCP servers の Resources を使うと、典型的な HTTP server の GET request handlers と同じように、clients にデータを公開できます。何かの action を実行するのではなく、情報を取得する必要があるシナリオに最適です。

#### 例で Resources を理解する

ユーザーが @document_name と入力してファイルを参照できる document mention feature を作りたいとしましょう。これには 2 つの操作が必要です。

- 利用可能なすべての documents の一覧を取得する（autocomplete 用）
- 特定の document の内容を取得する（mention されたとき）

ユーザーが @ を入力したとき、利用可能な documents を表示する必要があります。mention を含む message を送信したときは、その document の content を Claude に送る prompt に自動的に注入します。

#### Resources の仕組み

Resources は request-response pattern に従います。client が URI を含む ReadResourceRequest を送信し、MCP server が data で応答します。URI は、アクセスしたい resource の address のように機能します。

#### Resources の種類

resources には 2 種類あります。

- Direct Resources: docs://documents のような、変化しない static URIs
- Templated Resources: docs://documents/{doc_id} のような、parameters を含む URIs

templated resources では、Python SDK が URI から parameters を自動的に解析し、function に keyword arguments として渡します。

#### Resources の実装

Resources は @mcp.resource() decorator を使って定義します。両方の種類を作成する方法は次のとおりです。

##### Direct Resource（Documents の一覧）

```python
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

##### Templated Resource（Document の取得）

```python
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

#### MIME Types

Resources は、strings、JSON、binary など、あらゆる種類の data を返すことができます。mime_type parameter は、返している data の種類について clients に hint を与えます。

- application/json - 構造化された JSON data
- text/plain - プレーンテキスト content
- 異なる data formats 用のその他任意の有効な MIME type

MCP Python SDK は return values を自動的に serialize します。手動で JSON strings に変換する必要はありません。

#### Resources のテスト

MCP Inspector を使って resources をテストできます。次のコマンドで server を実行します。

```bash
uv run mcp dev mcp_server.py
```

次に、ブラウザで inspector に接続します。次のものが表示されます。

- Resources: direct/static resources の一覧
- Resource Templates: parameters を受け取る templated resources の表示

任意の resource をクリックしてテストし、client が受け取る exact response structure を確認できます。

#### Key Points

- Resources は data を公開し、tools は actions を実行する
- static data には direct resources を使い、parameterized queries には templated resources を使う
- MIME types は clients が response format を理解する助けになる
- SDK は serialization を自動的に処理する
- templated URIs の parameter names は function arguments になる

Resources は、MCP clients が data を利用できるようにするためのクリーンな方法を提供します。document mentions、file browsing、または server から情報を取得する必要があるあらゆるシナリオを可能にします。

---

### レッスン 67: resources にアクセスする

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287783>  

Open in Claude

MCP の Resources により、server は情報にアクセスするために tool calls を必要とするのではなく、prompts に直接含められる data を公開できます。これにより、Claude のような AI models に context を提供する、より効率的な方法が生まれます。

#### Resource Requests を理解する

MCP server 上で resources を定義したら、client にはそれらを request して使う方法が必要です。client はアプリケーションと MCP server の間の bridge として機能し、communication と data parsing を自動的に処理します。

flow は単純です。ユーザーが document を参照したい場合（たとえば "@report.pdf" と入力した場合）、アプリケーションは MCP client を使って server からその resource を取得し、その内容を Claude に送る prompt に直接含めます。

#### Resource Reading の実装

core functionality には、MCP client 内の read_resource function が必要です。この function は、どの resource を取得するかを識別する URI parameter を取ります。

```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
```

MCP server からの response には contents list が含まれます。通常は最初の element だけが必要で、そこに実際の resource data と MIME type などの metadata が含まれています。

#### 異なる Content Types の処理

Resources は異なる種類の content を返せるため、client はそれらを適切に parse する必要があります。MIME type が data の扱い方を教えてくれます。

```python
if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)

    return resource.text
```

このアプローチにより、JSON resources は適切に Python objects へ parse され、plain text resources は strings として返されます。MIME type は、正しい parsing strategy を決めるための hint として機能します。

#### 必要な Imports

これを正しく動作させるには、MCP client に次の imports が必要です。

```python
import json
from pydantic import AnyUrl
```

json module は JSON responses の parse を処理し、AnyUrl は URI parameter の適切な type handling を保証します。

#### Resource Access のテスト

実装後、CLI application を通じて機能をテストできます。「What's in the @report.pdf document?」のように入力すると、システムは次のように動作するはずです。

1. autocomplete list に利用可能な resources を表示する
2. resource を選択できるようにする
3. resource content を自動的に取得する
4. その content を Claude への prompt に含める

主な利点は、Claude が document content を prompt 内で直接受け取るため、その情報にアクセスするための tool calls が不要になることです。これにより、やり取りがより速く効率的になります。

アプリケーションとの統合

あなたが書く MCP client code は、アプリケーションの他の部分で使われることを覚えておいてください。read_resource function は、他の components が document contents を取得したり、利用可能な resources を list したり、resource data を prompts に統合したりするために呼び出せる building block になります。

この separation of concerns により、コードはきれいに保たれます。MCP client は server との communication を処理し、application logic はその data をどう効果的に使うかに集中します。

---

### レッスン 68: prompts を定義する

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287784>  

Open in Claude

MCP servers の Prompts を使うと、clients が自分でゼロから prompts を書く代わりに利用できる、事前構築済みの高品質な instructions を定義できます。ユーザーが自力で考えるものより良い結果を出す、丁寧に作られた templates だと考えてください。

#### なぜ Prompts を使うのか？

Claude に document を markdown に再整形してほしいとしましょう。ユーザーは単に「convert report.pdf to markdown」と入力しても問題なく動作します。しかし、formatting、structure、output requirements に関する具体的な instructions を含む、十分にテストされた prompt を使ったほうが、おそらくはるかに良い結果が得られます。

重要なポイントは、ユーザーが自分でこれらのタスクを達成できるとしても、MCP server authors によって慎重に開発・テストされた prompts を使うことで、より一貫性があり高品質な結果を得られるということです。

#### Prompts の仕組み

Prompts は、clients が直接使える user and assistant messages の集合を定義します。client が prompt を request すると、server は Claude にそのまま送信できる messages の list を返します。

基本構造は次のようになります。

- @mcp.prompt() decorator を使って prompts を定義する
- 各 prompt に name と description を追加する
- 完全な prompt を形成する messages の list を返す
- これらの prompts は、高品質で、十分にテストされ、MCP server の目的に関連しているべきである

#### Format Command の構築

document formatting prompt を実装する方法は次のとおりです。まず、base message types を import する必要があります。

```python
from mcp.server.fastmcp import base
```

次に prompt function を定義します。

```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra formatting.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""

    return [
        base.UserMessage(prompt)
    ]
```

#### Prompts のテスト

MCP Inspector を使って prompts をテストできます。Prompts section に移動し、prompt を選択して、必要な parameters を入力します。inspector は、Claude に送信される generated messages を表示します。

これにより、実際のアプリケーションで使う前に、prompt が variables を正しく interpolates し、期待される message structure を生成することを確認できます。

#### Best Practices

MCP server 用の prompts を作成するときは、次の点を意識してください。

- server の目的の中心となる tasks に集中する
- 曖昧な request ではなく、詳細で具体的な instructions を書く
- 異なる inputs で prompts を徹底的にテストする
- users が各 prompt の役割を理解できるよう、明確な descriptions を含める
- prompt が server の tools や resources とどのように連携するかを考慮する

prompts は、ユーザーが簡単には自力で得られない価値を提供するためのものだということを覚えておいてください。つまり、MCP server が扱う domain におけるあなたの専門性を表すものであるべきです。

---

### レッスン 69: client 内の prompts

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287786>  

Open in Claude

MCP の Prompts は、client が使える user and assistant messages の集合を定義します。これらの prompts は高品質で、十分にテストされており、MCP server 全体の目的に関連しているべきです。

#### List Prompts の実装

最初のステップは、MCP client に list_prompts method を実装することです。この method は server から利用可能なすべての prompts を取得します。

```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

この単純な実装では、session の list_prompts method を呼び出し、result から prompts array を返します。

#### 個別の Prompts を取得する

get_prompt method は、arguments が補間された特定の prompt を取得します。prompt を request するとき、prompt function に keyword arguments として渡される arguments を提供します。

```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

この method は result から messages を返します。これらは Claude に直接渡せる conversation を形成します。

#### Prompt Arguments の仕組み

server 側で prompt function を定義するとき、parameters を受け取ることができます。たとえば、document formatting prompt は doc_id parameter を期待するかもしれません。

```python
def format_document(doc_id: str):

# The doc_id gets interpolated into the prompt
```

client が get_prompt を呼び出すとき、arguments dictionary には期待される keys が含まれている必要があります。MCP server はこれらを prompt function に keyword arguments として渡し、dynamic content を prompt template に挿入できるようにします。

#### CLI で Prompts をテストする

実装後、command-line interface を通じて prompts をテストできます。forward slash を入力すると、利用可能な prompts が commands として表示されます。prompt を選択すると、利用可能な options（document IDs など）から選ぶよう求められる場合があり、その後 complete prompt が Claude に送信されます。

workflow は次のようになります。

1. ユーザーが prompt（"format" など）を選択する
2. システムが必要な arguments（どの document を format するかなど）を求める
3. 補間された values とともに prompt が Claude に送信される
4. Claude は tools を使って追加 data を取得し、task を完了できる

#### Prompt Best Practices

MCP server 用の prompts を作成するときは、次の点を意識してください。

- server の目的に関連させる
- deployment 前に徹底的にテストする
- 明確で具体的な instructions を使う
- 利用可能な tools と相性よく動作するように設計する
- users がどの arguments を提供する必要があるかを考慮する

Prompts は、事前定義された機能と dynamic user needs の間をつなぎ、parameterization による柔軟性を維持しながら、複雑な tasks に対する構造化された starting points を Claude に提供します。

---

### レッスン 70: MCP review

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287790>  

Open in Claude

---

### レッスン 71: Quiz on Model Context Protocol

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289126>  

Open in Claude
Loading...

---

### レッスン 72: Anthropic apps

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287787>  

Open in Claude

この module では、Anthropic が構築した 2 つの強力な applications、Claude Code と Computer Use を探ります。これらはそれ自体で便利なツールであるだけでなく、AI agents が実際に動作している完璧な例でもあります。仕組みを理解することで、後で自分自身の agents を構築するためのしっかりした基礎が得られます。

#### Our Plan

理解を段階的に積み上げる流れで進めます。

- Claude Code - terminal で動作するこの agentic coding assistant から始める
- Computer Use - Claude が desktop applications と対話できるようにする tools のセットを探る
- Agents - これらの applications が agents として成功している理由を理解する

#### Claude Code

Claude Code は、さまざまな programming tasks を支援できる terminal-based coding assistant です。command line の中で Claude を使えるようになり、次のことにすぐ対応できると考えてください。

- files を編集し、bugs を修正する
- coding questions に答える
- development workflows を支援する

完全な setup process を順に見ていき、その後、小さな sample project で Claude Code を使って、実際にどのように動作するかを正確に確認します。

#### Computer Use

Computer Use は Claude の capabilities をさらに大きく広げます。これは、Claude が完全な desktop computer environment と対話できるようにする tools のコレクションです。つまり Claude は次のことができます。

- websites にアクセスし、internet を閲覧する
- desktop applications と対話する
- visual interface navigation を必要とする tasks を実行する

これは text-only interactions と比べて、可能なことを劇的に拡張します。

#### なぜこれらが Agents にとって重要なのか

Claude Code と Computer Use はどちらも、agents を理解するための優れた case studies です。agents を効果的にする key principles を示しています。

- Tool integration and usage
- Multi-step task execution
- Environmental interaction
- Autonomous problem-solving

これらの real-world implementations を調べることで、Claude Code と Computer Use が成功している理由についての insights が得られ、それが自分自身の agent development work に活かされます。

次の section では、Claude Code の setup process から始めましょう。

---

### レッスン 73: Claude Code setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287788>  

Model Context Protocol の紹介
14 レッスン中 0 完了 (0%)
Start

Curriculum

Course Overview
Introduction
Welcome to the course
Introducing MCP
MCP clients
Hands-on with MCP servers
Project setup
Defining tools with MCP
The server inspector
Course satisfaction survey
Connecting with MCP clients
Implementing a client
Defining resources
Accessing resources
Defining prompts
Prompts in the client
Assessment and wrap Up
Final assessment on MCP
MCP review

About this course

Data and Privacy
Skilljar とは何ですか？なぜログインしているのですか？

Skilljar は、私たちの教育コンテンツをホストする learning management system です。Anthropic course materials にアクセスするためにログインしています。この別プラットフォームにより、interactive learning experiences を提供し、progress を追跡し、すべての course resources に整理された形でアクセスできるようにしています。

Skilljar は私の learning activity についてどのような情報を収集しますか？

Skilljar は、course progress、lesson completion status、quiz scores、materials に費やした時間などの基本的な learning analytics を収集します。この data は、あなたが course をどのように進めているかを理解し、completion certificates を提供するために役立ちます。すべての data collection は learning experience の改善に焦点を当てており、Skilljar's Privacy Policy の対象となります。

私の Skilljar data は Anthropic account data とどう違いますか？

Skilljar はこの course platform 内での learning progress のみを追跡します。一方、Anthropic account は Anthropic Console および/または Claude AI services へのアクセスを管理します。

Skilljar は安全ですか？私の data はどこに保存されますか？

はい。Skilljar は data encryption、secure hosting、regular security audits を含む industry-standard security measures を採用しています。あなたの learning data は、適切な access controls を備えた secure servers に保存されます。Skilljar は SOC 2 compliant であり、data protection の best practices に従って、あなたの情報が安全かつ非公開に保たれるようにしています。

learning activity や account を削除するにはどうすればよいですか？

learning data または account の削除をリクエストするには、academy-support@anthropic.com に email してください。リクエストは、適用される privacy laws と私たちの data retention policies に従って処理されます。compliance や security などの legitimate business purposes のために一部の data を保持する必要がある場合がありますが、法的に許される範囲で personal information はすべて削除します。

learning content にアクセスするには Anthropic account が必要ですか？

いいえ、この learning content にアクセスするために Anthropic account は必要ありません。course は Skilljar 上でホストされており、アクセスには Skilljar account のみが必要です。ただし、course 完了後に Claude AI services を使いたい場合は、claude.ai で別途 Anthropic account を作成する必要があります。

© 2025 Anthropic PBC

---

### レッスン 74: Claude Code in action

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287805>  

Open in Claude

Claude Code はコードを書くためだけのツールではありません。software project のあらゆる段階であなたと並走するように設計されています。initial setup から deployment、support まで対応できる、チーム内のもう 1 人の engineer のようなものだと考えてください。

#### The /init Command

Claude Code で project に取り組み始めるとき、最初に実行したいのが /init command です。これにより、Claude は codebase 全体を scan し、project structure、dependencies、coding style、architecture を理解します。

Claude は学習したすべてを CLAUDE.md という特別な file にまとめます。この file は以後のすべての conversations に context として自動的に含まれるため、Claude は project に関する重要な details を覚えています。

異なる scopes に対して複数の CLAUDE.md files を持つことができます。

- Project - project に取り組むすべての engineers 間で共有される
- Local - git に check in されないあなた個人の notes
- User - すべての projects にわたって使用される

/init を実行するとき、Claude に特に注目してほしい areas について special directions を追加できます。生成される file には、Claude が従うべき build commands、coding guidelines、project-specific patterns が含まれます。

# command を使って CLAUDE.md file に素早く notes を追加することもできます。たとえば、# Always use descriptive variable names と入力すると、この guideline を project、local、または user memory に追加するよう促されます。

#### 一般的な Workflows

Claude は effort multiplier として扱うと最も効果的です。提供する context と structure が多いほど、より良い結果が得られます。最も効果的な workflow は次のとおりです。

##### Step 1: Claude に Context を渡す

Claude に何かを作るよう依頼する前に、作成したい feature に関連する codebase 内の files を特定します。まず Claude にこれらの files を読んで analyze するよう依頼します。これにより、Claude は coding patterns と既存機能の examples を得て、それらを土台にできます。

##### Step 2: Claude に Solution の計画を立てさせる

すぐに implementation に進むのではなく、Claude に problem を考え抜いて plan を作成するよう依頼します。まだ code は一切書かず、必要な approach と steps だけに集中するよう、Claude に具体的に伝えます。

##### Step 3: Claude に Solution を実装させる

しっかりした plan ができたら、それを実装するよう Claude に依頼します。Claude は、これまで一緒に行った context と planning work に基づいて code を書きます。

#### Test-Driven Development Workflow

さらに良い結果を得るために、test-driven approach を使うこともできます。

1. Claude に context を渡す - 前と同じように、関連 files を Claude に見せる
2. Claude に test cases を考えさせる - 新しい feature を検証する tests を Claude に brainstorm させる
3. Claude にその tests を実装させる - 最も relevant な tests を選び、Claude に書かせる
4. tests に合格する code を Claude に書かせる - Claude はすべての tests が通るまで implementation を iterate する

この approach は、Claude が目指すべき明確な success criteria を持つため、より robust な code を生み出すことがよくあります。

#### 実践例

これらの workflows が実際にどう見えるかを示します。既存 project に document conversion tool を追加したいとしましょう。

```
// First, ask Claude to read relevant files
> Read the math.py and document.py files

// Then ask for planning (not implementation)
> Plan to implement document_path_to_markdown tool:

1. Create a function that:

- Takes a file path parameter
- Validates the file exists
- Determines file type from extension
- Reads binary data from file
- Leverages existing binary_document_to_markdown function
- Returns markdown string

2. Add appropriate documentation
3. Register the tool with MCP server
4. Add tests

// Finally, ask for implementation
> Implement the plan
```

その後 Claude は function を作成し、必要な files を更新し、tests を書き、test suite を実行してすべてが正しく動作することまで確認します。

#### 追加 Commands

Claude Code には、いくつかの便利な commands が含まれています。

- /clear - conversation history をクリアし、context をリセットする
- /init - codebase を scan し、CLAUDE.md documentation を作成する
- # - CLAUDE.md file に notes を追加する

Claude は、git への staging と committing、tests の実行、dependencies の管理といった routine development tasks も処理できます。editor と terminal を行き来する代わりに、あなたが大きな全体像に集中している間、Claude にこれらの tasks を任せることができます。

Claude Code で成功するための鍵は、これが単なる code generator ではなく、collaborative partner として設計されていることを覚えておくことです。より多くの context と structure を提供するほど、Claude は project の構築と保守をより効果的に支援できます。

Downloads
app_starter.zip
(opens in new tab)

---

### レッスン 75: MCP servers による拡張

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287792>  

Open in Claude
0 seconds of 2 minutes, 30 secondsVolume 90%

Claude Code には MCP client が組み込まれているため、MCP servers を接続して Claude にできることを大幅に拡張できます。これにより、development workflow をカスタマイズする非常に強力な可能性が開けます。

#### MCP が Claude を拡張する仕組み

Model Context Protocol により、Claude Code は MCP servers を通じて external services and tools に接続できます。Claude の built-in capabilities に限定される代わりに、特定の tools、resources、integrations を提供する servers を接続することで custom functionality を追加できます。

各 MCP server は、3 つの主要コンポーネントを通じて Claude に異なる種類の functionality を公開できます。Tools（actions を実行するため）、Prompts（templates のため）、Resources（data にアクセスするため）です。

#### MCP Server のセットアップ

Claude Code に MCP server を追加するのは簡単です。command line を使って server を登録します。

```bash
claude mcp add [server-name] [command-to-start-server]
```

たとえば、uv run main.py で起動する document processing server がある場合は、次のように実行します。

```bash
claude mcp add documents uv run main.py
```

登録されると、Claude Code は起動時に自動的に server に接続します。

#### 例: Document Processing

実用的な例は、Claude が PDF や Word documents を読めるようにするツールを作成することです。"document_path_to_markdown" tool を持つ MCP server を構築することで、Claude に document contents を markdown format に変換するよう依頼できます。

「Convert the tests/fixtures/mcp_docs.docx file to markdown」と Claude に依頼すると、Claude は自動的に custom tool を使って document を読み込み、converted content を返します。

#### 人気の MCP Integrations

MCP ecosystem には、多くの一般的な development tools and services 用の servers が含まれています。

- sentry-mcp - Sentry に記録された bugs を自動的に発見して修正する
- playwright-mcp - testing と troubleshooting のために Claude に browser automation capabilities を与える
- figma-context-mcp - Figma designs を Claude に公開する
- mcp-atlassian - Claude が Confluence と Jira にアクセスできるようにする
- firecrawl-mcp-server - web scraping capabilities を Claude に追加する
- slack-mcp - Claude が messages を投稿したり、特定の threads に返信したりできるようにする

#### Development Workflow を構築する

本当の力は、自分の specific development process に合う複数の MCP servers を組み合わせることで発揮されます。たとえば次のように設定できます。

- production error details を取得する Sentry server
- ticket requirements を読む Jira server
- work が完了したときに team に通知する Slack server
- internal tools and APIs 用の custom servers

これにより、Claude がすでに使っているすべての tools and services とシームレスに連携できる development environment が作られます。その結果、Claude はあなた固有の workflow に合わせて調整された、はるかに強力な coding assistant になります。

---

### レッスン 76: Agents and workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287796>  

Open in Claude

Workflows と agents は、Claude が単一の request では完了できない user tasks を扱うための strategies です。この course を通じて、実はすでに両方を作成してきました。tools を使い、Claude に tasks の完了方法を考えさせたとき、それは agent でした。

#### Workflows と Agents をいつ使うか

判断基準は、その task をどれだけよく理解しているかです。

- Claude が problem を解くために通るべき正確な flow や steps を思い描ける場合、または app の UX が users を特定の tasks に制約している場合は workflows を使う
- Claude にどの task や task parameters を渡すことになるか正確には分からない場合は agents を使う

Workflows は、事前に決められた一連の steps を通じて specific problem を解くための、Claude への一連の calls です。Agents は Claude に goal と tools の集合を与え、提供された tools を通じてその goal をどう完了するかを Claude に考えさせます。

#### 例: Image to CAD Workflow

実用的な workflow example を見てみましょう。ユーザーが metal part の image を drag and drop すると、それから STEP file（3D models の industry standard）を作成する web app を構築していると想像してください。

ユーザーが image file を提供したときに何をすべきかはかなり明確であり、そのすべてを predefined series of steps として code で簡単に書き出せます。これは workflow に非常に適した候補です。

workflow は次のように分解できます。

1. image を Claude に渡し、object を describe するよう依頼する
2. description に基づいて、Claude に CadQuery library を使って object を model するよう依頼する
3. rendering を作成する
4. Claude に original image と rendering を比較して grade するよう依頼する。問題があれば修正する

#### Evaluator-Optimizer Pattern

この modeling workflow は evaluator-optimizer pattern の例です。仕組みは次のとおりです。

- Producer: input を受け取り output を作成する（Claude が CadQuery を使って part を model し、rendering を作成する）
- Grader: 何らかの criteria に照らして output を評価する
- Feedback loop: grader が output を受け入れない場合、改善のために feedback が producer に戻る
- Iteration: grader が output を受け入れるまで cycle を繰り返す

#### Workflow Patterns を学ぶ理由

さまざまな workflows を識別する目的は、自分自身の features を実装するための repeatable recipes の集合を得ることです。Evaluator-Optimizer は、他の engineers にとってうまく機能してきた workflow pattern の 1 つです。自分の app でも使うことを検討してください。

覚えておくべきなのは、workflows を識別すること自体が何かをしてくれるわけではないということです。実装するには、実際の code を書く必要があります。ただし、これらの patterns は多くの engineers にとって成功してきたものなので、理解し、自分の projects に適用する価値があります。

---

### レッスン 77: Parallelization workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287804>  

Open in Claude
0 seconds of 3 minutes, 44 secondsVolume 90%

AI applications を構築していると、表面的には単純に見えるものの、効果的に実装しようとすると複雑になる tasks によく出会います。parallelization workflows という強力な pattern を探り、複雑な tasks を管理しやすく focused な pieces に分解する方法を見てみましょう。

#### Complex Single Prompts の問題

ユーザーが parts の images を upload すると、使用すべき最適な material の recommendations を受け取る material designer application を構築していると想像してください。最初は、image を Claude に送り、metal、polymer、ceramic、composite、elastomer、wood の中から選ぶよう simple prompt で依頼したくなるかもしれません。

この approach は動作するかもしれませんが、1 回の request で Claude に多くの heavy lifting を求めています。各 material type に対する具体的な criteria がなければ、結果は可能なほど信頼できるものにはなりません。

これを改善するために、各 material の詳細な criteria を 1 つの巨大な prompt に追加しようと思うかもしれません。しかし、これは新たな問題を生みます。Claude はこれらすべての異なる considerations を同時に処理しなければならず、混乱や suboptimal results につながる可能性があります。

#### より良い Approach: Parallelization

すべてを 1 つの request に詰め込む代わりに、task を複数の parallel requests に分割できます。各 request は、specialized criteria を使って single material type に対する part の suitability を評価することに集中します。

仕組みは次のとおりです。

1. 同じ image を Claude に同時に複数回送る
2. 各 request には 1 つの material に対する specialized criteria（metal criteria、polymer criteria、ceramic criteria など）を含める
3. Claude は各 material に対する part の suitability を独立して評価する
4. すべての analysis results を集め、final aggregation step に渡す

最後の step では、すべての individual analysis results を Claude に送り返し、それらを比較して final material recommendation を行うよう依頼します。

#### Parallelization Workflows の仕組み

parallelization pattern は単純な構造に従います。

- single task を multiple sub-tasks に分割する - complex decision を focused で specialized な evaluations に分解する
- sub-tasks を parallel に実行する - すべての evaluations を同時に実行して processing を速くする
- results をまとめて aggregate する - specialized analyses を final decision に結合する
- parallelized sub-tasks は identical である必要はない - それぞれ specialized prompt、set of tools、または evaluation criteria を持てる

#### この Approach の利点

Parallelization workflows には、いくつかの重要な advantages があります。

- Focused attention: Claude は複数の competing considerations を同時にバランスさせようとするのではなく、一度に 1 つの specific aspect に集中できます。これにより、各 material type に対してより thorough で accurate な analysis が得られます。
- Easier optimization: 各 material evaluation の prompts を独立して改善・テストできます。metal analysis がうまく機能していない場合、他に影響を与えずにその prompt だけを refine できます。
- Better scalability: 評価する新しい materials を追加するのは簡単です。parallel request をもう 1 つ追加するだけです。既存 prompts を書き直したり、新しい criteria が既存のものに干渉するかを心配したりする必要はありません。
- Improved reliability: complex task を分解することで、AI model の cognitive load を減らし、より一貫した reliable results を得られます。

#### Parallelization を使うタイミング

この pattern は、独立した evaluations に分解できる complex decision がある場合にうまく機能します。AI に複数の criteria を考慮させたり、複数の options を比較させたり、異なる domains of expertise に関わる decisions を下させたりする状況を探してください。

鍵は、意味のある形で分離できる tasks を特定することです。各 parallel sub-task は独立して動作でき、final decision に distinct piece of analysis を提供できるべきです。

---

### レッスン 78: Chaining workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287800>  

Open in Claude

Chaining workflows は最初は当たり前に見えるかもしれませんが、Claude を扱うときに出会う最も有用な patterns の 1 つです。この approach は、complex tasks や、Claude が一貫して扱うのに苦労する long prompts を扱うときに特に価値があります。

#### Workflow Chaining とは？

chaining workflow は、大きく複雑な task を、より小さな sequential subtasks に分解します。Claude にすべてを一度に依頼する代わりに、互いに積み上がる focused steps に作業を分割します。

実用例を見てみましょう。videos を自動的に作成して投稿する social media marketing tool を構築しているとします。Claude に巨大な prompt で全部を処理させる代わりに、次のように分解できます。

1. Twitter で related trending topics を見つける
2. 最も interesting な topic を選ぶ（Claude を使用）
3. topic を research する（Claude を使用）
4. short format video 用の script を書く（Claude を使用）
5. AI avatar と text-to-speech を使って video を作成する
6. video を social media に投稿する

#### なぜ 1 つの大きな Prompt ではなく Chain するのか？

Claude tasks をすべて 1 つの prompt にまとめればよいのでは、と思うかもしれません。主な利点は focus です。Claude に一度に 1 つの specific task を与えると、複数の requirements を同時に処理するのではなく、その task をうまく行うことに集中できます。

chaining approach には、いくつかの advantages があります。

- large tasks を smaller, non-parallelizable subtasks に分割する
- 各 task の間で optional に non-LLM processing を行う
- Claude を overall task の 1 つの aspect に集中させる

#### Long Prompt Problem

ここで chaining が本当に価値を持ちます。Claude に多くの specific constraints を満たす content を書かせる必要がある状況によく出会います。technical article を Claude に書かせたいとして、次の条件を指定するとしましょう。

- AI によって書かれたことに言及しない
- emojis を使わない
- 陳腐または過度に casual な language を避ける
- professional で technical な tone で書く

これらすべての constraints を明確に述べても、Claude は依然として一部の rules に違反する content を生成するかもしれません。emojis を使ったり、AI authorship に触れたり、unprofessional に聞こえたりする article が返ってくる可能性があります。

#### Chaining Solution

1 つの巨大な prompt と格闘する代わりに、2-step chaining approach を使います。

1. Step 1: initial prompt を送り、最初の result が完璧でない可能性を受け入れます。Claude は article を生成しますが、一部の constraints に違反しているかもしれません。
2. Step 2: 問題修正に specifically focused した follow-up request を行います。Claude が書いた article を提供し、targeted revision instructions を与えます。

```
Revise the article provided below. Follow these steps to rewrite the article: 1. Identify any location where the text identifies the author as an AI and remove them 2. Find and remove all emojis 3. Locate any cringey writing and replace it with text that would be written by a technical writer
```

この approach が機能するのは、Claude が content creation と constraint adherence のバランスを取ろうとするのではなく、revision task のみに完全に集中できるからです。

#### Chaining を使うタイミング

Chaining workflows は、特に次のような場合に有用です。

- 複数の requirements を持つ complex tasks がある
- long prompts で Claude が一部の constraints を一貫して無視する
- steps の間で outputs を process または validate する必要がある
- 各 interaction を focused で manageable に保ちたい

chaining は余分な作業のように見えるかもしれませんが、多くの場合、すべてを 1 つの prompt に詰め込むよりも良い results を生みます。鍵は、task が focused sequential steps に分解する価値があるほど complex であるタイミングを見極めることです。

---

### レッスン 79: Routing workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287801>  

Open in Claude

Routing workflows は、AI applications における一般的な問題を解決します。つまり、異なる種類の user requests には異なる handling approaches が必要だという問題です。one-size-fits-all prompt を使う代わりに、incoming requests を分類し、specialized processing pipelines に route できます。

#### Generic Prompts の問題

user topics から video scripts を生成する social media marketing tool を考えてみましょう。ユーザーは topic として "programming" や "surfing" を入力するかもしれませんが、これらは非常に異なる types of content を生成すべきです。

Programming topics には、明確な explanations と definitions を含む educational content が求められます。Surfing topics には、excitement と visual appeal を強調する entertainment-focused scripts の方が合います。single generic prompt では、両方を効果的に扱えません。

#### Content Categories の設定

最初の step は、アプリケーションが生成する必要があるかもしれない異なる types of content を定義することです。requests を次のような genres に分類できます。

- Entertainment - High-energy で culturally relevant な content、trendy language を含む
- Educational - relatable examples を使った明確で engaging な explanations
- Comedy - clever observations と timing を持つ sharp で unexpected な content
- Personal vlog - conversational storytelling を持つ authentic で intimate な content
- Reviews - strengths and weaknesses を強調する decisive で experience-based な content
- Storytelling - vivid details と emotional connection を使う immersive な content

各 category には専用の prompt template を用意します。たとえば educational prompt では、Claude に「relatable examples と thought-provoking questions を使って complex information を digestible insights に変える、clear で engaging な script」を作成するよう求めるかもしれません。

#### Routing の実際の仕組み

routing process は 2 steps で行われます。

1. Categorization - ユーザーの topic を Claude に送り、predefined genres の 1 つに分類するよう依頼する
2. Specialized Processing - category result を使って適切な prompt template を選択し、content を生成する

たとえば、ユーザーが topic として "Python functions" を入力した場合、まず Claude に分類を依頼します。

```
Categorize the topic of a video into one of the listed categories:
<topic>Python functions</topic>

<categories>
- Educational
- Entertainment
- Comedy
- Personal vlog
- Reviews
- Storytelling
</categories>
```

Claude は "Educational" と応答するので、次に educational prompt template を使って実際の script content を生成します。

#### Routing Workflow Architecture

routing workflow は次の pattern に従います。

- User input はまず router component に送られる
- router は最初の Claude call を使って request を categorize する
- category に基づいて、input は 1 つの specific processing pipeline に forwarded される
- 各 pipeline は、その category に optimized された独自の workflow、prompts、tools を持てる

重要なポイントは、user input がすべての pipelines ではなく、1 つの specialized pipeline にだけ送られることです。これにより、各 pipeline を specific use case に対して高度に optimized できます。

#### Routing を使うタイミング

Routing workflows は、次のような場合にうまく機能します。

- アプリケーションが、異なる approaches を必要とする多様な types of requests を扱う
- use cases をカバーする categories を明確に定義できる
- categorization step を Claude が reliably に処理できる
- specialized processing の performance benefit が routing step の overhead を上回る

この pattern は、customer service bots、content generation tools、そして「正しい」response が request type の理解に大きく依存するあらゆる application で特に価値があります。

---

### レッスン 80: Agents and tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287803>  

Open in Claude

Agents は、これまで扱ってきた structured workflows からの転換を表します。workflows は、task を完了するために必要な exact steps が分かっている場合に最適ですが、agents はその steps が何であるべきか分からない場合に力を発揮します。rigid sequence を定義する代わりに、Claude に goal と tools の集合を与え、その tools を組み合わせて objective を達成する方法を Claude に考えさせます。

この flexibility により、agents は多様で予測不能な tasks を扱う必要がある applications の構築に魅力的です。agent を一度作成し、reasonably well に動作することを確認すれば、幅広い problems を解決するために deploy できます。ただし、この flexibility には reliability と cost の trade-offs が伴います。これについては後で詳しく見ます。

#### Tools が Agent を作る仕組み

agents の本当の力は、simple tools を予想外の ways で組み合わせられる能力にあります。基本的な datetime tools のセットを考えてみましょう。

- get_current_datetime - current date and time を取得する
- add_duration_to_datetime - 指定された date に time を追加する
- set_reminder - specific time の reminder を作成する

これらの tools は個別には単純に見えますが、Claude はそれらを連鎖させて、驚くほど complex な requests を処理できます。

「What's the time?」に対しては、Claude は単に get_current_datetime を呼び出します。しかし「What day of the week is it in 11 days?」に対しては、get_current_datetime に続けて add_duration_to_datetime を呼び出します。来週水曜日に gym reminder を設定する場合は、3 つすべての tools を順番に使うかもしれません。

Claude は、より多くの情報が必要な場合も認識できます。「When does my 90-day warranty expire?」と尋ねると、expiration date を計算する前に、いつ商品を購入したかを尋ねる必要があると分かります。

#### Tools は Abstract であるべき

効果的な agents を構築するための重要なポイントは、hyper-specialized なものではなく、reasonably abstract な tools を提供することです。Claude Code はこの principle を完璧に示しています。

Claude Code は、次のような generic で flexible な tools にアクセスできます。

- bash - 任意の command を実行する
- read - 任意の file を読む
- write - 任意の file を作成する
- edit - files を変更する
- glob - files を見つける
- grep - file contents を検索する

注目すべきことに、"refactor code" や "install dependencies" のような specialized tools はありません。その代わり、Claude はこれらの basic tools を使って complex tasks を達成する方法を考えます。この abstraction により、developers が明示的に計画していなかった無数の programming scenarios に対応できます。

#### Best Practice: Combinable Tools

agents を設計するときは、Claude が creative ways で組み合わせられる tools を提供してください。たとえば、social media video agent には次のものを含められます。

- bash - video processing のために FFMPEG にアクセスする
- generate_image - prompts から images を作成する
- text_to_speech - text を audio に変換する
- post_media - content を social platforms に upload する

この tool set により、simple workflows（video を作成して投稿する）と、agent がまず sample image を生成し、user approval を得てから video creation に進むような、より interactive experiences の両方が可能になります。

agent は user feedback and preferences に基づいて approach を適応できます。これは rigid workflow では実現が難しいものです。この flexibility こそが、dynamic で user-responsive な applications を構築するうえで agents を強力にしているものです。

---

### レッスン 81: Environment inspection

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287798>  

Open in Claude

AI agents を構築するとき、見落とされがちな重要概念が 1 つあります。それが environment inspection です。Claude は盲目的に動作します。効果的に働くには、自分の actions の results を observe し、understand できる必要があります。

#### Environment Inspection が重要な理由

Claude が computer use とどのように動作するかを考えてみてください。Claude が text を入力したり button をクリックしたりするたびに、何が起こったかを理解するためにすぐ screenshot を受け取ります。これは単なる便利機能ではなく、essential です。

Claude の視点では、button をクリックすると new page に移動するかもしれませんし、menu が開くかもしれませんし、他にもさまざまな changes が起こる可能性があります。results を見ることができなければ、Claude には action が成功したか、environment の new state がどのようなものかを理解する方法がありません。

#### Writing の前に Reading

同じ principle は file operations にも当てはまります。Claude が file を変更する前に、current contents を理解する必要があります。これは obvious に思えるかもしれませんが、agents を構築するときに常に従うべき pattern です。

上の例では、Python file に new route を追加するよう依頼されたとき、Claude はまず existing code を読み、current structure を理解します。その後で初めて、existing functionality を壊さずに request された変更を安全に行えます。

#### Environment Inspection のための System Prompts

system prompts を通じて、Claude に environment を inspect するよう導けます。video generation のような complex tasks では、これは特に重要になります。

次のことを行う必要がある video creation agent を考えてみましょう。

- FFmpeg のような tools を使って video content を生成する
- audio dialogue が正しく配置されていることを確認する
- visual elements が期待どおりに表示されていることを確認する

system prompt instructions に次のような内容を含めるかもしれません。

- Use the bash tool to run whisper.cpp and generate caption files with timestamps to verify dialogue placement
- Use FFmpeg to extract screenshots from the video at regular intervals to visually inspect the output
- Compare the generated content against the original requirements

#### Environment Inspection の利点

Claude が environment を inspect できると、いくつかの点が改善します。

- Better progress tracking - Claude は task completion にどれだけ近づいているかを判断できる
- Error handling - unexpected results を検出し、修正できる
- Quality assurance - task を完了とみなす前に output を verify できる
- Adaptive behavior - 観察した内容に基づいて approach を調整できる

#### Practical Implementation

自分自身の agents を設計するときは、常に「Claude はこの action がうまくいったことをどうやって知るのか？」と問いかけてください。files、APIs、user interfaces のどれを扱う場合でも、Claude が自分の actions の results を observe できる tools and instructions を提供します。

これは次のようなことを意味します。

- modifications の前に file contents を読む
- UI interactions の後に screenshots を撮る
- expected data があるか API responses を確認する
- generated content を requirements に照らして validate する

Environment inspection は、Claude を blind executor of commands から、自分の working environment を本当に理解し適応できる agent へと変えます。

---

### レッスン 82: Workflows vs agents

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287794>  

Open in Claude

AI-powered applications を構築するとき、2 つの異なる architectural approaches、workflows と agents のどちらを選ぶかが必要になることがよくあります。それぞれに明確な advantages と trade-offs があり、異なる scenarios に適しています。

#### Workflows とは？

Workflows は、既知の problem または problems の集合を解くために設計された、Claude への predefined series of calls です。steps の flow を事前に思い描ける場合、つまり task を完了するために必要な exact sequence が分かっている場合に workflows を使います。

workflows は、大きな task をはるかに小さく specific な subtasks に分解するものだと考えてください。各 step は単一の area に集中するため、Claude はより precise に作業できます。

#### Agents とは？

agents では、Claude に basic tools の集合が与えられ、それらの tools を使って task を完了する plan を組み立てることが期待されます。workflows と異なり、どのような tasks が提供されるか正確には分からないため、system はより adaptive である必要があります。

Agents は、tools を予想外の ways で組み合わせることで、多種多様な challenges の扱い方を creative に考え出せます。

#### Workflows の利点

- Claude は一度に 1 つの subtask に集中でき、一般に higher accuracy につながる
- 各 exact step が分かっているため、evaluate and test がはるかに簡単
- より predictable and reliable な execution
- specific で well-defined な problems の解決により適している

#### Agents の利点

- より flexible な user experience を可能にする
- はるかに flexible な task completion - Claude は tools を予想外の ways で組み合わせ、多種多様な tasks を完了できる
- development 中に予測されなかった novel situations を扱える
- 必要に応じて users に additional input を求められる

#### Workflows の欠点

- はるかに less flexible - specific types of tasks の解決に専用化される
- 一般により constrained な user experience - flow への exact inputs を知っている必要がある
- より多くの upfront planning and design work が必要

#### Agents の欠点

- workflows と比べて successful task completion rate が低い
- agent がどの series of steps を実行するか分からないことが多いため、instrument、test、evaluate がより難しい
- behavior の予測可能性が低い

#### 各 Approach を使うタイミング

engineer としての主な goal は、problems を reliably に解決することです。users は、おそらくあなたが fancy agent を作ったことには関心がありません。彼らは一貫して動く product を求めています。

一般的な recommendation は、可能な限り workflows の実装に集中し、本当に必要な場合にのみ agents に頼ることです。Workflows はほとんどの production applications が必要とする reliability and predictability を提供します。一方 agents は、exact requirements を事前に決められない scenarios に対して flexibility を提供します。

well-defined processes がある場合は workflows を検討し、creative problem-solving を必要とする unpredictable で varied な user requests を扱う必要がある場合は agents を検討してください。

---

### レッスン 83: Quiz on Agents and Workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289130>  

Open in Claude
Loading...

---

### レッスン 84: Final Assessment

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/290899>  

Open in Claude
Loading...

---

### レッスン 85: Course Wrap Up

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287802>  

Open in Claude

---
