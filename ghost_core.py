# ghost_core.py
# Primary control node that unifies bot processes, bridges, tasks, and command relay

import json
import os
from threading import Thread
from neurochain_bootstrapper import NeuroChain
from bridge_controller import BridgeController
from ghost_logger import GhostLogger

class GhostCore:
    def __init__(self):
        self.logger = GhostLogger()
        self.bridge = BridgeController(self.logger)
        self.chain = NeuroChain()
        self.running = False
        self.profile = "default"
        self.env_path = "./ghost_env.json"

    def load_environment(self):
        if os.path.exists(self.env_path):
            with open(self.env_path, "r") as f:
                env = json.load(f)
                self.profile = env.get("profile", "default")
                self.logger.log(f"[ENVIRONMENT LOADED] Profile: {self.profile}")
        else:
            self.logger.log("[NO ENV FOUND] Generating new environment...")
            self.save_environment()

    def save_environment(self):
        env = {
            "profile": self.profile
        }
        with open(self.env_path, "w") as f:
            json.dump(env, f, indent=2)
        self.logger.log("[ENVIRONMENT SAVED]")

    def run(self):
        self.running = True
        self.logger.log("[GHOST CORE BOOTING UP]")
        self.load_environment()

        task_thread = Thread(target=self.chain.execute_tasks)
        bridge_thread = Thread(target=self.bridge.sync_all)

        task_thread.start()
        bridge_thread.start()

        task_thread.join()
        bridge_thread.join()

        self.logger.log("[GHOST CORE SHUTDOWN COMPLETE]")

# Live run hook
if __name__ == "__main__":
    core = GhostCore()
    core.run()