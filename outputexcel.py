import os.path
import xlwt
import xlrd
from xlutils.copy import copy
import os

index = 0
totals = dict()

def OpenExcel(excelfile, searchfile, wsheet, **results):

    global totals
    for key in results:
       totals[key] = 0
       
    articleName = searchfile.split('/')
    article = articleName[-1]
    #Determine file to write to
    if excelfile.endswith('.xls') :
       filename = excelfile
    else:
       filename = excelfile + '.xls'

    if(os.path.isfile(filename)):
       tempbook = xlrd.open_workbook(filename, formatting_info = True)

       workbook = copy(tempbook)
       worksheet = workbook.add_sheet(wsheet)

    else:
       workbook = xlwt.Workbook(encoding = 'ascii')
       worksheet = workbook.add_sheet(wsheet)

    return worksheet, workbook


def CloseExcel(workbook, excelfile):

   if excelfile.endswith('.xls') :
      filename = excelfile
   else:
      filename = excelfile + '.xls'

   workbook.save(filename)

def WriteTotal(worksheet):

   global totals
   global index

   column = 1

   #Write the total results for each word
   for key in totals:
      worksheet.write(index, column, "Final Total")
      worksheet.write(index, column + 1, totals[key])
      column += 3
   
   

#Function for writing results to an excel file
def MakeExcel(worksheet, excelfile, searchfile, keyword, **results):

    global index
    global totals
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
       #keep track of overall totals
       totals[k] = totals[k] +  summ
       column += 3
       index = tempindex
  
    index = maxindex + 2




