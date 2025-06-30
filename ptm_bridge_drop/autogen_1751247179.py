from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a Python script for a simple moving average crossover trading strategy. This strategy involves two moving averages: a short-term moving average and a long-term moving average. When the short-term moving average crosses above the long-term moving average, it's a buy signal. When it crosses below, it's a sell signal.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def moving_average_crossover_strategy(data, short_window=40, long_window=100):
    """
    Implements a moving average crossover trading strategy.
    
    Parameters:
    - data: DataFrame with 'Close' price column.
    - short_window: The window size for the short-term moving average.
    - long_window: The window size for the long-term moving average.
    
    Returns:
    - signals: DataFrame containing the trading signals and moving averages.
    """
    # Assert that the 'Close' column is in the data
    assert 'Close' in data.columns, "The data should contain a 'Close' column."
    
    # Create a signal DataFrame with the same index
    signals = pd.DataFrame(index=data.index)
    signals['Close'] = data['Close']
    
    # Create short simple moving average (SMA)
    signals['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    
    # Create long simple moving average (SMA)
    signals['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    # Create signals
    signals['Signal'] = 0.0
    signals['Signal'][short_window:] = np.where(signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1.0, 0.0)
    
    # Generate trading orders
    signals['Position'] = signals['Signal'].diff()

    return signals

def plot_signals(signals):
    """
    Plots the trading signals and moving averages.
    
    Parameters:
    - signals: DataFrame containing the trading signals and moving averages.
    """
    # Plot close price, short and long moving averages
    plt.figure(figsize=(14, 7))
    plt.plot(signals['Close'], label='Close Price', color='black', alpha=0.5)
    plt.plot(signals['Short_MA'], label='Short Moving Average', color='blue', alpha=0.9)
    plt.plot(signals['Long_MA'], label='Long Moving Average', color='red', alpha=0.9)
    
    # Plot the buy signals
    plt.plot(signals.loc[signals.Position == 1.0].index,
             signals.Short_MA[signals.Position == 1.0],
             '^', markersize=10, color='green', alpha=0.7, label='Buy Signal')
             
    # Plot the sell signals
    plt.plot(signals.loc[signals.Position == -1.0].index,
             signals.Short_MA[signals.Position == -1.0],
             'v', markersize=10, color='red', alpha=0.7, label='Sell Signal')
    
    # Customize the plot
    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# Example loading historical data using pandas
# Make sure to replace 'your_data.csv' with your actual data file
def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return data

# To run the strategy
if __name__ == '__main__':
    # Load your data
    data = load_data('your_data.csv')
    
    # Run the trading strategy
    signals = moving_average_crossover_strategy(data)
    
    # Plot the results
    plot_signals(signals)
```

### Notes:
- Use historical data with a `Date` column as an index and a `Close` column containing closing prices.
- The script contains a function `load_data` to load data from a CSV file.
- The `plot_signals` function visualizes the buy and sell signals and the moving averages.
- You can adjust the `short_window` and `long_window` parameters to test different configurations of the strategy.

Ensure that you have the necessary libraries installed (`pandas`, `numpy`, and `matplotlib`) using:
```bash
pip install pandas numpy matplotlib
```

Remember to replace `'your_data.csv'` with the path to your actual dataset.