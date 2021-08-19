import requests
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium import webdriver


if __name__ == "__main__" :
    url = "https://www.coupang.com/vp/products/47370431?itemId=167595546&vendorItemId=3398849213&sourceType=CATEGORY&categoryId=178340&isAddedCart="
    # headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}


    options = webdriver.ChromeOptions()
    # options.headless = False
    options.add_argument("lang=ko_KR")      ### 문제해결을 위한 추가문장
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")    # 문제해결을 위한 추가문장
    ## headless chrome 을 숨기기 위한 user agent 정보를 할당
    options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
    # 실행 pc 의 디스플레이 해상도 정보
    # options.add_argument("window-size = 1920x1080")


    browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe")

    # browser.maximize_window()
    browser.get(url)



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