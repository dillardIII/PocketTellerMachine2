from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I will create a simple Python code to implement and test two trading strategies: Moving Average Crossover and Mean Reversion. For this, we will use the `pandas` library for data manipulation and `yfinance` to download stock price data.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start='2020-01-01', end='2022-12-31'):
    data = yf.download(stock, start, end)
    return pd.DataFrame(data)

# Calculate moving average
def calculate_MA(data, window):
    return data['Close'].rolling(window).mean()

# Moving Average Crossover strategy
def MA_crossover(data, short_window, long_window):
    ShortMA = calculate_MA(data, short_window)
    LongMA = calculate_MA(data, long_window)

    Buy_Signal = (ShortMA > LongMA)
    Sell_Signal = (ShortMA < LongMA)

    return Buy_Signal, Sell_Signal

# Mean Reversion strategy
def mean_reversion(data, window):
    mean = calculate_MA(data, window)
    std_dev = data['Close'].rolling(window).std()

    upper_band = mean + (std_dev * 2)
    lower_band = mean - (std_dev * 2)

    Buy_Signal = (data['Close'] < lower_band)
    Sell_Signal = (data['Close'] > upper_band)

    return Buy_Signal, Sell_Signal

# Test strategies
def test_strategies(stock):
    data = download_data(stock)

    # Moving Average Crossover
    Buy_Signal, Sell_Signal = MA_crossover(data, 50, 200)
    print(f"Moving Average Crossover - Buy signals: {Buy_Signal.sum()}, Sell signals: {Sell_Signal.sum()}")

    # Mean Reversion
    Buy_Signal, Sell_Signal = mean_reversion(data, 20)
    print(f"Mean Reversion - Buy signals: {Buy_Signal.sum()}, Sell signals: {Sell_Signal.sum()}")

# Test strategies on Apple stock
test_strategies('AAPL')
```

This code will download the historical price data for the specified stock, calculate buy and sell signals for each strategy, and print the number of each type of signal. This is a very basic implementation and does not take into account transaction costs, slippage, or risk management. It also assumes that you can trade at the closing price of each day, which is not always possible in real trading. 

Please note that these strategies are oversimplified for the sake of this example. In real trading, you would need to use more sophisticated strategies and perform rigorous backtesting and forward testing before deploying any strategy.