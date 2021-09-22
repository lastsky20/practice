import pyautogui

## 스크린샷
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

## RGB 값 
rgb = pyautogui.pixel(23, 18) # 픽셀의 rgb 정보를 가져옴
print(rgb)

print(pyautogui.pixelMatchesColor(23, 18, (60, 60, 60)))  # x좌표, y좌표, RGB 값 으로 픽셀의 값이 맞는지 비교

