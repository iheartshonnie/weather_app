import requests

API_KEY = "YOUR API KEY HERE"
BASE_URL = "https://openweathermap.org/api/weather-api"

def get_weather_for_city(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return {'temperature': None, 'description': 'City not found'}
