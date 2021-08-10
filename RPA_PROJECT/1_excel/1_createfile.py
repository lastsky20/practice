from openpyxl import Workbook   # 엑셀 관련 라이브러리

wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 활성화된 시트 선택
ws.title = "TestSheet1"  # 타이틀 변경
wb.save("text.xlsx")  # 파일 저장
wb.close()  # 파일 닫기

