# Simple Moving Average (SMA) Strategy
def run_strategy():
    prices = [100, 105, 110, 115, 120]
    sma = sum(prices) / len(prices)
    print(f"SMA: {sma}")
    if prices[-1] > sma:
        print("Signal: Buy")
    else:
        print("Signal: Hold")

if __name__ == "__main__":
    run_strategy()
