# ghostbot_task_engine.py
# Purpose: Self-Updating Task Engine for GhostBot (PTM AI Core)
# Powers recursive task assignment, autonomous scheduling, learning, and background optimization

import os
import json
import time
import random
import datetime
from utils.logger import log_event
from core.ghostbrain import GhostBrain
from core.task_library import TaskLibrary
from core.recursive_updater import RecursiveUpdater

class GhostBotTaskEngine:
    def __init__(self):
        self.ghostbrain = GhostBrain()
        self.tasklib = TaskLibrary()
        self.updater = RecursiveUpdater()
        self.task_queue = []
        self.last_executed = {}

    def load_task_profile(self):
        """Load or initialize GhostBot's task profile."""
        if os.path.exists("memory/task_profile.json"):
            with open("memory/task_profile.json", "r") as f:
                self.task_queue = json.load(f)
        else:
            self.task_queue = self.tasklib.get_default_tasks()
            self.save_task_profile()

    def save_task_profile(self):
        """Persist current task profile."""
        with open("memory/task_profile.json", "w") as f:
            json.dump(self.task_queue, f, indent=4)

    def add_task(self, task_name, metadata={}):
        """Add a new task to the queue."""
        task = {
            "name": task_name,
            "metadata": metadata,
            "timestamp": str(datetime.datetime.now()),
            "status": "queued"
        }
        self.task_queue.append(task)
        self.save_task_profile()
        log_event("Task Added", task)

    def run_task_loop(self):
        """Run queued tasks autonomously and recursively update system."""
        for task in self.task_queue:
            if task["status"] != "done":
                result = self.ghostbrain.process_task(task)
                task["status"] = "done"
                task["result"] = result
                task["completed_at"] = str(datetime.datetime.now())
                log_event("Task Completed", task)

                self.last_executed[task["name"]] = result

        self.save_task_profile()

    def recursive_update_check(self):
        """Periodically pull updates and inject improvements."""
        result = self.updater.pull_core_updates()
        if result["status"] == "success":
            log_event("Core Update Pulled", result)
            self.ghostbrain.learn_from_update(result["changes"])
        else:
            log_event("Update Skipped", result)

    def run_engine(self):
        """Master loop for GhostBot's self-management logic."""
        self.load_task_profile()

        while True:
            self.run_task_loop()
            self.recursive_update_check()

            time.sleep(60 * 5)  # Check every 5 minutes


# --- Startup Routine ---
if __name__ == "__main__":
    engine = GhostBotTaskEngine()
    engine.run_engine()