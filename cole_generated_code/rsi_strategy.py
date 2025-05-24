# Relative Strength Index (RSI) Strategy
def run_strategy():
    rsi = 72
    print(f"RSI: {rsi}")
    if rsi > 70:
        print("Signal: Overbought - Consider selling")
    elif rsi < 30:
        print("Signal: Oversold - Consider buying")
    else:
        print("Signal: Neutral")

if __name__ == "__main__":
    run_strategy()
