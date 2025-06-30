from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple implementation using the Flask framework in Python to create an API that returns "Hello World" when the endpoint "/hello" is called.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a new Flask web server from the __main__ module. The `@app.route('/hello')` decorator in Flask is a way to specify an URL so that when the URL is visited, it will trigger the associated function. In this case, when '/hello' is visited, it will trigger the `hello_world()` function which simply returns the string 'Hello World'. 

Lastly, the `app.run(debug=True)` enables the application to run on your local server in debug mode. This means that when you make changes to your code, it will automatically update without needing to manually restart the server.