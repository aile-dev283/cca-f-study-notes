"""
S1 Step1: インライン tool 定義でエージェントループ（MCP なし）

学習ポイント (D1+D2):
- tool_use → tool_result の往復で「エージェントループ」を形成する仕組み
- エスカレーション判断をどのタイミングで行うか（システムプロンプトの設計）
- 同じロジックを Step2 (02_agent_mcp.py) で MCP 経由に置き換える → 比較が試験に出る

→ 02_agent_mcp.py と対比: ツール定義が inline か MCP 経由かの違いだけで
  エージェントループの本体は同じ。これが D2「なぜ MCP か」の答えにつながる。
"""

import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
client = anthropic.Anthropic()

# --- スタブ実装 ---

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


def get_customer(customer_id: str) -> dict:
    customer = CUSTOMER_DB.get(customer_id)
    return customer if customer else {"error": f"Customer {customer_id} not found"}


def lookup_order(order_id: str) -> dict:
    order = ORDER_DB.get(order_id)
    return order if order else {"error": f"Order {order_id} not found"}


def process_refund(order_id: str, reason: str) -> dict:
    if order_id not in ORDER_DB:
        return {"error": f"Order {order_id} not found"}
    return {
        "success": True,
        "refund_id": f"REF-{order_id}",
        "amount": ORDER_DB[order_id]["price"],
    }


def escalate_to_human(reason: str, priority: str = "normal") -> dict:
    return {"escalated": True, "ticket_id": "ESC-9999", "priority": priority, "reason": reason}


TOOL_DISPATCH = {
    "get_customer": get_customer,
    "lookup_order": lookup_order,
    "process_refund": process_refund,
    "escalate_to_human": escalate_to_human,
}

TOOLS = [
    {
        "name": "get_customer",
        "description": "Retrieve customer profile by customer ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "string", "description": "Customer ID, e.g. CUST-4471"}
            },
            "required": ["customer_id"],
        },
    },
    {
        "name": "lookup_order",
        "description": "Look up order details by order ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string", "description": "Order ID, e.g. ORD-88421"}
            },
            "required": ["order_id"],
        },
    },
    {
        "name": "process_refund",
        "description": "Process a refund for a specific order.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "reason": {"type": "string", "description": "Reason for the refund"},
            },
            "required": ["order_id", "reason"],
        },
    },
    {
        "name": "escalate_to_human",
        "description": (
            "Escalate this case to a human agent. Use only when the issue cannot be "
            "resolved automatically (e.g. legal threats, VIP requests, system errors)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reason": {"type": "string"},
                "priority": {
                    "type": "string",
                    "enum": ["low", "normal", "high", "urgent"],
                    "description": "Escalation priority",
                },
            },
            "required": ["reason"],
        },
    },
]

SYSTEM = """You are a customer support agent for an e-commerce company.
Use the available tools to resolve customer issues efficiently.
- Always look up customer and order details before taking action.
- Process refunds directly when the reason is valid (damaged, wrong item, not received).
- Escalate to a human ONLY when truly necessary: unresolvable disputes, legal threats, or VIP escalations.
- After resolving, confirm the outcome clearly to the customer."""


def run_agent(user_message: str) -> None:
    print(f"Customer: {user_message}\n")
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=SYSTEM,
            tools=TOOLS,
            messages=messages,
        )

        tool_results = []
        for block in response.content:
            if block.type == "text":
                print(f"Agent: {block.text}")
            elif block.type == "tool_use":
                fn = TOOL_DISPATCH[block.name]
                result = fn(**block.input)
                print(f"  [Tool] {block.name}({block.input}) → {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result),
                })

        if response.stop_reason == "end_turn":
            break

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    run_agent(
        "Hi, I'm Jane (CUST-4471). My order ORD-88421 arrived damaged and I need a refund ASAP."
    )
