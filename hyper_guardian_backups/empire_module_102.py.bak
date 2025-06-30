Creating a Python module that incorporates advanced features like intelligent recursion can be quite useful for a variety of tasks, especially for complex problem-solving or data processing. Here is an example of what such a module might look like. This module will perform advanced operations intelligently, making use of recursion when necessary to optimize solutions for specific problems.

### `intelligent_recursion.py`

```python
# intelligent_recursion.py

import functools

class IntelligentRecursion:
    """
    A class to encapsulate intelligent recursion techniques.
    """

    def __init__(self):
        self.memo = {}

    def memoize(self, func):
        """Memoization decorator to cache function results."""
        @functools.wraps(func)
        def wrapper(*args):
            if args not in self.memo:
                self.memo[args] = func(*args)
            return self.memo[args]
        return wrapper

    def intelligent_fibonacci(self, n):
        """
        Calculate the n-th Fibonacci number using recursion with memoization.
        """
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        @self.memoize
        def _fibonacci(n):
            if n in (1, 2):
                return 1
            return _fibonacci(n - 1) + _fibonacci(n - 2)

        return _fibonacci(n)
    
    def intelligent_factorial(self, n):
        """
        Calculate the factorial of n using recursion, with memoization for optimization.
        """
        if n < 0:
            raise ValueError("n must be a non-negative integer")

        @self.memoize
        def _factorial(n):
            if n in (0, 1):
                return 1
            return n * _factorial(n - 1)

        return _factorial(n)

    def intelligent_tower_of_hanoi(self, n, source, target, auxiliary):
        """
        Solves the Tower of Hanoi problem for n disks.
        """

        def _tower_of_hanoi(n, source, target, auxiliary):
            if n == 1:
                print(f"Move disk 1 from {source} to {target}")
                return
            _tower_of_hanoi(n - 1, source, auxiliary, target)
            print(f"Move disk {n} from {source} to {target}")
            _tower_of_hanoi(n - 1, auxiliary, target, source)

        _tower_of_hanoi(n, source, target, auxiliary)

# Module level utility functions

def calculate_fibonacci(n):
    """Utility function to calculate Fibonacci numbers."""
    ir = IntelligentRecursion()
    return ir.intelligent_fibonacci(n)

def calculate_factorial(n):
    """Utility function to calculate factorial."""
    ir = IntelligentRecursion()
    return ir.intelligent_factorial(n)

def solve_tower_of_hanoi(n, source='A', target='C', auxiliary='B'):
    """Utility function to solve the Tower of Hanoi problem."""
    ir = IntelligentRecursion()
    ir.intelligent_tower_of_hanoi(n, source, target, auxiliary)

if __name__ == '__main__':
    # Example usage
    print("Fibonacci(10):", calculate_fibonacci(10))
    print("Factorial(5):", calculate_factorial(5))
    print("Tower of Hanoi with 3 disks:")
    solve_tower_of_hanoi(3)
```

### Explanation:

- **Memoization**: This technique is used in the `memoize` decorator to cache results of expensive function calls, thereby avoiding redundant calculations.

- **Recursive Methods**: `intelligent_fibonacci` and `intelligent_factorial` are optimized through memoization, while `intelligent_tower_of_hanoi` utilizes classic recursion as it is straightforward.

- **Utility Functions**: These are provided at the module level to make the use of the `IntelligentRecursion` class convenient.

This module effectively demonstrates intelligent recursion through memoization as a method to improve the efficiency of recursive computations in Python.