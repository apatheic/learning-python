# In this program we find and delete the default sheet, then create a new sheet named "Calculations"

from openpyxl import Workbook

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

wb.save('new_wb.xlsx')
