def assign_pattern_confidence(strategy_results):
    win_trades = [r for r in strategy_results if r > 0]
    win_rate = len(win_trades) / len(strategy_results) if strategy_results else 0
    if win_rate >= 0.7:
        return "High Confidence"
    elif win_rate >= 0.5:
        return "Moderate Confidence"
    else:
        return "Low Confidence"

# Example strategy test results
sma_cross_results = [5, 10, -3, 7, 8, -2, 4, 9, -1, 6]
rsi_reversal_results = [-5, -3, 2, -4, -1, -3, 1, -6, 0, -2]

print("[CONFIDENCE SCORE]: SMA Cross:", assign_pattern_confidence(sma_cross_results))
print("[CONFIDENCE SCORE]: RSI Reversal:", assign_pattern_confidence(rsi_reversal_results))