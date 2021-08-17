import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

##################################################
## headless 크롬(백그라운드) 을 사용하기 위한 옵션
options = webdriver.ChromeOptions()
options.headless = True
## headless chrome 을 숨기기 위한 user agent 정보를 할당
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
# 실행 pc 의 디스플레이 해상도 정보
options.add_argument("window-size=1920x1080")
##################################################

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
#             "Accept-Language" : "ko-KR,ko"}

    

browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe", options = options)
browser.maximize_window()
browser.get(url)

## none headless chrome UserAgent
# User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/92.0.4515.131 Safari/537.36

## headless chrome UserAgent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/92.0.4515.131 Safari/537.36

d_value = browser.find_element_by_id("detected_value")

print(d_value)

quit()

