from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_heatmap_ui.py ===
from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🔥 NODE HEATMAP</title>
    <style>
        body { background: #000; color: #0f0; font-family: monospace; }
        .node { display: inline-block; width: 100px; height: 100px; margin: 10px;
                text-align: center; line-height: 100px; border-radius: 8px; }
        .online { background: green; }
        .processing { background: orange; }
        .idle { background: gray; }
    </style>
</head>
<body>
    <h1>🔥 NODE HEATMAP</h1>
    {% for node in nodes %}
        <div class="node {{ node['status'] }}">{{ node['id'] }}</div>
    {% endfor %}
</body>
</html>
"""

def load_nodes():
    if os.path.exists("node_map.json"):
        with open("node_map.json") as f:
            return json.load(f)
    return []

@app.route("/")
def heatmap():
    nodes = load_nodes()
    return render_template_string(TEMPLATE, nodes=nodes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

def log_event():ef drop_files_to_bridge():