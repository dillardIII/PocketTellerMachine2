def adjust_strategy_based_on_bias(strategy_key, bias):
    if bias == "Bullish Bias":
        return f"{strategy_key}_Aggressive"
    elif bias == "Bearish Bias":
        return f"{strategy_key}_Defensive"
    else:
        return f"{strategy_key}_Neutral"

# Example usage
adjusted_strategy = adjust_strategy_based_on_bias("RSI_Reversal", "Bullish Bias")
print("[ADJUSTED STRATEGY]:", adjusted_strategy)