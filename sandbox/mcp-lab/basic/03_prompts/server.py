"""
MCP Basic 03: Prompts プリミティブ

Prompts = サーバーが再利用可能なプロンプトテンプレートを公開する。
クライアントは get_prompt() で引数を渡し、完成したメッセージリストを受け取る。

Tools との違い:
  Tools → エージェントが自律的に呼び出す（副作用あり）
  Prompts → ユーザー/クライアントがトリガーし、LLM への入力を構成する（副作用なし）
"""

from mcp.server.fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent
from pydantic import Field

mcp = FastMCP("SupportPrompts")


@mcp.prompt(
    name="draft_refund_response",
    description="Generates a customer-friendly refund acknowledgement email draft.",
)
def draft_refund_response(
    customer_name: str = Field(description="Customer's full name"),
    order_id: str = Field(description="Order ID being refunded"),
    amount: str = Field(description="Refund amount with currency, e.g. $89.99 USD"),
) -> list[PromptMessage]:
    text = (
        f"Draft a professional and empathetic email to {customer_name} "
        f"confirming that their refund for order {order_id} of {amount} "
        f"has been approved and will be processed within 3-5 business days. "
        f"Keep the tone warm and concise."
    )
    return [PromptMessage(role="user", content=TextContent(type="text", text=text))]


@mcp.prompt(
    name="escalation_summary",
    description="Creates a concise handoff summary for a human agent.",
)
def escalation_summary(
    issue: str = Field(description="Brief description of the customer issue"),
    priority: str = Field(description="Priority: low / normal / high / urgent"),
    attempted: str = Field(
        default="None",
        description="What was already attempted to resolve the issue",
    ),
) -> list[PromptMessage]:
    text = (
        f"Write a concise handoff summary for a human support agent.\n"
        f"Priority: {priority}\n"
        f"Issue: {issue}\n"
        f"Already attempted: {attempted}\n\n"
        f"Include: what happened, what failed, and what the agent should do next."
    )
    return [PromptMessage(role="user", content=TextContent(type="text", text=text))]


if __name__ == "__main__":
    mcp.run()
