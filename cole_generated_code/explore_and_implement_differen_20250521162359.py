Implementing different trading strategies can be complex and time-consuming. Here, we present simple python code to illustrate two commonly used trading strategies: Moving Average Crossover and Bollinger Bands. To put these strategies into existing trading system that adapts and learns could involve advanced machine learning techniques, which is out of this scope.

Libraries needed: pandas, pandas_datareader, matplotlib, numpy.

```python
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np

# Load data
def load_financial_data(start_date, end_date, output_file, ticker):
    try:
        df = pd.read_pickle(output_file)
        print('File data found...reading data')
    except FileNotFoundError:
        print('File not found...downloading the data')
        df = pdr.get_data_yahoo(ticker, start_date, end_date)
        df.to_pickle(output_file)
    return df

# Moving Average Crossover Strategy
def implement_simple_moving_average_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()
    return signals

# Bollinger Band Strategy
def implement_bollinger_band_strategy(data, window):
    signals = pd.DataFrame(index=data.index)
    signals['Close'] = data['Close']
    signals['middle_band'] = signals['Close'].rolling(window=window).mean()
    signals['upper_band'] = signals['middle_band'] + 1.96*signals['Close'].rolling(window=window).std()
    signals['lower_band'] = signals['middle_band'] - 1.96*signals['Close'].rolling(window=window).std()
    signals['signal'] = np.where(signals['Close'] < signals['lower_band'], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

# Usage
ticker = 'AAPL'
output_file = 'AAPL_data.pkl'
start_date = '2005-01-01'
end_date = '2022-12-31'

data = load_financial_data(start_date, end_date, output_file, ticker)

signals_ma = implement_simple_moving_average_strategy(data, 40, 100)
signals_bb = implement_bollinger_band_strategy(data, 40)

```
Remember to replace 'ticker', 'output_file', 'start_date' and 'end_date' with actual values. Also, the moving average window and Bollinger bands window can be adjusted for different strategies.

This is a very basic implementation. Please note that these scripts do not contain any buying or selling of the actual stocks. Also, transaction costs were not included. Real-world application of the strategies should consider transaction costs, market impacts, risk management, etc. For realistic and robust trading systems, more advanced techniques such as machine learning and portfolio optimization should be considered.