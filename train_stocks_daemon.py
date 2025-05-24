# train_stocks_daemon.py

import time
from train_stocks import run_full_stock_training
from datetime import datetime

def stock_training_loop():
    while True:
        print(f"[{datetime.now().isoformat()}] [DAEMON]: Starting full stock training cycle...")
        try:
            run_full_stock_training()
            print(f"[{datetime.now().isoformat()}] [DAEMON]: Training cycle complete.")
        except Exception as e:
            print(f"[{datetime.now().isoformat()}] [DAEMON ERROR]: {e}")
        time.sleep(60 * 60)  # Sleep 1 hour before next loop

if __name__ == "__main__":
    stock_training_loop()