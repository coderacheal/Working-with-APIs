import requests


API_KEY = '3e66a6bcecbb3d442fa28cb96148ddcb'
URL = 'https://api.openweathermap.org/data/2.5/weather'


city = input("Enter city name: ")
request_url = f'{URL}?appid={API_KEY}&q={city}&units=metric'

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    print(f'Weather: {weather}')
    print(f'Temperature: {temperature} Celcius')
    print(f'Humidity: {humidity}')

else:
    print(f"Data on {city} not found")
