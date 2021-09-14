import requests

from bs4 import BeautifulSoup

WEBSITE = "https://www.amazon.in/Logitech-MK850-Performance-Wireless-Keyboard/dp/B01NAVO5PF/ref=sr_1_1?dchild=1&keywords=MK+850&qid=1631586874&sr=8-1"
response = requests.get(WEBSITE)
if response.status_code != 200:
    print(f"Sorry! Could not access website with status code = {response.status_code}")
    exit(1)

bs = BeautifulSoup(response.text, 'html.parser')
price = bs.find(id="twister-plus-price-data-price")
print(f"Price = {price['value']}")
