Creating a new, advanced Python module for a hypothetical "unstoppable PTM empire" with intelligent recursion would involve crafting a module that leverages recursion in an innovative and efficient way. Here, we'll create a module called `ptm_recursion` that contains functions demonstrating intelligent recursion in solving complex problems, such as a recursive solver for combinatorial problems and optimizing recursive algorithms using techniques like memoization or dynamic programming. This example shows a balance of complexity and clarity for educational purposes.

```python
# ptm_recursion.py

from functools import lru_cache
from typing import Dict, Tuple, List

class PTMRecursion:
    """A module encapsulating advanced recursive techniques."""

    @staticmethod
    @lru_cache(maxsize=None)
    def fibonacci(n: int) -> int:
        """
        Calculate the nth Fibonacci number using memoized recursion for optimization.

        :param n: The index in the Fibonacci sequence.
        :return: The nth Fibonacci number.
        """
        if n < 2:
            return n
        return PTMRecursion.fibonacci(n - 1) + PTMRecursion.fibonacci(n - 2)

    @staticmethod
    def count_paths(m: int, n: int) -> int:
        """
        Count the number of unique paths from the top-left to the bottom-right in an m x n grid.

        :param m: Number of rows.
        :param n: Number of columns.
        :return: Number of unique paths.
        """
        # Initialize a cache to store intermediate results
        cache: Dict[Tuple[int, int], int] = {}

        def recurse(x: int, y: int) -> int:
            # Base case: If we're at the last row or column
            if x == m - 1 or y == n - 1:
                return 1
            # Check if result is cached
            if (x, y) in cache:
                return cache[(x, y)]

            # Recursive case: Sum of paths from the right and down
            cache[(x, y)] = recurse(x + 1, y) + recurse(x, y + 1)
            return cache[(x, y)]

        return recurse(0, 0)

    @staticmethod
    def all_subsets(nums: List[int]) -> List[List[int]]:
        """
        Find all subsets of a set using intelligent recursion.

        :param nums: The input list.
        :return: A list of all subsets.
        """
        result: List[List[int]] = []

        def recurse(index: int, current: List[int]):
            # Base case: All elements considered
            if index == len(nums):
                result.append(current[:])
                return
            # Recursive case: Include the current element or not
            recurse(index + 1, current + [nums[index]])
            recurse(index + 1, current)

        recurse(0, [])
        return result
```

### Description:

1. **Memoized Fibonacci:** Demonstrates optimizing recursion with memoization using `lru_cache`. This avoids redundant calculations by caching results of already computed Fibonacci numbers.

2. **Count Paths in a Grid:** Solves a classic combinatorial problem using recursion with a manual caching mechanism to reduce the time complexity.

3. **Subsets of a Set:** Uses recursion to generate all possible subsets of a given list, showcasing a divide-and-conquer technique by considering each element's inclusion or exclusion.

This module can be expanded and improved based on specific requirements or use-cases within your PTM empire's broader applications. It aims to balance between recursive complexity and performance by leveraging intelligent optimization techniques.