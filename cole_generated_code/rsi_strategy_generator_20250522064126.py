Here's a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the `pandas` and `yfinance` libraries. This strategy will generate a "buy" signal when the RSI is below 30 (indicating oversold conditions) and a "sell" signal when the RSI is above 70 (indicating overbought conditions).

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Download historical data as dataframe
def download_data(stock, start, end):
    data = pdr.get_data_yahoo(stock, start, end)
    return data

# Calculate RSI
def calculate_RSI(data, window):
    delta = data['Adj Close'].diff()
    up_days = delta.copy()
    up_days[delta<=0]=0.0
    down_days = abs(delta.copy())
    down_days[delta>0]=0.0
    RS_up = up_days.rolling(window).mean()
    RS_down = down_days.rolling(window).mean()
    rsi= 100-100/(1+RS_up/RS_down)
    return rsi

# Generate RSI Strategy
def generate_RSI_strategy(data, rsi):
    buy_signals = (rsi < 30)
    sell_signals = (rsi > 70)
    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    return data

# Main function
def main():
    stock = 'AAPL' # Apple stock
    start = '2020-01-01'
    end = '2022-12-31'
    data = download_data(stock, start, end)
    rsi = calculate_RSI(data, 14) # 14-day RSI
    data = generate_RSI_strategy(data, rsi)
    print(data)

if __name__ == "__main__":
    main()
```
This code will print a dataframe with the historical data of the specified stock, along with two additional columns: `Buy_Signal` and `Sell_Signal`. These columns will contain `True` or `False` depending on whether the conditions for the RSI strategy are met.