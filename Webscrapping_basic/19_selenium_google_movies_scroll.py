import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://play.google.com/store/movies/top"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Accept-Language" : "ko-KR,ko"}



browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe")
browser.maximize_window()
browser.get(url)

# 지정 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")
# browser.execute_script("window.scrollTo(0, 2080)")

## 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2
## 브라우저의 높이 값 "scrollHeight" 을 가져옴
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    ## 브라우저의 스크롤을 현재 브라우저의 높이만큼 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)
    
    ## 스크롤을 내린 후 현재 높이값을 다시 가져옴
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    # 현재 스크롤 높이와 이전 스크롤 높이의 값이 같을 때 까지 반복
    if prev_height == curr_height :
        break

    prev_height = curr_height

print("스크롤 내리기 종료")


# res = requests.get(url, headers = headers)
# res.raise_for_status()

# 현재 실행되어 있는 브라우저의 페이지 소스를 가져옴
soup = BeautifulSoup(browser.page_source, "lxml")

## attrs 부분에 리스트 형태로 2개의 조건을 다 가지고 옴
# movies = soup.find_all("div", attrs = {"class" : ["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"})

print(len(movies))

for movie in movies : 
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    
    # 할인전 가격이 없으면 스킵
    if original_price :
        original_price = original_price.get_text()
    else : 
        continue

    # 할인 된 가격
    price = movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 "href" 정보를 가져옴
    link = movie.find("a", attrs = {"class" : "JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 된 금액 : {price}")
    print("링크 :" "https://play.google.com" + link)
    print("-" * 50)

browser.quit()