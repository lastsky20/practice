import pyautogui

## 마우스 이동(절대좌표)
# pyautogui.moveTo(100, 100)
# 화면의 좌측 위 모서리 좌표 : 0, 0
# 좌표정보는 모니터 크기나 해상도에 따라 다름

pyautogui.moveTo(100, 200, duration=1)
# duration : 마우스 이동 속도
# 1초에 걸쳐 마우스 커서 이동

pyautogui.moveTo(100, 100, duration = 0.25)
pyautogui.moveTo(200, 200, duration = 0.25)
pyautogui.moveTo(300, 300, duration = 0.25)


## 마우스 이동(상대좌표)
pyautogui.move(300, 300, duration = 1)
pyautogui.move(-100, -100, duration = 3)

# 마우스 좌표 정보 
print(pyautogui.position())
p = pyautogui.position()
print(p[0], p[1]) # p[0] : x, p[1] : y


