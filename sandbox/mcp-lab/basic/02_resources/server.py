"""
MCP Basic 02: Resources プリミティブ

Resources = サーバーがデータ/ファイルを URI で公開する（副作用なし・読み取り専用）。
Tools との違い: Resources はデータの参照。Tools はアクションの実行。

URI テンプレート: docs://documents/{doc_id}
固定 URI:         docs://catalog
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentResources")

DOCUMENTS = {
    "policy-refund": (
        "Refund Policy v2.1\n\n"
        "Refunds must be requested within 30 days of purchase.\n"
        "Damaged items are eligible for a full refund.\n"
        "Processing takes 3-5 business days after approval."
    ),
    "policy-shipping": (
        "Shipping Policy v1.4\n\n"
        "Standard shipping: 5-7 business days.\n"
        "Express shipping: 1-2 business days.\n"
        "Free standard shipping on orders over $50."
    ),
    "faq": json.dumps({
        "q1": "How do I track my order?",
        "a1": "Log in to your account and visit Order History.",
        "q2": "What payment methods are accepted?",
        "a2": "Visa, Mastercard, PayPal, and bank transfer.",
        "q3": "Can I change my order after placing it?",
        "a3": "Changes can be made within 1 hour of placing the order.",
    }, indent=2),
}


@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def get_document(doc_id: str) -> str:
    """ドキュメントを URI テンプレートで取得する。"""
    if doc_id not in DOCUMENTS:
        raise ValueError(
            f"Document '{doc_id}' not found. Available: {list(DOCUMENTS.keys())}"
        )
    return DOCUMENTS[doc_id]


@mcp.resource("docs://catalog", mime_type="application/json")
def list_catalog() -> str:
    """利用可能なドキュメント一覧を返す固定リソース。"""
    return json.dumps({"documents": list(DOCUMENTS.keys())})


if __name__ == "__main__":
    mcp.run()
