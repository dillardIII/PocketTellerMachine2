Creating an advanced Python module that leverages intelligent recursion is an exciting task! Here, I'll outline a Python module that implements smart recursive strategies for solving various kinds of problems. This module will include a memoization decorator to optimize recursive calls, a few example recursive functions, and an explanation of its usage. I'll name this module `intelligent_recursion.py`.

```python
# intelligent_recursion.py

from functools import wraps

def memoize(func):
    """Decorator to memoize the results of recursive calls."""
    cache = {}

    @wraps(func)
    def memoizer(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoizer

class RecursiveSolution:
    """Class for demonstrating intelligent recursion strategies."""

    @staticmethod
    @memoize
    def fibonacci(n):
        """Calculate the nth Fibonacci number using recursion with memoization."""
        if n <= 0:
            raise ValueError("Fibonacci numbers are defined for positive integers.")
        if n in (1, 2):
            return 1
        return RecursiveSolution.fibonacci(n - 1) + RecursiveSolution.fibonacci(n - 2)

    @staticmethod
    @memoize
    def factorial(n):
        """Calculate the factorial of n using recursion with memoization."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * RecursiveSolution.factorial(n - 1)

    @staticmethod
    @memoize
    def permutations(elements):
        """Generate all permutations of a list of elements."""
        if len(elements) <= 1:
            yield elements
        else:
            for i in range(len(elements)):
                for perm in RecursiveSolution.permutations(elements[:i] + elements[i+1:]):
                    yield [elements[i]] + perm

if __name__ == "__main__":
    # Example usage of the RecursiveSolution class
    
    # Fibonacci
    print("Fibonacci(10):", RecursiveSolution.fibonacci(10))
    print("Fibonacci(15):", RecursiveSolution.fibonacci(15))
    
    # Factorial
    print("Factorial(5):", RecursiveSolution.factorial(5))
    print("Factorial(7):", RecursiveSolution.factorial(7))

    # Permutations
    print("Permutations of [1, 2, 3]:")
    for p in RecursiveSolution.permutations([1, 2, 3]):
        print(p)
```

### Explanation:

1. **Memoization Decorator**: 
   - The `memoize` decorator wraps a function to cache its results, avoiding redundant calculations in recursive calls.

2. **Recursive Methods**:
   - **Fibonacci**: Computes the nth Fibonacci number. Memoization optimizes this function significantly, reducing time complexity from exponential to linear.
   - **Factorial**: Computes factorial of a number using recursive approach with memoization.
   - **Permutations**: Generates permutations of a given list. It uses recursion to build permutations by fixing each element and generating permutations of the remaining list.

3. **Example Usage**:
   - The `if __name__ == "__main__":` block demonstrates how to use the class methods. It prints out Fibonacci numbers, factorials, and generates permutations of a list.

This module is designed to be easily extended with more advanced recursive functions, all benefiting from the intelligent use of memoization.