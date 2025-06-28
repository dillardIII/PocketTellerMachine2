```python
import random

def generate_random_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    size = 10
    start = 1
    end = 100
    random_list = generate_random_list(size, start, end)
    print("Unsorted List:", random_list)
    sorted_list = bubble_sort(random_list)
    print("Sorted List:", sorted_list)

if __name__ == '__main__':
    main()
```