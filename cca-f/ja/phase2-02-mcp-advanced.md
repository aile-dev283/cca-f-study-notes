<!-- markdownlint-disable -->

# Model Context Protocol: Advanced Topics

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics>  
**所要時間:** 未記載  
**対象ドメイン:** D2  
**フェーズ:** Phase 2  

---

## カリキュラム

### レッスン 01: Let's get started

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349>  

Open in Claude
0 seconds of 1 minute, 28 secondsVolume 90%

---

### レッスン 02: Sampling

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296288>  

Open in Claude

Sampling（サンプリング）は、サーバーが接続済みの MCP クライアントを通じて Claude のような言語モデルにアクセスできるようにする仕組みである。サーバーが直接 Claude を呼び出すのではなく、自分の代わりにクライアントへ呼び出しを依頼する。これにより、テキスト生成の責任とコストがサーバーからクライアントへ移される。

Sampling が解決する問題

Wikipedia から情報を取得する research ツールを備えた MCP サーバーがあると想像してほしい。データをすべて収集した後、それらをまとまりのあるレポートへと要約する必要がある。選択肢は 2 つある。

選択肢 1: MCP サーバーに Claude への直接アクセスを与える。サーバーは自前の API キーを持ち、認証を処理し、コストを管理し、Claude 連携のためのコードをすべて実装する必要がある。これでも動作はするが、大きな複雑さが加わる。

選択肢 2: Sampling を使う。サーバーはプロンプトを生成し、クライアントに「私の代わりに Claude を呼び出してもらえますか?」と依頼する。すでに Claude への接続を持っているクライアントが呼び出しを行い、結果を返す。

Sampling の仕組み

フローは単純である。

サーバーが作業を完了する（Wikipedia の記事を取得するなど）
サーバーがテキスト生成を求めるプロンプトを作成する
サーバーがクライアントへサンプリングリクエストを送る
クライアントが渡されたプロンプトで Claude を呼び出す
クライアントが生成されたテキストをサーバーへ返す
サーバーが生成されたテキストをレスポンスの中で利用する
Sampling の利点
サーバーの複雑さを軽減する: サーバーが言語モデルと直接連携する必要がない
コスト負担を移す: トークン使用料を支払うのはサーバーではなくクライアント
API キーが不要: サーバーは Claude 用の認証情報を持つ必要がない
公開サーバーに最適: 公開サーバーが全ユーザー分の AI コストを抱え込むのは避けたい
実装

Sampling のセットアップには、両側でのコードが必要である。

サーバー側

ツール関数の中で、create_message 関数を使ってテキスト生成をリクエストする。

@mcp.tool()
async def summarize(text_to_summarize: str, ctx: Context):
prompt = f"""
Please summarize the following text:
{text_to_summarize}
"""

result = await ctx.session.create_message(
messages=[
SamplingMessage(
role="user",
content=TextContent(
type="text",
text=prompt
)
)
],
max_tokens=4000,
system_prompt="You are a helpful research assistant",
)

if result.content.type == "text":
return result.content.text
else:
raise ValueError("Sampling failed")
クライアント側

サーバーのリクエストを処理するサンプリングコールバックを作成する。

async def sampling_callback(
context: RequestContext, params: CreateMessageRequestParams
):

# Call Claude using the Anthropic SDK

text = await chat(params.messages)

return CreateMessageResult(
role="assistant",
model=model,
content=TextContent(type="text", text=text),
)

そして、クライアントセッションを初期化する際にこのコールバックを渡す。

async with ClientSession(
read,
write,
sampling_callback=sampling_callback
) as session:
await session.initialize()
Sampling を使うべきとき

Sampling は、一般公開される MCP サーバーを構築するときに最も価値を発揮する。見知らぬユーザーが自分の負担で無制限にテキストを生成するような事態は避けたい。Sampling を使えば、各クライアントが自分の AI 利用料を支払いつつ、サーバーの機能の恩恵を受けられる。

この手法は本質的に、AI 連携の複雑さをサーバーからクライアントへと移すものであり、クライアント側にはすでに必要な接続と認証情報が整っていることが多い。

---

### レッスン 03: Sampling walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172>  

Open in Claude
← Previous
Next →
Downloads
sampling.zip
(opens in new tab)

---

### レッスン 04: Log and progress notifications

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284>  

Open in Claude

ログ通知と進捗通知は実装が簡単だが、MCP サーバーを扱う際のユーザー体験に大きな違いをもたらす。これらは、長時間かかる処理の最中に何が起きているのかをユーザーに伝え、「何か壊れたのでは?」と不安にさせないようにする。

トピックの調査やデータ処理など、完了に時間のかかるツールを Claude が呼び出すと、ユーザーは処理が終わるまで通常は何も見えない。ツールが動いているのか止まってしまったのか分からず、もどかしい思いをすることになる。

ログ通知と進捗通知を有効にすると、ユーザーは裏側で何が起きているかをリアルタイムのフィードバックとして受け取れる。処理が進むにつれて、プログレスバー、ステータスメッセージ、詳細なログが見られる。

仕組み

Python の MCP SDK では、ログ通知と進捗通知は、ツール関数に自動的に渡される Context 引数を通じて機能する。この context オブジェクトは、実行中にクライアントへ情報を返すためのメソッドを提供する。

@mcp.tool(
name="research",
description="Research a given topic"
)
async def research(
topic: str = Field(description="Topic to research"),
*,
context: Context
):
await context.info("About to do research...")
await context.report_progress(20, 100)
sources = await do_research(topic)

await context.info("Writing report...")
await context.report_progress(70, 100)
results = await generate_report(sources)

return results

使用する主なメソッドは次のとおり。

context.info() - クライアントへログメッセージを送る
context.report_progress() - 現在値と総数を指定して進捗を更新する
クライアント側の実装

クライアント側では、これらの通知を処理するコールバック関数をセットアップする必要がある。サーバーがこれらのメッセージを発するが、それをユーザーにどう提示するかはクライアントアプリケーション次第である。

async def logging_callback(params: LoggingMessageNotificationParams):
print(params.data)

async def print_progress_callback(
progress: float, total: float | None, message: str | None
):
if total is not None:
percentage = (progress / total) * 100
print(f"Progress: {progress}/{total} ({percentage:.1f}%)")
else:
print(f"Progress: {progress}")

async def run():
async with stdio_client(server_params) as (read, write):
async with ClientSession(
read,
write,
logging_callback=logging_callback
) as session:
await session.initialize()

await session.call_tool(
name="add",
arguments={"a": 1, "b": 3},
progress_callback=print_progress_callback,
)

ログコールバックはクライアントセッションを作成する際に渡し、進捗コールバックは個々のツール呼び出しの際に渡す。これにより、異なる種類の通知をそれぞれ適切に処理する柔軟性が得られる。

提示方法の選択肢

これらの通知をどう提示するかは、アプリケーションの種類によって異なる。

CLI アプリケーション - メッセージと進捗を単にターミナルへ出力する
Web アプリケーション - WebSocket、Server-Sent Events、ポーリングを使ってブラウザへ更新をプッシュする
デスクトップアプリケーション - UI 内のプログレスバーやステータス表示を更新する

これらの通知の実装は完全に任意である点を忘れないでほしい。完全に無視しても、特定の種類だけ表示しても、自分のアプリケーションに合った形で提示してもよい。これらはあくまで、長時間処理の最中に何が起きているかをユーザーが理解できるようにするためのユーザー体験の向上策にすぎない。

---

### レッスン 05: Notifications walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036>  

Open in Claude
← Previous
Next →
Downloads
notifications.zip
(opens in new tab)

---

### レッスン 06: Roots

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296289>  

Open in Claude

Roots（ルート）は、ローカルマシン上の特定のファイルやフォルダーへのアクセスを MCP サーバーに付与する方法である。「やあ MCP サーバー、これらのファイルにアクセスしていいよ」と告げる権限システムのようなものと考えてよいが、単に権限を付与する以上のことを行う。

Roots が解決する問題

Roots がなければ、よくある問題に直面する。ファイルパスを受け取って MP4 を MOV 形式に変換する動画変換ツールを備えた MCP サーバーがあると想像してほしい。

ユーザーが Claude に「biking.mp4 を mov 形式に変換して」と頼むと、Claude はファイル名だけでツールを呼び出すことになる。だがここに問題がある。Claude には、そのファイルが実際にどこにあるのかをファイルシステム全体から探す手段がない。

ファイルシステムは複雑で、さまざまなディレクトリにファイルが散在しているかもしれない。ユーザーは biking.mp4 が自分の Movies フォルダーにあると分かっているが、Claude にはその文脈がない。

ユーザーに常にフルパスを入力させればこれを解決できるが、それはあまりユーザーフレンドリーではない。毎回完全なファイルパスを打ち込みたい人などいない。

Roots の実際の動作

Roots を使うとワークフローはこう変わる。

ユーザーが動画ファイルの変換を依頼する
Claude が list_roots を呼び出し、アクセスできるディレクトリを確認する
Claude がアクセス可能なディレクトリに対して read_dir を呼び出し、ファイルを探す
見つかったら、Claude がフルパスを使って変換ツールを呼び出す

これは自動的に行われ、ユーザーはフルパスを指定せず「biking.mp4 を変換して」と言うだけでよい。

セキュリティと境界

Roots はアクセスを制限することでセキュリティももたらす。Desktop フォルダーへのアクセスのみを付与すれば、MCP サーバーは Documents や Downloads など他の場所のファイルにはアクセスできない。

承認されたルートの外にあるファイルへ Claude がアクセスしようとするとエラーになり、現在のサーバー構成ではそのファイルにアクセスできないことをユーザーに伝えられる。

実装の詳細

MCP SDK はルート制限を自動的に強制するわけではない。これは自分で実装する必要がある。典型的なパターンは、次のような is_path_allowed() というヘルパー関数を作ることである。

要求されたファイルパスを受け取る
承認済みのルートのリストを取得する
要求されたパスがそれらのルートのいずれかの内側にあるかをチェックする
アクセス可否として true/false を返す

そして、ファイルやディレクトリにアクセスするツールでは、実際のファイル操作を行う前にこの関数を呼び出す。

主な利点
ユーザーフレンドリー - ユーザーがフルパスを指定する必要がない
絞り込まれた検索 - Claude は承認されたディレクトリ内のみを探すため、ファイルの発見が速くなる
セキュリティ - 承認領域外の機密ファイルへの偶発的なアクセスを防ぐ
柔軟性 - ルートはツールを通じて提供することも、プロンプトへ直接注入することもできる

Roots は、Claude がファイルを見つけるために必要な文脈を与えつつ、アクセスできる範囲に明確な境界を保つことで、MCP サーバーをより強力かつより安全にする。

---

### レッスン 07: Roots walkthrough

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839>  

Open in Claude
← Previous
Next →
Downloads
roots.zip
(opens in new tab)

---

### レッスン 08: Survey

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/297276>  

Open in Claude
Loading...

---

### レッスン 09: JSON message types

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296290>  

Open in Claude

MCP（Model Context Protocol）は、クライアントとサーバー間の通信を扱うために JSON メッセージを使う。これらのメッセージタイプを理解することは、特に streamable HTTP transport のような異なるトランスポート方式を扱う際に、MCP を使いこなすうえで極めて重要である。

メッセージ形式

MCP の通信はすべて JSON メッセージを通じて行われる。各メッセージタイプは、ツールの呼び出し、利用可能なリソースの一覧表示、システムイベントの通知など、特定の目的を担っている。

典型的な例を示す。Claude が MCP サーバーの提供するツールを呼び出す必要があるとき、クライアントは「Call Tool Request」メッセージを送る。サーバーはこのリクエストを処理し、ツールを実行し、その出力を含む「Call Tool Result」メッセージで応答する。

MCP 仕様

メッセージタイプの完全なリストは、GitHub 上の公式 MCP 仕様リポジトリで定義されている。この仕様は各種 SDK リポジトリ（Python や TypeScript の SDK など）とは別物であり、MCP がどう動作すべきかについての権威ある情報源として機能する。

メッセージタイプは便宜上 TypeScript で記述されているが、これは TypeScript コードとして実行されるからではなく、TypeScript がデータ構造と型を明確に記述する手段を提供してくれるからである。

メッセージのカテゴリ

MCP のメッセージは主に 2 つのカテゴリに分かれる。

リクエスト・リザルト型メッセージ

これらのメッセージは常にペアで現れる。リクエストを送ると、リザルトが返ってくることを期待する。

Call Tool Request → Call Tool Result
List Prompts Request → List Prompts Result
Read Resource Request → Read Resource Result
Initialize Request → Initialize Result
通知メッセージ

これらは一方向のメッセージで、イベントを知らせるが応答を必要としない。

Progress Notification - 長時間処理に関する更新
Logging Message Notification - システムのログメッセージ
Tool List Changed Notification - 利用可能なツールが変化したとき
Resource Updated Notification - リソースが変更されたとき
クライアントメッセージ対サーバーメッセージ

MCP 仕様は、メッセージを送り手が誰かによって整理している。

クライアントメッセージには、クライアントがサーバーへ送るリクエスト（ツール呼び出しなど）や、クライアントが送る可能性のある通知が含まれる。

サーバーメッセージには、サーバーがクライアントへ送るリクエストや、サーバーがブロードキャストする通知が含まれる。

なぜこれが重要か

サーバーがクライアントへメッセージを送れるという点を理解しておくことは、異なるトランスポート方式を扱う際に特に重要である。streamable HTTP transport のような一部のトランスポートには、どの種類のメッセージがどの方向に流れられるかについての制約がある。

重要な洞察は、MCP が双方向プロトコルとして設計されているという点である。つまり、クライアントもサーバーも通信を開始できる。これは、自分のユースケースに合った適切なトランスポート方式を選ぶ必要があるときに極めて重要になる。

---

### レッスン 10: The STDIO transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291>  

Open in Claude

MCP のクライアントとサーバーは JSON メッセージを交換して通信するが、それらのメッセージは実際にどのように伝送されるのだろうか。利用される通信路は transport（トランスポート）と呼ばれ、HTTP リクエストや WebSocket、さらには JSON をはがきに書く方法（最後のものは本番利用には推奨されない）まで、実装方法はいくつかある。

Stdio transport

MCP サーバーやクライアントを初めて開発するとき、最もよく使われるトランスポートは stdio transport である。このアプローチは単純で、クライアントが MCP サーバーをサブプロセスとして起動し、標準入力・標準出力ストリームを通じて通信する。

仕組みは次のとおり。

クライアントはサーバーの stdin を使ってサーバーへメッセージを送る
サーバーは stdout に書き込んで応答する
サーバーとクライアントのどちらでも、いつでもメッセージを送れる
クライアントとサーバーが同じマシン上で動作している場合にのみ機能する
Stdio の実際の動作を見る

別個のクライアントを書かなくても、ターミナルから直接 MCP サーバーをテストできる。uv run server.py でサーバーを実行すると、stdin を読み取り stdout に応答を書き込む。つまり、ターミナルに JSON メッセージを直接貼り付けて、サーバーの応答をその場で確認できる。

ターミナルの出力には、初期化やツール呼び出しの例メッセージを含め、メッセージのやり取りの全体が表示される。

MCP 接続シーケンス

すべての MCP 接続は、特定の 3 メッセージのハンドシェイクから始まる必要がある。

Initialize Request - クライアントが最初にこれを送る
Initialize Result - サーバーが capabilities とともに応答する
Initialized Notification - クライアントが確認する（応答は期待されない）

このハンドシェイクの後でなければ、ツール呼び出しやプロンプト一覧などの他のリクエストを送ることはできない。

メッセージタイプとフロー

MCP は双方向に流れるさまざまなメッセージタイプをサポートする。

重要な洞察は、応答を必要とするメッセージ（リクエスト → リザルト）と、必要としないメッセージ（通知）がある、という点である。クライアントとサーバーのどちらも、いつでも通信を開始できる。

4 つの通信シナリオ

どのトランスポートでも、4 つの異なる通信パターンを扱う必要がある。

クライアント → サーバー リクエスト: クライアントが stdin に書き込む
サーバー → クライアント レスポンス: サーバーが stdout に書き込む
サーバー → クライアント リクエスト: サーバーが stdout に書き込む
クライアント → サーバー レスポンス: クライアントが stdin に書き込む

stdio transport の優れた点はそのシンプルさにある。どちらの側も、これら 2 つのチャネルを使っていつでも通信を開始できる。

なぜこれが重要か

stdio transport を理解することは重要である。なぜなら、それは双方向通信がシームレスに行える「理想的な」ケースを表しているからだ。HTTP のような他のトランスポートに移ると、サーバーがクライアントへ常にリクエストを開始できるとは限らないという制約に直面する。stdio transport は、他のトランスポート方式の制約に取り組む前に、完全な MCP 通信がどのようなものかを理解するための基準点となる。

開発とテストには stdio transport が最適である。クライアントとサーバーを別々のマシンで動かす必要がある本番デプロイには、それぞれにトレードオフのある他のトランスポートの選択肢を検討する必要がある。

---

### レッスン 11: The StreamableHTTP transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287>  

Open in Claude

streamable HTTP transport は、MCP クライアントがリモートにホストされたサーバーへ HTTP 接続を通じて接続できるようにする。クライアントとサーバーが同じマシン上にあることを要求する標準入出力（standard I/O）トランスポートとは異なり、このトランスポートは誰でもアクセスできる公開 MCP サーバーの可能性を開く。

ただし重要な注意点がある。一部の設定は MCP サーバーの機能を大きく制限しうる。アプリケーションがローカルの標準入出力トランスポートでは完璧に動くのに、HTTP トランスポートでデプロイすると壊れる場合、これが原因である可能性が高い。

重要となる設定

streamable HTTP transport の挙動を制御する 2 つの主要な設定がある。

stateless_http - 接続状態の管理を制御する
json_response - レスポンス形式の扱いを制御する

デフォルトではどちらの設定も false だが、特定のデプロイシナリオではこれらを true に設定せざるを得ないことがある。これらを有効にすると、進捗通知、ログ、サーバー起点のリクエストといった中核機能が壊れる可能性がある。

HTTP 通信の課題

これらの制約がなぜ存在するのかを理解するには、HTTP 通信の仕組みを振り返る必要がある。標準的な HTTP では次のとおり。

クライアントはサーバーへ簡単にリクエストを開始できる（サーバーには既知の URL がある）
サーバーはこれらのリクエストに簡単に応答できる
サーバーはクライアントへ簡単にはリクエストを開始できない（クライアントには既知の URL がない）
クライアントからサーバーへ戻すレスポンスのパターンが問題になる

影響を受ける MCP メッセージタイプ

この HTTP の制約は、特定の MCP 通信パターンに影響する。次のメッセージタイプは、素の HTTP では実装が難しくなる。

サーバー起点のリクエスト: Create Message リクエスト、List Roots リクエスト
通知: Progress 通知、Logging 通知、Initialized 通知、Cancelled 通知

これらはまさに、制約的な HTTP 設定を有効にしたときに壊れる機能である。プログレスバーが消え、ログが機能しなくなり、サーバー起点のサンプリングリクエストが失敗する。

Streamable HTTP の解決策

streamable HTTP transport は HTTP の制約を回避する巧妙な解決策を提供するが、トレードオフを伴う。stateless_http=True や json_response=True を使わざるを得ない場合、本質的にはトランスポートに対して、制約を回避するのではなく HTTP の制約の中で動作するよう指示していることになる。

これらの制約を理解しておくと、次のような点について十分な情報に基づいた判断ができる。

デプロイシナリオごとにどのトランスポートを使うか
HTTP の制約を優雅に処理するために MCP サーバーをどう設計するか
リモートホスティングの利点のために、いつ機能の低下を受け入れるか

鍵となるのは、これらの制約が存在することを知り、それに応じて MCP サーバーのアーキテクチャを計画することである。アプリケーションがサーバー起点のリクエストやリアルタイム通知に大きく依存している場合、トランスポートの選択を見直すか、代替の通信パターンを実装する必要があるかもしれない。

---

### レッスン 12: StreamableHTTP in depth

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286>  

Open in Claude

StreamableHTTP は、ある根本的な問題に対する MCP の解決策である。一部の MCP 機能はサーバーがクライアントへリクエストを行うことを必要とするが、HTTP はこれを難しくする。StreamableHTTP がどのようにこの制約を回避するか、そしてその回避策を破らざるを得なくなるのはどんなときかを見ていこう。

中核的な問題

サンプリング、通知、ログのような一部の MCP 機能は、サーバーがクライアントへリクエストを開始することに依存している。しかし HTTP は、クライアントがサーバーへリクエストを行うように設計されており、その逆向きではない。StreamableHTTP は、Server-Sent Events（SSE）を使った巧妙な回避策でこれを解決する。

StreamableHTTP の仕組み

その仕掛けは、クライアントとサーバーの間に永続的な接続を確立する複数ステップのプロセスを通じて実現される。

初期接続のセットアップ

プロセスは、どの MCP 接続とも同じように始まる。

クライアントがサーバーへ Initialize Request を送る
サーバーが特別な mcp-session-id ヘッダーを含む Initialize Result を返す
クライアントがそのセッション ID を付けて Initialized Notification を送る

このセッション ID は極めて重要で、クライアントを一意に識別し、以降のすべてのリクエストに含めなければならない。

SSE による回避策

初期化の後、クライアントは GET リクエストを行って Server-Sent Events 接続を確立できる。これにより、サーバーがいつでもメッセージをクライアントへストリーミングするために使える、長寿命の HTTP レスポンスが作られる。

この SSE 接続が、サーバーからクライアントへの通信を可能にする鍵である。サーバーはこの永続的なチャネルを通じて、リクエストや通知などのメッセージを送れるようになる。

ツール呼び出しと 2 つの SSE 接続

クライアントがツール呼び出しを行うと、事態はより複雑になる。システムは 2 つの別個の SSE 接続を作成する。

プライマリ SSE 接続: サーバー起点のリクエストに使われ、無期限に開いたままになる
ツール固有の SSE 接続: 各ツール呼び出しごとに作成され、ツールの結果が送られると自動的に閉じる
メッセージのルーティング

異なる種類のメッセージは、それぞれ異なる接続を通じてルーティングされる。

進捗通知: プライマリ SSE 接続を通じて送られる
ログメッセージとツールの結果: ツール固有の SSE 接続を通じて送られる

回避策を破る構成フラグ

StreamableHTTP には 2 つの重要な構成オプションがある。

stateless_http
json_response

これらを True に設定すると、SSE による回避策の仕組みが壊れることがある。特定のシナリオではこれらのフラグを有効にしたくなるかもしれないが、そうするとサーバーからクライアントへの通信に依存する完全な MCP 機能が制限される。

重要なポイント

StreamableHTTP は HTTP の制約を回避しなければならないため、他の MCP トランスポートよりも複雑である。SSE ベースの回避策は HTTP 上での完全な MCP 機能を可能にするが、デバッグや最適化のためには 2 接続モデルを理解しておくことが極めて重要である。

StreamableHTTP で MCP アプリケーションを構築する際は、初期化後のすべてのリクエストにセッション ID が必要であること、そしてシステムが複数の SSE 接続を自動的に管理して、さまざまな種類のサーバーからクライアントへの通信を扱うことを忘れないでほしい。

---

### レッスン 13: State and the StreamableHTTP transport

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285>  

Open in Claude

MCP サーバーの stateless_http フラグと json_response フラグは、サーバーの振る舞いの根本的な側面を制御する。これらをいつ、なぜ使うのかを理解することは、特にサーバーをスケールさせたり本番環境にデプロイしたりする予定がある場合に極めて重要である。

Stateless HTTP が必要になるとき

人気が出た MCP サーバーを構築したと想像してほしい。最初は、単一のサーバーインスタンスにわずかなクライアントが接続するだけかもしれない。

サーバーが成長すると、何千ものクライアントが接続しようとするかもしれない。単一のサーバーインスタンスでは、そのトラフィックをすべて捌くようにはスケールしない。

典型的な解決策は水平スケーリング、すなわちロードバランサーの背後で複数のサーバーインスタンスを動かすことである。

しかし、ここで話が複雑になる。MCP クライアントには 2 つの別個の接続が必要であることを思い出してほしい。

サーバーからクライアントへのリクエストを受け取るための GET SSE 接続
ツールを呼び出して応答を受け取るための POST リクエスト

ロードバランサーがあると、これらのリクエストは異なるサーバーインスタンスへルーティングされるかもしれない。ツールが（サンプリングを通じて）Claude を使う必要がある場合、POST リクエストを処理するサーバーは、GET SSE 接続を処理するサーバーと連携しなければならない。これはサーバー間の複雑な連携問題を生む。

Stateless HTTP がこれをどう解決するか

stateless_http=True を設定するとこの連携問題は解消されるが、大きなトレードオフを伴う。

ステートレス HTTP を有効にすると次のようになる。

クライアントはセッション ID を受け取らない - サーバーは個々のクライアントを追跡できない
サーバーからクライアントへのリクエストがない - GET SSE 経路が利用不能になる
サンプリングがない - Claude や他の AI モデルを使えない
進捗レポートがない - 長時間処理中に進捗更新を送れない
サブスクリプションがない - リソース更新をクライアントへ通知できない

ただし利点が 1 つある。クライアントの初期化がもはや必須でなくなる。クライアントは最初のハンドシェイク処理なしに直接リクエストを行える。

JSON Response を理解する

json_response=True フラグはより単純で、POST リクエストのレスポンスについてストリーミングを無効にするだけである。ツールの実行に伴って複数の SSE メッセージを受け取る代わりに、最終結果のみをプレーンな JSON として受け取る。

ストリーミングを無効にすると次のようになる。

途中の進捗メッセージがない
実行中のログ出力がない
最終的なツール結果のみ
これらのフラグを使うべきとき

ステートレス HTTP を使うのは次の場合。

ロードバランサーを用いた水平スケーリングが必要
サーバーからクライアントへの通信が不要
ツールが AI モデルのサンプリングを必要としない
接続のオーバーヘッドを最小化したい

JSON レスポンスを使うのは次の場合。

ストリーミングレスポンスが不要
よりシンプルな非ストリーミングの HTTP レスポンスを好む
プレーンな JSON を期待するシステムと連携している
開発環境対本番環境

ローカルでは標準入出力トランスポートで開発しているが、本番では HTTP トランスポートでデプロイする予定がある場合は、本番で使うのと同じトランスポートでテストすること。ステートフルモードとステートレスモードの挙動の違いは大きくなりうるので、デプロイ後ではなく開発中に問題を見つけるほうがよい。

これらのフラグは MCP サーバーの動作方法を根本的に変えるので、自分の具体的なスケーリングと機能の要件に基づいて選択すること。

Downloads
transport-http.zip
(opens in new tab)

---

### レッスン 14: Assessment on MCP concepts

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301>  

Open in Claude
Loading...

---

### レッスン 15: Wrapping up

**URL:** <https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296350>  

Open in Claude
0 seconds of 48 secondsVolume 90%

---
