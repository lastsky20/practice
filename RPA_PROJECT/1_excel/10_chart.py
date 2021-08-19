from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string  ## 좌표 정보를 가져오기 위한 모듈

wb = load_workbook("sample2.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, Reference

