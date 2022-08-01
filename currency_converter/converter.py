import requests

from_currency = str(input('Enter Currency to convert from: ')).upper()
to = str(input('Enter Currency to convert to: ')).upper()
amt = float(input('Enter Amount: '))

host_url = 'api.frankfurter.app'
response = requests.get(
    f"https://${host_url}/latest?amount={amt}&from={from_currency}&to={to}")
# print(response.status_code)
# print(am)
