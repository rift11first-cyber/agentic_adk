import os
import asyncio
from agents import shopping_manager
from google.adk.runners import InMemoryRunner
from google.genai.types import Content, Part

# Set a dummy API key if the framework requires it for initialization (mocking purposes)
if "GEMINI_API_KEY" not in os.environ:
    os.environ["GEMINI_API_KEY"] = "dummy_api_key_for_local_testing"

def run_agent():
    print("Initializing Agentic AI Shopping Assistant...")
    query_text = "I need a durable backpack for a 5-day hiking trip in the rain"
    print(f"User Query: {query_text}\n")
    
    runner = InMemoryRunner(agent=shopping_manager, auto_create_session=True)
    try:
        # Construct Content object
        query = Content(role="user", parts=[Part.from_text(text=query_text)])
        
        events = runner.run(
            user_id="user_1",
            session_id="session_1",
            new_message=query
        )
        
        for event in events:
            print(f"Event type: {type(event).__name__}")
            
    except Exception as e:
        print(f"Error running agent: {e}")

if __name__ == "__main__":
    run_agent()
