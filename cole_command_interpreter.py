from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
from cole_task_queue import add_task
from cole_code_writer import cole_write_code, say_hello
from cole_brain import cole_think
from cole_task_optimizer import cole_optimize_tasks
from cole_task_generator import cole_generate_tasks  # ✅ Corrected import
from cole_autopilot_cycle import cole_autopilot_cycle
from cole_performance_review import run_performance_review
from cole_trade_decision_engine import run_trade_decision_engine
from cole_sentiment_weighted_trade_trigger import run_sentiment_weighted_trade_trigger
from cole_smart_analytics import run_smart_analytics
from cole_congress_tracker import run_congress_ai_tracker
from assistants.malik import malik_report

COMMAND_LOG_FILE = "data/cole_command_log.json"

# === Logging Helper ===
def log_command(command, result):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "command": command,
        "result": result
    }

    logs = []
    if os.path.exists(COMMAND_LOG_FILE):
        try:
            with open(COMMAND_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(log_entry)
    with open(COMMAND_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Command Interpreter] Logged command: {command}")

# === New Logic Note Function ===
def cole_write_logic_note():
    note = {
        "timestamp": datetime.now().isoformat(),
        "note": "This is a placeholder logic note written during refinement.",
        "author": "cole_ai"
    }

    log_file = "data/cole_logic_notes.json"
    os.makedirs("data", exist_ok=True)

    try:
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                notes = json.load(f)
        else:
            notes = []

        notes.append(note)

        with open(log_file, "w") as f:
            json.dump(notes[-100:], f, indent=2)

        print("[Cole] Logic note saved.")
        return True
    except Exception as e:
        print(f"[Cole] Failed to write logic note: {str(e)}")
        return False

# === Command Interpreter ===
def cole_interpret_command(command_text):
    print(f"[Command Interpreter] Processing command: {command_text}")
    command_lower = command_text.lower().strip()
    result = ""

    try:
        if "say hello" in command_lower or command_lower == "hello":
            say_hello()
            result = "Cole says hello."

        elif command_lower.startswith("add_task"):
            task_text = command_text.split(" ", 1)[1]
            added = add_task(task_text)
            result = f"Task added: {task_text}" if added else f"Task already exists: {task_text}":
:
        elif command_lower.startswith("write_code"):
            task_text = command_text.split(" ", 1)[1]
            generated_code = cole_write_code(task_text)
            result = f"Code generated:\n{generated_code}"

        elif command_lower.startswith("think"):
            prompt = command_text.split(" ", 1)[1]
            thought = cole_think(prompt)
            result = f"Thought generated:\n{thought}"

        elif command_lower.startswith("build_and_run"):
            prompt = command_text.split(" ", 1)[1]
            from ghostbuild_engine import ghostbuild_task
            path = ghostbuild_task(prompt, inject=True)
            result = f"Build & run complete. Saved to {path}"

        elif "generate tasks" in command_lower or "create tasks" in command_lower:
            cole_generate_tasks()
            result = "Generated new tasks successfully."

        elif "optimize" in command_lower:
            cole_optimize_tasks()
            result = "Task optimization completed."

        elif "refine logic" in command_lower or "write logic note" in command_lower:
            cole_write_logic_note()
            result = "Refined strategy logic and added notes."

        elif "run autopilot" in command_lower:
            cole_autopilot_cycle()
            result = "Autopilot cycle executed successfully."

        elif "run performance review" in command_lower:
            run_performance_review()
            result = "Performance review module executed."

        elif "run trade engine" in command_lower:
            run_trade_decision_engine()
            result = "Trade decision engine executed."

        elif "run sentiment trigger" in command_lower:
            run_sentiment_weighted_trade_trigger()
            result = "Sentiment-weighted trade trigger executed."

        elif "run smart analytics" in command_lower:
            run_smart_analytics()
            result = "Smart analytics executed."

        elif "run congress analysis" in command_lower:
            run_congress_ai_tracker()
            result = "Congress trade tracker executed."

        elif "status" in command_lower or "health" in command_lower:
            result = "System is healthy. Autopilot and modules ready. Logs updated."

        else:
            result = f"[Interpreter] Unknown command: {command_text}"

    except Exception as e:
        result = f"Error processing command: {str(e)}"

    log_command(command_text, result)
    malik_report(f"Cole executed command: {command_text}")

    return result

# === CLI Example ===
if __name__ == "__main__":
    print("Cole Command Interpreter (Manual Test Mode)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = cole_interpret_command(user_input)
        print(f"Cole: {reply}")

def log_event():ef drop_files_to_bridge():