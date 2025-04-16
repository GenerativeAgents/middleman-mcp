"""Middleman MCP CLI implementation."""

import os
import click

from ..server import run_server


@click.group()
def cli() -> None:
    """Middleman MCP CLI tools."""
    print("Middleman MCP CLI tools を起動しています...")
    pass


@cli.command()
@click.option(
    "--transport",
    "-t",
    default="stdio",
    help="トランスポート方式を指定します (stdio, websocket, etc.)",
)
def server(transport: str) -> None:
    """MCPサーバーを実行します。"""
    print(f"MCPサーバーを実行しています（トランスポート: {transport}）...")
    
    api_key = os.environ.get("MIDDLEMAN_API_KEY", "")
    if not api_key:
        print("警告: MIDDLEMAN_API_KEY環境変数が設定されていません。")
        print("一部の機能が正常に動作しない可能性があります。")
    
    run_server(transport=transport)


if __name__ == "__main__":
    cli()
