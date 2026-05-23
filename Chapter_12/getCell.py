from openpyxl import load_workbook

wb = load_workbook('example3.xlsx')
sheet = wb['Sheet1']

sheet['A1']
#<Cell Sheet1.A1>

sheet['A1'].value
#datetime.datetime(2015, 4, 5, 13, 34 ,2)

c = sheet['B1']
c.value
#'Apples'

print(f'Row {str(c.row)} Column {c.column}: {c.value}')
print(f'Cell {c.coordinate}: {c.value}')
sheet['C1'].value
