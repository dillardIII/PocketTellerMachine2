from ghost_env import INFURA_KEY, VAULT_ADDRESS
Certainly! Below is a Python file implementing a simple moving average crossover trading strategy. This strategy uses two moving averages: a short-term moving average and a long-term moving average. When the short-term moving average crosses above the long-term moving average, it generates a buy signal. Conversely, when the short-term moving average crosses below the long-term moving average, it generates a sell signal.

```python
# trading_strategy_2.py

import pandas as pd
import numpy as np

def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short-term and long-term moving averages.

    :param data: Pandas DataFrame with at least a 'Close' column
    :param short_window: Integer, period for short-term moving average
    :param long_window: Integer, period for long-term moving average
    :return: Pandas DataFrame with 'Short_MA' and 'Long_MA' columns
    """
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    return data

def generate_signals(data):
    """
    Generate buy and sell signals based on moving average crossover strategy.

    :param data: Pandas DataFrame with 'Short_MA' and 'Long_MA' columns
    :return: Pandas DataFrame with 'Signal' column (1 for buy, -1 for sell, 0 for hold)
    """
    data['Signal'] = 0
    data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1
    data.loc[data['Short_MA'] < data['Long_MA'], 'Signal'] = -1
    return data

def backtest_strategy(data, initial_capital=10000):
    """
    Backtest the trading strategy.

    :param data: Pandas DataFrame with at least 'Signal' and 'Close' columns
    :param initial_capital: Float, initial amount of capital for trading
    :return: Final portfolio value (float) and Pandas Series of portfolio values over time
    """
    positions = data['Signal'].shift().fillna(0)
    daily_returns = positions * data['Close'].pct_change().fillna(0)

    portfolio_values = (1 + daily_returns).cumprod() * initial_capital
    final_value = portfolio_values.iloc[-1]

    return final_value, portfolio_values

def run_strategy(data, short_window=10, long_window=50, initial_capital=10000):
    """
    Run the complete trading strategy.

    :param data: Pandas DataFrame with at least a 'Close' column
    :param short_window: Integer, window for short-term moving average
    :param long_window: Integer, window for long-term moving average
    :param initial_capital: Float, initial amount of capital for trading
    :return: Final portfolio value (float) and DataFrame containing signals and portfolio values
    """
    data = calculate_moving_averages(data, short_window, long_window)
    data = generate_signals(data)
    final_value, portfolio_values = backtest_strategy(data, initial_capital)
    
    data['Portfolio_Value'] = portfolio_values
    
    return final_value, data

# Example usage:
# if __name__ == "__main__":
#     data = pd.read_csv('your_price_data.csv')
#     final_value, strategy_data = run_strategy(data)
#     print(f"Final portfolio value: {final_value}")
#     strategy_data[['Close', 'Short_MA', 'Long_MA', 'Signal', 'Portfolio_Value']].to_csv('strategy_results.csv')
```

### Explanation:
1. **Moving Averages Calculation**: The `calculate_moving_averages` function computes the short-term and long-term moving averages using rolling windows.

2. **Signal Generation**: The `generate_signals` function determines whether the strategy is in a buy, sell, or hold state by comparing the moving averages.

3. **Backtest**: The `backtest_strategy` function simulates trading over historical data, updating the portfolio's value based on the positions suggested by the signals.

4. **Run Strategy**: The `run_strategy` function is the main function that orchestrates the calculation of moving averages, signal generation, and strategy backtesting. It returns the final portfolio value and a DataFrame with all calculated data.

To execute the strategy, make sure you have historical price data formatted as a CSV file with at least a 'Close' column. Adjust the file path and names as necessary.