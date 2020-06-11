import ezsheets

ss = ezsheets.createSpreadsheet('new sheet')
ss = ezsheets.Spreadsheet('1ZZMOIoJDUEJKcpY2ZWNDvOsDHs90oz9V2QgAo9JT0DI')
ezsheets.listSpreadsheets()

ss.title
ss.title = 'Class Data'
ss.spreadSheetId
ss.url
ss.sheetTitles
ss.sheets
ss[0]
ss['Students']
del ss[0] # delete Students sheet

ss.downloadAsExcel()
ss.downloadAsOsd()
ss.downloadAsCsv()
ss.downloadAsTsv()
ss.downloadAsPDF()
ss.downloadAsHTML()

ss.refresh() # refresh spreadsheet/workbook
ezsheets.convertAddress('A2') #(1, 2)
ezsheets.convertAddress(1,2) #'A2'
ezsheets.getColumnLetterOf(2)
ezsheets.getColumnNumberOf('B')

sheet.getRow(2) # get whole row data
sheet.getColumn('A') # get whole column data by letter or index
sheet.updateRow(3, ['Pumpkin', '11.50']) # update whole row
sheet.updateRows(Rows)
sheet.delete() # delete sheet
ss[0].clear() # Clear all the cells on the 'Sheet 1' sheet

sheet.rowCount
sheet.columnCount

ss.createSheet('Bacon', 0) # create new sheet at index 0
ss1[0].copyTo(ss2) # copy first sheet from ss1 to ss2
