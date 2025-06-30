Certainly! Let's create a Python utility for a strategy or empire-building game that helps in optimizing resource allocation. This utility will include a function to allocate resources efficiently among various tasks such as military building, research, and infrastructure development while keeping certain constraints in mind. We'll implement a basic linear programming approach using the SciPy library.

```python
import numpy as np
from scipy.optimize import linprog

def allocate_resources(budget, military_cost, research_cost, infra_cost, max_military, max_research, max_infra):
    """
    Determines the optimal allocation of resources among military, research,
    and infrastructure given constraints.

    :param budget: Total available resources (numeric).
    :param military_cost: Cost of allocating resources to the military (numeric).
    :param research_cost: Cost of allocating resources to research (numeric).
    :param infra_cost: Cost of allocating resources to infrastructure (numeric).
    :param max_military: Maximum allowable proportion for military allocation (numeric).
    :param max_research: Maximum allowable proportion for research allocation (numeric).
    :param max_infra: Maximum allowable proportion for infrastructure allocation (numeric).
    
    :return: A dictionary with the optimal resource allocation.
    """
    # Objective function coefficients (negative for maximization)
    c = [-military_cost, -research_cost, -infra_cost]

    # Coefficients for inequality constraints
    A = [
        [1, 0, 0],  # Military constraint
        [0, 1, 0],  # Research constraint
        [0, 0, 1],  # Infrastructure constraint
        [1, 1, 1]   # Total budget constraint
    ]

    # Right-hand side of inequality constraints
    b = [max_military * budget, max_research * budget, max_infra * budget, budget]

    # Bounds for each variable
    x_bounds = [(0, budget), (0, budget), (0, budget)]

    # Optimize
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    if result.success:
        allocation = {
            'Military': result.x[0],
            'Research': result.x[1],
            'Infrastructure': result.x[2]
        }
        return allocation
    else:
        raise ValueError("No feasible solution found")

# Example usage
budget = 1000
military_priority = 6
research_priority = 3
infra_priority = 4

max_military_prop = 0.5
max_research_prop = 0.4
max_infra_prop = 0.6

optimal_allocation = allocate_resources(
    budget,
    military_priority,
    research_priority,
    infra_priority,
    max_military_prop,
    max_research_prop,
    max_infra_prop
)

print("Optimal Resource Allocation:")
for resource, amount in optimal_allocation.items():
    print(f"{resource}: {amount:.2f}")
```

### Explanation:

1. **Inputs**: The function takes the total budget and costs (or priorities) for military, research, and infrastructure. Additionally, it takes constraints on maximum proportions that can be allocated to each category.

2. **Constraints**: The constraints ensure that allocations do not exceed specified proportions of the total budget and sum up to the total budget.

3. **Optimization**: We use the `linprog` function from the SciPy library, which performs linear programming optimization to find the best strategy.

4. **Output**: The function returns a dictionary containing the optimal resource allocation based on constraints and priorities.

To use this function, you need to have SciPy installed. You can install it via pip:

```bash
pip install scipy
```

This utility can be further expanded by introducing additional categories or more sophisticated constraints based on the requirements of the game.