import time
from ptm_gpt_agent import run_ptm_gpt_agent

def gpt_thinking_loop():
    while True:
        try:
            run_ptm_gpt_agent("Suggest a new smart feature for PTM.")
        except Exception as e:
            print("[GPT Thinking] Error:", e)
        time.sleep(600)  # Think every 10 minutes