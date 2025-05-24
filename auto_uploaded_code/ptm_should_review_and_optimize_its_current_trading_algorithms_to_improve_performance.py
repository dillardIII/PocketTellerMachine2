As an AI model developed by OpenAI, I can provide you with a general idea of how you might approach this task in Python. However, I can't write specific code for you without knowing the details of your current trading algorithms. 

Here is a general approach:

1. Load and Analyze the Data: You will need to load your trading data into Python. You can use libraries like pandas for this. Analyze the data to understand its characteristics.

```python
import pandas as pd

data = pd.read_csv('trading_data.csv')
print(data.head())
```

2. Implement the Current Algorithm: Implement your current trading algorithm in Python. This will serve as your baseline for comparison.

```python
def current_algorithm(data):
    # Your current trading algorithm here
    pass
```

3. Measure Performance: Measure the performance of your current algorithm. This could be in terms of profit, loss, accuracy of predictions, etc.

```python
def measure_performance(data, algorithm):
    # Measure the performance of the algorithm
    pass

print(measure_performance(data, current_algorithm))
```

4. Optimize the Algorithm: Now, you can start optimizing your algorithm. This could involve using machine learning techniques to predict market movements, using more sophisticated algorithms, etc. The specifics will depend on your current algorithm and your trading strategy.

```python
def optimized_algorithm(data):
    # Your optimized trading algorithm here
    pass
```

5. Compare Performance: Finally, compare the performance of your optimized algorithm to your current algorithm.

```python
print(measure_performance(data, optimized_algorithm))
```

Remember, trading involves risk and optimizing an algorithm based on past performance does not guarantee future results. Always use sound judgement and consider other factors outside of your algorithm.