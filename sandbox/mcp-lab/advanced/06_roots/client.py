"""
MCP Advanced 06: Roots クライアント側

roots を宣言してセッションを初期化し、境界内/外のアクセスを試みる。

Roots の宣言方法:
  ClientSession(...) の roots パラメーターに Root オブジェクトのリストを渡す。
  サーバーが list_roots() を呼ぶと、このリストが返される。
"""

import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import Root

SERVER_PATH = Path(__file__).resolve().parent / "server.py"
SANDBOX_ROOT = Path(__file__).resolve().parents[3]   # sandbox/
SAMPLES_DIR = SANDBOX_ROOT / "s6-structured-extraction" / "samples"


async def main() -> None:
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER_PATH)],
    )

    # samples/ ディレクトリのみを許可 roots として宣言
    allowed_roots = [Root(uri=f"file://{SAMPLES_DIR}", name="samples")]

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, roots=allowed_roots) as session:
            await session.initialize()

            print("=== Roots Demo ===")
            print(f"Declared root: {SAMPLES_DIR}\n")

            # 1) 許可ディレクトリの一覧（成功するはず）
            print("--- list_directory: samples/ (in allowed root) ---")
            result = await session.call_tool(
                "list_directory", {"dir_path": str(SAMPLES_DIR)}
            )
            print(result.content[0].text)

            # 2) 許可ファイルを読む（成功するはず）
            print("\n--- read_file: invoice.txt (in allowed root) ---")
            result = await session.call_tool(
                "read_file", {"file_path": str(SAMPLES_DIR / "invoice.txt")}
            )
            print(result.content[0].text[:300])

            # 3) 許可外パスへのアクセス（アクセス拒否）
            print("\n--- read_file: /etc/passwd (outside allowed root) ---")
            result = await session.call_tool(
                "read_file", {"file_path": "/etc/passwd"}
            )
            print(result.content[0].text)

            # 4) 許可外ディレクトリ（アクセス拒否）
            print("\n--- list_directory: /tmp (outside allowed root) ---")
            result = await session.call_tool(
                "list_directory", {"dir_path": "/tmp"}
            )
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
