import requests

res = requests.get("http://www.naver.com")
res.raise_for_status()      # 예외처리
res2 = requests.get("http://www.tistory.com")
res2.raise_for_status()     # 예외처리
res3 = requests.get("http://www.google.co.kr")
res3.raise_for_status()


print("응답코드 :", res.status_code)
print("응답코드 :", res2.status_code)
print("응답코드 :", res3.status_code)

# if res.status_code == requests.codes.ok:
#     print("Ok")
#     #print("Error Code : {0}".format(res.status_code))
# else :
#     print("Error Code : {0}".format(res.status_code))

res.raise_for_status()  # 예외처리

with open("myGoogle.html", "w", encoding = "utf8") as f:
    f.write(res3.text)

    