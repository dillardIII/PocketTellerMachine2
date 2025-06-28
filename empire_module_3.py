```python
import sys
from datetime import datetime

def greet_user(name):
    """
    Greets the user with their name and the current time.
    
    Args:
        name (str): The name of the user.
        
    Returns:
        str: A greeting message with the current time.
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Hello, {name}! The current time is {current_time}."

def calculate_sum(a, b):
    """
    Calculates the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

def main():
    # Check for user input
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
    else:
        user_name = "Guest"
    
    # Greet the user
    greeting = greet_user(user_name)
    print(greeting)

    # Perform a sample computation
    a, b = 3.5, 4.5
    result = calculate_sum(a, b)
    print(f"The sum of {a} and {b} is {result}.")

if __name__ == '__main__':
    main()
```