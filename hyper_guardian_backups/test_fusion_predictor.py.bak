from cole_memory_brain import load_memory

def predict_stock_bias(symbol):
    memory = load_memory()
    journals = memory.get("journals", [])
    related = [j for j in journals if j.get("symbol") == symbol]

    bullish_signals = 0
    bearish_signals = 0

    for j in related:
        sentiment = j.get("impact", j.get("sentiment", "")).lower()
        if "bullish" in sentiment:
            bullish_signals += 1
        elif "bearish" in sentiment:
            bearish_signals += 1

    if bullish_signals > bearish_signals:
        prediction = "Bullish Bias"
    elif bearish_signals > bullish_signals:
        prediction = "Bearish Bias"
    else:
        prediction = "Neutral Bias"

    print(f"[PREDICTION]: {symbol} → {prediction} (Bullish: {bullish_signals} / Bearish: {bearish_signals})")
    return prediction

# Example predictions
predict_stock_bias("TSLA")
predict_stock_bias("AMC")
predict_stock_bias("NVDA")