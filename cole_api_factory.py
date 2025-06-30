from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import datetime
import json

API_FOLDER = "cole_generated_apis"
REGISTER_FILE = "cole_generated_apis/__init__.py"
LOG_FILE = "data/cole_api_log.json"

os.makedirs(API_FOLDER, exist_ok=True)

def create_api_module(endpoint_name, route_code):
    filename = f"{endpoint_name}.py"
    filepath = os.path.join(API_FOLDER, filename)

    # Write the code file
    with open(filepath, "w") as f:
        f.write(route_code)

    # Register the new route in __init__.py
    if not os.path.exists(REGISTER_FILE):
        with open(REGISTER_FILE, "w") as f:
            f.write("from flask import Blueprint\n\napi_blueprint(= Blueprint('api', __name__)\n"))

    with open(REGISTER_FILE, "a") as f:
        f.write(f"\nfrom .{endpoint_name} import register\nregister(api_blueprint)\n")

    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "endpoint": endpoint_name,
        "filepath": filepath
    }

    # Log creation
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"[Cole API Factory] API created: {endpoint_name}")
    return filepath

def get_api_template(endpoint, message):
    return f"""from flask import jsonify

def register(bp):
    @bp.route('/{endpoint}')
    def {endpoint}():
        return jsonify({{"message": "{message}"}})
"""

def log_event():ef drop_files_to_bridge():