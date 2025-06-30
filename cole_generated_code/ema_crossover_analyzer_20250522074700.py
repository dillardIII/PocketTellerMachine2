from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you write a Python code to analyze EMA crossover. Here's a simple example using pandas library for data manipulation and yfinance to download stock price data.

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def analyze_crossover(symbol):
    # Download historical data as dataframe
    data = yf.download(symbol, start="2020-01-01", end="2022-12-31")

    # Calculate 50-day EMA
    data['50_EMA'] = calculate_ema(data['Close'], 50)

    # Calculate 200-day EMA
    data['200_EMA'] = calculate_ema(data['Close'], 200)

    # Create a column to hold the sign of the difference between the two EMAs
    data['Crossover'] = (data['50_EMA'] - data['200_EMA']).apply(np.sign)

    # Find where the difference changes (i.e., where a crossover occurs)
    data['Crossover_Signal'] = np.where(data['Crossover'].diff() != 0, data['Close'], np.nan)

    return data

# Test the function
print(analyze_crossover('AAPL'))
```

This code will download the historical price data for the given symbol (in this case, AAPL for Apple Inc.), calculate the 50-day and 200-day exponential moving averages (EMAs), and then find where the two EMAs cross over. The 'Crossover_Signal' column in the returned dataframe will contain the closing price at the points where a crossover occurs, and NaNs elsewhere.

Please note that this is a simple example and might need to be adjusted based on your specific needs. Also, you need to install yfinance and pandas libraries if you haven't done so. You can install them using pip:

```bash
pip install yfinance pandas numpy
```