from cole_memory_brain import log_memory_event
from datetime import datetime

congress_trade = {
    "id": "congress001",
    "representative": "Nancy Pelosi",
    "symbol": "NVDA",
    "type": "Purchase",
    "amount": "$1M-$5M",
    "reported_date": "2025-05-15",
    "timestamp": datetime.now().isoformat()
}

log_memory_event("journals", congress_trade)