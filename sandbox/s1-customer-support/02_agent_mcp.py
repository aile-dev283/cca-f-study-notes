"""
S1 Step2: MCP 経由エージェント（mcp-lab/basic/01_tools/server.py を使用）

学習ポイント (D1+D2):
- MCP ツール定義 → Anthropic API 形式に変換する必要がある（mcp_tool_to_anthropic）
- ツール呼び出しは session.call_tool() → MCP サーバーが実行
- エージェントループ本体は 01_agent_basic.py と同じ

→ 01_agent_basic.py と対比:
  * ツール定義が inline（Pythonの dict）か MCP サーバーから取得するか
  * ツール実行が直接関数呼び出しか MCP session.call_tool() か
  これだけが違う。アーキテクチャ的には「実装の分離」が MCP の価値。

前提: mcp-lab/basic/01_tools/server.py が同じ sandbox 内に存在すること
"""

import asyncio
import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
client = anthropic.Anthropic()

SERVER_PATH = (
    Path(__file__).resolve().parent.parent / "mcp-lab" / "basic" / "01_tools" / "server.py"
)

SYSTEM = """You are a customer support agent for an e-commerce company.
Use the available tools to resolve customer issues efficiently.
- Always look up customer and order details before taking action.
- Process refunds directly when the reason is valid.
- Escalate to a human ONLY when truly necessary."""


def mcp_tool_to_anthropic(mcp_tool) -> dict:
    """MCP ツール定義を Anthropic API のツール形式に変換する。"""
    return {
        "name": mcp_tool.name,
        "description": mcp_tool.description or "",
        "input_schema": mcp_tool.inputSchema,
    }


async def run_agent_with_mcp(user_message: str) -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # MCP サーバーからツール一覧を取得 → Anthropic 形式に変換
            mcp_tools = (await session.list_tools()).tools
            anthropic_tools = [mcp_tool_to_anthropic(t) for t in mcp_tools]
            print(f"Tools loaded from MCP: {[t.name for t in mcp_tools]}\n")

            print(f"Customer: {user_message}\n")
            messages = [{"role": "user", "content": user_message}]

            while True:
                response = client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=1024,
                    system=SYSTEM,
                    tools=anthropic_tools,
                    messages=messages,
                )

                tool_results = []
                for block in response.content:
                    if block.type == "text":
                        print(f"Agent: {block.text}")
                    elif block.type == "tool_use":
                        # MCP サーバーへツール呼び出しをディスパッチ
                        mcp_result = await session.call_tool(block.name, block.input)
                        result_text = (
                            mcp_result.content[0].text if mcp_result.content else "{}"
                        )
                        print(f"  [MCP] {block.name}({block.input}) → {result_text}")
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_text,
                        })

                if response.stop_reason == "end_turn":
                    break

                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    asyncio.run(run_agent_with_mcp(
        "Hi, I'm Jane (CUST-4471). My order ORD-88421 arrived damaged and I need a refund ASAP."
    ))
