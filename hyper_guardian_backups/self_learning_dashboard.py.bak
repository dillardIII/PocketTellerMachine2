# self_learning_dashboard.py

from flask import Flask, render_template_string, jsonify
import os
import json

app = Flask(__name__)

# === Self-Learning Log Viewer ===
@app.route('/self_learning_dashboard')
def self_learning_dashboard():
    try:
        if not os.path.exists("data/cole_self_learning_log.json"):
            log = []
            message = "No self-learning logs yet."
        else:
            with open("data/cole_self_learning_log.json", "r") as f:
                log = json.load(f)
            message = ""

        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cole Self-Learning Dashboard</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #121212; color: #f0f0f0; padding: 20px; }
                h1 { color: #6fd672; }
                table { width: 100%; border-collapse: collapse; background-color: #1f1f1f; }
                th, td { border: 1px solid #333; padding: 8px; text-align: left; }
                th { background-color: #222; }
                .message { color: #aaa; padding: 10px; }
            </style>
        </head>
        <body>
            <h1>Cole Self-Learning Log</h1>
            {% if message %}
            <div class="message">{{ message }}</div>
            {% else %}
            <table>
                <tr>
                    <th>Timestamp</th>
                    <th>Detected Pattern</th>
                    <th>Suggested Task</th>
                    <th>Reason</th>
                </tr>
                {% for entry in log %}
                <tr>
                    <td>{{ entry.timestamp }}</td>
                    <td>{{ entry.pattern }}</td>
                    <td>{{ entry.suggested_task }}</td>
                    <td>{{ entry.reason }}</td>
                </tr>
                {% endfor %}
            </table>
            {% endif %}
        </body>
        </html>
        """
        return render_template_string(html_template, log=log, message=message)
    except Exception as e:
        return jsonify({"error": str(e)})

# === API Direct JSON View (Optional) ===
@app.route('/api/self_learning_log')
def api_self_learning_log():
    try:
        if not os.path.exists("data/cole_self_learning_log.json"):
            return jsonify({"log": [], "message": "No self-learning logs yet."})
        with open("data/cole_self_learning_log.json", "r") as f:
            log = json.load(f)
        return jsonify({"log": log})
    except Exception as e:
        return jsonify({"error": str(e)})

# === CLI Direct Run ===
if __name__ == '__main__':
    app.run(port=5001, debug=True)