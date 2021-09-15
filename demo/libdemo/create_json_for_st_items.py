from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

response = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(response.text, 'lxml-xml')

item_elements = bs.find_all("item")

items = []
for item in item_elements:
    title = item.find("title").text.strip()
    link = item.find("link").text.strip()
    description = item.find("description").text.strip()
    pubdate = item.find("pubDate").text
    try:
        pd = datetime.strptime(pubdate[5:16], "%d %b %Y")
        pdate = pd.strftime("%d-%b-%Y")
        days = (datetime.now() - pd).days
    except:
        pdate = None
        days = 0

    item_dict = {"title": title, "link": link, "description": description,
                 "pubdate": pdate, "days": days}

    items.append(item_dict)

with open("items.json", "wt") as f:
    json.dump(items, f)
