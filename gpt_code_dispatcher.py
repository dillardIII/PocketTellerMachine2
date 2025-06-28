# === FILE: gpt_code_dispatcher.py ===
# 🚀 GPT Code Dispatcher – Writes generated code into gpt_outbox for bridge pickup

import os

OUTBOX_DIR = "gpt_outbox"

def dispatch_code(filename: str, code: str):
    os.makedirs(OUTBOX_DIR, exist_ok=True)
    file_path = os.path.join(OUTBOX_DIR, filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[Dispatcher] ✅ Code dispatched: {filename}")
    except Exception as e:
        print(f"[Dispatcher] ❌ Error writing file: {e}")

# === Example Usage ===
if __name__ == "__main__":
    # Replace this with dynamically generated code from GPT
    sample_code = "# Example: Hello World Script\nprint('Hello from GPT Dispatcher')"
    dispatch_code("hello_gpt.py", sample_code)