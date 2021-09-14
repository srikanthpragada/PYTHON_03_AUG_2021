import requests

from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
response = requests.get(WEBSITE)
if response.status_code != 200:
    print("Sorry! Could not access website!")

bs = BeautifulSoup(response.text, 'html.parser')

for t in bs.find_all("img"):
    title = t['title'] if 'title' in t.attrs else 'Null'
    src = t['src']
    if not src.startswith("http"):
        src = WEBSITE + "/" + src

    print(f"{src} - {title}")
