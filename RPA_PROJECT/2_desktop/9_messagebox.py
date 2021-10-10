import pyautogui

# pyautogui.countdown(3)  # 카운트 다운

# pyautogui.alert("메시지", "경고") # ("본문", "타이틀")

pyautogui.confirm("계속 진행?", "확인") # ("본문", "타이틀") / 확인, 취소버튼
# 반환값 = Ok, Cancel

print(pyautogui.prompt("내용 입력", "입력"))   # 사용자 입력
# 반환값 = 사용자 입력값

result = pyautogui.password("비민번호 입력")    # 비밀번호 입력, 입력값은 마스크 처리
# 반환값 = 입력한 비밀번호 
print(result)

## pyautogui.readthedocs.io  // 데스크탑 자동화 official 사이트

