from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
sheet = wb.active 
italic24Font = Font(size=24, italic=True)

sheet['A1'] = 'Hello, World!'
sheet['A1'].font = italic24Font  

wb.save('styled.xlsx')
