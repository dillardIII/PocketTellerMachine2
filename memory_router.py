from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Memory Router:
Coordinates memory access between assistant modules, ensuring they can retrieve, store, and react to shared PTM memory.
Allows plug-and-play access for any new assistant, tool, or logic module.
"""

from cole_brain import get_last, log_memory, log_state

def route_memory_event(event_key, data, source="unknown"):
    """
    Routes a new memory entry into PTM's brain and logs the source.
    """
    print(f"[🧠 Memory Router] Routing '{event_key}' from {source}...")
    log_memory(event_key, data)
    log_state(f"{source}_last_memory_event", event_key)

def recall_shared_memory(key):
    """
    Retrieves shared memory entry by key.
    """
    print(f"[🧠 Memory Recall] Fetching memory for: {key}")
    return get_last(key)

# === Example usage
if __name__ == "__main__":
    route_memory_event("latest_market_trigger", {"symbol": "AAPL", "signal": "bullish breakout"}, source="Strategist")
    print("Recalled:", recall_shared_memory("latest_market_trigger"))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():