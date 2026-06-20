"""
MCP Basic 02: Resources クライアント

list_resources() でリソース一覧を取得し、
read_resource() で URI を指定してコンテンツを読む。
"""

import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import AnyUrl

SERVER_PATH = Path(__file__).resolve().parent / "server.py"


async def main() -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1) リソース一覧
            resources = (await session.list_resources()).resources
            print("=== Available Resources ===")
            for r in resources:
                print(f"  {r.uri}  [{r.mimeType}]")

            # 2) カタログ（固定 URI）
            print("\n=== read_resource: docs://catalog ===")
            result = await session.read_resource(AnyUrl("docs://catalog"))
            print(result.contents[0].text)

            # 3) URI テンプレートで個別ドキュメントを取得
            print("\n=== read_resource: docs://documents/policy-refund ===")
            result = await session.read_resource(AnyUrl("docs://documents/policy-refund"))
            print(result.contents[0].text)

            # 4) 存在しないドキュメント（エラー確認）
            print("\n=== read_resource: docs://documents/nonexistent ===")
            try:
                result = await session.read_resource(AnyUrl("docs://documents/nonexistent"))
                print(result.contents[0].text)
            except Exception as e:
                print(f"Error (expected): {e}")


if __name__ == "__main__":
    asyncio.run(main())
