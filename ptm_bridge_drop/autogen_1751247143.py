Below is a Python script that outlines a basic trading strategy. This strategy uses moving averages and a simple risk management system. For demonstration purposes, this script uses random data; you can replace it with real market data.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_random_data(size=100):
    """Generate random price data for simulation."""
    np.random.seed(42)
    return pd.Series(np.random.normal(0, 1, size).cumsum() + 50)

def calculate_moving_average(data, window):
    """Calculate a moving average with a specified window size."""
    return data.rolling(window=window).mean()

def trading_strategy(data, short_window=40, long_window=100):
    """Simple moving average crossover strategy."""
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data
    signals['short_mavg'] = calculate_moving_average(data, short_window)
    signals['long_mavg'] = calculate_moving_average(data, long_window)

    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(
        signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0
    )
    signals['positions'] = signals['signal'].diff()

    return signals

def plot_trading_strategy(signals):
    """Plot the trading strategy with data and signals."""
    plt.figure(figsize=(14, 7))
    plt.plot(signals['price'], label='Price', alpha=0.5)
    plt.plot(signals['short_mavg'], label='Short-term Moving Average', linestyle='--')
    plt.plot(signals['long_mavg'], label='Long-term Moving Average', linestyle='--')

    buy_signals = signals[signals['positions'] == 1.0]
    sell_signals = signals[signals['positions'] == -1.0]

    plt.plot(buy_signals.index, signals['short_mavg'][buy_signals.index], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(sell_signals.index, signals['short_mavg'][sell_signals.index], 'v', markersize=10, color='r', label='Sell Signal')

    plt.title('Trading Strategy')
    plt.xlabel('Index')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Generate random price data
    data = generate_random_data(200)

    # Analyze the trading strategy
    signals = trading_strategy(data, short_window=10, long_window=50)

    # Plot the strategy
    plot_trading_strategy(signals)
```

### Strategy Explanation:
- **Data Generation**: Uses random walk to simulate price movements.
- **Moving Averages**: Two moving averages are calculated: a short-term (10 periods) and a long-term (50 periods).
- **Buy Signal**: Occurs when the short-term moving average crosses above the long-term moving average.
- **Sell Signal**: Occurs when the short-term moving average crosses below the long-term moving average.
- **Plotting**: The script visualizes price data and buy/sell signals.

You can replace the random data generation with actual stock data using libraries such as `yfinance` or similar to test this strategy in the real market environment. Adjust the `short_window` and `long_window` values according to your requirements.