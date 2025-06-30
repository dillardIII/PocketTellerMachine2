from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mutation_chart.py ===
import matplotlib.pyplot as plt
import os
import json

def plot_mutation_history(history, title="Mutation Evolution", output_file="mutation_evolution.png"):
    generations = []
    scores = []
    labels = []

    for entry in history:
        gen = entry["generation"]
        score_text = entry["score"]
        score_a = int(score_text.split("A:")[1].split("|")[0].strip())

        generations.append(gen)
        scores.append(score_a)
        labels.append(entry["strategy"])

    plt.figure(figsize=(10, 6))
    plt.plot(generations, scores, marker='o', linestyle='-', label='Mutated Strategy Score')

    for i, label in enumerate(labels):
        plt.text(generations[i], scores[i] + 0.2, label, fontsize=8, ha='center')

    plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Score (Higher = Better)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    output_dir = "duel_logs"
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, output_file)
    plt.savefig(full_path)
    print(f"[CHART] Evolution chart saved to {full_path}")
    return full_path

def log_event():ef drop_files_to_bridge():