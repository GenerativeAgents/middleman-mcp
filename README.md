# middleman-mcp

## Installation

Install the package from PyPI:

```bash
pip install middleman-mcp
```

## Usage

1.  **Set the API Key:**
    Make sure you have the `MIDDLEMAN_API_KEY` environment variable set.

    ```bash
    export MIDDLEMAN_API_KEY="your_api_key_here"
    ```

2.  **Run the MCP Server:**
    You can start the MCP server using the command-line interface. The simplest way is:

    ```bash
    middleman-mcp
    ```

## Development Setup (Using Local Clone)

If you need to work with the development version:

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