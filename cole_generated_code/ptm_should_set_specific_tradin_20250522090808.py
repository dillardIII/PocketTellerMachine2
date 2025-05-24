Sure, I can provide a basic example of how you might set up a Python program to set daily trading goals. This example will use a simple dictionary to store the goals, and will allow you to add, view and check if you have reached your goals.

```python
class TradingGoals:
    def __init__(self):
        self.goals = {}

    def add_goal(self, goal_name, target_value):
        self.goals[goal_name] = {'target': target_value, 'current': 0}

    def update_goal(self, goal_name, current_value):
        if goal_name in self.goals:
            self.goals[goal_name]['current'] = current_value
        else:
            print(f"No goal named {goal_name} found.")

    def check_goal(self, goal_name):
        if goal_name in self.goals:
            return self.goals[goal_name]['current'] >= self.goals[goal_name]['target']
        else:
            print(f"No goal named {goal_name} found.")
            return False

    def view_goals(self):
        for goal, values in self.goals.items():
            print(f"Goal: {goal}, Target: {values['target']}, Current: {values['current']}")

# Usage
ptm = TradingGoals()
ptm.add_goal("Increase Engagement", 100)
ptm.add_goal("Increase Performance", 200)

# Update goals
ptm.update_goal("Increase Engagement", 50)
ptm.update_goal("Increase Performance", 150)

# Check goals
print(ptm.check_goal("Increase Engagement"))  # False
print(ptm.check_goal("Increase Performance"))  # False

# View goals
ptm.view_goals()
```

This is a very basic example and might not fit your exact needs. In a real-world scenario, you might want to connect this to a database or an API that tracks your actual trading data.