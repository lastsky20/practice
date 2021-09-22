from PIL.ImageOps import grayscale
import pyautogui
import time
import sys


## 화면 해상도에 따라 인식 실패 확률 높음 

## 이미지 인식 및 찾기
## 해당 이미지의 첫번째 1개 이미지만 찾음
# menu = pyautogui.locateOnScreen("test_go.png", confidence = 0.7)
# print(menu)

# pyautogui.moveTo(menu[0], menu[1])

# pyautogui.click(menu) # 반환값을 인수로 사용시 해당 이미지의 중간점을 클릭
# pyautogui.sleep(1)
# pyautogui.click(menu[0]+50, menu[1]+50, duration=3.5)


## 화면의 모든 이미지를 찾음
#
# for i in pyautogui.locateAllOnScreen("u_icon.png") :
#     print(i)
#     pyautogui.moveTo(i)

# u_icon = pyautogui.locateAllOnScreen("u_icon.png")
# for i in u_icon :
#     print(i)

## 속도 개선
# 1. 그레이 스케일(Gray Scale) : 30% 개선 / 정확도 떨어짐
# for i in pyautogui.locateAllOnScreen("u_icon.png", grayscale = True) : # grayscale 옵션을 트루로 지정, 
#     print(i)
#     pyautogui.moveTo(i)

# 2. 범위 지정
# for i in pyautogui.locateAllOnScreen("u_icon.png", region = (x, y, width, height)) : # 범위 지정
#     print(i)
#     pyautogui.moveTo(i)

# 3. 정확도 조정
# install : pip install opencv-python
# for i in pyautogui.locateAllOnScreen("test1.png", confidence = 0.9) : # confidence 기본값 : 0.999(99%)
#     print(i)
#     pyautogui.moveTo(i)

# j = pyautogui.locateOnScreen("head.png", confidence = 0.9)
# pyautogui.moveTo(j)



## 자동화 대상이 바로 로딩되지 않은 경우
# while 문을 활용하여 루프
# menu_icon = pyautogui.locateOnScreen("file_test.png")
# while menu_icon is None :
#     menu_icon = pyautogui.locateOnScreen("file_test.png")
#     print("Searching..")
# pyautogui.click(menu_icon)


# 타임아웃 설정
timeout = 10
start_time = time.time()
menu_icon = None
print("시작 시간 :", start_time)
while menu_icon is None :
    menu_icon = pyautogui.locateOnScreen("file_test.png")
    end_time = time.time()
    print(end_time)
    if end_time - start_time > timeout : 
        print("timeout")
        sys.exit()
    print("Searching..")
pyautogui.click(menu_icon)








