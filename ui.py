from Tkinter import *
import urllib
import xlwt

master = Tk()

master.title("Project2")

def text():
    type = "HTML"

def text2():
    type = "PDF"

def usertxt():
    type = "TXT"

def Go():
    searchfile = fileEnter.get()
    keywords =  keywordEnter.get()
    excelfile = outputEnter.get()

    #if file is html

    #if file is pdf

    #if file is txt


    #output results

type = StringVar()

#Add file heading
head = Label(master, text="File:")
head.grid(row=0,column=0,sticky= W)

#Add file text box
fileEnter = Entry(master)
fileEnter.grid(row=1,column=0)

#Add HTML Radio Button
HTMLbutton = Radiobutton(master, text="HTML", fg="black", command=text,variable=type, value =1)
HTMLbutton.grid(row=2,column=0,sticky=E)

#Add PDF Radio Button
PDFbutton = Radiobutton(master, text="PDF ", fg="black", command=text2, variable= type, value =2 )
PDFbutton.grid(row=2, column=2)

#Add text Radio button
TXTbutton = Radiobutton(master, text="TXT", fg="black", command= usertxt,variable=type, value= 3)
TXTbutton.grid(row=2,column=3)

#Add keyword heading 
head1 = Label(master, text="Keywords:")
head1.grid(row=4,column=0,sticky=W)

#Add keyword textbox
keywordEnter = Entry(master)
keywordEnter.grid(row=5,column=0)

#Add excel heading
head2=Label(master, text="Output Excel File:")
head2.grid(row=6,column=0,sticky=W)

#add excel text box
outputEnter = Entry(master)
outputEnter.grid(row=7,column=0)

#Add go button
GObutton = Button(master,text="Go!", fg="black", command= Go)
GObutton.grid(row=7,column=6)

mainloop()
