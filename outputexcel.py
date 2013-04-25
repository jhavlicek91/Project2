import os.path
from Tkinter import *
import tkFileDialog
import urllib
import xlwt
import xlrd
from xlutils.copy import copy
import os
import re
from bs4 import BeautifulSoup
import nltk 

#Function for writing results to an excel file
def MakeExcel(excelfile, searchfile, keyword, **results):

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

    print "%r  %r" % (searchfile, article)

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
    worksheet.write_merge(0, 0, 0, 10, article, style)
    worksheet.write(1, 1, 'Words', style2)
    worksheet.write(1, 2, 'Count', style2)

    #Write cells corresponding to the main words
    worksheet.write(2, 0, "Main Term")
    index = 2
    column = 1
    maxRow = index;
    for k in results:
        worksheet.write(index, column, k.capitalize())
        worksheet.write(index, column + 1, results[k][k.capitalize()])
        column += 3 

    #Write the rest of the cells
    column = 1

    for k in results: 
       index = 3 
       summ = 0
       for w in results[k]:
          if w != k.capitalize():
             worksheet.write(index, column, w)
             worksheet.write(index, column + 1, results[k][w])
             index += 1
          summ += results[k][w]

       colTotal = "SUM(C3:C" + str(index) + ")"
          
       #Write the sum of the keywords
       worksheet.write(index + 1, column, "Total")
       worksheet.write(index + 1, column + 1, summ)
       column += 3

       #keep track of the farthest row down used
       maxRow = max(maxRow, index + 1)

    worksheet.write(0, 11, maxRow)

    workbook.save(filename)
