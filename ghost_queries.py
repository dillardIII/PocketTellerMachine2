from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_queries.py ===
# 🧠 Ghost Intel Feed Engine – Queries and curates real-time insights

import json
import uuid
import requests
import os
from datetime import datetime

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_ENDPOINT = "https://api.perplexity.ai/search"

# === 🔍 Low-level query function ===
def query_perplexity(query):
    try:
        if not PERPLEXITY_API_KEY:
            raise ValueError("PERPLEXITY_API_KEY not set in environment.")

        payload = {
            "query": query,
            "sources": ["news", "finance"],
            "num_results": 5
        }

        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        print(f"[PERPLEXITY] 🧠 Asking: {query}")
        response = requests.post(PERPLEXITY_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if not data or "results" not in data:
            raise ValueError("Invalid response format from Perplexity.")

        results = [
            {
                "title": item.get("title"),
                "summary": item.get("summary"),
                "source": item.get("source")
            }
            for item in data["results"]
        ]

        print(f"[PERPLEXITY] ✅ {len(results)} results fetched.")
        return results

    except Exception as e:
        print(f"[PERPLEXITY ERROR] ❌ {e}")
        return [{"error": str(e), "query": query, "timestamp": datetime.utcnow().isoformat()}]

# === 🔎 Quick helpers for common reports ===
def get_latest_news():
    return query_perplexity("Top market news today")

def get_market_summary():
    return query_perplexity("Summarize global market performance today")

# === 🧠 High-level intel generation ===
def generate_ghost_intel(topics):
    """
    Pulls intelligence reports using Perplexity-style querying.

    Args:
        topics (list): List of strings to query.

    Returns:
        list: Formatted intel results.
    """
    print("[GHOST QUERIES] 🧠 Querying topics...")
    results = []

    for topic in topics:
        try:
            response = query_perplexity(topic)
            if isinstance(response, list):
                for res in response:
                    parsed = {
                        "id": str(uuid.uuid4()),
                        "topic": topic,
                        "title": res.get("title", "Untitled"),
                        "summary": res.get("summary", "No summary available."),
                        "source": res.get("source", "Unknown"),
                        "timestamp": datetime.utcnow().isoformat() + "Z"
                    }
                    results.append(parsed)
            else:
                results.append({
                    "id": str(uuid.uuid4()),
                    "topic": topic,
                    "summary": "Unexpected response format",
                    "error": str(response),
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                })

        except Exception as e:
            results.append({
                "id": str(uuid.uuid4()),
                "topic": topic,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })

    # Save log
    log_path = log_ghost_results(results)
    return results

def log_ghost_results(results):
    os.makedirs("logs/ghost_intel", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs/ghost_intel/query_{timestamp}.json"

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return log_file

def log_event():ef drop_files_to_bridge():