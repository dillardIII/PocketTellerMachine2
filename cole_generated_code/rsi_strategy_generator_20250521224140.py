Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the pandas library. This strategy generator will create a trading strategy based on the RSI indicator. The RSI is a momentum indicator that measures the speed and change of price movements. 

```python
import pandas as pd
import numpy as np

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(data, window=14):
    rsi = calculate_rsi(data, window)
    data = pd.concat([data, rsi], axis=1)
    data.columns = ['price', 'rsi']

    data['buy_signal'] = (data['rsi'] < 30)
    data['sell_signal'] = (data['rsi'] > 70)

    return data

# Test the strategy with some data
price_data = pd.DataFrame(np.random.rand(100) * 100)
strategy = rsi_strategy(price_data)
print(strategy)
```

This code will generate a DataFrame with the price data, the calculated RSI, and boolean columns for buy and sell signals. The buy signal is generated when the RSI is below 30 (indicating oversold conditions) and the sell signal is generated when the RSI is above 70 (indicating overbought conditions).

Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.