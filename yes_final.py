import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

f = open("yes_total.csv", "w")
f.write("뮤지컬/연극,제목,주최/기획,장소,YES24가격,YES24링크\n")

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
u = "http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=1&genre=15457"
driver.get(u)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
number = soup.select('p.li-sec-result')

for n in number:
    num = n.select_one('span#ListCntText').text
    num = num.strip().replace("개", "")

    num = int(num)/20 + 2
    i = 0
    while i < num:
        i = i + 1

        url ='http://ticket.yes24.com/New/Genre/Ajax/GenreList_Data.aspx?genre=15457&sort=3&area=&genretype=1&pCurPage=' + str(i) + '&pPageSize=20' #뮤지컬 > 전체보기 > 주간랭킹순
        r=requests.get(url)
        driver.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        container = soup.select('a')
        for c in container:
            title = c.select_one('p:nth-of-type(1)')
            if title == None: title=""
            else:
                title = title.text
                title = title.strip().replace(",", "")


            place = c.select_one('p:nth-of-type(3)')
            if place == None: place=""
            else: place = place.text
            place = place.strip().replace(",", "")

            link = ''.join(re.findall("\d+", c['onclick']))
            link = 'http://ticket.yes24.com/Perf/' + link

            driver.get(link)
            try:
                price = driver.find_element_by_css_selector("p.rn-product-price2>span.rn-red:nth-of-type(1)").text
                price = price.strip().replace(",", "")
            except:
                price = driver.find_element_by_css_selector("dd.rn-product-price span.rn-red").text
                price = price.strip().replace(",", "")

            try:
                host = driver.find_element_by_css_selector(
                    "div.rn-0805>div.rn08-txt>div>table>tbody>tr:nth-of-type(1)>td:nth-of-type(1)").text
                host = host.strip().replace(",", "")
            except:
                host = ""

            print(title, price+"원", host, place, link)

            f.write("뮤지컬," + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
f.close()

f = open("yes_total.csv", "a")

u = "http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=1&genre=15458"
driver.get(u)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
number = soup.select('p.li-sec-result')

for n in number:
    num = n.select_one('span#ListCntText').text
    num = num.strip().replace("개", "")

    num = int(num)/20 + 2
    i = 0
    while i < num:
        i = i + 1

        url ='http://ticket.yes24.com/New/Genre/Ajax/GenreList_Data.aspx?genre=15458&sort=3&area=&genretype=1&pCurPage=' + str(i) + '&pPageSize=20' 
        r=requests.get(url)
        driver.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        container = soup.select('a')
        for c in container:
            title = c.select_one('p:nth-of-type(1)').text
            title = title.strip().replace(",", "")


            place = c.select_one('p:nth-of-type(3)').text
            place = place.strip().replace(",", "")

            link = ''.join(re.findall("\d+", c['onclick']))
            link = 'http://ticket.yes24.com/Perf/' + link

            driver.get(link)
            try:
                price = driver.find_element_by_css_selector("p.rn-product-price2>span.rn-red:nth-of-type(1)").text
                price = price.strip().replace(",", "")
            except:
                price = driver.find_element_by_css_selector("dd.rn-product-price span.rn-red").text
                price = price.strip().replace(",", "")
            try:
                host = driver.find_element_by_css_selector(
                    "div.rn-0805>div.rn08-txt>div>table>tbody>tr:nth-of-type(1)>td:nth-of-type(1)").text
                host = host.strip().replace(",", "")
            except:
                host = ""

            print(title, price+"원", host, place, link)

            f.write("연극," + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
f.close()

f = open("yes_total.csv", "a")

u = "http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=2&genre=9991"
driver.get(u)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
number = soup.select('p.li-sec-result')

for n in number:
    num = n.select_one('span#ListCntText').text
    num = num.strip().replace("개", "")
    num=int(num)
    num = int(num)/20 + 2
    i = 0
    while i < num:
        i = i + 1

        url ='http://ticket.yes24.com/New/Genre/Ajax/GenreList_Data.aspx?genre=9991&sort=3&area=&genretype=1&pCurPage=' + str(i) + '&pPageSize=20' #뮤지컬 > 전체보기 > 주간랭킹순
        r=requests.get(url)
        driver.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        container = soup.select('a') 
        for c in container:
            title = c.select_one('p:nth-of-type(1)').text
            title = title.strip().replace(",", "")


            place = c.select_one('p:nth-of-type(3)').text
            place = place.strip().replace(",", "")

            link = ''.join(re.findall("\d+", c['onclick']))
            link = 'http://ticket.yes24.com/Perf/' + link

            driver.get(link)
            try:
                price = driver.find_element_by_css_selector("p.rn-product-price2>span.rn-red:nth-of-type(1)").text
                price = price.strip().replace(",", "")
            except:
                price = driver.find_element_by_css_selector("dd.rn-product-price span.rn-red").text
                price = price.strip().replace(",", "")
            try:
                host = driver.find_element_by_css_selector(
                    "div.rn-0805>div.rn08-txt>div>table>tbody>tr:nth-of-type(1)>td:nth-of-type(1)").text
                host = host.strip().replace(",", "")
            except:
                host = ""

            print(title, price+"원", host, place, link)


    f.write(title + ',' + host + ',' + place + ',아동/가족,' + price + '원,' + link + '\n')
f.close()

f = open("yes_total.csv", "a")

u = "http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=2&genre=9992"
driver.get(u)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
number = soup.select('p.li-sec-result')

for n in number:
    num = n.select_one('span#ListCntText').text
    num = num.strip().replace("개", "")
    num = int(num)
    num = int(num)/20 + 2
    i = 0
    while i < num:
        i = i + 1

        url ='http://ticket.yes24.com/New/Genre/Ajax/GenreList_Data.aspx?genre=9992&sort=3&area=&genretype=1&pCurPage=' + str(i) + '&pPageSize=20' #뮤지컬 > 전체보기 > 주간랭킹순
        r=requests.get(url)
        driver.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        container = soup.select('a')   
        for c in container:
            title = c.select_one('p:nth-of-type(1)').text
            title = title.strip().replace(",", "")

            place = c.select_one('p:nth-of-type(3)').text
            place = place.strip().replace(",", "")

            link = ''.join(re.findall("\d+", c['onclick']))
            link = 'http://ticket.yes24.com/Perf/' + link

            driver.get(link)
            try:
                price = driver.find_element_by_css_selector("p.rn-product-price2>span.rn-red:nth-of-type(1)").text
                price = price.strip().replace(",", "")
            except:
                price = driver.find_element_by_css_selector("dd.rn-product-price span.rn-red").text
                price = price.strip().replace(",", "")

            try:
                host = driver.find_element_by_css_selector("div.rn-0805>div.rn08-txt>div>table>tbody>tr:nth-of-type(1)>td:nth-of-type(1)").text
                host = host.strip().replace(",", "")
            except:
                host = ""

            print(title, price+"원", host, place, link)


    f.write('아동/가족,' + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
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


# 예사 뮤지컬
yes = pd.read_csv('./yes_total.csv',encoding='UTF-8')
yes_title=yes['제목']
yes_title=yes_title.tolist()

yes_place1 = yes['장소']
yes_place1 = yes_place1.tolist()
yes_place = yes['장소']
yes_place = yes_place.tolist()

yes_comp1 = yes['주최/기획']
yes_comp1 = yes_comp1.tolist()
yes_comp = yes['주최/기획']
yes_comp = yes_comp.tolist()
for i in range(len(yes_title)):
    yes_title[i] = yes_title[i].replace('뮤지컬', '').replace('연극', '').replace('대학로', '').replace('부산', '').replace('홍대', '').replace('[', '').replace(']', '').replace('새해선물', '').replace('오늘의컬쳐', '').replace('〈', '').replace('〉', '').replace(' ', '').replace('  ', '').replace('   ', '');
    yes_title[i] = ' '.join(yes_title[i])
    yes_title[i] = 'a'.join(str(x) for x in yes_title[i])
    yes_title[i] = 'a' + yes_title[i] + 'a'

    yes_place[i] = yes_place[i].replace(" ", "").replace("씨어터", "").replace("시어터", "")
    yes_place[i] = yes_place[i].upper()

    yes_comp[i] = yes_comp[i].replace(" ", "")


yes_list = []
yes_df = pd.DataFrame(yes_list, columns = ['제목', 'YES24가격', 'YES24링크'])
temp = 0

for i in range(len(yes_title)):
    max = 0
    for j in range(len(interpark_title)):

        compare_list = [yes_title[i], interpark_title[j]]

        tfidf_vectorizer = TfidfVectorizer(min_df=1)
        tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

        distances1 = (tfidf_matrix * tfidf_matrix.T)
        distances1 = distances1.toarray()[0][1]

        if yes_place[i] == interpark_place[j]:
            distances2 = 2
        elif yes_place[i] in interpark_place[j]:
            distances2 = 1
        elif interpark_place[j] in yes_place[i]:
            distances2 = 1
        else: distances2 = 0
        if yes_comp[i] == interpark_comp[j]:
            distances3 = 1
        else:
            distances3 = 0

        distances = distances1 + distances2 + distances3
        if distances > max:
            max_index = j
            max = distances

    if max > 1.25:
        name = interpark_title1[max_index]
        price = yes['YES24가격'][i]
        link = yes['YES24링크'][i]

        yes_df.loc[temp] = [name, price, link]
        temp = temp + 1



yes_df.to_csv('yes_final.csv', encoding="UTF-8")
