import requests

from bs4 import BeautifulSoup

WEBSITE = "https://www.amazon.in/Logitech-MK850-Performance-Wireless-Keyboard/dp/B01NAVO5PF"
response = requests.get(WEBSITE, timeout=5 ,
                         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})

if response.status_code != 200:
    print(f"Sorry! Could not access website with status code = {response.status_code}")
    exit(1)

bs = BeautifulSoup(response.text, 'html.parser')
price = bs.find('span', attrs={"class": "a-offscreen"})
print (price.text)

