from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "New Shit"
sheet['C3'] = 'Hello world!'
for i in range(10):
    sheet["A%d" % (i + 1)].value = i + 1

wb.save('保存一个新的excel.xlsx')
