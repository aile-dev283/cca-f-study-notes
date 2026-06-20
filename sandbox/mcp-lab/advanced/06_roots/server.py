"""
MCP Advanced 06: Roots プリミティブ（サーバー側）

Roots = クライアントが「アクセスを許可するファイルシステムのルート」を宣言する仕組み。
サーバーは ctx.session.list_roots() でその一覧を取得し、アクセス制御に使う。

重要な注意点（D2 試験頻出）:
  MCP SDK は Roots 制限を自動で強制しない。
  サーバー側で is_path_allowed() を実装して自分で検証する必要がある。

フロー:
  1. クライアントがセッション初期化時に roots を宣言
  2. サーバーのツールが ctx.session.list_roots() で一覧を取得
  3. サーバーが is_path_allowed() でパスを検証してからファイル操作を実行
"""

import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from mcp.types import Context
from pydantic import Field

mcp = FastMCP("RootsDemo")


async def get_allowed_roots(ctx: Context) -> list[str]:
    """クライアントが宣言した roots を取得する。空リストの場合は制限なし。"""
    try:
        result = await ctx.session.list_roots()
        return [str(r.uri).replace("file://", "") for r in result.roots]
    except Exception:
        return []


def is_path_allowed(path: Path, allowed_roots: list[str]) -> bool:
    """パスが許可された roots のいずれかに含まれるかを検証する。"""
    if not allowed_roots:
        return True  # roots 未宣言 = 制限なし
    resolved = path.resolve()
    return any(str(resolved).startswith(str(Path(r).resolve())) for r in allowed_roots)


@mcp.tool(name="read_file", description="Reads a file within the allowed workspace roots.")
async def read_file(
    file_path: str = Field(description="Absolute path to the file to read"),
    ctx: Context = None,
) -> str:
    allowed_roots = await get_allowed_roots(ctx)
    path = Path(file_path)

    if not is_path_allowed(path, allowed_roots):
        return json.dumps({
            "error": f"Access denied: '{file_path}' is outside allowed roots.",
            "allowed_roots": allowed_roots,
        })

    if not path.exists():
        return json.dumps({"error": f"File not found: {file_path}"})

    return path.read_text()


@mcp.tool(
    name="list_directory",
    description="Lists files in a directory within the allowed workspace roots.",
)
async def list_directory(
    dir_path: str = Field(description="Absolute path to the directory"),
    ctx: Context = None,
) -> str:
    allowed_roots = await get_allowed_roots(ctx)
    path = Path(dir_path)

    if not is_path_allowed(path, allowed_roots):
        return json.dumps({
            "error": f"Access denied: '{dir_path}' is outside allowed roots.",
            "allowed_roots": allowed_roots,
        })

    if not path.is_dir():
        return json.dumps({"error": f"Not a directory: {dir_path}"})

    contents = sorted(str(f) for f in path.iterdir())
    return json.dumps({"directory": str(path.resolve()), "contents": contents})


if __name__ == "__main__":
    mcp.run()
