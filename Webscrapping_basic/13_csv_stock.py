import csv
import requests
import re
from bs4 import BeautifulSoup
from requests.api import request

filename = "네이버 금융_시가 총액"
# f = open("filename.csv", "w", encoding = "utf8", newline = "")  # 파일을 오픈, 줄바꿈 없이 작성
f = open("filename.csv", "w", encoding = "utf-8-sig", newline = "")  # 엑셀 파일에서 한글이 깨지면 "utf-8-sig" 로 작성
write = csv.writer(f)   # csv 라이브버리의 writer 호출하고, 파일(f) 을 넘김

## split() 으로 탭을 제거 하고 리스트 형태로 저장
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	".split("\t")
write.writerow(title)

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

# 1. url 에서 table 태그로 시작하는 속성의 class 가 type_2 인 엘리먼트 -> tbody 태그의 tr 태그를 모두 가져옴
# 2. 위의 정보에서 모든 td 정보를 가져옴
# 3. 가져온 td 정보에서 len 함수를 사용하여 속성값이 1 이하인 td(테이블) 를 스킵함
# 4. strip() 을 사용하여 문자열의 처음 공백을 제거 함.
# 5. csv 를 작성.



for page in range(1, 5) :
    res = requests.get(url + str(page), headers)

    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")

    for row in data_rows :
        columns = row.find_all("td")
        if len(columns) <= 1 :
            continue
        
        ## strip() : 공백문자 제거
        data = [column.get_text().strip() for column in columns]        
        # print(data)
        write.writerow(data)    # 파일(f) 에 data 를 작성