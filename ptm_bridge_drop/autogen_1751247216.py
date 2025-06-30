from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a Python trading strategy focusing on a simple moving average crossover with some additional conditions to enhance its logic. This strategy is primarily designed for educational purposes and may need further refinement for real-life application:

```python
import pandas as pd
import numpy as np

def calculate_sma(data, window_size):
    """Calculates the Simple Moving Average (SMA) for the given data."""
    return data.rolling(window=window_size).mean()

def calculate_rsi(data, window_size=14):
    """Calculates the Relative Strength Index (RSI) for the given data."""
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_signals(data, sma_short_window=50, sma_long_window=200, rsi_window=14, rsi_oversold=30, rsi_overbought=70):
    """Generates trading signals based on SMA crossovers and RSI conditions."""
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data
    signals['sma_short'] = calculate_sma(data, sma_short_window)
    signals['sma_long'] = calculate_sma(data, sma_long_window)
    signals['rsi'] = calculate_rsi(data, rsi_window)

    # Buy signal: Short SMA crosses above Long SMA and RSI indicates oversold conditions.
    signals['buy_signal'] = ((signals['sma_short'] > signals['sma_long']) &
                             (signals['sma_short'].shift(1) <= signals['sma_long'].shift(1)) &
                             (signals['rsi'] < rsi_oversold))

    # Sell signal: Short SMA crosses below Long SMA and RSI indicates overbought conditions.
    signals['sell_signal'] = ((signals['sma_short'] < signals['sma_long']) &
                              (signals['sma_short'].shift(1) >= signals['sma_long'].shift(1)) &
                              (signals['rsi'] > rsi_overbought))

    return signals

if __name__ == "__main__":
    # Example usage with dummy data
    dates = pd.date_range('2020-01-01', '2020-12-31')
    np.random.seed(0)
    prices = pd.Series(np.random.normal(loc=100, scale=10, size=len(dates)), index=dates)

    # Generating signals
    signals = generate_signals(prices)

    # Extract buy and sell signals
    buy_signals = signals[signals['buy_signal']]
    sell_signals = signals[signals['sell_signal']]

    print("Buy Signals:")
    print(buy_signals[['price']])

    print("\nSell Signals:")
    print(sell_signals[['price']])
```

### Brief Explanation:
- **SMA Crossover:** The strategy uses two Simple Moving Averages (SMA), one short-term (`sma_short`) and the other long-term (`sma_long`). A buy signal is generated when the short-term SMA crosses above the long-term SMA, and a sell signal is generated when it crosses below.
- **RSI Filter:** To enhance the strategy, conditions based on the Relative Strength Index (RSI) are added to avoid false signals during non-trending periods. Buy signals are only valid if the RSI is below `rsi_oversold`, indicating an oversold condition, and sell signals are valid if the RSI is above `rsi_overbought`.
- **Customization:** Window sizes, RSI thresholds, and other parameters can be tuned for speciﬁc markets or assets.

This script should be tested thoroughly before utilizing any real capital, and adaptations might be required for integration into a live system or for handling specific data feeds.