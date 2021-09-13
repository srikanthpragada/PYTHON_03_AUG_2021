import requests

city = "Visakhapatnam"
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a336037d7de7c3966918c60e3419791a")
if response.status_code != 200:
    print(f"Sorry! Could not get details for city - {city}!")
    exit(1)

details = response.json()  # Get JSON converted to dict

print("Today weather is :  ", details['weather'][0]['description'])
