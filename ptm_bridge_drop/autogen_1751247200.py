from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a Python file (as requested) containing a simple trading strategy function. This strategy uses a momentum-based approach by analyzing moving averages to generate buy and sell signals. The code uses the `pandas` and `numpy` libraries for handling data and calculations. The strategy assumes you have historical stock data as a pandas DataFrame with columns: 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.

```python
# trading_strategy_6.py

import pandas as pd
import numpy as np

def momentum_trading_strategy(data, short_window=40, long_window=100):
    """
    A momentum-based trading strategy that uses simple moving averages.
    
    Parameters:
    - data: pd.DataFrame with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'
    - short_window: int, short moving average window
    - long_window: int, long moving average window
    
    Returns:
    - signals: pd.DataFrame, containing the original data along with generated signals
    """

    # Ensure data is sorted by date
    data = data.sort_values('Date')
    
    # Create a DataFrame to store signals
    signals = pd.DataFrame(index=data.index)
    signals['Date'] = data['Date']
    signals['Close'] = data['Close']
    
    # Calculate short and long moving averages
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Generate buy and sell signals
    signals['signal'] = 0
    signals['signal'][short_window:] = np.where(
        signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1, -1)
    
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Example usage
if __name__ == '__main__':
    # Example: Load your data into a DataFrame here
    # data = pd.read_csv('path_to_your_data.csv')

    # Example data setup
    example_data = {
        'Date': pd.date_range(start='2023-01-01', periods=200, freq='D'),
        'Open': np.random.rand(200) * 100,
        'High': np.random.rand(200) * 100,
        'Low': np.random.rand(200) * 100,
        'Close': np.random.rand(200) * 100,
        'Volume': np.random.randint(1000, 5000, size=200)
    }
    data = pd.DataFrame(example_data)
    
    # Apply the strategy
    signals = momentum_trading_strategy(data)
    
    # Output the signals DataFrame to see the results
    print(signals)
```

### Detailed Explanation:

- **Data Requirements**: The strategy function expects a pandas DataFrame with financial data. Ensure your data includes 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume'.

- **Moving Averages**: It calculates two moving averages (short and long) to capture momentum. A simple moving average (SMA) is used here, but you can swap in other types if preferred.

- **Signal Generation**: 
  - A signal of `1` (buy) is generated when the short-term moving average is above the long-term moving average.
  - A signal of `-1` (sell) is generated when the short-term average is below the long-term average.
  - The 'positions' column indicates when a change in position (buy/sell action) has occurred.

- **Run Example**: If no actual data is loaded, the code includes an example setup for testing. Replace the example data section with actual data loading logic.

Make sure to install the necessary libraries (`pandas` and `numpy`) if you haven't already, and modify the script to fit real-world data as needed.