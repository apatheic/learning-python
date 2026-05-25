from openpyxl import Workbook

wb = Workbook()
print(wb.active)
sheet = wb.active
print(sheet.title)
sheet.title = 'Spam Bacon Eggs Sheet'
print(wb.sheetnames)

wb.save('filemacker.xlsx')
