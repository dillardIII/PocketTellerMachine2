# === FILE: cole_tools/cole_auto_runner.py ===

# === Main Version Used by Autopilot System ===
def cole_auto_run(config=None):
    """
    Main autopilot logic loop for Cole AI.
    Accepts optional config dict or single string task.
    """
    if isinstance(config, str):
        print(f"[Cole Autopilot] Running single task: {config}")
        config = {"phase": "manual", "tasks": [config]}

    if config is None:
        config = {}

    print("[Cole Autopilot] Starting run with config:", config)

    # Extract config values
    phase = config.get("phase", "default")
    tasks = config.get("tasks", [])

    print(f"[Cole Autopilot] Current Phase: {phase}")
    for task in tasks:
        print(f"[Cole Autopilot] Executing Task: {task}")

    # Your expanded logic goes here (API calls, signal checks, etc.)

    print("[Cole Autopilot] Run completed.")

# === Legacy Version for Backward Compatibility ===
def cole_auto_run_old(config=None):
    """
    Legacy placeholder for previous systems using cole_auto_run.
    """
    if config is None:
        config = {}

    print("[Cole Autopilot - OLD] Starting legacy run with config:", config)

    phase = config.get("phase", "legacy")
    tasks = config.get("tasks", [])

    print(f"[Legacy Cole] Phase: {phase}")
    for task in tasks:
        print(f"[Legacy Cole] Handling Task: {task}")

    print("[Legacy Cole] Run completed.")

# === Sample Safe Use ===
if __name__ == "__main__":
    # Example task run (safe format)
    cole_auto_run({
        "phase": "manual",
        "tasks": ["Write a strategy to detect breakout stocks"]
    })