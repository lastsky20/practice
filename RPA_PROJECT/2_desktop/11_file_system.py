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
# for root, dirs, files in os.walk(".") :       # "." : 현재폴더 / 
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

pattern = "*.png"    # 패턴 정의, wild card mask
result = []

for root, dirs, files in os.walk(os.getcwd()) :     #"os.walk" : 부모폴더, 자식폴더, 파일
    for name in files :
        if fnmatch.fnmatch(name, pattern) :     # 두개의 인수를 비교
            result.append(os.path.join(root, name))     # 전체경로 + 파일명

print(result)
for r in result :
    print(r)

# 주어진 경로의 파일/폴더 비교 -> 리턴 값 TRUE 또는 FALSE / 경로가 없으면 FALSE
print(os.path.isdir("rpa_basic"))      # 해당 경로가 폴더인가
print(os.path.isfile("rpa_basic"))     # 해당 경로가 파일인가


# 주어진 경로가 존재유무
if os.path.exists("rpa_basic") : # 파일 또는 폴더의 존재유무
    print("파일 또는 폴더가 존재")
else :
    print("파일 또는 폴더가 존재하지 않음")

# 파일 만들기
open("new_text.txt").close()    # 빈 파일 생성

# 파일명 변경
os.rename("new_text.txt", "new_file_text.txt")      # 파일명 변경

# 파일 삭제
os.remove("new_file_text.txt")

# 폴더 생성
os.mkdir("new_fd")      # 폴더 생성, 현재 경로
os.mkdir("c:/")     # 절대 경로

os.makedirs("new_folders/a/b/c")       # 하위 폴더를 가지는 경로 생성

# 폴더명 변경
os.rename("new_folder", "new_folders")

# 폴더 삭제
os.rmdir("new_folders")     # 폴더 안에 비어 있을 때

import shutil   # 쉘 유틸
# 모든 하위 폴더 삭제
shutil.rmtree("new_folders")        # ※주의※ 폴더 안에 파일, 폴더 강제 삭제(모든 파일 삭제)

# 파일 복사
shutil.copy("run.png", "test_folder")   # 원본대상 / 대상 폴더

shutil.copy("run.png", "test_folder/copy_run.png")  # 원본대상 / 대상 폴더 및 파일명

shutil.copyfile("run.png", "test_folder/copy_run2.png")     # 원본대상 / 대상 파일 경로(only)

shutil.copy2("run.png", "test_folder/copy2.png")    # 원본대상 / 대상 폴더(파일) 경로

## copy, copyfile : 메타정보 복사 x, 복사시 파일의 메타정보가 새로 생성(날짜, 시간 등)
## copy2 : 메타정보 복사 o, 복사시 기존 파일의 메타정보가 그대로 복사(날짜, 시간 등)

# 폴더 복사
shutil.copytree("test_folder", "test_folder2")     # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동
shutil.move("test_folder", "test_folder3")  # 원본 폴더 경로, 대상(부모) 폴더 경로
shutil.move("test_folder", "test_folder5")  # 대상 폴더가 없을시 rename 생성




