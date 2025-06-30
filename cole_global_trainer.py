from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_global_trainer.py

import time
import logging
from train_stocks import run_stock_training
from train_options import run_option_training
from train_crypto import run_crypto_training
from train_forex import run_forex_training
from train_indexes import run_index_training
from train_etfs import run_etf_training

logging.basicConfig(
    filename="data/global_trainer.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def global_training_loop():
    logging.info("[PTM Global Trainer] Starting all-market training loop...")
    
    while True:
        try:
            run_stock_training()
            run_option_training()
            run_crypto_training()
            run_forex_training()
            run_index_training()
            run_etf_training()
            
            logging.info("[PTM Global Trainer] Completed full loop. Sleeping 30 min...")
        except Exception as e:
            logging.error(f"[Trainer Error] {e}")
        
        time.sleep(1800)  # Sleep 30 minutes

if __name__ == "__main__":
    global_training_loop()

def log_event():ef drop_files_to_bridge():