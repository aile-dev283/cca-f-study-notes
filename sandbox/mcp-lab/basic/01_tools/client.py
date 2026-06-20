"""
MCP Basic 01: Tools クライアント

MCP サーバーに stdio で接続し、ツール一覧の取得と呼び出しを確認する。
"""

import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = Path(__file__).resolve().parent / "server.py"


async def main() -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1) ツール一覧
            tools = (await session.list_tools()).tools
            print("=== Available Tools ===")
            for t in tools:
                print(f"  {t.name}: {t.description}")

            # 2) get_customer
            print("\n=== call_tool: get_customer ===")
            result = await session.call_tool("get_customer", {"customer_id": "CUST-4471"})
            print(result.content[0].text)

            # 3) lookup_order
            print("\n=== call_tool: lookup_order ===")
            result = await session.call_tool("lookup_order", {"order_id": "ORD-88421"})
            print(result.content[0].text)

            # 4) process_refund
            print("\n=== call_tool: process_refund ===")
            result = await session.call_tool("process_refund", {
                "order_id": "ORD-88421",
                "reason": "Item arrived damaged",
            })
            print(result.content[0].text)

            # 5) 存在しない顧客（エラーレスポンスの確認）
            print("\n=== call_tool: get_customer (not found) ===")
            result = await session.call_tool("get_customer", {"customer_id": "CUST-9999"})
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
