import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import csv


f = open("./interpark_region.csv", "w")
f.write("지역,제목,링크\n")
wr = csv.writer(f)

#서울, 경기, 강원, 충북, 충남, 경북, 경남, 전북, 전남, 제주
seoul_code = '01'
regions_code = [seoul_code, 10, 80, 70, 60, 30, 20, 50, 40, 90]

for region in regions_code:

    raw = requests.get("http://ticket.interpark.com/TiKi/Special/TPRegionReserve.asp?Region=420"+ str(region))
    html = BeautifulSoup(raw.text, "html.parser")
    lists = html.find_all('div', attrs={'class': 'content'})
    for list in lists:
        try:
            list_title = list.select_one("p.txt").text
            list_title = list_title.strip().replace(",", "")
            c = list.select_one("a")
            link = c.attrs['href'][-8:]
            link = "https://tickets.interpark.com/goods/" + link
            print(region, ",", end=" ")
            print(link, ",", end=" ")
            print(list_title)
        except:
            None
        f.write(str(region) + ',' + list_title + ',' + link + '\n')
f.close()
