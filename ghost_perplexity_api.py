from ghost_env import INFURA_KEY, VAULT_ADDRESS
import requests
import os

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_ENDPOINT = "https://api.perplexity.ai/search"

def query_perplexity(query, sources=["news", "finance"], num_results=5):
    """
    Queries Perplexity for real-time insights.

    Args:
        query (str): Search query.
        sources (list): List of sources to query from.
        num_results (int): Number of results to fetch.

    Returns:
        dict: First result with keys: title, summary, source.
    """
    try:
        if not PERPLEXITY_API_KEY:
            raise ValueError("PERPLEXITY_API_KEY is not set in environment.")

        payload = {
            "query": query,
            "sources": sources,
            "num_results": num_results
        }

        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        print(f"[PERPLEXITY API] 📡 Querying: {query}")
        response = requests.post(PERPLEXITY_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if "results" not in data or not data["results"]:
            raise ValueError("No results returned by Perplexity.")

        first = data["results"][0]
        return {
            "title": first.get("title", "No Title"),
            "summary": first.get("summary", "No summary."),
            "source": first.get("source", "Unknown")
        }

    except Exception as e:
        print(f"[PERPLEXITY API ERROR] ❌ {e}")
        return {"error": str(e), "query": query}

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():