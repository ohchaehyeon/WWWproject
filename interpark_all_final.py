import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from urllib.request import urlretrieve
import ssl
import os
import shutil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def filename(path, index, num):
    return path + "/" +  str(num) + ".jpg"

def replacement(a):
    a = a.replace("%", "")
    a = a.replace("남자", "")
    a = a.replace("여자", "")
    a = a.replace("\n", "")
    return a

f = open("interpark.csv", "w")
f.write("순위,뮤지컬/연극,제목,가격,남자관객,여자관객,10대,20대,30대,40대,50대,링크,장소,주최/기획,장르,이미지링크\n")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-features=VizDisplayCompositor')
driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)


# 뮤지컬

path1 = './musical'
if os.path.isdir(path1):
    shutil.rmtree(path1)
    os.mkdir(path1)
else:
    os.mkdir(path1)

driver.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Mus")

raw = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Mus")
html = BeautifulSoup(raw.text, "html.parser")

container = html.select("div.con tbody tr span.fw_bold a")

rank = 1
index = 1
for c in container:
    link = c.attrs['href'][-8:]
    link = "https://tickets.interpark.com/goods/" + link


    # 상세페이지 이동
    driver.get(link)
    time.sleep(1)

    try:
        exit_btn = driver.find_element_by_css_selector("button.popupCloseBtn.is-bottomBtn")
        exit_btn.click()
        time.sleep(0.2)
    except:
        exit_btn = ""

    title = driver.find_element_by_css_selector("h2.prdTitle").text
    title = title.replace(",", "")
    try:
        place = driver.find_element_by_css_selector("div.infoDesc > a").text
        place = place[:-5]
        place = place.replace(",", "")
    except:
        place = ""
    print(place)
    print(rank, ": ", title)

    # 상세이미지 가져오기
    ssl._create_default_https_context = ssl._create_unverified_context
    img = driver.find_elements_by_css_selector("div.contentDetail strong img")

    img_list = []
    for i in img:
        img_list.append(i.get_attribute('src'))

    # 상세이미지 저장
    num = 1

    path = path1 + "/" + str(index)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)

    for i in img_list:
        urlretrieve(i, filename(path, index, num))
        num = num + 1
    index = index + 1

    #최저가
    try:
        minprice = driver.find_element_by_css_selector("li.infoPriceItem.is-largePrice > a").text
        minprice = minprice.split('원')[0].replace(',', '')
    except:
        minprice = ""
    print(minprice)

    # 셩별 비율
    try:
        male = driver.find_element_by_css_selector("div.statGenderType.is-male").text
        male = replacement(male)
        female = driver.find_element_by_css_selector("div.statGenderType.is-female").text
        female = replacement(female)
        print(male, female)

    except:
        male = "0"
        female = "0"

    # 연령별 비율
    try:
        age_10 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(1) div.statAgePercent").text
        age_10 = replacement(age_10)

        age_20 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(2) div.statAgePercent").text
        age_20 = replacement(age_20)

        age_30 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(3) div.statAgePercent").text
        age_30 = replacement(age_30)

        age_40 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(4) div.statAgePercent").text
        age_40 = replacement(age_40)

        age_50 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(5) div.statAgePercent").text
        age_50 = replacement(age_50)

    except:
        age_10 = "0"
        age_20 = "0"
        age_30 = "0"
        age_40 = "0"
        age_50 = "0"
    print(age_10, age_20, age_30, age_40, age_50)

    # 주최/기획
    btn_string = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2)").text
    if btn_string != '부가정보':
        btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(3) a")

    else:
        btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2) a")

    driver.execute_script("arguments[0].click();", btn)
    driver.implicitly_wait(3)

    try:
        company = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]").text
    except:
        company = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]").text


    company = company.replace(",", "")


    # 썸네일 이미지 가져오기
    img_link = driver.find_element_by_css_selector("div.posterBoxTop img")
    img_link = img_link.get_attribute('src')


    print(img_link)

    gg = "뮤지컬"
    g = "뮤지컬"

    f.write(str(
        rank) + "," + g + "," + title + "," + minprice + "원" + "," + male + "," + female + "," + age_10 + "," + age_20 + "," + age_30 + "," + age_40 + "," + age_50 + "," + link + "," + place + "," + company + "," + gg + "," + img_link + '\n')

    rank = rank + 1


# 연극

path1 = './play'
if os.path.isdir(path1):
    shutil.rmtree(path1)
    os.mkdir(path1)
else:
    os.mkdir(path1)

driver.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Dra")

raw = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Dra")
html = BeautifulSoup(raw.text, "html.parser")

container = html.select("div.con tbody tr span.fw_bold a")

rank = 1
index = 1
for c in container:
    link = c.attrs['href'][-8:]
    link = "https://tickets.interpark.com/goods/" + link


    # 상세페이지 이동
    driver.get(link)
    time.sleep(1)

    try:
        exit_btn = driver.find_element_by_css_selector("button.popupCloseBtn.is-bottomBtn")
        exit_btn.click()
        time.sleep(0.2)
    except:
        exit_btn = ""

    title = driver.find_element_by_css_selector("h2.prdTitle").text
    title = title.replace(",", "")
    try:
        place = driver.find_element_by_css_selector("div.infoDesc > a").text
        place = place[:-5]
        place = place.replace(",", "")
    except:
        place = ""
    print(place)
    print(rank, ": ", title)

    # 상세이미지 가져오기
    ssl._create_default_https_context = ssl._create_unverified_context
    img = driver.find_elements_by_css_selector("div.contentDetail strong img")

    img_list = []
    for i in img:
        img_list.append(i.get_attribute('src'))

    # 상세이미지 저장
    num = 1

    path = path1 + "/" + str(index)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)

    for i in img_list:
        urlretrieve(i, filename(path, index, num))
        num = num + 1
    index = index + 1

    #최저가
    try:
        minprice = driver.find_element_by_css_selector("li.infoPriceItem.is-largePrice > a").text
        minprice = minprice.split('원')[0].replace(',', '')
    except:
        minprice = ""
    print(minprice)

    
    # 셩별 비율
    try:
        male = driver.find_element_by_css_selector("div.statGenderType.is-male").text
        male = replacement(male)
        female = driver.find_element_by_css_selector("div.statGenderType.is-female").text
        female = replacement(female)
        print(male, female)

    except:
        male = "0"
        female = "0"

    # 연령별 비율
    try:
        age_10 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(1) div.statAgePercent").text
        age_10 = replacement(age_10)

        age_20 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(2) div.statAgePercent").text
        age_20 = replacement(age_20)

        age_30 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(3) div.statAgePercent").text
        age_30 = replacement(age_30)

        age_40 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(4) div.statAgePercent").text
        age_40 = replacement(age_40)

        age_50 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(5) div.statAgePercent").text
        age_50 = replacement(age_50)

    except:
        age_10 = "0"
        age_20 = "0"
        age_30 = "0"
        age_40 = "0"
        age_50 = "0"
    print(age_10, age_20, age_30, age_40, age_50)

    # 주최/기획
    btn_string = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2)").text
    if btn_string != '부가정보':
        btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(3) a")

    else:
        btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2) a")

    driver.execute_script("arguments[0].click();", btn)
    driver.implicitly_wait(3)

    try:
        company = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]").text
    except:
        company = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]").text


    company = company.replace(",", "")


    # 썸네일 이미지 가져오기
    img_link = driver.find_element_by_css_selector("div.posterBoxTop img")
    img_link = img_link.get_attribute('src')


    print(img_link)

    gg = "연극"
    g = "연극" 

    f.write(str(
        rank) + "," + g + "," + title + "," + minprice + "원" + "," + male + "," + female + "," + age_10 + "," + age_20 + "," + age_30 + "," + age_40 + "," + age_50 + "," + link + "," + place + "," + company + "," + gg + "," + img_link + '\n')

    rank = rank + 1


# 연극
gg = '아동/가족'

for i in range(1,3):
    if i == 1:
        r = "http://ticket.interpark.com/TPGoodsList.asp?Ca=Fam&SubCa=Fam_M"
        g = "뮤지컬"
    else:
        r = "http://ticket.interpark.com/TPGoodsList.asp?Ca=Fam&SubCa=Fam_P"
        g =  "연극"

    driver.get(r)

    raw = requests.get(r)
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("div.con tbody tr span.fw_bold a")

    rank = 1

    for c in container:
        link = c.attrs['href'][-8:]
        link = "https://tickets.interpark.com/goods/" + link

        # 상세페이지 이동
        driver.get(link)
        time.sleep(1)

        try:
            exit_btn = driver.find_element_by_css_selector("button.popupCloseBtn.is-bottomBtn")
            exit_btn.click()
            time.sleep(0.2)
        except:
            exit_btn = ""

        title = driver.find_element_by_css_selector("h2.prdTitle").text
        title = title.replace(",", "")
        try:
            place = driver.find_element_by_css_selector("div.infoDesc > a").text
            place = place[:-5]
            place = place.replace(",", "")
        except:
            place = ""
        print(place)
        print(rank, ": ", title)
        
        #최저가
        try:
            minprice = driver.find_element_by_css_selector("li.infoPriceItem.is-largePrice > a").text
            minprice = minprice.split('원')[0].replace(',', '')
        except:
            minprice = ""
        print(minprice)

        # 셩별 비율
        try:
            male = driver.find_element_by_css_selector("div.statGenderType.is-male").text
            male = replacement(male)
            female = driver.find_element_by_css_selector("div.statGenderType.is-female").text
            female = replacement(female)
            print(male, female)

        except:
            male = "0"
            female = "0"

        # 연령별 비율
        try:
            age_10 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(1) div.statAgePercent").text
            age_10 = replacement(age_10)

            age_20 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(2) div.statAgePercent").text
            age_20 = replacement(age_20)

            age_30 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(3) div.statAgePercent").text
            age_30 = replacement(age_30)

            age_40 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(4) div.statAgePercent").text
            age_40 = replacement(age_40)

            age_50 = driver.find_element_by_css_selector("div.statAgeBar div.statAgeType:nth-of-type(5) div.statAgePercent").text
            age_50 = replacement(age_50)

        except:
            age_10 = "0"
            age_20 = "0"
            age_30 = "0"
            age_40 = "0"
            age_50 = "0"
        print(age_10, age_20, age_30, age_40, age_50)

        # 주최/기획
        btn_string = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2)").text
        if btn_string != '부가정보':
            btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(3) a")

        else:
            btn = driver.find_element_by_css_selector("ul.navList li:nth-of-type(2) a")

        driver.execute_script("arguments[0].click();", btn)
        driver.implicitly_wait(3)

        try:
            company = driver.find_element_by_xpath(
                "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]").text
        except:
            company = driver.find_element_by_xpath(
                "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]").text

        company = company.replace(",", "")

        # 썸네일 이미지 가져오기
        img_link = driver.find_element_by_css_selector("div.posterBoxTop img")
        img_link = img_link.get_attribute('src')

        f.write(str(rank) + "," + g + "," + title + "," + minprice + "원" + "," + male + "," + female + "," + age_10 + "," + age_20 + "," + age_30 + "," + age_40 + "," + age_50 + "," + link + "," + place +"," + company + "," + gg + "," + img_link + '\n')

        rank = rank + 1

        
f.close()
driver.close()
