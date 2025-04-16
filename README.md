# middleman-mcp

## MCP Server Setup

1. Clone the repository

```bash
git clone git@github.com:GenerativeAgents/middleman-mcp.git
```

2. Add the following to your `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "middleman": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/middleman-mcp",
        "run",
        "server.py"
      ],
      "env": {
        "MIDDLEMAN_API_KEY": "xxxxx"
      }
    }
  }
}
```