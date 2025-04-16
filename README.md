# middleman-mcp

Middleman MCP（Model Context Protocol）サーバーを実行するためのPythonパッケージです。

## インストール

```bash
pip install middleman-mcp
```

## CLIの使用方法

```bash
# APIキーの設定
export MIDDLEMAN_API_KEY=your-api-key

# MCPサーバーの実行
uvx middleman-mcp server
```

## Claude Desktopでの設定

1. Clone the repository

```bash
git clone git@github.com:GenerativeAgents/middleman-mcp.git
```

2. Add the following to your `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "middleman": {
      "command": "uvx",
      "args": [
        "middleman-mcp",
        "server"
      ],
      "env": {
        "MIDDLEMAN_API_KEY": "xxxxx"
      }
    }
  }
}
```

## 開発者向け情報

### テスト実行

```bash
uv run pytest
```

### リンター実行

```bash
uv run ruff check .
```

## 配布

事前に PyPI アカウントを作成し、`~/.pypirc`に以下を記述。

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository: https://upload.pypi.org/legacy/
username: __token__
password: <APIキー>

[pypitest]
repository: https://test.pypi.org/legacy/
username: __token__
password: <APIキー>
```

```bash
# 事前にテストを実行
uv run pytest

# 事前にpyproject.tomlのversionを更新
cat pyproject.toml

# 古いビルド成果物を削除
rm -rf dist/
rm -rf build/
rm -rf middleman_mcp.egg-info/

# ビルド
uv run python setup.py sdist
uv run python setup.py bdist_wheel

# descriptionの形式が正しいかチェック
uv run twine check dist/*

# 配信
uv run twine upload --repository pypitest dist/* # テスト用
uv run twine upload --repository pypi dist/* # 本番用
```
