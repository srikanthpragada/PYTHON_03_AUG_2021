import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

details = response.json()  # Get JSON converted to dict

print(f"Login       : {details['login']}")
print(f"Name        : {details['name']}")
print(f"Company     : {details['company']}")
print(f"Repo Count  : {details['public_repos']}")






