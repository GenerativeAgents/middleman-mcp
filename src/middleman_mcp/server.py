from mcp.server.fastmcp import FastMCP
from middleman_ai import ToolsClient
from middleman_ai.client import Presentation, Slide, Placeholder
import os
from typing import List, Dict, Any, Literal

mcp = FastMCP("Middleman Tools")

api_key = os.environ.get("MIDDLEMAN_API_KEY", "")
client = ToolsClient(api_key=api_key)


@mcp.tool()
def md_to_pdf(markdown_text: str) -> str:
    """
    Convert Markdown text to PDF and return the download URL.

    Args:
        markdown_text: The Markdown text to convert

    Returns:
        The URL to download the generated PDF
    """
    return client.md_to_pdf(markdown_text)


@mcp.tool()
def md_to_docx(markdown_text: str) -> str:
    """
    Convert Markdown text to DOCX and return the download URL.

    Args:
        markdown_text: The Markdown text to convert

    Returns:
        The URL to download the generated DOCX
    """
    return client.md_to_docx(markdown_text)


@mcp.tool()
def md_to_pptx(markdown_text: str) -> str:
    """
    Convert Markdown text to PPTX and return the download URL.

    Args:
        markdown_text: The Markdown text to convert

    Returns:
        The URL to download the generated PPTX
    """
    return client.md_to_pptx(markdown_text)


@mcp.tool()
def pdf_to_page_images(pdf_file_path: str) -> List[Dict[str, Any]]:
    """
    Convert a PDF file to page images and return the image URLs.

    Args:
        pdf_file_path: Path to the local PDF file

    Returns:
        A list of dictionaries with page_no and image_url for each page
    """
    return client.pdf_to_page_images(pdf_file_path)


@mcp.tool()
def json_to_pptx_analyze(pptx_template_id: str) -> List[Dict[str, Any]]:
    """
    Analyze a PPTX template structure.

    Args:
        pptx_template_id: The template ID (UUID)

    Returns:
        The template analysis result with slide types and placeholders
    """
    return client.json_to_pptx_analyze_v2(pptx_template_id)


@mcp.tool()
def json_to_pptx_execute(pptx_template_id: str, slides: List[Dict[str, Any]]) -> str:
    """
    Generate a PPTX from JSON data using a template.

    Args:
        pptx_template_id: The template ID (UUID)
        slides: A list of slide definitions with type and placeholders

    Returns:
        The URL to download the generated PPTX
    """
    presentation_slides = []
    for slide_data in slides:
        placeholders = []
        for ph in slide_data.get("placeholders", []):
            placeholders.append(Placeholder(name=ph["name"], content=ph["content"]))

        presentation_slides.append(
            Slide(type=slide_data["type"], placeholders=placeholders)
        )

    presentation = Presentation(slides=presentation_slides)
    return client.json_to_pptx_execute_v2(pptx_template_id, presentation)


def run_server(transport: Literal["stdio", "sse"] = "stdio"):
    """
    MCPサーバーを実行します。

    Args:
        transport: 使用するトランスポート方式（"stdio", "sse"）
    """
    mcp.run(transport=transport)


if __name__ == "__main__":
    run_server(transport="stdio")
