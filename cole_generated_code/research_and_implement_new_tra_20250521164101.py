The process of creating a trading algorithm involves handling financial data, creating strategies, backtesting them, and deploying them for investment use. Here's an example of a simple trading algorithm using Python and the libraries pandas, numpy, and yfinance.

```python
import pandas as pd
import numpy as np
import yfinance as yf

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_algo():
    # Download historical data as dataframe
    data = yf.download('AAPL', start='2019-01-01', end='2021-12-31')

    # Calculate SMA and EMA
    data['SMA'] = calculate_sma(data['Close'], 14)
    data['EMA'] = calculate_ema(data['Close'], 14)

    # Create a column 'Signal' such that if EMA > SMA then Signal = 1 else 0
    data['Signal'] = np.where(data['EMA'] > data['SMA'], 1, 0)

    # Create another column 'Position' which is the difference between 'Signal' and its previous element
    data['Position'] = data['Signal'].diff()

    # Print the data
    print(data)

    # Checking positions
    # If 'Position' column is 1 then Buy the stock, if it is -1 then Sell the stock
    buy_signals = data[data['Position'] == 1]
    sell_signals = data[data['Position'] == -1]

    print('Buy Signals:')
    print(buy_signals)
    print()
    print('Sell Signals:')
    print(sell_signals)

trading_algo()
```

In this simple trading bot:
1. The bot downloads historical price data of Apple Inc. using the `yfinance` library.
2. It then calculates the simple moving average (SMA) and exponential moving average (EMA) for the closing price of the stock for a period of 14 days.
3. Then, it generates signals based on the strategy: "Buy a share when the EMA surpasses the SMA, and sell it when the SMA surpasses the EMA". 
4. The bot follows this rule for the provided data and notes down the buy/sell signals.

Please note, this is just a simple example. Real-world trading algorithms employ much more sophisticated strategies and risk management techniques.
Make sure to completely test the strategy and perform risk management before using it in a live setting. There are still many disadvantages to automated trading. This is not financial advice and trading always involves risk.