import os.path
import xlwt
import xlrd
from xlutils.copy import copy
import os

index = 0

def OpenExcel(excelfile, searchfile):

    articleName = searchfile.split('/')
    article = articleName[-1]
    #Determine file to write to
    if excelfile.endswith('.xls') :
       filename = excelfile
    else:
       filename = excelfile + '.xls'
    
    if len(article) > 20:
       sheetName = article[-18:] + '...'
    else:
       sheetName = article

    if(os.path.isfile(filename)):
       tempbook = xlrd.open_workbook(filename, formatting_info = True)
       sheetList = tempbook.sheet_names()
       for sheet in sheetList:
          if sheet == sheetName:
             if sheetName.endswith('I'):
                sheetName = sheetName + "I"
	     else:
	        sheetName = sheetName + "_I"
             break
       workbook = copy(tempbook)
       worksheet = workbook.add_sheet(sheetName)

    else:
       workbook = xlwt.Workbook(encoding = 'ascii')
       worksheet = workbook.add_sheet(sheetName)

    return worksheet, workbook


def CloseExcel(workbook, excelfile):

   if excelfile.endswith('.xls') :
      filename = excelfile
   else:
      filename = excelfile + '.xls'

   workbook.save(filename)

#Function for writing results to an excel file
def MakeExcel(worksheet, excelfile, searchfile, keyword, **results):

    global index
    articleName = searchfile.split('/')
    article = articleName[-1]

    #Set font and style
    font = xlwt.Font()
    font.bold = True
    font.height = 0x010D
    font.underline = True
    style = xlwt.XFStyle()
    style.font = font

    worksheet.col(0).width = 3333
    worksheet.row(0).height = 400

    #Set font and style of file
    font2 = xlwt.Font()
    font2.bold = True
    font2.underline = True
    style2 = xlwt.XFStyle()
    style2.font = font2

    #Write the title of the file
    worksheet.write_merge(index, index, 0, 10, article, style)
    index += 1
    worksheet.write(index, 1, 'Words', style2)
    worksheet.write(index, 2, 'Count', style2)

    #Write cells corresponding to the main words
    worksheet.write(index, 0, "Main Term")
    index += 1
    column = 1
     
    for k in results:
       worksheet.write(index, column, k.capitalize())
       worksheet.write(index, column + 1, results[k][k])
       column += 3 

    #Write the rest of the cells
    column = 1
    tempindex = index
    maxindex = 0

    for k in results: 
       index += 1 
       summ = 0
       for w in results[k]:
          if w != k:
             worksheet.write(index, column, w.capitalize())
             worksheet.write(index, column + 1, results[k][w])
             index += 1
          summ += results[k][w]
          
       #Write the sum of the keywords
       worksheet.write(index + 1, column, "Total")
       worksheet.write(index + 1, column + 1, summ)
       maxindex = max(maxindex, index + 1)
       column += 3
       index = tempindex
       
    index = maxindex + 2




