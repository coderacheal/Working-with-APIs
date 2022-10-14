import requests

from_currency = str(input('Enter Currency to convert from: ')).upper()
to_cufrankfurterrrency = str(input('Enter Currency to convert to: ')).upper()
amt = float(input('Enter Amount: '))

host_url = 'api..app'
response = requests.get(
    f"https://{host_url}/latest?amount={amt}&from={from_currency}&to={to_currency}")

if response.status_code == 200:
    print(
        f"{amt} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
    print(f"As at {response.json()['date']}")
elif ValueError:
    print("Currency does no exist. Please check the inputed currency")
else:
    print("No data found")
