from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_merger.py ===
import os
import re
import json
from datetime import datetime

THREADS_DIR = "strategy_threads"
VOTE_DIR = "strategy_votes"
MERGED_DIR = "team_files/Merged"
os.makedirs(MERGED_DIR, exist_ok=True)

def load_strategy_code(version_tag, thread_id):
    base_name = thread_id.split(".")[0]
    candidate_dir = "team_files"

    for root, _, files in os.walk(candidate_dir):
        for file in files:
            if file.startswith(base_name) and version_tag in file and file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    return f.readlines()
    return []

def merge_logic_blocks(blocks):
    final = ["# === Merged Strategy ===\n", "def run_strategy(data):\n"]
    indent = "    "
    for logic in blocks:
        final.append(f"{indent}# --- Merge Logic Start ---\n")
        final.extend([indent + line.strip() + "\n" for line in logic])
        final.append(f"{indent}# --- Merge Logic End ---\n\n")
    final.append(f"{indent}return 'Buy AAPL'  # Default fallback\n")
    return final

def run_strategy_merger(thread_file):
    if not os.path.exists(thread_file):
        return "Thread file not found."

    with open(thread_file, "r") as f:
        thread = json.load(f)

    vote_file = thread_file.replace("strategy_threads", "strategy_votes").replace(".json", "_votes.json")
    if not os.path.exists(vote_file):
        return "No vote file found."

    with open(vote_file, "r") as f:
        votes = json.load(f)

    top_versions = sorted(votes["votes"].items(), key=lambda x: len(x[1]), reverse=True)
    top_tags = [v[0] for v in top_versions[:2]]

    # Extract code blocks from top versions
    code_blocks = []
    for tag in top_tags:
        code = load_strategy_code(tag, thread["thread_id"])
        if not code:
            continue
        body = [line for line in code if "def run_strategy" not in line and "import" not in line]:
        code_blocks.append(body)

    if not code_blocks:
        return "No valid strategies found to merge."

    merged_lines = merge_logic_blocks(code_blocks)

    # Save merged file
    new_name = thread["thread_id"].replace(".json", "_merged.py")
    new_path = os.path.join(MERGED_DIR, new_name)
    with open(new_path, "w") as f:
        f.writelines(merged_lines)

    print(f"[MERGER] Created hybrid strategy: {new_name}")
    return new_path

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():