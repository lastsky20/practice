import pyautogui


# fw = pyautogui.getActiveWindow()    # 현재 활성화된 윈도우 정보
# print(fw.title) # 제목
# print(fw.size)  # 사이즈
# print(fw.left, fw.top, fw.right, fw.bottom) # 좌표 정보

# for i in pyautogui.getAllWindows() :    # 모든 윈도우 정보 가져오기
#     print(i)


# for w in pyautogui.getWindowsWithTitle("제목 없음") :
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False :    
    w.activate()    # 윈도우 활성화(앞으로 가져오기
    
pyautogui.sleep(1)

if w.isMaximized == False : # 현재 최대화가 되지 않았다면
    w.maximize()

pyautogui.sleep(1)

if w.isMinimized == False : # 현재 최소화가 되지 않았다면
    w.minimize()

pyautogui.sleep(1)

w.restore() # 윈도우 원복

# w.close()   # 윈도우 닫기, 변경 데이터가 있으면 알림창

