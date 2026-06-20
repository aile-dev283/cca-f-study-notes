"""
S1 Step3: Claude Agent SDK 版（claude-code-sdk パッケージ）

CCA-F 出題範囲との対応:
  D1 T1.3  allowed_tools=["Task"] でサブエージェント委任を宣言的に有効化
  D1 T1.5  PostToolUse フックで $500 超の返金を決定論的にブロック

01_agent_basic.py との比較（試験頻出）:
─────────────────────────────────────────────────────────────────────
│ 項目            │ 01_agent_basic.py         │ 03_agent_sdk.py        │
│ インポート       │ import anthropic           │ claude_code_sdk        │
│ ループ管理       │ 自前の while True          │ SDK が管理（ClaudeSDKClient）│
│ ツール定義       │ TOOLS リスト (JSON)        │ @tool + MCP サーバー    │
│ ポリシー強制     │ システムプロンプト（確率的）│ PostToolUse フック（決定論的）│
│ サブエージェント  │ 手動実装必要              │ allowed_tools=["Task"] │
─────────────────────────────────────────────────────────────────────

PostToolUse フックの意義 (D1 T1.5 の核心):
  プロンプトで「$500 超は返金禁止」と書いても Claude が従わない場合がある。
  フックはコードで強制するため決定論的 ─ これが試験で問われる違い。

query() vs ClaudeSDKClient:
  query()          → 一方向（文字列プロンプト送信後すぐ stdin を閉じる）
                     インプロセス MCP サーバーとの双方向通信が不可
  ClaudeSDKClient → 双方向ストリーミング（stdin 常時オープン）
                     インプロセス MCP サーバー・フック・インタラプト に対応
"""

import asyncio
import json
from pathlib import Path

from dotenv import load_dotenv

# SDK v0.0.25 互換パッチ: rate_limit_event など未知メッセージタイプをスキップ
# （CLI v2.1.183 が送出するが SDK がまだハンドルしていない）
from claude_code_sdk._internal import message_parser as _mpm
from claude_code_sdk._errors import MessageParseError as _MPE

_orig_parse = _mpm.parse_message


def _safe_parse(data):
    try:
        return _orig_parse(data)
    except _MPE:
        return None


_mpm.parse_message = _safe_parse

from claude_code_sdk import (
    AssistantMessage,
    ClaudeCodeOptions,
    ClaudeSDKClient,
    HookContext,
    HookMatcher,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    create_sdk_mcp_server,
    tool,
)
from claude_code_sdk.types import HookJSONOutput

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# ---------------------------------------------------------------------------
# スタブ DB（01_agent_basic.py と同一）
# ---------------------------------------------------------------------------

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
    "ORD-99001": {
        "item": "Enterprise Server",
        "price": 1200.00,
        "status": "delivered",
        "customer_id": "CUST-1001",
    },
}

# ---------------------------------------------------------------------------
# インプロセス MCP ツール定義（@tool デコレータ）
#
# 01_agent_basic.py の TOOLS リスト + TOOL_DISPATCH に相当。
# claude_code_sdk の @tool で定義し create_sdk_mcp_server() でバインドすると
# 同一プロセス内で動作し、IPC オーバーヘッドなし。
# ---------------------------------------------------------------------------


@tool(
    "get_customer",
    "Retrieve customer profile by customer ID.",
    {"customer_id": str},
)
async def get_customer_tool(args: dict) -> dict:
    customer = CUSTOMER_DB.get(args["customer_id"])
    result = customer or {"error": f"Customer {args['customer_id']} not found"}
    return {"content": [{"type": "text", "text": json.dumps(result)}]}


@tool(
    "lookup_order",
    "Look up order details by order ID.",
    {"order_id": str},
)
async def lookup_order_tool(args: dict) -> dict:
    order = ORDER_DB.get(args["order_id"])
    result = order or {"error": f"Order {args['order_id']} not found"}
    return {"content": [{"type": "text", "text": json.dumps(result)}]}


@tool(
    "process_refund",
    "Process a refund for a specific order.",
    {"order_id": str, "reason": str},
)
async def process_refund_tool(args: dict) -> dict:
    order = ORDER_DB.get(args["order_id"])
    if not order:
        result = {"error": f"Order {args['order_id']} not found"}
    else:
        result = {
            "success": True,
            "refund_id": f"REF-{args['order_id']}",
            "amount": order["price"],
        }
    return {"content": [{"type": "text", "text": json.dumps(result)}]}


@tool(
    "escalate_to_human",
    (
        "Escalate this case to a human agent. Use only when the issue cannot be "
        "resolved automatically (legal threats, VIP requests, system errors)."
    ),
    {"reason": str, "priority": str},
)
async def escalate_to_human_tool(args: dict) -> dict:
    result = {
        "escalated": True,
        "ticket_id": "ESC-9999",
        "priority": args.get("priority", "normal"),
        "reason": args["reason"],
    }
    return {"content": [{"type": "text", "text": json.dumps(result)}]}


# インプロセス MCP サーバーとしてバインド
_MCP_NAME = "support"
support_server = create_sdk_mcp_server(
    _MCP_NAME,
    tools=[
        get_customer_tool,
        lookup_order_tool,
        process_refund_tool,
        escalate_to_human_tool,
    ],
)

# allowed_tools のリスト
# Claude Code では MCP ツールは "mcp__<server>__<tool>" として識別される
# "Task" を追加するとサブエージェント委任が可能（D1 T1.3）
MCP_TOOLS = [
    f"mcp__{_MCP_NAME}__get_customer",
    f"mcp__{_MCP_NAME}__lookup_order",
    f"mcp__{_MCP_NAME}__process_refund",
    f"mcp__{_MCP_NAME}__escalate_to_human",
    # "Task",  ← ここに追加するとサブエージェントを spawn できる（D1 T1.3）
]

# ---------------------------------------------------------------------------
# PostToolUse フック: 返金ポリシー強制（D1 T1.5）
#
# フックの入力フィールド（PostToolUse）:
#   hook_event_name : "PostToolUse"
#   tool_name       : 呼び出されたツール名（例 "mcp__support__process_refund"）
#   tool_input      : ツールに渡された引数
#   tool_response   : ツールが返した結果（MCP の場合は content リスト）
#
# 返り値 HookJSONOutput:
#   {}                           → 通過（ツール結果をそのまま Claude に渡す）
#   {"decision": "block",
#    "systemMessage": "..."}     → 結果をブロックし Claude に理由を伝える
# ---------------------------------------------------------------------------


async def refund_policy_hook(
    hook_input: dict,
    tool_use_id: str | None,
    context: HookContext,
) -> HookJSONOutput:
    """$500 超の自動返金を決定論的にブロックする。

    Claude へのプロンプトで「$500 超は禁止」と書いても確率的にしか守られない。
    このフックはコードで強制するため 100% 確実 ─ D1 T1.5 の核心。
    """
    # tool_response は MCP ツールが返した content リストまたはテキスト
    raw = hook_input.get("tool_response", {})
    parsed: dict = {}

    if isinstance(raw, list):
        # content: [{type: "text", text: "..."}] の形式
        try:
            parsed = json.loads(raw[0].get("text", "{}"))
        except (json.JSONDecodeError, IndexError, AttributeError):
            pass
    elif isinstance(raw, str):
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            pass
    elif isinstance(raw, dict):
        parsed = raw

    amount = parsed.get("amount", 0)
    print(f"  [Hook/PostToolUse] process_refund → amount=${amount}")

    if amount > 500:
        print(f"  [Hook/PostToolUse] BLOCKED: ${amount:.2f} exceeds $500 limit")
        return {
            "decision": "block",
            "systemMessage": (
                f"Refund of ${amount:.2f} exceeds the automatic approval limit of $500. "
                "The refund was NOT processed. Escalate to a human agent."
            ),
        }

    return {}  # 通過


# ---------------------------------------------------------------------------
# システムプロンプト
# ---------------------------------------------------------------------------

SYSTEM = """You are a customer support agent for an e-commerce company.
Use the available tools to resolve customer issues efficiently.
- Always look up customer and order details before taking action.
- Process refunds directly when the reason is valid (damaged, wrong item, not received).
- Escalate to a human ONLY when truly necessary: refunds above policy limits, unresolvable disputes, legal threats.
- After resolving, confirm the outcome clearly to the customer."""

# ---------------------------------------------------------------------------
# メインのエージェント実行（ClaudeSDKClient）
#
# 01_agent_basic.py との最大の違い:
#   01: while True → stop_reason チェック → ツール結果を手動でメッセージに追加
#   03: ClaudeSDKClient + receive_messages() ─ ループは SDK が管理
#
# query() ではなく ClaudeSDKClient を使う理由:
#   query() は文字列プロンプトの場合に stdin をすぐ閉じる（単方向）。
#   インプロセス MCP サーバーは双方向通信が必要なため ClaudeSDKClient を使う。
# ---------------------------------------------------------------------------


async def run_agent_sdk(user_message: str) -> None:
    options = ClaudeCodeOptions(
        system_prompt=SYSTEM,
        model="claude-haiku-4-5-20251001",
        # MCP ツールのみ許可。"Task" を追加でサブエージェント委任が可能（D1 T1.3）
        allowed_tools=MCP_TOOLS,
        # インプロセス MCP サーバーを登録
        mcp_servers={_MCP_NAME: support_server},
        # PostToolUse フックで返金ポリシーを強制（D1 T1.5）
        hooks={
            "PostToolUse": [
                HookMatcher(
                    matcher=f"mcp__{_MCP_NAME}__process_refund",
                    hooks=[refund_policy_hook],
                )
            ]
        },
        # 非インタラクティブ実行時は bypassPermissions で確認ダイアログを抑制
        permission_mode="bypassPermissions",
        max_turns=10,
    )

    print(f"Customer: {user_message}\n")

    async with ClaudeSDKClient(options=options) as client:
        await client.query(user_message)
        async for message in client.receive_messages():
            if message is None:
                # parse_message がスキップした未知メッセージタイプ
                continue
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock) and block.text:
                        print(f"Agent: {block.text}")
                    elif isinstance(block, ToolUseBlock):
                        args = json.dumps(block.input, ensure_ascii=False)
                        print(f"  [Tool→] {block.name}({args})")
                    elif isinstance(block, ToolResultBlock):
                        print(f"  [←Tool] {block.content}")
            elif isinstance(message, SystemMessage):
                # SDK 内部の init / status メッセージは非表示でよい
                pass
            elif isinstance(message, ResultMessage):
                status = "ERROR" if message.is_error else "OK"
                cost = f"${message.total_cost_usd:.4f}" if message.total_cost_usd else "N/A"
                print(f"\n[Session/{status}] turns={message.num_turns}, cost={cost}")
                break  # ResultMessage で会話終了


# ---------------------------------------------------------------------------
# 動作確認シナリオ
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Case A: 通常の返金（$89.99 → フックが通過）")
    print("=" * 60)
    asyncio.run(
        run_agent_sdk(
            "Hi, I'm Jane (CUST-4471). My order ORD-88421 arrived damaged and I need a refund ASAP."
        )
    )

    print()
    print("=" * 60)
    print("Case B: 高額返金（$1200 → フックがブロック → エスカレーション）")
    print("=" * 60)
    asyncio.run(
        run_agent_sdk(
            "Hi, I'm Bob (CUST-1001). I need a refund for order ORD-99001. The server arrived completely broken."
        )
    )
