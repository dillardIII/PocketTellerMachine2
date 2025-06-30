from ghost_env import INFURA_KEY, VAULT_ADDRESS
```python
import random

def generate_random_number(start, end):
    return random.randint(start, end)

def guess_number(secret_number, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number!")
                return True
            attempts += 1
        except ValueError:
            print("Invalid input! Please enter an integer.")
    print(f"Sorry, you've used all attempts. The number was {secret_number}.")
    return False

if __name__ == '__main__':
    START = 1
    END = 100
    secret_number = generate_random_number(START, END)
    print(f"Welcome to the number guessing game! Guess a number between {START} and {END}.")
    guess_number(secret_number)
```


def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():