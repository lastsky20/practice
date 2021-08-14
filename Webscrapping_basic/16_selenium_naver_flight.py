
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome("C:/Users/PC/Desktop/PythonWork/chromedriver_win32/chromedriver.exe")

url = "https://beta-flight.naver.com/"

browser.get(url)
browser.maximize_window()   # 창 최대화

# 1. 가는 날 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 엘리먼트의 날짜가 7월과 8월 두 부분으로 나눠서 출력됨
# "link_text" 모듈로 가져온 리스트 정보중 첫번째와 두번째 데이터로 서로 구분
# 가는날 이번달 27일, 28일 선택
# browser.find_element_by_link_text("27")[0].click()
# browser.find_element_by_link_text("28")[0].click()

# 가는날 다음달 27일, 28일 선택
# browser.find_element_by_link_text("27")[1].click()
# browser.find_element_by_link_text("28")[1].click()

time.sleep(1)
# 가는날 이번달 27일, 다음달28일 선택
browser.find_element_by_link_text("27")[0].click()  # 이번 달

time.sleep(1)
browser.find_element_by_link_text("28")[0].click()  # 이번 달


time.sleep(2)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[2]/i[1]").click()
