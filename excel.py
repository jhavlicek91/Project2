import xlwt

excelfile = 'testfile'
searchfile = 'Article1'

filename = excelfile + '.xls'
if len(searchfile) > 20:
	article = searchfile[:18] + '...'
else:
	article = searchfile

new_dict = {}

new_dict['hello'] = 3
new_dict['goodbye'] = 7

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet(article)

font = xlwt.Font()
font.bold = True
font.height = 0x010D
font.underline = True
style = xlwt.XFStyle()
style.font = font

worksheet.col(0).width = 3333
worksheet.row(0).height = 400

font2 = xlwt.Font()
font2.bold = True
font2.underline = True
style2 = xlwt.XFStyle()
style2.font = font2

worksheet.write_merge(0, 0, 0, 10, searchfile, style)
worksheet.write(1, 1, 'Words', style2)
worksheet.write(1, 2, 'Count', style2)

index = 2

for w in new_dict:
     worksheet.write(index, 1, w)
     worksheet.write(index, 2, new_dict[w])
     index += 1

workbook.save(filename)
