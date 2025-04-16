"""Middleman MCP Python Package.

このパッケージは、MCPサーバーを実行するためのツールを提供します。
"""

try:
    from importlib.metadata import version

    __version__ = version("middleman-mcp")
except ImportError:
    __version__ = "unknown"
