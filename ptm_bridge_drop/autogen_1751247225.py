from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a Python trading strategy script. This strategy uses a combination of moving averages and the Relative Strength Index (RSI) for trading signals. The script assumes that you have historical price data available and that you are using the pandas library for data manipulation and analysis.

```python
import pandas as pd

def moving_average(data: pd.Series, window: int) -> pd.Series:
    """Calculate the moving average over a specified window."""
    return data.rolling(window=window).mean()

def relative_strength_index(data: pd.Series, window: int) -> pd.Series:
    """Calculate the Relative Strength Index (RSI) over a specified window."""
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_signals(prices: pd.DataFrame, short_window: int = 40, long_window: int = 100, rsi_window: int = 14, rsi_overbought: int = 70, rsi_oversold: int = 30) -> pd.DataFrame:
    """Generate buy/sell signals based on moving averages and RSI."""
    signals = pd.DataFrame(index=prices.index)
    signals['Price'] = prices['Close']
    
    # Calculate short and long moving averages
    signals['Short_MA'] = moving_average(signals['Price'], short_window)
    signals['Long_MA'] = moving_average(signals['Price'], long_window)
    
    # Calculate RSI
    signals['RSI'] = relative_strength_index(signals['Price'], rsi_window)
    
    # Initialize signal column
    signals['Signal'] = 0
    
    # Buy signal:
    # When short MA crosses above long MA and RSI is below the oversold threshold
    buy_condition = (signals['Short_MA'] > signals['Long_MA']) & (signals['RSI'] < rsi_oversold)
    
    # Sell signal:
    # When short MA crosses below long MA or RSI is above the overbought threshold
    sell_condition = (signals['Short_MA'] < signals['Long_MA']) | (signals['RSI'] > rsi_overbought)
    
    signals.loc[buy_condition, 'Signal'] = 1
    signals.loc[sell_condition, 'Signal'] = -1
    
    signals['Position'] = signals['Signal'].diff()
    
    return signals

# Example usage:
# Assuming 'data' is a DataFrame with historical data and a 'Close' column for closing prices.
# data = pd.read_csv('historical_data.csv', parse_dates=True, index_col='Date')
# trading_signals = generate_signals(data)
# print(trading_signals)
```

### Key Components of the Strategy:
- **Moving Averages**: The strategy uses a short-term and a long-term moving average to identify potential buy/sell opportunities based on whether the shorter average crosses above or below the longer average.
- **Relative Strength Index (RSI)**: RSI is used to identify overbought or oversold conditions. The default values are 70 for overbought and 30 for oversold conditions. Adjust these parameters as needed.
- **Signal Generation**: Signals are generated based on the moving average crossovers and RSI thresholds. A signal of 1 indicates a buy, and -1 indicates a sell.

### How to Use:
1. Load your historical data into a pandas DataFrame with a 'Close' column.
2. Call the `generate_signals` function with this DataFrame to get the buy/sell signals.
3. Analyze the signals to implement them in a trading system or backtesting framework. 

You can adjust the parameters like window sizes and RSI thresholds to fit your trading preferences.