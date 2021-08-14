# pip install selenium
# Chrome://version  "92.0.4515.131"
# Chrome Driver 다운로드 및 워킹디렉토리로 복사
from selenium import webdriver      # selenium 라이브러리의 webdriver 모듈을 가져옴
from selenium.webdriver.common.keys import Keys     # 키 입력을 위한 라이브러리 

browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe")
# browser.get("http://www.naver.com")


# elem = browser.find_element_by_class_name("link_login")       # "link_login" 태그를 검색
# elem.click()      # 클릭

# elem2 = browser.find_element_by_id("query")   # "id" 속성값이 "query" 인 엘리먼트를 찾음
# elem2.send_keys("검색 문자열")
# elem2.send_keys(Keys.ENTER)

# elem2 = browser.find_elements_by_tag_name("a")      # 모든 "a" 태그를 검색 : element -> 단독 / elements -> 다중
# elem2.get_attribute("href")       # 모든 "href" 엘리먼트 정보를 리스트 형태로 가져옴
# for e in elem2 :
#   print(e.get_attribute("href"))     # 모든 "href" 링크 정보를 순차적으로 가져옴

# elem = browser.find_element_by_name("q")


# browser.get("http://www.daum.net")
# elem = browser.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/form/fieldset/div/div/input")
# elem.send_keys("주가총액")
# elem.send_keys(Keys.ENTER)



# browser.back()    # 뒤로 가기
# browser.forward() # 앞으로 가기
# browser.refresh() # 새로고침
# browser.get("http://www.daum.net")    # "다음" 사이트로 이동


# browser.close()       # 현재 브라우저 탭을 닫음
# browser.quit()        # 현재 브라우저를 종료함
