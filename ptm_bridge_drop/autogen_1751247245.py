Sure, I'll provide you with a Python script for a new trading strategy. This strategy will be based on a simple combination of simple moving averages (SMA) and the Relative Strength Index (RSI). The strategy will go long when a short-term SMA crosses above a long-term SMA and the RSI indicates an oversold condition, and go short when the short-term SMA crosses below the long-term SMA and the RSI indicates an overbought condition.

```python
import pandas as pd
import numpy as np

def calculate_sma(data, window):
    """
    Calculate Simple Moving Average (SMA).
    
    :param data: pd.Series or pd.DataFrame containing the 'Close' price.
    :param window: int, window length for the SMA.
    :return: pd.Series or pd.DataFrame, SMA values.
    """
    return data.rolling(window=window).mean()

def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).
    
    :param data: pd.Series of stock prices.
    :param window: int, window length (default is 14).
    :return: pd.Series, RSI values.
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def trading_strategy(data, short_window=50, long_window=200, rsi_window=14, rsi_oversold=30, rsi_overbought=70):
    """
    Implement a trading strategy based on SMA and RSI.

    :param data: pd.DataFrame with 'Close' price ready.
    :param short_window: int, the short SMA window.
    :param long_window: int, the long SMA window.
    :param rsi_window: int, RSI calculation window.
    :param rsi_oversold: int, oversold level for RSI.
    :param rsi_overbought: int, overbought level for RSI.
    :return: pd.DataFrame, original data with signals and position.
    """
    data['SMA_Short'] = calculate_sma(data['Close'], short_window)
    data['SMA_Long'] = calculate_sma(data['Close'], long_window)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)
    
    data['Signal'] = 0
    data['Signal'][(data['SMA_Short'].shift(1) < data['SMA_Long'].shift(1)) & 
                   (data['SMA_Short'] > data['SMA_Long']) &
                   (data['RSI'] < rsi_oversold)] = 1
    
    data['Signal'][(data['SMA_Short'].shift(1) > data['SMA_Long'].shift(1)) & 
                   (data['SMA_Short'] < data['SMA_Long']) &
                   (data['RSI'] > rsi_overbought)] = -1
    
    data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')
    
    return data

def backtest(data):
    """
    Backtest the trading strategy.

    :param data: DataFrame with 'Close', 'Signal', and 'Position'
    :return: total returns from the strategy.
    """
    data['Market Return'] = data['Close'].pct_change()
    data['Strategy Return'] = data['Market Return'] * data['Position'].shift(1)
    cumulative_strategy_return = (1 + data['Strategy Return'].dropna()).cumprod()[-1]
    
    return cumulative_strategy_return

# Example usage
if __name__ == "__main__":
    # This is just a placeholder DataFrame; replace with your data loading logic
    data = pd.DataFrame({
        'Close': np.random.randn(1000).cumsum()  # Random data simulating prices
    })

    strategy_data = trading_strategy(data)
    total_return = backtest(strategy_data)
    print(f"Total Strategy Return: {total_return:.2f}")
```

This script implements a trading strategy based on simple moving averages and RSI indicators. You can expand or modify this strategy with additional logic or different financial indicators to suit your aims. Always backtest any strategy with historical data to validate its performance before using it in a live trading environment.