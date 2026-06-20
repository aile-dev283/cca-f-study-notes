"""
MCP Basic 01: Tools プリミティブ

Tools = エージェントがアクション（副作用あり）を実行するための関数。
FastMCP の @mcp.tool() デコレーターで定義する。

顧客サポートの4ツールを実装:
  get_customer, lookup_order, process_refund, escalate_to_human

このサーバーは s1-customer-support/02_agent_mcp.py からも利用される。
"""

import json
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("CustomerSupportTools")

CUSTOMER_DB = {
    "CUST-4471": {"name": "Jane Doe", "email": "jane.doe@example.com", "tier": "gold"},
    "CUST-1001": {"name": "Bob Smith", "email": "bob@example.com", "tier": "standard"},
}
ORDER_DB = {
    "ORD-88421": {
        "item": "Laptop Stand",
        "price": 89.99,
        "status": "delivered",
        "customer_id": "CUST-4471",
    },
}


@mcp.tool(name="get_customer", description="Retrieve customer profile by customer ID.")
def get_customer(
    customer_id: str = Field(description="Customer ID, e.g. CUST-4471"),
) -> str:
    customer = CUSTOMER_DB.get(customer_id)
    if not customer:
        return json.dumps({"error": f"Customer {customer_id} not found"})
    return json.dumps(customer)


@mcp.tool(name="lookup_order", description="Look up order details by order ID.")
def lookup_order(
    order_id: str = Field(description="Order ID, e.g. ORD-88421"),
) -> str:
    order = ORDER_DB.get(order_id)
    if not order:
        return json.dumps({"error": f"Order {order_id} not found"})
    return json.dumps(order)


@mcp.tool(name="process_refund", description="Process a refund for a specific order.")
def process_refund(
    order_id: str = Field(description="Order ID to refund"),
    reason: str = Field(description="Reason for the refund"),
) -> str:
    if order_id not in ORDER_DB:
        return json.dumps({"error": f"Order {order_id} not found"})
    amount = ORDER_DB[order_id]["price"]
    return json.dumps({"success": True, "refund_id": f"REF-{order_id}", "amount": amount})


@mcp.tool(
    name="escalate_to_human",
    description=(
        "Escalate the case to a human agent. Use only when the issue cannot be resolved "
        "automatically (legal threats, VIP escalations, system errors)."
    ),
)
def escalate_to_human(
    reason: str = Field(description="Why escalation is needed"),
    priority: str = Field(
        default="normal",
        description="Priority level: low / normal / high / urgent",
    ),
) -> str:
    return json.dumps({
        "escalated": True,
        "ticket_id": "ESC-9999",
        "priority": priority,
        "reason": reason,
    })


if __name__ == "__main__":
    mcp.run()
