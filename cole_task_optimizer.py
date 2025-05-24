# === FILE: cole_task_optimizer.py ===

def cole_optimize_tasks(task_list):
    if not task_list:
        print("[Optimizer] Received empty task list.")
        return []

    optimized = []
    for task in task_list:
        if not isinstance(task, dict):
            print("[Optimizer] Skipping non-dict task:", task)
            continue

        priority = task.get('priority', 0)
        optimized.append((priority, task))

    # Sort by priority descending
    optimized.sort(reverse=True)
    return [task for _, task in optimized]