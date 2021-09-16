import requests

city = "Visakhapatnam"
yourid = ""
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={yourid}")
if response.status_code != 200:
    print(f"Sorry! Could not get details for city - {city}!")
    exit(1)

details = response.json()  # Get JSON converted to dict

print("Today weather is :  ", details['weather'][0]['description'])
