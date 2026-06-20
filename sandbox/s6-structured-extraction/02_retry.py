"""
S6 Step2: Pydantic validation + 失敗時 retry ループ

学習ポイント (D4):
- Pydantic モデルで出力スキーマを定義し、model_json_schema() でツールスキーマを自動生成
- validation エラーをフィードバックとして次ターンに渡す retry パターン
- D5 の「エラー伝播と回復」にも関連
"""

import json
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
import anthropic
from pydantic import BaseModel, ValidationError

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
client = anthropic.Anthropic()


class LineItem(BaseModel):
    description: str
    quantity: int
    unit_price: float


class Invoice(BaseModel):
    invoice_number: str
    vendor_name: str
    amount: float
    currency: str
    due_date: str  # YYYY-MM-DD
    line_items: list[LineItem] = []


# Pydantic スキーマからツール定義を自動生成
EXTRACTION_TOOL = {
    "name": "extract_invoice",
    "description": "Extracts structured invoice data from unstructured text.",
    "input_schema": Invoice.model_json_schema(),
}


def extract_with_retry(text: str, max_retries: int = 3) -> Invoice:
    messages = [
        {
            "role": "user",
            "content": f"Extract the invoice information:\n\n{text}",
        }
    ]
    last_error: Optional[str] = None

    for attempt in range(1, max_retries + 1):
        print(f"[Attempt {attempt}/{max_retries}]")

        if last_error:
            # 前回のエラーをフィードバックとして渡す
            messages.append({"role": "assistant", "content": "I'll try to fix the extraction."})
            messages.append({
                "role": "user",
                "content": f"The previous result failed validation: {last_error}. Please correct it.",
            })

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            tools=[EXTRACTION_TOOL],
            tool_choice={"type": "tool", "name": "extract_invoice"},
            messages=messages,
        )

        raw: Optional[dict] = None
        for block in response.content:
            if block.type == "tool_use":
                raw = block.input
                break

        if raw is None:
            last_error = "No tool_use block returned."
            print(f"  Error: {last_error}")
            continue

        try:
            invoice = Invoice.model_validate(raw)
            print(f"  Validation passed on attempt {attempt}.")
            return invoice
        except ValidationError as e:
            last_error = str(e)
            print(f"  Validation error: {e}")

    raise RuntimeError(f"Extraction failed after {max_retries} attempts. Last error: {last_error}")


if __name__ == "__main__":
    sample_path = Path(__file__).parent / "samples" / "invoice.txt"
    text = sample_path.read_text()

    result = extract_with_retry(text)
    print("\n=== Validated Invoice ===")
    print(result.model_dump_json(indent=2))
