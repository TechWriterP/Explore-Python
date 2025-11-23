import requests
from requests import *

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4698a858eb94b71fc05ecb1ca675e6c6"
weather_params ={
    "lat": 19.075983,
    "lon": 72.877655,
    "cnt": 4,
    "appid": "4698a858eb94b71fc05ecb1ca675e6c6"
}

response = requests.get(url=API_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for _ in range(0,4):
    weather_condition = weather_data["list"][0]["weather"][0]["id"]
    if weather_condition < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
