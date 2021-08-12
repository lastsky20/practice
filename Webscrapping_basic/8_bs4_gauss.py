import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

print("응답코드", res.status_code)

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs = {"class" : "title"})


# link = cartoons[0].a["href"]        # [] 를 사용해서 속성값을 가져올 수 있음
# print(link)


for cartoon in cartoons :
    print(cartoon.a.get_text())

with open("webtoonlist.txt", "w", encoding = "utf8") as f :
    for cartoon in cartoons :
        f.write(cartoon.a.get_text())
        f.write("\n")
        f.write(cartoon.a["href"])
        f.write("\n")
        f.write("\n")

