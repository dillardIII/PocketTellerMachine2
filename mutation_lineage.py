# === FILE: mutation_lineage.py ===
import os
import json
from datetime import datetime

LINEAGE_FILE = "evolution/mutation_family_tree.json"
os.makedirs(os.path.dirname(LINEAGE_FILE), exist_ok=True)

def init_family_tree():
    if not os.path.exists(LINEAGE_FILE):
        with open(LINEAGE_FILE, "w") as f:
            json.dump({}, f, indent=2)

def log_mutation(parent_file, child_file, reason="parameter adjustment"):
    init_family_tree()

    with open(LINEAGE_FILE, "r") as f:
        tree = json.load(f)

    parent = os.path.basename(parent_file)
    child = os.path.basename(child_file)

    if parent not in tree:
        tree[parent] = {
            "descendants": [],
            "mutations": []
        }

    # Add child to descendants
    tree[parent]["descendants"].append({
        "child": child,
        "mutation_reason": reason,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Also log in legacy format
    tree[parent]["mutations"].append({
        "mutated": child,
        "timestamp": datetime.utcnow().isoformat(),
        "reason": reason
    })

    with open(LINEAGE_FILE, "w") as f:
        json.dump(tree, f, indent=2)

    print(f"[FAMILY TREE] {child} logged as descendant of {parent}")