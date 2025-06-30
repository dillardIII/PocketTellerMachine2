from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
import requests

# === Configuration ===
BROKER_MODE = os.getenv("BROKER_MODE", "paper")  # 'paper' or 'live'
BROKER_API_URL = os.getenv("BROKER_API_URL", "https://sandbox.tradier.com/v1")
BROKER_API_KEY = os.getenv("BROKER_API_KEY", "your_api_key_here")

EXECUTION_LOG_FILE = "data/broker_trade_execution_log.json"

# === Logging Helper ===
def log_trade_execution(trade_details):
    logs = []
    if os.path.exists(EXECUTION_LOG_FILE):
        try:
            with open(EXECUTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "trade": trade_details
    })

    with open(EXECUTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Broker Interface] Trade logged: {trade_details}")

# === Execute Trade Order ===
def execute_trade_order(ticker, action, quantity=1, order_type="market"):
    """
    Executes a trade order.

    Args:
        ticker (str): Stock symbol (e.g., 'AAPL')
        action (str): 'buy' or 'sell'
        quantity (int): Number of shares
        order_type (str): 'market' or 'limit'

    Returns:
        dict: Result of trade execution (mocked for paper, API response for live)
    """
    print(f"[Broker Interface] Processing trade: {action.upper()} {quantity} {ticker} ({order_type})")

    if BROKER_MODE == "paper":
        # Mock paper trade execution
        trade_result = {
            "mode": "paper",
            "ticker": ticker,
            "action": action,
            "quantity": quantity,
            "order_type": order_type,
            "status": "executed",
            "price": round(100 + (5 * (1 if action == 'buy' else -1)), 2)  # mock price impact:
        }
        log_trade_execution(trade_result)
        return trade_result

    elif BROKER_MODE == "live":
        # Real broker API execution (Tradier example)
        endpoint = f"{BROKER_API_URL}/accounts/{os.getenv('BROKER_ACCOUNT_ID')}/orders"

        payload = {
            "class": "equity",
            "symbol": ticker,
            "side": action,
            "quantity": quantity,
            "type": order_type,
            "duration": "day"
        }

        headers = {
            "Authorization": f"Bearer {BROKER_API_KEY}",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            response = requests.post(endpoint, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            log_trade_execution(result)
            return result
        except Exception as e:
            error_log = {
                "mode": "live",
                "error": str(e),
                "payload": payload
            }
            log_trade_execution(error_log)
            return {"status": "error", "message": str(e)}

    else:
        error_msg = f"Invalid BROKER_MODE: {BROKER_MODE}"
        print(f"[Broker Interface] ERROR: {error_msg}")
        return {"status": "error", "message": error_msg}

# === CLI Test ===
if __name__ == "__main__":
    result = execute_trade_order("AAPL", "buy", quantity=2)
    print(f"Trade Result: {result}")

def log_event():ef drop_files_to_bridge():