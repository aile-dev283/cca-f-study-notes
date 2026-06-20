"""
MCP Advanced 04: Sampling プリミティブ（サーバー側）

Sampling = サーバーが LLM を直接呼ばず、クライアントに LLM 呼び出しを委譲する。

なぜ重要か（D2 試験頻出）:
  - サーバーが API キーを持たなくてよい
  - LLM コストはクライアント（ユーザー）が負担する
  - 公開 MCP サーバーに最適（サーバー運営者が全ユーザー分のコストを持たない）

フロー:
  client.call_tool("summarize_text", ...) →
  server: ctx.session.create_message(...) →  ← Sampling リクエスト
  client: sampling_callback で Claude を呼び出す →
  server: LLM の回答を受け取り tool の戻り値として返す
"""

import asyncio
from mcp.server.fastmcp import FastMCP
from mcp.types import Context, SamplingMessage, TextContent
from pydantic import Field

mcp = FastMCP("SamplingDemo")


@mcp.tool(
    name="summarize_text",
    description=(
        "Summarizes the given text using the client's language model via Sampling. "
        "The server does NOT call the LLM directly — it delegates to the client."
    ),
)
async def summarize_text(
    text: str = Field(description="Text to summarize (any length)"),
    ctx: Context = None,
) -> str:
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(
                    type="text",
                    text=f"Summarize the following text in 2-3 sentences:\n\n{text}",
                ),
            )
        ],
        max_tokens=512,
        system_prompt=(
            "You are a concise technical writer. "
            "Summarize clearly and accurately without adding opinions."
        ),
    )

    if result.content.type == "text":
        return result.content.text
    raise ValueError(f"Unexpected sampling result content type: {result.content.type}")


if __name__ == "__main__":
    mcp.run()
