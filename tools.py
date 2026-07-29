import os
import sys
import asyncio
from duckduckgo_search import DDGS
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

async def _fetch_from_mcp_server(query: str) -> str:
    # Set up the stdio parameters to run our local MCP server
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[os.path.join(os.path.dirname(__file__), "mcp_server.py")]
    )
    
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            
            # Call the 'search_products' tool from the MCP server
            result = await session.call_tool("search_products", arguments={"query": query})
            
            # Extract the text content from the result
            if result.content and len(result.content) > 0:
                return result.content[0].text
            return "No results found."

def search_products(query: str) -> str:
    """
    Dynamically fetches product recommendations by connecting to the MCP Server.
    """
    # Since ADK runs tools synchronously in some setups, we run the async client here
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we are already inside an event loop, this might require a different approach,
            # but for our simple ADK script, this should be fine or we could use nested_asyncio
            import nest_asyncio
            nest_asyncio.apply()
    except RuntimeError:
        pass
    
    return asyncio.run(_fetch_from_mcp_server(query))

def expand_search_query(user_request: str) -> str:
    """
    Analyzes the user's request and returns an expanded search query
    including synonyms and inferred context.
    """
    if "hiking" in user_request.lower() or "rain" in user_request.lower():
        return f"{user_request} durable waterproof outdoor gear camping buy"
    elif "city" in user_request.lower() or "walk" in user_request.lower():
        return f"{user_request} casual lightweight urban comfortable buy"
    return user_request
