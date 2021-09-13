import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

details = response.json()  # Get JSON converted to dict

for k, v in details.items():
    if v is not None and len(str(v)) > 0:
        print(f"{k:20}  {v}")






