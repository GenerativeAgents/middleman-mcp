"""Middleman MCP CLI implementation."""

import os
import click

from ..server import run_server


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Middleman MCP CLI tools.

    サブコマンドを指定しない場合、デフォルトでMCPサーバーをstdioトランスポートで起動します。
    """
    print("Middleman MCP CLI tools を起動しています...")
    if ctx.invoked_subcommand is None:
        print("デフォルトのサーバーコマンドを実行します...")
        ctx.invoke(server)


@cli.command()
def server() -> None:
    """MCPサーバーをstdioトランスポートで実行します。"""
    print("MCPサーバーを実行しています（トランスポート: stdio）...")

    api_key = os.environ.get("MIDDLEMAN_API_KEY", "")
    if not api_key:
        print("警告: MIDDLEMAN_API_KEY環境変数が設定されていません。")
        print("一部の機能が正常に動作しない可能性があります。")

    run_server(transport="stdio")


if __name__ == "__main__":
    cli()
