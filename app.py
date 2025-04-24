from flask import Flask, request, jsonify, render_template
from brain import TradingBrain

app = Flask(__name__)

# Initialize the brain
brain = TradingBrain()

# Home page (optional)
@app.route("/")
def home():
    return render_template("home.html", settings={})

# Endpoint to run the brain with POSTed data
@app.route("/run_brain", methods=["POST"])
def run_brain():
    data = request.get_json() or {}
    signal = brain.get_trade_signal(data)
    return jsonify(signal)

# (Optional) Example to change the strategy via POST
@app.route("/set_strategy", methods=["POST"])
def set_strategy():
    data = request.get_json() or {}
    strategy = data.get("strategy", "covered_call")
    brain.set_strategy(strategy)
    return jsonify({"status": "ok", "strategy": brain.strategy})

if __name__ == "__main__":
    app.run(debug=True)