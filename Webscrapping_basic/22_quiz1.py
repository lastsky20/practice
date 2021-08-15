import csv
import requests
import re
from bs4 import BeautifulSoup


url = "https://realty.daum.net/home/apt/danjis/38487"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}



res = requests.get(url, headers = headers)
res.raise_for_status()
print("응답코드", res.status_code)

soup = BeautifulSoup(res.text, "lxml")

# with open("text.txt", "w", encoding = "utf8") as f :
#     f.write(str(soup))

with open("daum.txt", "w", encoding = "utf8") as f :
    f.write(soup.prettify())

# items = soup.find_all("div", attrs = {"class" : "rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-o11vmf rn-ebii48 rn-vw2c0b rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})
# print(len(items))

# for item in items :
#     print(item.get_text())

# rn-1awozwy rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-16y2uox rn-1wbh5a2 rn-1mlwlqe rn-18u37iz rn-1777fci rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-bcqeeo rn-lgpkq rn-qi0n3 rn-c9eks5 rn-k5i03q rn-bnwqim rn-1lgpqti
# rn-1awozwy rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-16y2uox rn-1wbh5a2 rn-1mlwlqe rn-18u37iz rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-bcqeeo rn-lgpkq rn-qi0n3 rn-c9eks5 rn-k5i03q rn-bnwqim rn-1lgpqti

