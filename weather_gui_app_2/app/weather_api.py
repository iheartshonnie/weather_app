import requests

API_KEY = "4648d884354b1a375cba33b9f37b4fca"
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