from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: family_tree_graph.py ===
import os
import json
import matplotlib.pyplot as plt
import networkx as nx

LINEAGE_FILE = "evolution/mutation_family_tree.json"

def draw_family_tree(output_file="evolution/family_tree.png"):
    if not os.path.exists(LINEAGE_FILE):
        print("[FAMILY TREE] No lineage data found.")
        return

    with open(LINEAGE_FILE, "r") as f:
        tree = json.load(f)

    G = nx.DiGraph()

    for parent, info in tree.items():
        for descendant in info["descendants"]:
            child = descendant["child"]
            label = descendant.get("mutation_reason", "mutated")
            timestamp = descendant.get("timestamp", "")
            G.add_edge(parent, child, label=label + f"\n{timestamp}")

    pos = nx.spring_layout(G, k=0.5, iterations=100)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=2800, node_color="#E3F2FD", edge_color="#90CAF9", font_size=8, font_weight="bold", arrows=True)
    
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    os.makedirs("evolution", exist_ok=True)
    plt.title("🧬 PTM Mutation Family Tree", fontsize=14)
    plt.tight_layout()
    output_path = os.path.join("evolution", output_file)
    plt.savefig(output_path)
    print(f"[FAMILY TREE] Diagram saved to {output_path}")
    return output_path

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():