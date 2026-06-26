from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def research_topic(topic):

    response = client.search(
        query=topic,
        max_results=5
    )

    return response["results"]