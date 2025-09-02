import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# print(response.json())
MY_LAT = 18.9582
MY_LNG = 72.8321

parameters = {"lat": MY_LAT,
            "lng": MY_LNG,
              "formatted":0}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunrise)
print(sunset)