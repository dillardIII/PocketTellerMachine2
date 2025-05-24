Sure, I can provide a simple Python code that can help PTM to set specific trading goals for each day. This code will use a dictionary to store trading goals for each day of the week. Here it is:

```python
class TradingGoals:
    def __init__(self):
        self.goals = {
            "Monday": 0,
            "Tuesday": 0,
            "Wednesday": 0,
            "Thursday": 0,
            "Friday": 0,
        }

    def set_goal(self, day, goal):
        if day in self.goals:
            self.goals[day] = goal
        else:
            print("Invalid day. Please enter a valid day.")

    def get_goal(self, day):
        if day in self.goals:
            return self.goals[day]
        else:
            print("Invalid day. Please enter a valid day.")

    def print_goals(self):
        for day, goal in self.goals.items():
            print(f"Trading goal for {day}: {goal}")

# Usage
ptm_trading_goals = TradingGoals()

# Set trading goals
ptm_trading_goals.set_goal("Monday", 10000)
ptm_trading_goals.set_goal("Tuesday", 15000)
ptm_trading_goals.set_goal("Wednesday", 20000)
ptm_trading_goals.set_goal("Thursday", 15000)
ptm_trading_goals.set_goal("Friday", 10000)

# Print trading goals
ptm_trading_goals.print_goals()
```

This code will create a `TradingGoals` object for PTM. You can set the trading goal for each day using the `set_goal` method and get the trading goal for a specific day using the `get_goal` method. The `print_goals` method will print the trading goals for all days.