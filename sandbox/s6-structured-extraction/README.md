# S6: Structured Data Extraction (D4)

非構造化テキストから JSON を確実に抽出するパターン。

## 実行

```bash
# sandbox/ から実行
uv run python s6-structured-extraction/01_basic.py
uv run python s6-structured-extraction/02_retry.py
```

## ファイル構成

| ファイル | 内容 | 主なポイント |
|---------|------|------------|
| `01_basic.py` | tool_use で JSON 抽出 | `tool_choice` 強制・スキーマ設計 |
| `02_retry.py` | Pydantic + retry ループ | `model_json_schema()`・エラーフィードバック |
| `samples/invoice.txt` | 請求書サンプル | |
| `samples/support_ticket.txt` | サポートチケットサンプル | |

## 試験で問われる判断ポイント

- `tool_choice={"type": "tool", "name": "..."}` vs `{"type": "auto"}` の使い分け
  → 構造化出力を**確実に**得たい場合は強制呼び出し
- retry ループの終了条件（max_retries vs 信頼度しきい値）
- エラーフィードバックをどの粒度で次ターンに渡すか
