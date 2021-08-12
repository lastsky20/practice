import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}


for i in range(1, 6) : 
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers = headers)
    res.raise_for_status()

    print("응답코드", res.status_code)

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})  #정규식 : "^" search-product 로 시작하는 모든 문자열
    # print(items[0].find("div", attrs = {"class" : "name"}).get_text())


    with open("CouGoodsList{0}.txt".format(i), "w", encoding = "utf8") as f :

        for item in items :

            # 광고 제품은 제외
            ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
            if ad_badge :
                continue

            name = item.find("div", attrs = {"class" : "name"}).get_text()
            
            # 애플 제품은 제외
            if "Apple" in name :
                continue
            
            price = item.find("strong", attrs = {"class" : "price-value"})
            if price :
                price = price.get_text()
            else :
                price = "가격 정보 없음"
            
            rate = item.find("em", attrs = {"class" : "rating"})
            if rate :
                rate = rate.get_text()
            else :
                continue

            count = item.find("span", attrs = {"class" : "rating-total-count"})
            if count :      # (00) 형식
                count = count.get_text()
                count = count[1:-1]  # 1번째 인덱스 부터 제일 뒤에 -1 인덱스 까지
            else :
                continue
            
            link = item.find("a", attrs = {"class" : "search-product-link"})["href"]  # 링크 정보를 가져옴
            
            


            # print(name, price, rate, count)
            if float(rate) >= 4.5 and int(count) >= 50 :  # 평점 4.5, 리뷰 50 이상만 출력 
                f.write(name)
                f.write(" ")
                f.write(price)
                f.write(" ")
                f.write(rate)
                f.write(" ")
                f.write(count)
                f.write("\n")
                f.write("https://www.coupang.com" + link)
                f.write("\n")
                

                # print(f"제품명 : {name}")
                # print(f"가격 : {price}")
                # print(f"평점 : {rate}")
                # print(f"평점 수 : {count}")
                # print("링크 {0}:".format("https://www.coupang.com" + link))
                # print("-"*100)  # 줄 100개 긋기