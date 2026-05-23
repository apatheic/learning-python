from openpyxl import Workbook

wb = Workbook()
wb.save('new_wb.xlsx')
print(wb)
