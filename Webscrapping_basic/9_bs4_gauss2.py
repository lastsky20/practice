import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

print("응답코드", res.status_code)

soup = BeautifulSoup(res.text, "lxml")

# 평점 정보를 가져옴

total_rates = 0
cartoons = soup.find_all("div", attrs = {"class" : "rating_type"})

for cartoon in cartoons :
    rate = cartoon.find("strong").get_text()    # strong 엘리먼트의 정보를 가져옴
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))