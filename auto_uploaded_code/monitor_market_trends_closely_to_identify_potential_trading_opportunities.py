To monitor market trends and identify potential trading opportunities, we can use APIs provided by financial data providers such as Alpha Vantage, Yahoo Finance, etc. Here is a simple Python script that uses the Alpha Vantage API to monitor market trends. 

Please note that this is a basic script and real-world trading algorithms are much more complex and take many more factors into consideration. Also, you need to replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key.

```python
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

def calculate_sma(data, window):
    return data['4. close'].rolling(window).mean()

def calculate_ema(data, window):
    return data['4. close'].ewm(span=window, adjust=False).mean()

def get_market_trends(symbol):
    ts = TimeSeries(key='YOUR_ALPHA_VANTAGE_API_KEY', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

    # Calculate SMA and EMA
    data['SMA'] = calculate_sma(data, 14)
    data['EMA'] = calculate_ema(data, 14)

    return data

def identify_trading_opportunities(data):
    buy_signals = []
    sell_signals = []

    for i in range(2, data['4. close'].count()):
        if data['SMA'][i] > data['EMA'][i] and data['SMA'][i - 1] < data['EMA'][i - 1]:
            buy_signals.append(data['4. close'][i])
            sell_signals.append(float('nan'))
        elif data['SMA'][i] < data['EMA'][i] and data['SMA'][i - 1] > data['EMA'][i - 1]:
            sell_signals.append(data['4. close'][i])
            buy_signals.append(float('nan'))
        else:
            buy_signals.append(float('nan'))
            sell_signals.append(float('nan'))

    return buy_signals, sell_signals

def monitor_market_trends(symbol):
    data = get_market_trends(symbol)
    buy_signals, sell_signals = identify_trading_opportunities(data)

    data['Buy_Signal_Price'] = buy_signals
    data['Sell_Signal_Price'] = sell_signals

    return data

# Monitor market trends for a specific symbol
monitor_market_trends('GOOGL')
```

This script calculates the Simple Moving Average (SMA) and the Exponential Moving Average (EMA) for a given symbol. It then identifies potential buy and sell signals based on the crossover of these two indicators. A buy signal is generated when the SMA crosses above the EMA, and a sell signal is generated when the SMA crosses below the EMA.