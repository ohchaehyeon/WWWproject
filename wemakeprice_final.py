import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

f = open("wemakeprice_total.csv", "w")
f.write("뮤지컬/연극,제목,주최/기획,장소,위메프가격,위메프링크\n")

#chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-features=VizDisplayCompositor')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mpzilla/5.0')
#chrome_options.add_argument('--remote-debugging-port=9222')
#chrome_options.add_argument('--window-size=1920X1080')

driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
url = "https://ticket.wemakeprice.com/category/10001"
driver.get(url)

scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
    time.sleep(1)
    new_scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
    if scroll_pane_height == new_scroll_pane_height:
        break
    scroll_pane_height = new_scroll_pane_height

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('div.sub-cate-lst li')

for c in container:
    title = c.select_one('strong.tit').text
    title = title.strip().replace(",", "")

    price = c.select_one('ins').text
    price = price.strip().replace(",", "")

    # a_tag = c.select_one('ul > li > a')
    a_tag = c.select_one('a')
    # if link == None: link=""
    # else: link = "https://ticket.wemakeprice.com" + a_tag['href']
    link = "https://ticket.wemakeprice.com" + a_tag['href']
    place = c.select_one('p.open-period span:nth-of-type(2)').text
    place = place.strip().replace(",", "")
    driver.get(link)
    try:
        host = driver.find_element_by_css_selector("table.table1 tr:nth-of-type(1) td").text
        host = host.strip().replace(",", "")
    except :
        host = ""

    print(title, price, host, place, link)

    f.write("뮤지컬," + title + ',' + host + ',' + place + ',' + price + ',' + link + '\n')
f.close()

f = open("wemakeprice_total.csv", "a")

url = "https://ticket.wemakeprice.com/category/10003"
driver.get(url)

scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
    time.sleep(1)
    new_scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
    if scroll_pane_height == new_scroll_pane_height:
        break
    scroll_pane_height = new_scroll_pane_height

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('div.sub-cate-lst li')

for c in container:
    title = c.select_one('strong.tit').text
    title = title.strip().replace(",", "")
    if 'CGV' in title:
        continue
    if '롯데시네마' in title:
        continue
    if '메가박스' in title:
        continue

    price = c.select_one('ins').text
    price = price.strip().replace(",", "")
    a_tag = c.select_one('a')
    link = "https://ticket.wemakeprice.com" + a_tag['href']
    place = c.select_one('p.open-period span:nth-of-type(2)').text
    place = place.strip().replace(",", "")
    driver.get(link)
    try:
        host = driver.find_element_by_css_selector("table.table1 tr:nth-of-type(1) td").text
        host = host.strip().replace(",", "")
    except :
        host = ""

    print(title, price, host, place, link)

    f.write("연극," + title + ',' + host + ',' + place + ',' + price + ',' + link + '\n')
f.close()

f = open("wemakeprice_total.csv", "a")

url = "https://ticket.wemakeprice.com/category/10006"
driver.get(url)

btn = driver.find_element_by_css_selector("div.main-sec>div>ul>li:nth-child(2)>a").click()
scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
    time.sleep(1)
    new_scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')
    if scroll_pane_height == new_scroll_pane_height:
        break
    scroll_pane_height = new_scroll_pane_height

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('div.sub-cate-lst li')

for c in container:
    title = c.select_one('strong.tit').text
    title = title.strip().replace(",", "")
    if '체험' in title:
        continue
    price = c.select_one('ins').text
    price = price.strip().replace(",", "")
    a_tag = c.select_one('a')
    link = "https://ticket.wemakeprice.com" + a_tag['href']
    place = c.select_one('p.open-period span:nth-of-type(2)').text
    place = place.strip().replace(",", "")
    driver.get(link)
    try:
        host = driver.find_element_by_css_selector("table.table1 tr:nth-of-type(1) td").text
        host = host.strip().replace(",", "")
    except :
        host = ""

    print(title, price, host, place, link)

    f.write("아동/가족," + title + ',' + host + ',' + place + "," + price + ',' + link + '\n')
f.close()

interpark = pd.read_csv('./interpark.csv',encoding='UTF-8')
interpark_title1=interpark['제목'] #원래 title
interpark_title1=interpark_title1.tolist()
interpark_title=interpark['제목'] #변경 title
interpark_title=interpark_title.tolist()

interpark_place1 = interpark['장소']
interpark_place1 = interpark_place1.tolist()
interpark_place = interpark['장소']
interpark_place = interpark_place.tolist()

interpark_comp1 = interpark['주최/기획']
interpark_comp1 = interpark_comp1.tolist()
interpark_comp = interpark['주최/기획']
interpark_comp = interpark_comp.tolist()


for i in range(len(interpark_title)):
    interpark_title[i] = interpark_title[i].replace('뮤지컬', '').replace('연극', '').replace('대학로', '').replace('부산', '').replace('홍대', '').replace('[', '').replace(']', '').replace('〈', '').replace('〉', '').replace(' ', '').replace('  ', '').replace('   ', '');
    interpark_title[i] = ' '.join(interpark_title[i])
    interpark_title[i] = 'a'.join(str(x) for x in interpark_title[i])
    interpark_title[i] = 'a' + interpark_title[i] + 'a'

    interpark_place[i] = str(interpark_place[i]).replace(" ", "").replace("씨어터", "").replace("시어터", "")
    interpark_place[i] = interpark_place[i].upper()

    interpark_comp[i] = str(interpark_comp[i]).replace(" ", "")


# 위메프 뮤지컬
wmp = pd.read_csv('./wemakeprice_total.csv',encoding='UTF-8')
wmp_title=wmp['제목']
wmp_title=wmp_title.tolist()

wmp_place1 = wmp['장소']
wmp_place1 = wmp_place1.tolist()
wmp_place = wmp['장소']
wmp_place = wmp_place.tolist()

wmp_comp1 = wmp['주최/기획']
wmp_comp1 = wmp_comp1.tolist()
wmp_comp = wmp['주최/기획']
wmp_comp = wmp_comp.tolist()
for i in range(len(wmp_title)):
    wmp_title[i] = wmp_title[i].replace('뮤지컬', '').replace('연극', '').replace('대학로', '').replace('부산', '').replace('홍대', '').replace('[', '').replace(']', '').replace('새해선물', '').replace('오늘의컬쳐', '').replace('〈', '').replace('〉', '').replace(' ', '').replace('  ', '').replace('   ', '');
    wmp_title[i] = ' '.join(wmp_title[i])
    wmp_title[i] = 'a'.join(str(x) for x in wmp_title[i])
    wmp_title[i] = 'a' + wmp_title[i] + 'a'

    wmp_place[i] = wmp_place[i].replace(" ", "").replace("씨어터", "").replace("시어터", "")
    wmp_place[i] = wmp_place[i].upper()

    wmp_comp[i] = wmp_comp[i].replace(" ", "")


wmp_list = []
wmp_df = pd.DataFrame(wmp_list, columns = ['제목', '위메프가격', '위메프링크'])
temp = 0

for i in range(len(wmp_title)):
    max = 0
    for j in range(len(interpark_title)):

        compare_list = [wmp_title[i], interpark_title[j]]

        tfidf_vectorizer = TfidfVectorizer(min_df=1)
        tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

        distances1 = (tfidf_matrix * tfidf_matrix.T)
        distances1 = distances1.toarray()[0][1]

        if wmp_place[i] == interpark_place[j]:
            distances2 = 2
        elif wmp_place[i] in interpark_place[j]:
            distances2 = 1
        elif interpark_place[j] in wmp_place[i]:
            distances2 = 1
        else: distances2 = 0
        if wmp_comp[i] == interpark_comp[j]:
            distances3 = 1
        else:
            distances3 = 0

        distances = distances1 + distances2 + distances3
        if distances > max:
            max_index = j
            max = distances

    if max > 1.25:
        name = interpark_title1[max_index]
        price = wmp['위메프가격'][i]
        link = wmp['위메프링크'][i]

        wmp_df.loc[temp] = [name, price, link]
        temp = temp + 1



wmp_df.to_csv('wemakeprice_final.csv', encoding="UTF-8")
