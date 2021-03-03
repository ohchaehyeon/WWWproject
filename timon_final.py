from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
                                                                             
f = open("timon_total.csv", "w")
f.write("뮤지컬/연극,제목,주최/기획,장소,티몬가격,티몬링크\n")

#chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-features=VizDisplayCompositor')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mpzilla/5.0')
#chrome_options.add_argument('--remote-debugging-port=9222')
#chrome_options.add_argument('--window-size=1920X1080')

driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
url = "http://www.tmon.co.kr/deallist/18170002"
driver.get(url)
#driver.implicitly_wait(2)

cancel_btn = driver.find_element_by_css_selector("button._closeAllTimeAlert.expires.layer_time_text_button")
cancel_btn.click()
#driver.implicitly_wait(2)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('li.item')

for c in container:
    title = c.select_one('p.title_name').text
    title = title.strip().replace(",", "")

    price = c.select_one('span.price > i')
    if price == None: price=""
    else:
        price = price.text
        price = price.strip().replace(",", "")


    a_tag = c.select_one('a')
    link = a_tag['href']
    driver.get(link)
    #driver.implicitly_wait(2)

    place = ""
    try:
        place = driver.find_element_by_css_selector("h4.info__area__tit").text

    except:
        try: place = driver.find_element_by_css_selector("p.deal_title_sub span:nth-of-type(3)").text
        except: place = ""

    time.sleep(2)
    host_btn = driver.find_element_by_css_selector("ul.tab-navigation li:nth-child(4)")
    host_btn.click()
    #driver.implicitly_wait(2)

    try:
        host = driver.find_element_by_css_selector("#_wrapProductInfoNotes > div > div > div > table > tbody > tr:nth-child(1) > td").text
        host = host.strip().replace(",", "")
    except:
        host = ""

    print(title, price+"원", host, place, link)

    f.write("뮤지컬," + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
f.close()

f = open("timon_total.csv", "a")

time.sleep(2)
url = "http://www.tmon.co.kr/deallist/18170004"
driver.get(url)
#driver.implicitly_wait(2)

#cancel_btn = driver.find_element_by_css_selector("button._closeAllTimeAlert.expires.layer_time_text_button")
#cancel_btn.click()

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('li.item')

for c in container:
    title = c.select_one('p.title_name').text
    title = title.strip().replace(",", "")

    price = c.select_one('span.price > i')
    if price == None: price=""
    else:
        price = price.text
        price = price.strip().replace(",", "")
    a_tag = c.select_one('a')
    link = a_tag['href']
    driver.get(link)
    #driver.implicitly_wait(2)

    subtitle = driver.find_element_by_css_selector("h2.deal_title_main").text
    subtitle = subtitle.strip().replace(",", "")
    if 'CGV' in subtitle:
        continue
    if '롯데시네마' in subtitle:
        continue
    if '메가박스' in subtitle:
        continue

    place = ""
    try:
        place = driver.find_element_by_css_selector("h4.info__area__tit").text

    except:
        try:
            place = driver.find_element_by_css_selector("p.deal_title_sub span:nth-of-type(3)").text
        except:
            place = ""

    time.sleep(2)
    host_btn = driver.find_element_by_css_selector("ul.tab-navigation li:nth-child(4)")
    host_btn.click()
    #driver.implicitly_wait(2)
    try:
        host = driver.find_element_by_css_selector("#_wrapProductInfoNotes > div > div > div > table > tbody > tr:nth-child(1) > td").text
        host = host.strip().replace(",", "")
    except:
        host = ""

    print(title, price+"원", host, place, link)

    f.write("연극," + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
f.close()


f = open("timon_total.csv", "a")

time.sleep(2)
url = "http://www.tmon.co.kr/deallist/18170006"
driver.get(url)
#driver.implicitly_wait(2)

#cancel_btn = driver.find_element_by_css_selector("button._closeAllTimeAlert.expires.layer_time_text_button")
#cancel_btn.click()

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
container = soup.select('li.item')

for c in container:
    title = c.select_one('p.title_name').text
    title = title.strip().replace(",", "")

    price = c.select_one('span.price > i')
    if price == None: price=""
    else:
        price = price.text
        price = price.strip().replace(",", "")

    a_tag = c.select_one('a')
    link = a_tag['href']
    driver.get(link)
    #driver.implicitly_wait(2)

    subtitle = driver.find_element_by_css_selector("h2.deal_title_main").text
    subtitle = subtitle.strip().replace(",", "")
    if '체험' in subtitle:
        continue
    place = ""
    try:
        place = driver.find_element_by_css_selector("h4.info__area__tit").text

    except:
        place = place

    time.sleep(2)
    host_btn = driver.find_element_by_css_selector("ul.tab-navigation li:nth-child(4)")
    host_btn.click()
    #driver.implicitly_wait(2)

    try:
        host = driver.find_element_by_css_selector("#_wrapProductInfoNotes > div > div > div > table > tbody > tr:nth-child(1) > td").text
        host = host.strip().replace(",", "")

    except: host = ""

    print(title, price+"원", host, place, link)
    f.write("아동/가족," + title + ',' + host + ',' + place + ',' + price + '원,' + link + '\n')
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


# 티몬 뮤지컬
timon = pd.read_csv('./timon_total.csv',encoding='UTF-8')
timon_title=timon['제목']
timon_title=timon_title.tolist()

timon_place1 = timon['장소']
timon_place1 = timon_place1.tolist()
timon_place = timon['장소']
timon_place = timon_place.tolist()

timon_comp1 = timon['주최/기획']
timon_comp1 = timon_comp1.tolist()
timon_comp = timon['주최/기획']
timon_comp = timon_comp.tolist()
for i in range(len(timon_title)):
    timon_title[i] = timon_title[i].replace('뮤지컬', '').replace('연극', '').replace('대학로', '').replace('부산', '').replace('홍대', '').replace('[', '').replace(']', '').replace('새해선물', '').replace('오늘의컬쳐', '').replace('〈', '').replace('〉', '').replace(' ', '').replace('  ', '').replace('   ', '');
    timon_title[i] = ' '.join(timon_title[i])
    timon_title[i] = 'a'.join(str(x) for x in timon_title[i])
    timon_title[i] = 'a' + timon_title[i] + 'a'

    timon_place[i] = timon_place[i].replace(" ", "").replace("씨어터", "").replace("시어터", "")
    timon_place[i] = timon_place[i].upper()

    timon_comp[i] = timon_comp[i].replace(" ", "")


timon_list = []
timon_df = pd.DataFrame(timon_list, columns = ['제목', '티몬가격', '티몬링크'])
temp = 0

for i in range(len(timon_title)):
    max = 0
    for j in range(len(interpark_title)):

        compare_list = [timon_title[i], interpark_title[j]]

        tfidf_vectorizer = TfidfVectorizer(min_df=1)
        tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

        distances1 = (tfidf_matrix * tfidf_matrix.T)
        distances1 = distances1.toarray()[0][1]

        if timon_place[i] == interpark_place[j]:
            distances2 = 2
        elif timon_place[i] in interpark_place[j]:
            distances2 = 1
        elif interpark_place[j] in timon_place[i]:
            distances2 = 1
        else: distances2 = 0
        if timon_comp[i] == interpark_comp[j]:
            distances3 = 1
        else:
            distances3 = 0

        distances = distances1 + distances2 + distances3
        if distances > max:
            max_index = j
            max = distances

    if max > 1.25:
        name = interpark_title1[max_index]
        price = timon['티몬가격'][i]
        link = timon['티몬링크'][i]

        timon_df.loc[temp] = [name, price, link]
        temp = temp + 1



timon_df.to_csv('timon_final.csv', encoding="UTF-8")

