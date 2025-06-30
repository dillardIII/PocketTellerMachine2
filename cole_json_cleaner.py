from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
from datetime import datetime

# === Config ===
INPUT_FILE = "data/trades.json"
OUTPUT_FILE = "data/trades_cleaned.json"
REMOVE_INVALID = False  # Set True to remove entries with critical missing data

# === Fields Validation Map ===
REQUIRED_FIELDS = {
    "symbol": str,
    "strategy": str,
    "entry": float,
    "exit": float,
    "result": float,
    "timestamp": str
}

# === Default Fallback Values ===
DEFAULTS = {
    "strategy": "Unknown_Strategy",
    "entry": 0.0,
    "exit": 0.0,
    "result": 0.0
}

# === Cleaner Function ===
def clean_trades(input_file, output_file):
    with open(input_file, "r") as f:
        try:
            trades = json.load(f)
        except json.JSONDecodeError:
            print("[ERROR]: Invalid JSON format.")
            return

    cleaned_trades = []

    for trade in trades:
        clean_trade = {}
        missing_critical = False

        for field, field_type in REQUIRED_FIELDS.items():
            if field not in trade or trade[field] == "" or trade[field] is None:
                if REMOVE_INVALID and field != "strategy":
                    print(f"[WARNING]: Missing critical field '{field}' in trade: {trade.get('id', '')}")
                    missing_critical = True
                    break
                else:
                    # Apply default
                    clean_trade[field] = DEFAULTS.get(field, "")
            else:
                # Try casting to correct type
                try:
                    if field_type == float:
                        clean_trade[field] = float(trade[field])
                    elif field_type == str:
                        clean_trade[field] = str(trade[field])
                    else:
                        clean_trade[field] = trade[field]
                except (ValueError, TypeError):
                    print(f"[WARNING]: Invalid data type for '{field}' in trade: {trade.get('id', '')}. Applying default.")
                    clean_trade[field] = DEFAULTS.get(field, "")

        # Always keep id and timestamp if present:
        clean_trade["id"] = trade.get("id", f"auto_{datetime.now().isoformat()}")
        clean_trade["timestamp"] = trade.get("timestamp", datetime.now().isoformat())

        if not missing_critical:
            cleaned_trades.append(clean_trade)

    with open(output_file, "w") as f:
        json.dump(cleaned_trades, f, indent=2)
    print(f"[CLEANER]: Cleaned trades saved to {output_file} | Total cleaned: {len(cleaned_trades)}")


# === Run Cleaner ===
if __name__ == "__main__":
    clean_trades(INPUT_FILE, OUTPUT_FILE)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():