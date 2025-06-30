# === FILE: routes/bot_control_routes.py ===

# 🎮 Bot Control Routes – Flask routes to trigger PTM bots from the control panel UI

from flask import Blueprint, Response
import subprocess

bot_control = Blueprint("bot_control", __name__)

# === Utilities ===

def run_python_module(module_name):
    """Run a Python file as a subprocess and return the output."""
    try:
        result = subprocess.run(
            ["python3", f"{module_name}.py"],
            capture_output=True,
            text=True,
            timeout=60
        )
        output = result.stdout + result.stderr
        return output
    except Exception as e:
        return f"❌ Error running {module_name}: {e}"

# === Routes ===

@bot_control.route("/run_bot/inspector")
def run_inspector():
    output = run_python_module("bots/inspector_bot")
    return Response(output, mimetype="text/plain")

@bot_control.route("/run_bot/watcher")
def run_watcher():
    output = run_python_module("ghostforge_repair_watcher")
    return Response(output, mimetype="text/plain")

@bot_control.route("/run_bot/autobuilder")
def run_autobuilder():
    output = run_python_module("bots/ghostforge_autobuilder")
    return Response(output, mimetype="text/plain")

@bot_control.route("/run_bot/full")
def run_full_sweep():
    output1 = run_python_module("bots/inspector_bot")
    output2 = run_python_module("ghostforge_repair_watcher")
    output3 = run_python_module("bots/ghostforge_autobuilder")
    return Response(output1 + "\n\n" + output2 + "\n\n" + output3, mimetype="text/plain")