from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, request, jsonify
from test_fusion_ai_executor import ai_fusion_execute
from trade_logger import log_trade_to_memory
from datetime import datetime

app = Flask(__name__)

# === Status Check ===
@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "Cole Event Listener is active"})

# === Trigger AI Trade via Webhook/Event ===
@app.route("/api/event_trigger", methods=["POST"])
def event_trigger():
    data = request.get_json()
    symbol = data.get("symbol", "AAPL")
    base_strategy = data.get("strategy", "RSI_Reversal")
    trigger_reason = data.get("reason", "Unknown Trigger")

    print(f"[EVENT RECEIVED]: {trigger_reason} for {symbol} using {base_strategy}")

    ai_fusion_execute(symbol, base_strategy)

    # Optionally, simulate a log to memory (can be refined to only real trades)
    trade_data = {
        "id": f"event_{datetime.now().timestamp()}",
        "symbol": symbol,
        "strategy": base_strategy,
        "result": 20.5,  # Placeholder result
        "timestamp": datetime.now().isoformat(),
        "voice_summary": f"Triggered by {trigger_reason}"
    }
    log_trade_to_memory(trade_data)

    return jsonify({"message": f"AI trade triggered for {symbol} via event: {trigger_reason}."})

# === Run Event Listener API ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():