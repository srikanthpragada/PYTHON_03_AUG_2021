from bs4 import BeautifulSoup
import json

with open("courses.xml", "rt") as f:
    content = f.read()

bs = BeautifulSoup(content, 'lxml-xml')

courses = bs.find_all("course")

courses_list = []
for c in courses:
    title = c.find("title").text
    fee = c.find("fee").text
    course_dict = {"title": title, "fee": fee}
    courses_list.append(course_dict)


with open("courses.json", "wt") as f:
    json.dump(courses_list, f)

