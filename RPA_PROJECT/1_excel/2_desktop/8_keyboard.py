import pyautogui
import pyperclip       # 클립보드 관련된 커맨드



w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()

pyautogui.write("1234")
pyautogui.write("\n")   # 줄바꿈
# pyautogui.write("54321", interval=0.5)    # 인터벌(속도) 조절
pyautogui.write("54321")

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.5)  # 방향키 조작
pyautogui.write("대한민국 한글")    # 한글 직접입력 안됨
# 특수문자
pyautogui.keyDown("shift")  # 키 누르고 있기
pyautogui.press("4")    # 키 입력
pyautogui.keyUp("shift") # 키 떼기

# 키 조랍(전체 선택)
pyautogui.keyDown("Ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("Ctrl")

# ->  간편한 조합키
pyautogui.hotkey("Ctrl", "alt", "shift", "a")


# 한글 입력
pyperclip.copy("1q2w3e4r")
pyautogui.hotkey("Ctrl", "v")
pyperclip.copy("대한민국 한글")
pyautogui.hotkey("Ctrl", "v")


# 자동화 종료
# win : Ctrl + Alt + Del
# mac : cmd + shift + option + q