# test_self_learning_generator.py

from cole_self_learning_task_generator import generate_self_learning_tasks, run_self_learning_generator

# === Manual Preview of Generated Tasks ===
print("=== Previewing Generated Self-Learning Tasks ===")
tasks = generate_self_learning_tasks()
print("[TASK GENERATION RESULT]:")
for task in tasks:
    print(task)

# === Trigger Full Self-Learning Task Generator ===
print("\n=== Running Cole's Self-Learning Generator Manually ===")
run_self_learning_generator()