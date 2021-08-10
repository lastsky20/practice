import requests

res = requests.get("http://www.naver.com")
res.raise_for_status()      # 예외처리
res2 = requests.get("http://www.tistory.com")
res2.raise_for_status()     # 예외처리


print("응답코드 :", res.status_code)
print("응답코드 :", res2.status_code)

# if res.status_code == requests.codes.ok:
#     print("Ok")
#     #print("Error Code : {0}".format(res.status_code))
# else :
#     print("Error Code : {0}".format(res.status_code))

res.raise_for_status()  # 예외처리

    