"""
S6 Step1: tool_use で JSON スキーマ抽出（基本）

学習ポイント (D4):
- tool_choice={"type": "tool", "name": ...} で特定ツールを強制呼び出しし、
  構造化 JSON を確実に取得する
- 非構造化テキスト → 定義済みスキーマ の変換パターン
"""

import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
client = anthropic.Anthropic()

EXTRACTION_TOOL = {
    "name": "extract_invoice",
    "description": "Extracts structured invoice data from unstructured text.",
    "input_schema": {
        "type": "object",
        "properties": {
            "invoice_number": {"type": "string", "description": "Invoice number, e.g. INV-2026-0042"},
            "vendor_name": {"type": "string", "description": "Name of the vendor/seller"},
            "amount": {"type": "number", "description": "Total amount due (numeric only)"},
            "currency": {"type": "string", "description": "Currency code, e.g. USD, JPY"},
            "due_date": {"type": "string", "description": "Due date in YYYY-MM-DD format"},
            "line_items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "unit_price": {"type": "number"},
                    },
                    "required": ["description", "quantity", "unit_price"],
                },
            },
        },
        "required": ["invoice_number", "vendor_name", "amount", "currency", "due_date"],
    },
}


def extract_invoice(text: str) -> dict:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        tools=[EXTRACTION_TOOL],
        tool_choice={"type": "tool", "name": "extract_invoice"},  # 強制呼び出し
        messages=[
            {
                "role": "user",
                "content": f"Extract the invoice information from the following text:\n\n{text}",
            }
        ],
    )

    for block in response.content:
        if block.type == "tool_use":
            return block.input

    raise ValueError("No tool_use block in response")


if __name__ == "__main__":
    sample_path = Path(__file__).parent / "samples" / "invoice.txt"
    text = sample_path.read_text()

    print("=== Input ===")
    print(text)
    print("\n=== Extracted JSON ===")
    result = extract_invoice(text)
    print(json.dumps(result, indent=2, ensure_ascii=False))
