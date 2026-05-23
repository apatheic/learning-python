# In this program we find and delete the default sheet, then create a new sheet named "Calculations"

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

#create workbook
wb = Workbook()
wb.create_sheet('Calculations')

#remove default worksheet
default_sheet = 'Sheet'
if default_sheet in wb.sheetnames:
    sheet_to_remove = wb[default_sheet]
    wb.remove(sheet_to_remove)

# set some values to cells
calcs_sheet = wb['Calculations']
calcs_sheet['A1'].value = 1
calcs_sheet['A2'].value = 2
calcs_sheet.cell(row=3, column=1, value=3)
calcs_sheet['A4'].value = '=A1+A2+A3'

# read values from cells
print(calcs_sheet['A1'].value)
print(calcs_sheet.cell(row=1, column=1).value)

#set styles
calcs_sheet['A4'].font = Font(bold=True, color='cf352e')
calcs_sheet['A4'].fill = PatternFill(patternType='solid', start_color='f3ce45')
calcs_sheet['A4'].alignment = Alignment(horizontal='center', vertical='center')

wb.save('new_wb.xlsx')
