from openpyxl.styles import Font
from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook("sample2.xlsx")
ws = wb.active

a1 = ws["A1"]
b1 = ws["B1"]
c1 = ws["C1"]


# a열의 너비를 5로 설정
ws.column_dimensions["A"].width = 5

# 1번째 줄의 높이를 50으로 설정
ws.row_dimensions[1].height = 50

# 빨간색, 이탤릭
a1.font = Font(color = "FF0000", italic = True, bold = True)


wb.save("sample2_text.xlsx")
