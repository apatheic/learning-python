# In this program we find and delete the default sheet, then create a new sheet named "Calculations"

from openpyxl import Workbook

wb = Workbook()
wb.create_sheet('Calculations')
default_sheet = 'Sheet'
if default_sheet in wb.sheetnames:
    sheet_to_remove = wb[default_sheet]
    wb.remove(sheet_to_remove)

wb.save('new_wb.xlsx')
