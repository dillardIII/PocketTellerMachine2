from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide you with a simple Python trading strategy script that utilizes a moving average crossover strategy. The script will simulate a trading strategy that uses both a short-term and a long-term moving average to generate buy and sell signals.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def moving_average_crossover_strategy(ticker, start_date, end_date, short_window=40, long_window=100):
    """
    Implements a moving average crossover strategy.
    
    :param ticker: Stock ticker symbol as a string.
    :param start_date: Start date for historical data in 'YYYY-MM-DD' format.
    :param end_date: End date for historical data in 'YYYY-MM-DD' format.
    :param short_window: The short moving average window.
    :param long_window: The long moving average window.
    :return: DataFrame with historical price data and trading signals.
    """
    
    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculate moving averages
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    
    # Initialize signal column
    data['Signal'] = 0
    
    # Generate buy/sell signals
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    
    # Create positions (1 for buy, -1 for sell)
    data['Position'] = data['Signal'].diff()
    
    # Plot
    plt.figure(figsize=(12, 8))
    plt.plot(data['Close'], label=f'{ticker} Close Price', color='blue', alpha=0.5)
    plt.plot(data['Short_MA'], label='Short Moving Average', color='green', alpha=0.5)
    plt.plot(data['Long_MA'], label='Long Moving Average', color='red', alpha=0.5)
    plt.scatter(data.index, data['Position'] == 1, label='Buy Signal', marker= '^', color='green', lw=3)
    plt.scatter(data.index, data['Position'] == -1, label='Sell Signal', marker= 'v', color='red', lw=3)
    plt.title(f'Moving Average Crossover Strategy on {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    
    return data


# Example usage
if __name__ == "__main__":
    strategy_data = moving_average_crossover_strategy('AAPL', '2022-01-01', '2023-01-01')
    print(strategy_data.tail())
```

### Explanation:
- **Moving Averages**: The strategy uses a short-term moving average (`Short_MA`) and a long-term moving average (`Long_MA`) to determine buy or sell signals. When the short-term average crosses above the long-term average, a buy signal is generated. Conversely, a sell signal is generated when the short-term average crosses below the long-term average.
- **Signals and Positions**: Buy signals (represented by a 1) and sell signals (represented by -1) are stored in the `Signal` column. The change in signals is used to determine `Position`: `1` for entering a position (buy) and `-1` for exiting (sell).
- **Plotting**: The script generates a plot showing the closing price, short and long moving averages, and buy/sell signals as arrows on the plot.

You can run this script to simulate moving average crossovers for a given stock within specified dates. Adjust `short_window` and `long_window` to tune the sensitivity of the strategy.