from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
sheet = wb.active

sheet['A1'] = "Seria 1"
for i in range (1,11):
    sheet.append([i])
chart = BarChart()
chart.title = "First Data Series."
data = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=11)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "C2")

wb.save('sampleChart1.xlsx')
