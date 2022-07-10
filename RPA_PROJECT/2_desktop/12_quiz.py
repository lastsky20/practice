# 1. 그림판 실행(단축키 : win + r, 입력값 : mspaint) -> 윈도우 최대화
# 2. 텍스트 기능을 이용, 빈 영역에 "참 잘했어요" 입력
# 3. 5초 대기 후 그림판 종료 -> 저장하지 않음을 자동으로 선택

import pyautogui
import time
import sys
import pyperclip


pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.hotkey("enter")

pyautogui.sleep(1)
aw = pyautogui.getActiveWindow()

if aw.isMaximized == False : 
    aw.maximize()

# for i in pyautogui.locateAllOnScreen("mspaint_text.png", confidence = 0.999) : # confidence 기본값 : 0.999(99%)
    # print(i)

i = pyautogui.locateOnScreen("mspaint_text.png", confidence = 0.8)
if i :
    print(i)
    pyautogui.moveTo(i)
else :
    sys.exit()

pyautogui.sleep(1)
pyautogui.click(i)

# pyautogui.moveTo(i[1] + 200)
# pyautogui.move(i[0], i[1] + 500, duration = 3)
pyautogui.click(i[0], i[1] + 500, duration = 3)
pyautogui.click()
pyautogui.sleep(1)
pyperclip.copy("Good job")
pyautogui.hotkey("Ctrl", "v")

pyautogui.sleep(5)
aw.close()
pyautogui.sleep(0.5)
# pyautogui.hotkey("n")
pyautogui.press("n")
