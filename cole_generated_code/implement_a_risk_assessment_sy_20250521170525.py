Here is a basic Python implementation for a risk assessment system:

```python
class Trade:
  def __init__(self, trade_id, value, risk_level):
    self.trade_id = trade_id
    self.value = value
    self.risk_level = risk_level 

class RiskAssessmentSystem:
  def __init__(self):
    self.trades = []
  
  def add_trade(self, trade):
    self.trades.append(trade)
  
  def assess_risks(self):
    high_risk_trades = []
    medium_risk_trades = []
    low_risk_trades = []

    for trade in self.trades:
      if trade.risk_level > 7:
        high_risk_trades.append(trade)
      elif trade.risk_level > 4:
        medium_risk_trades.append(trade)
      else:
        low_risk_trades.append(trade)
    return high_risk_trades, medium_risk_trades, low_risk_trades
  
  def potential_loss(self, risk_trades):
    potential_loss = 0
    for trade in risk_trades:
      potential_loss += trade.value
    return potential_loss


# example usage
RAS = RiskAssessmentSystem()
RAS.add_trade(Trade('1', 50000, 8))
RAS.add_trade(Trade('2', 30000, 5))
RAS.add_trade(Trade('3', 10000, 2))

high_risk, medium_risk, low_risk = RAS.assess_risks()

print(f"Potential high risk loss: {RAS.potential_loss(high_risk)}")
print(f"Potential medium risk loss: {RAS.potential_loss(medium_risk)}")
print(f"Potential low risk loss: {RAS.potential_loss(low_risk)}")
```

In this code, we have a `Trade` class which represents a single trade, with a trade ID, its value and its risk level.

The `RiskAssessmentSystem` class stores all the trades and has functions for adding trades and assessing their risks. The `assess_risks` function categorizes all trades into high, medium and low risk based on their risk level. The `potential_loss` function calculates the possible monetary loss for a given set of trades.

Please note that in a real-world situation, risk assessment methods could be significantly more complex, taking into account a wider range of factors such as market conditions, specific details about the securities being traded, etc. This is a simplified example.