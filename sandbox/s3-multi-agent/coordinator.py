"""
S3: Multi-Agent Research System — Pure API オーケストレーター

学習ポイント (D1):
- コーディネーターが専門サブエージェントに委任するパターン
- 各サブエージェントは独立した system プロンプトを持つ別の Claude 呼び出し
- 「モデルを使い分ける」判断: 検索/分析は Haiku、最終レポートは Sonnet

試験で問われる設計判断:
  Q: なぜサブエージェントを使うか?
  A1: 文脈分離（各エージェントが自分の役割だけに集中）
  A2: コンテキストウィンドウの管理（中間処理結果がメインコンテキストを汚染しない）
  A3: 並列化（非同期で複数タスクを同時実行できる）

このファイルはシーケンシャル版。並列版は asyncio.gather() を使う（コメント参照）。

Claude Code の native subagent を使う場合は .claude/agents/*.md を参照。
"""

import asyncio
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
client = anthropic.Anthropic()


def call_sub_agent(
    system: str,
    task: str,
    model: str = "claude-haiku-4-5-20251001",
) -> str:
    """
    サブエージェントを模倣: 専用 system プロンプトと独立コンテキストを持つ Claude 呼び出し。
    実際の Claude Code subagent は .claude/agents/ で定義し /agents コマンドで管理する。
    """
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": task}],
    )
    return response.content[0].text


async def call_sub_agent_async(system: str, task: str, model: str = "claude-haiku-4-5-20251001") -> str:
    """asyncio.gather() で並列実行するための非同期ラッパー。"""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, call_sub_agent, system, task, model)


async def run_research_pipeline(topic: str) -> None:
    print(f"=== Multi-Agent Research: '{topic}' ===\n")

    # --- Sub-agent 1: Web Searcher（模擬） ---
    print("[1/3] Sub-agent: Web Searcher")
    search_result = call_sub_agent(
        system=(
            "You are a web search specialist. Given a topic, simulate finding 3 relevant "
            "authoritative sources with key facts. Format your response as a JSON array: "
            '[{"title": "...", "url": "https://...", "key_facts": ["fact1", "fact2"]}]'
        ),
        task=f"Find information about: {topic}",
    )
    print(f"  Found {len(search_result)} chars of search data.\n")

    # --- Sub-agent 2: Document Analyzer ---
    print("[2/3] Sub-agent: Document Analyzer")
    analysis = call_sub_agent(
        system=(
            "You are a document analysis specialist. Given search results, extract the most "
            "important insights, identify patterns or trends, and note any contradictions or gaps. "
            "Be concise and structured."
        ),
        task=f"Analyze these search results and extract key insights:\n\n{search_result}",
    )
    print(f"  Analysis complete ({len(analysis)} chars).\n")

    # --- Sub-agent 3: Report Writer（高品質モデルを使用）---
    print("[3/3] Sub-agent: Report Writer (Sonnet)")
    report = call_sub_agent(
        system=(
            "You are a technical report writer. Write a structured report with exactly these sections:\n"
            "## Executive Summary\n(2-3 sentences)\n\n"
            "## Key Findings\n- Finding 1\n- Finding 2\n- Finding 3\n\n"
            "## Next Steps\n- Step 1\n- Step 2"
        ),
        task=(
            f"Write a report on '{topic}'.\n\n"
            f"Based on this analysis:\n{analysis}\n\n"
            f"Original sources:\n{search_result}"
        ),
        model="claude-sonnet-4-6",  # レポート生成は高品質モデルを選択
    )

    print("\n" + "=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print(report)


# 並列実行の例（コメントアウト）:
#
# async def run_parallel(topic: str) -> None:
#     # Web Searcher と Document Analyzer を並列実行（独立したタスクの場合）
#     search_task = call_sub_agent_async(system=SEARCH_SYSTEM, task=topic)
#     related_task = call_sub_agent_async(system=RELATED_SYSTEM, task=topic)
#     search_result, related = await asyncio.gather(search_task, related_task)
#     # → 2つのサブエージェントが同時に走る（コンテキスト分離 + 並列化）


if __name__ == "__main__":
    asyncio.run(run_research_pipeline(
        "MCP Sampling feature and its role in enterprise AI cost management"
    ))
