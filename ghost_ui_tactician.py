# 👻 GhostUI Tactician – autonomously generates new dashboard UI modules
# Each cycle, it writes new HTML/JS snippets for trading dashboards.

import os
import time
import random

UI_DIR = "ptm_ui_auto"

def ensure_ui_dir():
    if not os.path.exists(UI_DIR):
        os.makedirs(UI_DIR)
        print(f"[GhostUI] 🛠️ Created UI directory: {UI_DIR}")

def generate_random_ui():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33"]
    widgets = ["Trade History", "Live Orders", "Volatility Chart", "AI Mood Indicator", "Ghost Trades Log"]
    color = random.choice(colors)
    widget = random.choice(widgets)

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>PTM Auto Dashboard</title>
    <style>
        body {{ background-color: {color}; color: white; font-family: Arial, sans-serif; }}
        .widget {{ margin: 20px; padding: 20px; background: rgba(0,0,0,0.5); border-radius: 10px; }}
    </style>
</head>
<body>
    <h1>GhostUI Tactician Dashboard</h1>
    <div class="widget">{widget}</div>
</body>
</html>
"""
    filename = f"{UI_DIR}/auto_dashboard_{int(time.time())}.html"
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"[GhostUI] 🎨 Created new dashboard UI: {filename}")

def tactician_loop():
    ensure_ui_dir()
    print("[GhostUI] 👻 Starting UI tactician loop...")
    while True:
        generate_random_ui()
        time.sleep(120)  # every 2 min

if __name__ == "__main__":
    tactician_loop()