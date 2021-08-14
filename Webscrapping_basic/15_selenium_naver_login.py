from selenium import webdriver      # selenium 라이브러리의 webdriver 모듈을 가져옴
from selenium.webdriver.common.keys import Keys     # 키 입력을 위한 라이브러리 
import time

browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe")

#1. 네이버 사이트 접속
browser.get("http://www.naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)       # 3초 대기

#5. 아이디를 재 입력

# 기존의 입력되어 있는 문자열을 클리어
browser.find_element_by_id("id").clear()

# 아이디를 재 입력
browser.find_element_by_id("id").send_keys("my_id")


# 6. html 정보 출력
# html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit() # 전체 브라우저 종료