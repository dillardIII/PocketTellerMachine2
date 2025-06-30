# === FILE: vault_profit_trigger.py ===

# 📃 Vault Profit Trigger – Monitors the vault and sends real ETH payouts

import time
import os
from wallet_payout_engine import payout_from_profit_log
from utils.logger import log_event

# Interval in seconds (5 minutes)
PROFIT_CHECK_INTERVAL = 300

def vault_profit_loop():
    print("[VaultTrigger] ⏰ Starting vault profit loop...")
    
    while True:
        try:
            log_event("VaultProfitLoop", {"status": "Checking for new profits"})
            
            result = payout_from_profit_log()
            
            if result:
                log_event("VaultProfitLoop", {"tx_hash": result})
        
        except Exception as e:
            log_event("VaultProfitLoop", {"error": str(e)})
        
        time.sleep(PROFIT_CHECK_INTERVAL)

# === Start loop if run directly ===
if __name__ == '__main__':
    vault_profit_loop()