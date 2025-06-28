```python
import random
import string

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def count_vowels(input_string):
    """Count the number of vowels in a given string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

def main():
    # Generate a random string
    random_string = generate_random_string()
    print(f"Random String: {random_string}")
    
    # Count vowels in the random string
    vowel_count = count_vowels(random_string)
    print(f"Number of vowels in the random string: {vowel_count}")

if __name__ == '__main__':
    main()
```