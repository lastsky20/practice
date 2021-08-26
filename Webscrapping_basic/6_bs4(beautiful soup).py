import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

print("응답코드", res.status_code)

soup = BeautifulSoup(res.text, "lxml")      # pip install lxml

# print(soup.title)
# print(soup.title.get_text())    # 문자만 출력
# print(soup.a)       # 첫번째 "a" 의 엘리먼트 출력
# print(soup.a.attrs)     # "a" 엘리먼트의 딕셔너리 형태로 속성을 출력
# print(soup.a["href"])       # "a" 엘리먼트의 "href" 속성값 출력
# print(soup.find("a", attrs = {"class":"Nbtn_upload"}))        # 속성값 "class : Nbtn_upload" 정보 출력 "a" 엘리먼트를 찾아서 출력 
# print(soup.find(attrs = {"class" : "Nbtn_upload"} ))        # "class" "Nbtn_upload" 속성값을 찾아서 출력
# print(sout.prettify())    # html 문서를 정리해서 보여줌.

rank = soup.find("li", attrs={"class" : "rank01"})      # "li" 로 시작하는 "class" 가 "rank01" 인 줄을 탐색
print(rank.a.get_text())

# rank = soup.find_all("li", attrs = {"class" : "rank01"})      # find_all : 모든 엘리먼트를 찾음

# next1 = rank.next_sibling.next_sibling      # 다음 줄의 정보를 가져옴 / 형제 
# print(next1.a.get_text())                   # 개행문자의 간섭으로 "next_sibling" 개체를 두번 호출

# next2 = next1.next_sibling.next_sibling
# print(next2.a.get_text())

# next1 = next2.previous_sibling.previous_sibling     # 이전 줄의 정보를 가져옴
# print(next1.a.get_text())

# # print(next1.parent)     # next1 의 부모 패스로 이동
# next2 = next1.find_next_sibling("li")       # "li" 태그를 가진 다음줄을 검색
# print(next2.a.get_text())

# next3 = next2.find_next_sibling("li")
# print(next3.a.get_text())

# next2 = next3.find_previous_sibling("li")
# print(next2.a.get_text())

# all_next = rank.find_next_siblings("li")    # 다음 모든 형제 노드의 태그를 가져옴
# print(all_next)


webtoon = soup.find("a", text = "노답소녀-40화")     # "노답소녀-40화" 텍스트를 가진 "a" 태그를 찾음
print(webtoon)














# with open("NaverWebtoon.html", "w", encoding = "utf8") as f :
#     f.write(res.text)

