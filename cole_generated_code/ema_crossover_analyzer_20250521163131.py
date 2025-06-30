from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a Python code using Pandas and yfinance libraries for Exponential Moving Average (EMA) crossover analysis:

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data,window):
    return data.ewm(span=window,adjust=False).mean()

def ema_crossover_analyzer(ticker, shorter_window, longer_window):
    # Download historical data as dataframe
    data = yf.download(ticker)

    # Calculate Short-term and Long-term EMA
    data['Short_EMA'] = calculate_ema(data['Close'],shorter_window)
    data['Long_EMA'] = calculate_ema(data['Close'],longer_window)

    # Create a function to signal when to buy and sell
    def create_signals(data):
        buy_signal = []
        sell_signal = []
        flag = 0
        for i in range(len(data)):
            if data['Short_EMA'][i] > data['Long_EMA'][i]:
                if flag != 1:
                    buy_signal.append(data['Close'][i])
                    sell_signal.append(np.nan)
                    flag = 1
                else:
                    buy_signal.append(np.nan)
                    sell_signal.append(np.nan)
            elif data['Short_EMA'][i] < data['Long_EMA'][i]:
                if flag != 0:
                    buy_signal.append(np.nan)
                    sell_signal.append(data['Close'][i])
                    flag = 0
                else:
                    buy_signal.append(np.nan)
                    sell_signal.append(np.nan)
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)

        return buy_signal, sell_signal

    # Store the buy and sell signals in variables
    data['Buy_Signal'], data['Sell_Signal'] = create_signals(data)

    return data

# Example usage:
ticker = 'AAPL' # Apple stock
shorter_window = 12 # 12 day EMA
longer_window = 26 # 26 day EMA
result = ema_crossover_analyzer(ticker, shorter_window, longer_window)
print(result)
```

This script will analyze the EMA crossover for the given ticker symbol. It uses the EMA with a shorter window and a longer window. Whenever the short-term EMA crosses above the long-term EMA, it will signal a buy, and vice versa for a sell signal. You can adjust the windows for different EMA lengths. The resulting dataframe will have the columns for Close price, Short-term EMA, Long-term EMA, buy signals (Close price at the time of buy signal, NaN otherwise), and sell signals (Close price at the time of sell signal, NaN otherwise).

Make sure to `pip install pandas yfinance` before running this code.