"""
MCP Basic 03: Prompts クライアント

list_prompts() でプロンプト一覧と引数スキーマを取得し、
get_prompt() で引数を渡してメッセージリストを受け取る。
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

            # 1) プロンプト一覧と引数スキーマ
            prompts = (await session.list_prompts()).prompts
            print("=== Available Prompts ===")
            for p in prompts:
                print(f"  {p.name}: {p.description}")
                if p.arguments:
                    for arg in p.arguments:
                        req = "required" if arg.required else "optional"
                        print(f"    - {arg.name} ({req}): {arg.description}")

            # 2) draft_refund_response を取得
            print("\n=== get_prompt: draft_refund_response ===")
            result = await session.get_prompt("draft_refund_response", {
                "customer_name": "Jane Doe",
                "order_id": "ORD-88421",
                "amount": "$89.99 USD",
            })
            for msg in result.messages:
                content = msg.content
                text = content.text if hasattr(content, "text") else str(content)
                print(f"[{msg.role}] {text}")

            # 3) escalation_summary を取得
            print("\n=== get_prompt: escalation_summary ===")
            result = await session.get_prompt("escalation_summary", {
                "issue": "Customer CUST-4471 received damaged item ORD-88421, refund not processing",
                "priority": "high",
                "attempted": "process_refund tool returned success but customer reports no refund received",
            })
            for msg in result.messages:
                content = msg.content
                text = content.text if hasattr(content, "text") else str(content)
                print(f"[{msg.role}] {text}")


if __name__ == "__main__":
    asyncio.run(main())
