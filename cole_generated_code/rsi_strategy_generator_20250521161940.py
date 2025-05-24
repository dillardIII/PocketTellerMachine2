Python Code:

```python

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_RSI(data, window):
    delta = data.diff()

    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    
    ma_up = up.ewm(com = window - 1, adjust=True).mean()
    ma_down = down.ewm(com = window - 1, adjust=True).mean()
   
    RSI = ma_up / ma_down
    RSI = 100 - (100/(1 + RSI))
    
    return RSI

def implement_RSI_strategy(data, RSI):
    data['buy_signal'] = (RSI < 30)
    data['sell_signal'] = (RSI > 70)
    return data

def main():
    ticker = "AAPL"
    df = yf.download(ticker, start="2019-01-01", end=datetime.now().strftime('%Y-%m-%d'))

    window = 14
    close = df['Adj Close']
    RSI = calculate_RSI(close, window)

    df = implement_RSI_strategy(df, RSI)

    plt.figure(figsize=(12,5))
    plt.title('Buy and sell signals based on RSI strategy')
    plt.plot(df.index, close, label='Close Price', color='blue', alpha=0.35)
    plt.scatter(df.index, df['buy_signal'], color='green', label='Buy Signal', marker='^', alpha=1)
    plt.scatter(df.index, df['sell_signal'], color='red', label='Sell Signal', marker='v', alpha=1)
    plt.legend(loc='upper left')
    plt.grid()

    plt.show()

if __name__ == "__main__":
    main()

```

Please make sure you have installed yfinance, pandas, numpy, and matplotlib python packages. Please note that this code will only flag potential buy and sell points based on RSI readings, and should not be the only metric used when making investment decisions.