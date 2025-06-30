from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, jsonify, request
from test_fusion_predictor import predict_stock_bias
from test_fusion_ai_executor import ai_fusion_execute
from cole_memory_brain import load_memory

app = Flask(__name__)

# === API: Check AI Brain Status ===
@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "Cole AI Brain is online", "mode": "Fusion + Evolution Mode"})

# === API: Get Stock Bias Prediction ===
@app.route("/api/predict_bias", methods=["GET"])
def predict_bias():
    symbol = request.args.get("symbol", "AAPL")
    bias = predict_stock_bias(symbol)
    return jsonify({"symbol": symbol, "predicted_bias": bias})

# === API: Trigger Fusion Execution Trade ===
@app.route("/api/execute_trade", methods=["POST"])
def execute_trade_api():
    data = request.get_json()
    symbol = data.get("symbol", "AAPL")
    base_strategy = data.get("strategy", "RSI_Reversal")
    ai_fusion_execute(symbol, base_strategy)
    return jsonify({"message": f"Fusion trade executed for {symbol} using {base_strategy}."})

# === API: Get Full Brain Memory Snapshot ===
@app.route("/api/memory_snapshot", methods=["GET"])
def memory_snapshot():
    memory = load_memory()
    return jsonify(memory)

# === Run API ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():