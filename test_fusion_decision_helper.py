from ghost_env import INFURA_KEY, VAULT_ADDRESS
from cole_memory_brain import load_memory

def analyze_sentiment_for_symbol(symbol):
    memory = load_memory()
    journals = memory.get("journals", [])
    related = [j for j in journals if j.get("symbol") == symbol]:
:
    for j in related:
        print(f"[FOUND EVENT]: {j.get('event_type', j.get('source', 'Unknown'))} - {j.get('summary', j.get('details', 'No details'))} → {j.get('impact', j.get('sentiment', 'Unknown'))}")

# Example
analyze_sentiment_for_symbol("TSLA")
analyze_sentiment_for_symbol("AMC")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():