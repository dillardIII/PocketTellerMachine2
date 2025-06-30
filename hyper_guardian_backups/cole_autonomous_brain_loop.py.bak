import time
import random
from datetime import datetime
from test_fusion_predictor import predict_stock_bias
from test_fusion_strategy_adjuster import adjust_strategy_based_on_bias
from brain import execute_trade
from cole_memory_brain import log_memory_event
from test_auto_evolve_from_trades import analyze_strategy_performance
from cole_agent_team import ai_team_meeting
from cole_agent_team_v2_emotional import ai_team_debate

SYMBOLS = ["AAPL", "TSLA", "AMC", "NVDA"]
BASE_STRATEGIES = ["RSI_Reversal", "SMA_Cross", "Iron_Condor"]

# === Autonomous Decision Loop (Basic Mode) ===
def autonomous_ai_brain_loop(cycles=5, wait_seconds=10):
    for cycle in range(cycles):
        print(f"\n[CYCLE {cycle + 1} STARTED]: {datetime.now().isoformat()}")
        
        for symbol in SYMBOLS:
            base_strategy = random.choice(BASE_STRATEGIES)
            bias = predict_stock_bias(symbol)
            adjusted_strategy = adjust_strategy_based_on_bias(base_strategy, bias)
            
            if "Bullish" in bias:
                result = round(random.uniform(10, 100), 2)
            elif "Bearish" in bias:
                result = round(random.uniform(-100, -10), 2)
            else:
                result = round(random.uniform(-20, 20), 2)
            
            trade = execute_trade(symbol, adjusted_strategy, result)
            log_memory_event("trades", trade)
            print("[AUTONOMOUS AI TRADE]:", trade)
        
        print(f"[CYCLE {cycle + 1} COMPLETED]. Waiting {wait_seconds} seconds before next cycle.")
        time.sleep(wait_seconds)

# === Autonomous Decision Loop with Corrections (Evolution Mode) ===
def autonomous_ai_brain_loop_with_corrections(cycles=5, wait_seconds=10):
    for cycle in range(cycles):
        print(f"\n[CYCLE {cycle + 1} STARTED]: {datetime.now().isoformat()}")
        
        for symbol in SYMBOLS:
            base_strategy = random.choice(BASE_STRATEGIES)
            bias = predict_stock_bias(symbol)
            adjusted_strategy = adjust_strategy_based_on_bias(base_strategy, bias)
            
            if "Bullish" in bias:
                result = round(random.uniform(10, 100), 2)
            elif "Bearish" in bias:
                result = round(random.uniform(-100, -10), 2)
            else:
                result = round(random.uniform(-20, 20), 2)
            
            trade = execute_trade(symbol, adjusted_strategy, result)
            log_memory_event("trades", trade)
            print("[AUTONOMOUS AI TRADE]:", trade)
        
        print("[AI CHECKPOINT]: Analyzing strategy performance...")
        analyze_strategy_performance()
        
        print(f"[CYCLE {cycle + 1} COMPLETED]. Waiting {wait_seconds} seconds before next cycle.")
        time.sleep(wait_seconds)

# === Autonomous Multi-Agent AI Team Loop ===
def autonomous_ai_brain_team_loop(symbols):
    for symbol in symbols:
        ai_team_meeting(symbol)

# === Autonomous Emotional AI Team Debate Loop ===
def autonomous_ai_emotional_team_loop(symbols):
    for symbol in symbols:
        ai_team_debate(symbol)

# === MAIN MODE SELECTOR ===
if __name__ == "__main__":
    print("\n[MODE]: Basic AI Brain Loop Starting...")
    autonomous_ai_brain_loop(cycles=3, wait_seconds=5)
    
    print("\n[MODE]: Enhanced AI Brain Loop with Corrections Starting...")
    autonomous_ai_brain_loop_with_corrections(cycles=3, wait_seconds=5)

    print("\n[MODE]: Multi-Agent AI Brain Team Loop Starting...")
    autonomous_ai_brain_team_loop(["TSLA", "AAPL", "NVDA"])

    print("\n[MODE]: Emotional AI Team Debate Loop Starting...")
    autonomous_ai_emotional_team_loop(["TSLA", "AAPL", "NVDA"])