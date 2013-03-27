from Tkinter import *
import urllib
import xlwt
import os
import re

#Make window
master = Tk()
master.title("Project2")

#Add file heading
head = Label(master, text="File:")
head.grid(row=0,column=0,sticky= W)

#Add file text box
fileEnter = Entry(master)
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
keywordEnter = Entry(master, width = 50)
keywordEnter.grid(row=5,column=0)

#Add excel heading
head2=Label(master, text="Output Excel File:")
head2.grid(row=6,column=0,sticky=W)

#add excel text box
outputEnter = Entry(master)
outputEnter.grid(row=7,column=0)

def ReadTextFile(FileName, keywords):
    #Get the text file to search through and open it
    f = file(FileName, 'r')

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

    #Close the file you read
    f.close()

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
       ReadTextFile("temp.txt", keywords)

    #if txt file is selected
    if ftype.get() == 3:
       ReadTextFile(searchfile, keywords)

#Add go button
GObutton = Button(master,text="Go!", fg="black", command= Go)
GObutton.grid(row=7,column=6)


mainloop()
