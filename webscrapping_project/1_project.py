import requests
import re
from bs4 import BeautifulSoup
from requests.api import request
from selenium import webdriver



## 날씨 정보 url
url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8"

## 네이버 뉴스
url2 = "https://news.naver.com/"

## 네이버 it 뉴스
url3 = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

res1 = requests.get(url1, headers = headers)
res2 = requests.get(url2, headers = headers)
res3 = requests.get(url3, headers = headers)

res1.raise_for_status()
res2.raise_for_status()
res3.raise_for_status()

soup1 = BeautifulSoup(res1.text, "lxml")
soup2 = BeautifulSoup(res1.text, "lxml")
soup3 = BeautifulSoup(res1.text, "lxml")

print("[오늘의 날씨]")
print(soup1.find("p", {"class" : "cast_txt"}).get_text())
print(f"현재 : {soup1.find('span', {'class' : 'todaytemp'}).get_text()} 'C")
soup1_swap = soup1.find('span', {'class' : 'rain_rate wet'})
print(f"오전 강수확률 : {soup1_swap.find('span', {'class' : 'num'}).get_text()} %")
print(f"오전 강수확률 : {soup1.find('span', {'class' : 'point_time afternoon'}).get_text().strip()}")