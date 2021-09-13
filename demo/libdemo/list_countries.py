import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)
countries = response.json()  # Get JSON converted to dict

for c in countries:
    print(f"{c['name']:55}  {c['capital']}")






