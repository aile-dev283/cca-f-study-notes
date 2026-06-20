"""
MCP Advanced 05: Log & Progress 通知（クライアント側）

logging_callback と progress_callback を登録して通知を受け取る。
"""

import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import LoggingMessageNotificationParams

SERVER_PATH = Path(__file__).resolve().parent / "server.py"


async def logging_callback(params: LoggingMessageNotificationParams) -> None:
    print(f"  [LOG] {params.data}")


async def progress_callback(
    progress: float,
    total: float | None,
    message: str | None,
) -> None:
    if total:
        bar_len = 25
        filled = int(bar_len * progress / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        pct = progress / total * 100
        print(f"  [PROGRESS] [{bar}] {pct:5.1f}% ({int(progress)}/{int(total)})")
    else:
        print(f"  [PROGRESS] {progress}")


async def main() -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read,
            write,
            logging_callback=logging_callback,
        ) as session:
            await session.initialize()

            print("=== Log & Progress Demo ===\n")
            result = await session.call_tool(
                "analyze_data",
                {"dataset_name": "customer_transactions_2026", "num_steps": 4},
                progress_callback=progress_callback,
            )

            print(f"\nFinal result: {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
