```python
import random

def generate_random_number(start, end):
    """Generate a random number between start and end."""
    return random.randint(start, end)

def check_guess(guess, actual):
    """Check if the guess is correct, too low, or too high."""
    if guess < actual:
        return "Your guess is too low."
    elif guess > actual:
        return "Your guess is too high."
    else:
        return "Congratulations! You guessed it right."

def main():
    start = 1
    end = 100
    actual_number = generate_random_number(start, end)
    print(f"Guess the number between {start} and {end}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            result = check_guess(guess, actual_number)
            print(result)
            if guess == actual_number:
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
```