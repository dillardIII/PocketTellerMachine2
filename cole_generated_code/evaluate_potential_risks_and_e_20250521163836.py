Here is a simple Python code for Risk Management. In this example, we calculate Value at Risk (VaR) for a portfolio. VaR is a financial metric that estimates the risk of investment. 

Please note that risk assessment and management for trading are very complex topics and involve several methods and techniques. This code only provides the most basic risk assessment.

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as web

def calculate_portfolio_var(tickers, weights=None):
    if weights is None: 
        weights = np.ones(len(tickers))/len(tickers)  
        
    portfolio_data = pd.DataFrame()
    
    for t in tickers:
        portfolio_data[t] = web.DataReader(t, data_source='yahoo', start='01-01-2010')['Adj Close']
        
    log_returns = np.log(portfolio_data / portfolio_data.shift(1))
    cov_matrix = log_returns.cov() * 250   # assuming 250 trading days in a year
    
    portfolio_var = np.dot(weights.T, np.dot(cov_matrix, weights))
    
    return portfolio_var

tickers = ['AAPL', 'GOOG', 'MSFT'] 
weights = np.array([0.3, 0.4, 0.3])
portfolio_var = calculate_portfolio_var(tickers, weights)

print("The Portfolio VaR is :", portfolio_var)
```

In our calculation, we are making several assumptions: 
- All stocks are equally weighted.
- The historical stock price is representative of future performance.
- We only are interested in a rough approximation of risk.

For a more accurate calculation, we would need to adjust these assumptions, possibly use a more complex model for price movement, consider other financial instruments as well, account for derivatives etc. This might involve advanced mathematical methods and is typically done by quantitative analysts or 'quants'.

You also asked about a risk management protocol. A complete protocol would be quite detailed and involves decision makers from across the company. Here are some steps that a company might take:
1. Identify potential risks - This can be done through analysis, expert interviews, scenario planning etc.
2. Analyze and evaluate the risks - This involves an estimation of the potential impact and the likelihood of occurrence. 
3. Treat/mitigate the risks - This might involve taking actions to reduce the likelihood or impact, sharing the risk (e.g. insurance), accepting the risk or avoiding the risk (e.g. not engaging in a business activity).
4. Monitor and review - The company should keep track of identified risks, actions taken and look out for new risks.
Note that this process is iterative and need to be revisited regularly. Besides, these steps should be recorded and communicated clearly within the organization.

A simple Python code for creating a Risk Management Protocol cannot be written as it involves detailed decision-making process and human judgment, we cannot code human psychology, cognitive biases and perception of risk. We can write code to assess and quantify the risks, but the protocol itself is a decision-making process.