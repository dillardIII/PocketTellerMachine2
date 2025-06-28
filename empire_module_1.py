```python
import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value inclusive.
    
    Parameters:
    - min_value (int): The minimum value for the random number.
    - max_value (int): The maximum value for the random number.
    
    Returns:
    - int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def sum_of_numbers(num_list):
    """
    Calculates the sum of a list of numbers.
    
    Parameters:
    - num_list (list): A list of numbers.
    
    Returns:
    - int: The sum of the numbers in num_list.
    """
    return sum(num_list)

def main():
    # Generate a list of random numbers
    random_numbers = [generate_random_number(1, 10) for _ in range(5)]
    print(f"Random Numbers: {random_numbers}")
    
    # Calculate the sum of the random numbers
    total_sum = sum_of_numbers(random_numbers)
    print(f"Sum of Numbers: {total_sum}")

if __name__ == '__main__':
    main()
```