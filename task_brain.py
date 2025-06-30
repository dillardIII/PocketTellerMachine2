from ghost_env import INFURA_KEY, VAULT_ADDRESS
# task_brain.py
# Purpose: Self-starting task engine for autonomous operation

import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_file
from autonomy_config import get_config
from priority_engine import get_priority_list
from persona_delegator import assign_persona

class TaskBrain:
    def __init__(self):
        self.config = get_config()
        self.priority_list = get_priority_list()

    def evaluate_tasks(self):
        log_event("TaskBrain", "Evaluating potential tasks")
        tasks = self.scan_environment()
        prioritized = self.prioritize(tasks)
        self.execute(prioritized)

    def scan_environment(self):
        # Replace with live system checks: time, market status, user state
        return [
            {"name": "Check market open", "urgency": 10},
            {"name": "Review watchlist", "urgency": 8},
            {"name": "Evaluate trade profit", "urgency": 9}
        ]

    def prioritize(self, tasks):
        sorted_tasks = sorted(tasks, key=lambda t: self.priority_list.get(t["name"], 0), reverse=True)
        return sorted_tasks

    def execute(self, tasks):
        for task in tasks:
            persona = assign_persona(task["name"])
            log_event("TaskBrain", f"Routing '{task['name']}' to {persona}")
            # Example: persona_task_engine.run(task["name"], persona)