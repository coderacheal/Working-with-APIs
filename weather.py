import requests


MY_API_KEY = '3e66a6bcecbb3d442fa28cb96148ddcb'
URL = 'https://api.openweathermap.org/data/2.5/weather'


print("Hi, and welcome to Racheal's Weather App ;)")
city = input("Enter city name: ")
request_url = f'{URL}?appid={MY_API_KEY}&q={city}&units=metric'

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'].title()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    print('--------------------------------------')
    print(f'Weather: {weather}')
    print(f'Temperature: {temperature} Celcius')
    print(f'Humidity: {humidity}')
    print('--------------------------------------')


else:
    print(f"Data on {city} not found")
    print('--------------------------------------')

