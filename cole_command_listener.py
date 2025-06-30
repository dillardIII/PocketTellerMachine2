from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, request, jsonify

app = Flask(__name__)

# === Cole Command Receiver ===
@app.route("/api/cole_receive_command", methods=["POST"])
def cole_receive_command():
    data = request.json
    if not data or "command" not in data:
        return jsonify({"status": "error", "message": "Missing command in payload."}), 400

    # Log or process the command
    command = data["command"]
    print(f"[COLE RECEIVED COMMAND]: {command}")
    
    # Here you can route the command into Cole's brain, task queue, or logs
    # For now, we just confirm
    return jsonify({"status": "success", "message": f"Cole received your command: {command}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

def log_event():ef drop_files_to_bridge():