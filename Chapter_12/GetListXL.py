import openpyxl

wb = openpyxl.load_workbook('example3.xlsx')
print(wb.sheetnames)
#['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb['Sheet3']
print(sheet)
#<Worksheet "Sheet3">

print(type(sheet))
#<class 'openpyxl.worksheet.worksheet.Worksheet'>

print(sheet.title)
#'Sheet 3'
anotherSheet = wb.active
print(anotherSheet)
#<Worksheet "Sheet1">
