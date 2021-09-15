from bs4 import BeautifulSoup

with open("courses.xml", "rt") as f:
    content = f.read()

bs = BeautifulSoup(content, 'lxml-xml')

courses = bs.find_all("course")

for c in courses:
    title = c.find("title").text
    fee = c.find("fee").text
    print(f"{title:20} {fee:6}")