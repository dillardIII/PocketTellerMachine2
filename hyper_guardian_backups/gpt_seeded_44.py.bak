Sure! Let’s create a Python utility for managing and optimizing resources in an empire strategy game. This tool, `EmpireResourceOptimizer`, will help players efficiently allocate resources like wood, stone, and food to different tasks in the game, such as building structures, training troops, and researching technologies. 

Here's a basic outline of the utility:

1. **Resource Allocation**: Distribute resources based on priority tasks.
2. **Resource Generation**: Calculate resources generated over time.
3. **Optimization**: Suggest the best allocation based on current needs and available resources.

```python
class EmpireResourceOptimizer:
    def __init__(self, initial_resources):
        # Initial available resources: {'wood': 1000, 'stone': 500, 'food': 300}
        self.resources = initial_resources
        self.task_requirements = {}
        self.task_priorities = {}
        self.generation_rates = {}  # e.g., {'wood': 10, 'stone': 5, 'food': 8} units per minute

    def add_task(self, task_name, requirements, priority):
        """
        Add a task with its resource requirements and priority.
        Priority is an integer; higher values mean higher priority.
        """
        self.task_requirements[task_name] = requirements
        self.task_priorities[task_name] = priority

    def calculate_generation(self, minutes):
        """
        Calculate the amount of each resource generated over a given number of minutes.
        """
        generated = {resource: rate * minutes for resource, rate in self.generation_rates.items()}
        self.resources = {resource: self.resources.get(resource, 0) + generated.get(resource, 0) for resource in self.resources}
        return generated

    def optimize_allocation(self):
        """
        Suggest optimal resource allocation based on task priorities.
        """
        sorted_tasks = sorted(self.task_priorities, key=self.task_priorities.get, reverse=True)
        optimal_allocation = {}

        for task in sorted_tasks:
            if all(self.resources[res] >= self.task_requirements[task].get(res, 0) for res in self.task_requirements[task]):
                optimal_allocation[task] = "Can be completed"
                for res in self.task_requirements[task]:
                    self.resources[res] -= self.task_requirements[task][res]
            else:
                optimal_allocation[task] = "Insufficient resources"

        return optimal_allocation

    def display_resources(self):
        """
        Display the current available resources.
        """
        return self.resources

    def set_generation_rate(self, generation_rates):
        """
        Set resource generation rates.
        """
        self.generation_rates = generation_rates

# Example usage
empire = EmpireResourceOptimizer(initial_resources={'wood': 1000, 'stone': 500, 'food': 300})

empire.set_generation_rate({'wood': 10, 'stone': 5, 'food': 8})

empire.add_task('Build Farm', {'wood': 100, 'stone': 50}, priority=1)
empire.add_task('Train Soldiers', {'food': 200}, priority=3)
empire.add_task('Research Mining', {'wood': 50, 'stone': 20}, priority=2)

# Generate resources for an hour
empire.calculate_generation(minutes=60)

# Optimize resource allocation
allocation = empire.optimize_allocation()

# Display current resources and allocation suggestions
print("Current Resources:", empire.display_resources())
print("Allocation Suggestion:", allocation)
```

### Explanation:

- **Resource Tracking**: Tracks initial resources and updates them as tasks are completed or more resources are generated.
- **Task Management**: Allows adding tasks with required resources and priority levels.
- **Resource Generation**: Computes resources generated over time.
- **Optimal Allocation**: Prioritizes tasks based on priorities and suggests what can be done with the available resources.

The user can easily add more features or complexity to this utility, like handling multiple civilizations, dynamic priority adjustments, or adjusting generation rates based on external factors.