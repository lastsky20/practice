import pyautogui
import time

# time.sleep(3)
pyautogui.sleep(3) # 3초 대기
p = pyautogui.position()

pyautogui.sleep(3)
print(p)

## 마우스 클릭
pyautogui.click(p[0], p[1], duration=1) # 1초에 걸쳐서 클릭, mouseDown + mouseUp
# pyautogui.mouseDown() # 마우스 누르고 있는 상태
# pyautogui.moseUp() # 마우스를 뗀 상태
# pyautogui.doubleClick() # 마우스 더블 클릭
# pyautogui.click(clicks=500, duration=1) # 1초에 걸쳐서 500번 클릭

# pyautogui.rightClick() # 마우스 우 클릭
# pyautogui.middleClick() # 마우스 휠 동작
# pyautogui.drag(100, 100) # 현재 위치 기준으로 마우스 드래그(x, y)
# pyautogui.dragTo(100, 100) # 절대 좌표 기준으로 드래그

pyautogui.scroll(300) # 300 방향으로 스크롤
pyautogui.scroll(-300) # 아래 300 방향으로 스크롤