from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_mode.py ===

import time
import os
from task_planner import generate_project_plan, generate_task
from packet_emitter import send_packet_to_team, emit_packet_to_team
from ghost_memory import store_task_log, record_assignment

ACTIVE_TEAMS = ["GPT", "Replit", "Cole", "Strategist", "Mentor"]
DEFAULT_PROJECT = "PocketTellerMachine"
DEFAULT_PHASE = "Phase One"

def start_autonomy_mode():
    print("[AUTONOMY MODE] 🚀 Initializing team coordination and build deployment...")
    plan = generate_project_plan(DEFAULT_PHASE)

    for team, tasks in plan.items():
        for task in tasks:
            print(f"[ASSIGNMENT] Sending task to {team}: {task['title']}")
            packet = {
                "recipient": team,
                "task_name": task['title'],
                "files": task.get("files", {}),
                "instructions": task.get("instructions", "Proceed with task."),
                "metadata": {"phase": DEFAULT_PHASE}
            }
            send_packet_to_team(packet)
            store_task_log(team, task)
            time.sleep(1)  # delay for realism / pacing

    print("[AUTONOMY MODE] ✅ Task packets sent to all teams.")

def assign_tasks(project=DEFAULT_PROJECT):
    print(f"\n🧠 Initiating Autonomy Mode for {project}...\n")
    for team in ACTIVE_TEAMS:
        print(f"\n📡 Assigning task to: {team}")

        task = generate_task(team, project)
        if not task:
            print(f"⚠️ No task generated for {team}.")
            continue

        packet = emit_packet_to_team(team, task)
        if not packet:
            print(f"❌ Packet emission failed for {team}.")
            continue

        record_assignment(team, task, packet)
        print(f"✅ Task assigned to {team}: {task['task_name']}")

if __name__ == "__main__":
    start_autonomy_mode()
    assign_tasks()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():