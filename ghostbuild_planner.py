from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
from ghostbuild_engine import ghostbuild_task

def ghostbuild_thinker():
    print("[GhostThinker] Asking GPT what to build next...")
    idea_prompt = "What is the next feature or strategy I should add to make my AI trading system more autonomous? Return just the prompt for the code you want to build."
    from cole_brain import cole_think
    task_prompt = cole_think(idea_prompt)
    print(f"[GhostThinker] GPT Response: {task_prompt}")
    ghostbuild_task(task_prompt)

if __name__ == "__main__":
    while True:
        ghostbuild_thinker()
        print("[GhostThinker] Sleeping for 1 hour...")
        time.sleep(3600)

def log_event():ef drop_files_to_bridge():