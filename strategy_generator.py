import os
from cole_code_writer import cole_write_code
from assistants.malik import malik_report

GENERATED_FOLDER = "cole_generated_code"
os.makedirs(GENERATED_FOLDER, exist_ok=True)

def generate_strategy_replacement(failed_strategy_name):
    base_prompt = f"Create a new trading strategy to replace {failed_strategy_name}. Include buy/sell logic and explain why it may outperform the original."

    print(f"[STRATEGY GEN] Generating replacement for: {failed_strategy_name}")
    malik_report(f"[Strategy Generator] Replacing failed strategy: {failed_strategy_name}")

    try:
        code = cole_write_code(base_prompt)
        filename = f"{GENERATED_FOLDER}/{failed_strategy_name.replace(' ', '_')}_v2.py"

        with open(filename, "w") as f:
            f.write(code)

        print(f"[STRATEGY GEN] Saved new strategy: {filename}")
        malik_report(f"[Strategy Generator] New version saved: {filename}")
        return filename

    except Exception as e:
        print(f"[STRATEGY GEN ERROR] {e}")
        return None