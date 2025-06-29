# === FILE: task_q_writer.py ===
# 🤖 GPT Task Queue Writer – feeds commands into gpt_task_queue.txt for ReplitTaskSQ to execute

def add_task(command_line):
    with open("gpt_task_queue.txt", "a") as f:
        f.write(command_line + "\n")
    print(f"[TaskQWriter] 📝 Queued task: {command_line}")

# === Examples ===
if __name__ == "__main__":
    add_task("create_file empire_core.py")
    add_task("write_line empire_core.py print('👑 Empire online')")
    add_task("run_script empire_core.py")