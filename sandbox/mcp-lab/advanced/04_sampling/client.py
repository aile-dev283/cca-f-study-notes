"""
MCP Advanced 04: Sampling クライアント側

sampling_callback を実装し ClientSession に渡す。
サーバーから create_message リクエストが来たら Anthropic SDK で Claude を呼び出す。
"""

import asyncio
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import (
    CreateMessageResult,
    TextContent,
    RequestContext,
    CreateMessageRequestParams,
)

load_dotenv(Path(__file__).resolve().parents[3] / ".env")
sdk_client = anthropic.Anthropic()
SERVER_PATH = Path(__file__).resolve().parent / "server.py"


async def sampling_callback(
    context: RequestContext,
    params: CreateMessageRequestParams,
) -> CreateMessageResult:
    """
    サーバーの create_message リクエストを Anthropic SDK で処理する。
    このコールバックがあることで、サーバーは API キーを必要としない。
    """
    messages = [
        {"role": m.role, "content": m.content.text}
        for m in params.messages
        if hasattr(m.content, "text")
    ]

    response = sdk_client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=params.maxTokens or 512,
        system=params.systemPrompt or "",
        messages=messages,
    )

    text = response.content[0].text if response.content else ""
    return CreateMessageResult(
        role="assistant",
        model="claude-haiku-4-5-20251001",
        content=TextContent(type="text", text=text),
    )


async def main() -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        # sampling_callback をセッションに渡す → サーバーの LLM 呼び出しを代行
        async with ClientSession(read, write, sampling_callback=sampling_callback) as session:
            await session.initialize()

            print("=== Sampling Demo ===")
            print("サーバーは LLM を直接呼ばない。クライアントの sampling_callback に委譲する。\n")

            text_to_summarize = (
                "The Model Context Protocol (MCP) Sampling feature allows MCP servers to "
                "request language model completions through the connected client, rather than "
                "calling the LLM API directly. This design has several benefits: the server "
                "does not need its own API key, the cost of LLM inference is borne by the "
                "client (the user), and it enables public MCP servers where the operator "
                "should not subsidize each user's AI usage. The server sends a "
                "create_message request to the client, which then calls its own LLM "
                "(Claude in this case) and returns the result back to the server."
            )

            print(f"Input text ({len(text_to_summarize)} chars):\n{text_to_summarize}\n")

            result = await session.call_tool("summarize_text", {"text": text_to_summarize})
            print("Summary (generated via Sampling):")
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
