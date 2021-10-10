# 파일 및 폴더 관리

import os
# print(os.getcwd())  # current working directory

# os.chdir("Quiz")    
# print(os.getcwd())

# os.chdir("..")  # 부모 폴더로 이동
# print(os.getcwd())

# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())

# os.chdir("c:/") # 절대 경로로 이동
# print(os.getcwd())


# # 파일 (절대)경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\PC\Desktop\PythonWork\myfile.txt")) # "r"은 문자를 있는 그대로 출력

## 파일 정보 가져오기
import time
import datetime 

## 파일의 생성 날짜
# ctime = os.path.getctime("mynote.txt")
# print(ctime)  # 생성 날짜

# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y{0}%m{1}%d{2} %H{3}:%M{4}:%S{5}".format("년", "월", "일", "시", "분", "초")))

# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y년%m월%d일 %H시%M분%S초"))

# ## 파일 수정 날짜
# mtime = os.path.getmtime("mynote.txt")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y년%m월%d일 %H시%M분%S초"))

# ## 파일의 마지막 접근날짜
# atime = os.path.getatime("mynote.txt")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y년%m월%d일 %H시%M분%S초"))

# ## 파일의 크기
# fsize = os.path.getsize("mynote.txt")
# print(fsize)    # 바이트 단위로 파일 사이즈 가져오기

# ## 파일 목록 가져오기
# # 현재 폴더의 파일 목록 가져오기
# dlist = os.listdir()
# for d in dlist :
#     print(os.path.join(os.getcwd(), d))

# # 주어진 폴더의 파일 목록 가져오기
# print(os.listdir("WEBSCRAPPING_BASIC"))

# ## 주어진 폴더의 모든 하위 파일 목록 가져오기
# result = os.walk("RPA_PROJECT") # 주어진 폴더
# result2 = os.walk(".")  # 현재 폴더
# print(result)

# for root, dirs, files in result :   # 폴더, 하위폴더, 하위 파일 목록
#     # resultdir = os.path.join(os.getcwd(), root)
#     for file in files :
#         print(os.path.join(root, file))

# ## 지정 경로에서 파일 찾기
# fname = "5_screen.py"
# result3 = []
# for root, dirs, files in os.walk(".") :
#     if fname in files : 
#         result3.append(os.path.join(root, fname))
#         print(result3)

# ## 절대 경로에서 파일 찾기
# for root, dirs, files in os.walk(os.getcwd()) :
#     if fname in files : 
#         result3.append(os.path.join(root, fname))
#         print(result3)       



## 특정 패턴의 파일 찾기
import fnmatch

pattern = "*.png"    # 패턴 정의
result = []

for root, dirs, files in os.walk(os.getcwd()) :
    for name in files :
        if fnmatch.fnmatch(name, pattern) :
            result.append(os.path.join(root, name))

print(result)
for r in result :
    print(r)



