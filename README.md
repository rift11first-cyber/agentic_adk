# Agentic AI Shopping Assistant

This project is a multi-agent recommendation system built using the **Google Agent Development Kit (ADK)** in Python. It performs generative product searches with intelligent query expansion to provide personalized shopping experiences.

## Features

- **Google ADK Framework**: Utilizes the Google ADK to define hierarchical agents and execute workflows (`ShoppingManager` and `RetrievalAgent`).
- **Dynamic MCP Integration**: Instead of mock data, the system fetches live product results via the Model Context Protocol (MCP) using a local Python-based MCP server querying DuckDuckGo.
- **Intelligent Query Expansion**: Natural language queries are semantically expanded (e.g., inferring that "hiking" requires "durable outdoor gear") before being sent to the retrieval pipeline.

## Project Structure

- `agents.py`: Defines the `ShoppingManager` and `RetrievalAgent` using `google.adk.Agent`.
- `tools.py`: Implements the ADK tools, including query expansion and a dynamic MCP client that communicates with the local MCP server over stdio.
- `mcp_server.py`: A local MCP server implementation that uses `duckduckgo-search` to fetch real, live product data.
- `main.py`: The entry point that orchestrates the execution using ADK's `InMemoryRunner`.

## Setup & Execution

1. Ensure your virtual environment is active.
2. Run the application:
   ```bash
   python main.py
   ```

The script will automatically start the MCP server behind the scenes via the `stdio_client`, pass the user query to the Shopping Manager agent, fetch real live data, and generate a dynamic product recommendation.
