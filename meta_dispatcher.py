from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🛰️ MetaDispatcher – registers AIs and assigns tasks

import threading
import time

class MetaDispatcher:
    def __init__(self):
        self.ai_registry = {}
        self.active_tasks = {}
        self.loop_running = False

    def register_ai(self, ai_name, task_function):
        self.ai_registry[ai_name] = task_function
        print(f"[MetaDispatcher] 📘 Registered AI: {ai_name}")

    def assign_task(self, ai_name, task_name, *args, **kwargs):
        if ai_name in self.ai_registry:
            print(f"[MetaDispatcher] 🛰️ Assigning task '{task_name}' to {ai_name}...")
            t = threading.Thread(target=self._execute_task, args=(ai_name, task_name, *args), kwargs=kwargs)
            t.start()
            self.active_tasks[ai_name] = task_name
        else:
            print(f"[MetaDispatcher] ❌ AI '{ai_name}' not found.")

    def _execute_task(self, ai_name, task_name, *args, **kwargs):
        try:
            self.ai_registry[ai_name](*args, **kwargs)
            print(f"[MetaDispatcher] ✅ Task '{task_name}' completed by {ai_name}.")
        except Exception as e:
            print(f"[MetaDispatcher] ⚠️ {ai_name} failed '{task_name}': {e}")

    def list_status(self):
        print("\n[MetaDispatcher] 📋 Current AI Task Assignments:")
        for ai, task in self.active_tasks.items():
            print(f" - {ai} → {task}")
        print("")

    def start_task_monitor(self, interval=10):
        if self.loop_running:
            print("[MetaDispatcher] 🔁 Monitor already running.")
            return
        self.loop_running = True
        print("[MetaDispatcher] 🧭 Task monitor started.")
        while self.loop_running:
            self.list_status()
            time.sleep(interval)

    def stop_task_monitor(self):
        self.loop_running = False
        print("[MetaDispatcher] 🛑 Monitor stopped.")

def log_event():ef drop_files_to_bridge():