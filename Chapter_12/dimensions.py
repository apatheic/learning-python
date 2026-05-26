from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet['A1'] = 'Tall Row'
sheet['B2'] = 'Fat Column'

#Make row height
sheet.row_dimensions[1].height = 70

#Make column width
sheet.column_dimensions['B'].width = 20

wb.save('dimensions.xlsx')
