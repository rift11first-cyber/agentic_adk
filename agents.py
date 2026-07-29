from google.adk import Agent
from tools import search_products, expand_search_query

retrieval_agent = Agent(
    name="RetrievalAgent",
    instruction="""You are the Retrieval Agent for a Shopping Assistant.
Your task is to take the user's initial request, expand it using the expand_search_query tool, 
and then search for products using the search_products tool. 
Return the best matching products as a formatted response.""",
    tools=[search_products, expand_search_query]
)

shopping_manager = Agent(
    name="ShoppingManager",
    instruction="""You are an AI Shopping Assistant Manager.
You help users find the best products based on their natural language queries.
You should use the retrieval_agent to fetch personalized recommendations for the user.
Present the recommendations clearly and explain why they fit the user's needs.""",
    sub_agents=[retrieval_agent]
)
