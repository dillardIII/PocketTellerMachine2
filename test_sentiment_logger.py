from ghost_env import INFURA_KEY, VAULT_ADDRESS
from cole_memory_brain import log_memory_event
from datetime import datetime

sentiment_event = {
    "id": "sentiment001",
    "source": "QuiverQuant",
    "symbol": "AMC",
    "summary": "AMC mentions on Reddit surged 120% in last 24 hours.",
    "sentiment": "Bullish",
    "confidence": "Medium",
    "timestamp": datetime.now().isoformat()
}

log_memory_event("journals", sentiment_event)

def log_event():ef drop_files_to_bridge():