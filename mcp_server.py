import json
import logging
from duckduckgo_search import DDGS
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, CallToolResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

server = Server("shopping-mcp")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_products",
            description="Searches the web for real product recommendations based on a query.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The product search query",
                    }
                },
                "required": ["query"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "search_products":
        query = arguments.get("query")
        logger.info(f"Searching for products: {query}")
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query + " shopping product best price", max_results=5))
            
            # Format the results dynamically
            formatted_results = json.dumps(results, indent=2)
            return [TextContent(type="text", text=formatted_results)]
        except Exception as e:
            return [TextContent(type="text", text=f"Error performing search: {e}")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
