from rich import print
from bs4 import BeautifulSoup
import requests


def schedule_parser():
    url = 'https://student.lpnu.ua/students_schedule?departmentparent_abbrname_selective=ІКТА&studygroup_abbrname_selective=КІ-34&semestrduration=1'
    src = requests.get(url)
    soup = BeautifulSoup(src.text, "lxml")
    all_info = soup.find("div", class_="view-content")
    day = {}
    content = all_info.find_all("div", class_="view-grouping")
    count = 0
    for i in content:
        lessons = {}
        for j in i.find_all("div", class_="week_color"):
            lesson = {}
            lesson["id_lesson"] = j.find_parent().previous_element.previous_element
            lesson["name_lesson"] = j.find("div", class_="group_content").text
            link = soup.find("div", class_="group_content").find("span").find("a")
            lesson["link_lesson"] = link.get("href")
            lessons["lesson_" + lesson["id_lesson"]] = lesson
        count += 1
        day["name_"+ str(count)] = i.find("div", class_="view-grouping-header").text
        day["lessons_"+ str(count)] = lessons
    return day


print(schedule_parser())