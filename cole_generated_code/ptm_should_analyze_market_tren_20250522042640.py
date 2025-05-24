To analyze market trends and set up alerts for potential trading opportunities, we can use the pandas library for data analysis and manipulation, yfinance to download historical market data from Yahoo finance, and smtplib for setting up email alerts. Here is a simple example of how you could do this:

```python
import pandas as pd
import yfinance as yf
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the stock to analyze
stock = 'AAPL'

# Download historical data as dataframe
data = yf.download(stock, start='2020-01-01', end='2022-12-31')

# Calculate moving averages
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Define a signal
data['Signal'] = 0.0  
data['Signal'][data['MA10'] > data['MA50']] = 1.0

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print data
print(data)

# Set up email alert
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('YourEmail@gmail.com', 'YourPassword')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('YourEmail@gmail.com', 'YourEmail@gmail.com', message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

# Check for trading opportunities and send email
if data['Position'].iloc[-1] == 1.0:
    send_email("Trading Alert", "Buy " + stock)
elif data['Position'].iloc[-1] == -1.0:
    send_email("Trading Alert", "Sell " + stock)
```

Please replace 'YourEmail@gmail.com' and 'YourPassword' with your actual email and password. Also, this code assumes that you have enabled "Less secure app access" in your Google account. If not, you might face issues in sending emails.

This is a very basic trading strategy and doesn't take into account many factors that could influence the trading decision. You should use this as a starting point and build a more comprehensive strategy based on your needs.

Also, keep in mind that this is a simplistic example and real-world trading involves more complex analysis and risk. Always consult with a financial advisor before making trading decisions.