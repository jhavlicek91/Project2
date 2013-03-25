import xlwt

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label = 'I')
worksheet.write(1, 0, label = 'MADE')
worksheet.write(2, 0, label = 'A')
worksheet.write(3, 0, label = 'THING')
workbook.save('Test_Workbook.xls')
