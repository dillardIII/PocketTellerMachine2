from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: task_planner.py ===

import random

# Example task pool for each team
TASK_POOL = {
    "GPT": [
        {"task_name": "Draft Strategy Logic", "instructions": "Create strategy logic for trade execution."},
        {"task_name": "Refactor Codebase", "instructions": "Simplify core modules, reduce repetition."}
    ],
    "Replit": [
        {"task_name": "Render HTML Dashboard", "instructions": "Build and style dashboard UI components."},
        {"task_name": "Handle File Upload", "instructions": "Implement file upload logic in Flask."}
    ],
    "Cole": [
        {"task_name": "Execute Trade Cycle", "instructions": "Run full trade loop on last suggestion."},
        {"task_name": "Check Risk Settings", "instructions": "Validate stop-loss and risk config."}
    ],
    "Strategist": [
        {"task_name": "Recommend Best Strategy", "instructions": "Score strategy pool and pick highest."},
        {"task_name": "Analyze Market Conditions", "instructions": "Summarize latest signals and patterns."}
    ],
    "Mentor": [
        {"task_name": "Generate Lesson Plan", "instructions": "Build quiz + lesson for RSI and MACD."},
        {"task_name": "Respond to User Feedback", "instructions": "Adjust tone and response timing."}
    ]
}

def generate_project_plan(phase="Phase One"):
    """
    Returns a plan with a list of tasks per team.
    """
    plan = {}
    for team, options in TASK_POOL.items():
        num = 1 if phase == "Phase One" else 2:
        plan[team] = random.sample(options, min(num, len(options)))
    return plan

def generate_task(team, project="PTM"):
    """
    Returns a random single task dict for the specified team.
    """
    if team not in TASK_POOL:
        return None
    task = random.choice(TASK_POOL[team])
    task["project"] = project
    return task

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():