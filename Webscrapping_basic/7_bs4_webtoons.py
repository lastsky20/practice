import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

print("응답코드", res.status_code)

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs = {"class" : "title"})      # find_all : 모든 엘리먼트를 찾음
# "class" 속성이 "title" 인 모든 "a" 엘리먼트를 반환

with open("webtoons.txt", "w", encoding = "utf8") as f:                                                               # 태그명이 "a" 이고 "class" 명이 "title" 값을 찾음
    for cartoon in cartoons :
        f.write(cartoon.get_text())
        f.write("\n")


