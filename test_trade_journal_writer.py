from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
from datetime import datetime

def write_trade_journal(trade):
    journal_entry = {
        "trade_id": trade.get("id"),
        "symbol": trade.get("symbol"),
        "strategy": trade.get("strategy"),
        "result": trade.get("result"),
        "grade": trade.get("grade"),
        "lesson": generate_lesson(trade),
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open("data/trade_journals.json", "a") as f:
            json.dump(journal_entry, f)
            f.write("\n")
        print("[JOURNAL WRITTEN]:", journal_entry)
    except Exception as e:
        print("[ERROR]: Could not write journal.", e)

def generate_lesson(trade):
    if trade["result"] > 0:
        return f"Good execution of {trade['strategy']} on {trade['symbol']}. Keep observing this pattern."
    else:
        return f"Loss on {trade['strategy']} for {trade['symbol']}. Review entry points and risk controls."

# Example usage
example_trade = {
    "id": "sample123",
    "symbol": "TSLA",
    "strategy": "protective_put",
    "result": -15,
    "grade": "D"
}

write_trade_journal(example_trade)

def log_event():ef drop_files_to_bridge():