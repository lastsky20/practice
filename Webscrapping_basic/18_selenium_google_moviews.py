import requests
from bs4 import BeautifulSoup

## url 
## 구글의 동적 웹페이지 
url = "https://play.google.com/store/movies/top"

## USER AGENT
## 언어설정 : ko
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Accept-Language" : "ko-KR,ko"}

## 1. request(url, headers)
res = requests.get(url, headers = headers)

## 2. 예외처리, 오류검사
res.raise_for_status()

## 3. soup 객체 생성 -> res.text 파서 lxml
soup = BeautifulSoup(res.text, "lxml")

## 4. div 태그의 class 가 "ImZGtf mpg5gc" 인 엘리먼트를 find_all
movies = soup.find_all("div", attrs = {"class" : "ImZGtf mpg5gc"})

## test
print(len(movies))

## 5. 가져온 정보의 타이틀(영화제목) 출력
for movie in movies :
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)


