import xlwt

filename = excelFile + '.xls'
if len(searchFile) > 20:
	article = searchFile[:18] + '...'
else:
	article = searchFile

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet(article)
font = xlwt.Font()
font.bold = True
font.height = 0x00FF
font.underline = True
style = xlwt.XFStyle()
style.font = font
cell0 = 'I'
worksheet.write_merge(0, 0, 0, 10, searchFile, style)
worksheet.col(0).width = 3333
worksheet.row(0).height = 400
worksheet.write(1, 1, 'MADE')
worksheet.write(2, 1, 'A')
worksheet.write(3, 1, 'THING')
workbook.save(filename)
