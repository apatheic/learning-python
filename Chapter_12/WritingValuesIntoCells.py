from openpyxl import Workbook

wb = Workbook()
sheet = wb['Sheet']
sheet['A1'] = "Hello, Excel!"
print(sheet['A1'].value)

wb.save('HelloExcel.py')
