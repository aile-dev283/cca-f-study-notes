"""
MCP Advanced 05: Log & Progress 通知（サーバー側）

長時間処理の進捗をリアルタイムでクライアントに通知する。

API:
  await context.info("message")              → ログ通知
  await context.report_progress(cur, total)  → 進捗通知

ユーザー体験:
  通知なし → 「何かが壊れたのでは？」と不安になる
  通知あり → 処理が進んでいることが分かり安心できる
"""

import asyncio
from mcp.server.fastmcp import FastMCP
from mcp.types import Context
from pydantic import Field

mcp = FastMCP("LogProgressDemo")


@mcp.tool(
    name="analyze_data",
    description="Simulates a multi-step data analysis with real-time progress notifications.",
)
async def analyze_data(
    dataset_name: str = Field(description="Name of the dataset to analyze"),
    num_steps: int = Field(default=5, ge=1, le=10, description="Number of analysis steps"),
    ctx: Context = None,
) -> str:
    await ctx.info(f"Starting analysis of dataset: '{dataset_name}'")
    await ctx.report_progress(0, num_steps)

    results = []
    for i in range(1, num_steps + 1):
        await asyncio.sleep(0.4)  # 処理時間をシミュレート
        step_result = f"Step {i}: processed {i * 1000} records, found {i * 3} anomalies"
        results.append(step_result)
        await ctx.info(step_result)
        await ctx.report_progress(i, num_steps)

    await ctx.info("Analysis complete. Generating summary...")
    summary = f"Analyzed {num_steps * 1000} total records across {num_steps} steps."
    return summary


if __name__ == "__main__":
    mcp.run()
