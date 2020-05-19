import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
wb.sheetnames

sheet = wb['Sheet3']
sheet
type(sheet)

sheet.title
anotherSheet = wb.active
anotherSheet
