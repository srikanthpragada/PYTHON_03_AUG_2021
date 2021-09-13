import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

countries = response.json()  # Get JSON converted to dict

for c in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    print(f"{c['name']:55}  {c['population']:10}  {c['area']:10.0f}")
