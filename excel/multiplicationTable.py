import openpyxl
import sys

wb = openpyxl.Workbook()
sheet = wb.active

n = int(sys.argv[1]) + 1

for i in range(1, n):
    sheet['A' + str(i+1)] = i
    sheet[chr(ord('A')+i) + str(1)] = i

for i in range(1, n):
    sheet['B' + str(i+1)] = 

wb.save('multi-table.xlsx')
