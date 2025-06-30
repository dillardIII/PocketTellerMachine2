from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_prompt_generator.py ===

def generate_prompt(task):
    """
    Converts a task (dict or string) into a GPT-style prompt.
    """
    try:
        if isinstance(task, dict):
            task_name = task.get("name") or task.get("task", "general_task")
            task_input = task.get("input", "")
        elif isinstance(task, str):
            task_name = "general_task"
            task_input = task
        else:
            return "Invalid task format"

        if task_name == "predict_market_trend":
            return "Develop an algorithm for predicting market trends using historical and news data."

        elif task_name == "analyze_trade_result":
            return "Analyze the outcome of the most recent trade and provide insights."

        elif task_name == "cole_write_code":
            return f"Write Python code to: {task_input}"

        else:
            return f"Run task: {task_name} with input: {task_input}"

    except Exception as e:
        return f"Prompt generation failed: {str(e)}"

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():