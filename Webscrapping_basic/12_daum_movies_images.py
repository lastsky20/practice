import requests as res2
import re
from bs4 import BeautifulSoup
from requests.api import request


for year in range(2015, 2020) :
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

    res = res2.get(url, headers = headers)
    res.raise_for_status()

    print("응답코드", res.status_code)

    soup = BeautifulSoup(res.text, "lxml")

    # 테스트 코드
    # images = soup.find("img", attrs = {"class" : "thumb_img"})
    # print(images["src"])

    # img 태그로 시작하는 attrs(속성) 의 class 가 thumb_img 인 모든 엘리먼트를 찾아서 가져옴
    images = soup.find_all("img", attrs = {"class" : "thumb_img"})

    # with 문 안에 with 문을 작성하면 오류 발생(??????)
    # with open("movieList.txt", "w", encoding = "utf8") as f :
    for idx, image in enumerate(images) :
        image_url = image["src"]
        if image_url.startswith("//") :
            image_url = "https:" + image_url

        # f.write(image_url)
        # f.write("\n")

        image_res = res2.get(image_url, headers = headers)
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, idx+1), "wb") as f :    # wb : 바이너리 형태의 파일을 쓰기
                # 해당 링크의 사진을 파일로 저장 함
                f.write(image_res.content)

        if idx >= 29 :
            break



