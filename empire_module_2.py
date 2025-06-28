```python
import sys

def greet_user(name):
    """
    Function to greet the user with the provided name.
    
    Args:
    name (str): The name of the user.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def main():
    # Greet the user
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(greet_user(name))

    # Add two numbers
    a = 5
    b = 10
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

if __name__ == '__main__':
    main()
```