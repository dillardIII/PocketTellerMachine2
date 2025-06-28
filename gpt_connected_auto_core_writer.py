# === FILE: gpt_connected_auto_core_writer.py ===
# ✅ Works with openai==1.93.0 and later

import os
import time
from openai import OpenAI

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def write_file_to_bridge(filename, code):
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    path = os.path.join(BRIDGE_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"[GPTAutoWriter] ✅ Dropped file: {path}")

def generate_code_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You write standalone .py files."},
                {"role": "user", "content": prompt}
            ]
        )
        code = response.choices[0].message.content
        return code
    except Exception as e:
        print(f"[GPTAutoWriter] ⚠️ GPT error: {e}")
        return None

def interactive_loop():
    print("[GPTAutoWriter] 🤖 Ready. Type your strategy or code request. Type 'exit' to quit.")
    counter = 0
    while True:
        user_input = input("\n[GPTAutoWriter] 💬 What file should I generate?: ").strip()
        if user_input.lower() == "exit":
            print("[GPTAutoWriter] 👋 Exiting...")
            break
        code = generate_code_with_gpt(user_input)
        if code:
            filename = f"gpt_generated_{counter}.py"
            write_file_to_bridge(filename, code)
            counter += 1
        time.sleep(1)

if __name__ == "__main__":
    interactive_loop()