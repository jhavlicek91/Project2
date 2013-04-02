from Tkinter import *
import urllib
import xlwt
import xlrd
import os
import re

#Make window
master = Tk()
master.title("Project2")

#Add file heading
head = Label(master, text="File:")
head.grid(row=0,column=0,sticky= W)

#Add file text box
fileEnter = Entry(master, width = 35)
fileEnter.grid(row=1,column=0)

ftype = IntVar() 
#Add HTML Radio Button
HTMLbutton = Radiobutton(master, text="HTML", fg="black", variable = ftype, value =1)
HTMLbutton.grid(row=2,column=0,sticky=E)

#Add PDF Radio Button
PDFbutton = Radiobutton(master, text="PDF ", fg="black", variable= ftype, value =2 )
PDFbutton.grid(row=2, column=2)

#Add text Radio button
TXTbutton = Radiobutton(master, text="TXT", fg="black", variable= ftype, value= 3)
TXTbutton.grid(row=2,column=3)

#Add keyword heading 
head1 = Label(master, text="Keywords:")
head1.grid(row=4,column=0,sticky=W)

#Add keyword textbox
keywordEnter = Entry(master, width = 35)
keywordEnter.grid(row=5,column=0)

#Add excel heading
head2=Label(master, text="Output Excel File:")
head2.grid(row=6,column=0,sticky=W)

#add excel text box
outputEnter = Entry(master, width = 35)
outputEnter.grid(row=7,column=0)

def ReadTextFile(FileName, keywords):
    #Get the text file to search through and open it
    f = file(FileName, 'r')

    #account for capital letters as well
    caps = keywords.title()
    keywords = keywords + " " + caps

    #Get the keyword(s) you want to search for
    words = keywords.split()

    #Create dictionary that has each keyword and the 
    #number of times it appeared in the file
    new_dict = {}

    for w in words:
       new_dict[w] = 0
    
    for line in f:
        for w in words:
            instances = re.findall(w, line)
            amount = len(instances)
            new_amount = amount + new_dict[w]
            new_dict[w] = new_amount
            
    for key in new_dict.keys():
        print "%r: %r" % (key, new_dict[key])

    halfway = len(new_dict) / 2;

    for i in range (0, halfway):
       key = new_dict.keys()[i]
       key2 = new_dict.keys()[i + halfway]
       new_dict[key] += new_dict[ key2 ] 
    
    #Close the file you read
    f.close()

    return new_dict;
       

#Function for when go is clicked
def Go():
    searchfile = fileEnter.get()
    keywords =  keywordEnter.get()
    excelfile = outputEnter.get()

    #if html is selected
    #if ftype.get() == 1:
        #html function
        #ReadTextFile()

    #if pdf is selected
    if ftype.get() == 2:
       print "PDF"
       os.system("python pdf2txt.py -o temp.txt " + searchfile + ".pdf") 
       results = ReadTextFile("temp.txt", keywords)
       #Delete the temporary file
       os.remove("temp.txt");

    #if txt file is selected
    if ftype.get() == 3:
       results = ReadTextFile(searchfile, keywords)

    #Write output to the excel file
    MakeExcel(excelfile, searchfile, results);

def MakeExcel(excelfile, searchfile, results):
    filename = excelfile + '.xls'
    if len(searchfile) > 20:
	    article = searchfile[:18] + '...'
    else:
	    article = searchfile

    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet(article)
    workbook.save(filename)

    hold = FindStart(filename, article)
    worksheet.write(6, 10, hold)
    
    index = 2

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

    cell = sheet.Cells(1, 1)    

    halfway = len(results) / 2

    for w in range(0, halfway):
         key = results.keys()[w]
         worksheet.write(index, 1, key)
         worksheet.write(index, 2, results[key])
         index += 1

    workbook.save(filename)

def FindStart(filename, article):
    wkbk = xlrd.open_workbook(filename)
    wkst = wkbk.sheet_by_name(article)
    index = 2

    check = wkst.cell_value(0, 0)
    
    return check

#Add go button
GObutton = Button(master,text="Go!", fg="black", command= Go)
GObutton.grid(row=7,column=6)


mainloop()
