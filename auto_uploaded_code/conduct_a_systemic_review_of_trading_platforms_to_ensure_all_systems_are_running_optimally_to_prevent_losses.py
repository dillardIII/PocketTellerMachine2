While your request cannot be accomplished via a Python script since it requires manual actions such as checking the actual applications, servers, and interfaces, a Python script can be devised to check if some web-based APIs are still operating as expected by sending regular requests and awaiting responses. Python also offers libraries to check system-specific parameters like memory usage, CPU load, etc.

However, remember each trading platform provides its own API with different endpoints and requirements, the specific details of trades, accounts, operations are proprietary and confidential. 

Below is a general Python script that sends a get request to an API and checks the status. 

**Note:** This below code purely hypothetical.

```python
import requests
import os
from datetime import datetime

# List of trading platform APIs
apis = {
    "Platform A": "http://api.platformA.com/status",
    "Platform B": "http://api.platformB.com/status",
    "Platform C": "http://api.platformC.com/status"
}

def check_platform_status():
    for platform, api in apis.items():
        try:
            response = requests.get(api)
            if response.status_code == 200:
                print(f'{platform} is running optimally at {datetime.now()}')
            else:
                print(f'{platform} may have issues, returned status code {response.status_code} at {datetime.now()}')

        except requests.RequestException as e:
            print(f'Cannot reach {platform} at {datetime.now()}, error: {e}')

check_platform_status()
```

System health check:

```python
import psutil

def check_system_health():
    # Checking CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_usage}')

    # Checking memory usage
    memory_usage = psutil.virtual_memory().percent
    print(f'Memory Usage: {memory_usage}')

    # Checking disk usage
    disk_usage = psutil.disk_usage('/').percent
    print(f'Disk Usage: {disk_usage}')

check_system_health()
```

Remember to run these scripts periodically (using schedulers like cron in Unix systems) to continuously monitor system and API status.

Also, make sure you have appropriate error handling and logging in place for this kind of scripts.
It's highly recommended to understand each trading platform's API documentation thoroughly and implement any API-specific error handling as necessary.