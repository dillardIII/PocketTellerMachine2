# === FILE: auto_file_writer_gpt.py ===
# 📜 AutoFileWriterGPT – Grimoire of evolving trading spells
# 🧬 Feeds empire with ever-mutating trading strategies (spells) via GPT

import time
import random
import json
import openai

QUEUE_FILE = "gpt_task_queue.txt"
GPT_PROMPTS = [
    "Write a Python script for an RSI breakout trading strategy with risk management.",
    "Generate a volatility mean-reversion bot with trailing stops.",
    "Create a machine learning predictor that forecasts the next candlestick.",
    "Design an options flow heatmap analyzer that logs large unusual trades.",
    "Make a liquidity sweep hunter that detects big bid-ask changes."
]

openai.api_key = os.getenv("OPENAI_API_KEY")  # Pulls from your env var

def queue_task(line):
    with open(QUEUE_FILE, "a") as f:
        f.write(line + "\n")
    print(f"[AutoFileWriterGPT] 📝 Queued: {line}")

def generate_trading_spell():
    prompt = random.choice(GPT_PROMPTS)
    print(f"[AutoFileWriterGPT] 🪄 Asking GPT: {prompt}")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a quantitative trading strategist."},
                {"role": "user", "content": prompt}
            ]
        )
        code = response["choices"][0]["message"]["content"]
        filename = f"spell_{int(time.time())}.py"

        with open(filename, "w") as f:
            f.write(code)
        print(f"[AutoFileWriterGPT] ✨ Created new spell file: {filename}")

        # Schedule it for execution
        queue_task(f"run_script {filename}")

    except Exception as e:
        print(f"[AutoFileWriterGPT] ❌ GPT call failed: {e}")

def auto_writer_loop():
    while True:
        generate_trading_spell()
        wait_time = random.choice([180, 300, 420])  # slower so each spell is substantial
        print(f"[AutoFileWriterGPT] ⏳ Sleeping {wait_time}s before next spell...")
        time.sleep(wait_time)

if __name__ == "__main__":
    print("[AutoFileWriterGPT] 🚀 Starting your perpetual trading grimoire...")
    auto_writer_loop()