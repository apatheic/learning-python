from openpyxl import load_workbook

wb = load_workbook('example3.xlsx')
sheet = wb['Sheet1']
print(sheet['A1': 'C3'])

for rowOfCellObject in sheet['A1': 'C3']:
    for cellObj in rowOfCellObject:
        print(cellObj.coordinate, cellObj.value)
    print('---END OF THE LINE---')
