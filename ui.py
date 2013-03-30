from Tkinter import *
import tkFileDialog
import urllib
import xlwt
import os
import re
from bs4 import BeautifulSoup


#Class for searching textfiles for keywords        
def ReadTextFile(FileName, keywords):
    #Get the text file to search through and open it
    f = file(FileName, 'r')

    #account for capital letters as well
    caps = list()
    for l in keywords:
        cap = l.title()   
        caps.append(cap)

    for c in caps:
        keywords.append(c)

    #Create dictionary that has each keyword and the 
    #number of times it appeared in the file
    new_dict = {}

    #Initialize the dictionary
    for w in keywords:
       new_dict[w] = 0

    #Go through each line in the text and search for every word in it
    for line in f:
        for w in keywords:
            instances = re.findall(w, line)
            amount = len(instances)
            new_amount = amount + new_dict[w]
            new_dict[w] = new_amount

    #print out resultss          
    for key in new_dict.keys():
        print "%r: %r" % (key, new_dict[key])

    #sort dictionary
    sort = sorted(new_dict) 
    
    #create a new dictionary without both capital and non capital letters
    complete = dict()
    halfway = len(new_dict) / 2;
    for i in range(0, halfway):
       key = sort[i]
       key2 = sort[i + halfway]
       complete[key] = new_dict[key] + new_dict[ key2 ] 
    
    #Close the file you read
    f.close()

    return complete;

#Function for writing results to an excel file
def MakeExcel(excelfile, searchfile, results, keyword):

    filename = excelfile + '.xls'
    if len(searchfile) > 20:
	    article = searchfile[:18] + '...'
    else:
	    article = searchfile

    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet(article)

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
    worksheet.write_merge(0, 0, 0, 10, searchfile, style)
    worksheet.write(1, 1, 'Words', style2)
    worksheet.write(1, 2, 'Count', style2)

    #Write cells corresponding to the main word
    index = 2
    worksheet.write(index, 0, "Main Term")
    worksheet.write(index, 1, keyword)
    worksheet.write(index, 2, results[keyword])

    #Write the rest of the cells
    index = 3
    summ = 0
    for w in results.keys():
         if w != keyword:
             worksheet.write(index, 1, w)
             worksheet.write(index, 2, results[w])
             index += 1
         summ += results[w]

    #Write the sum of the keywords
    worksheet.write(index + 1, 1, "Total")
    worksheet.write(index + 1, 2, summ)

    workbook.save(filename)


class WindowOne:

    def __init__(self, parent):

        frame = Frame(parent)
        frame.pack()
        self.parent = parent

        #Add file heading
        self.heading = Label(frame, text="File:")
        self.heading.grid(row = 0,column = 0,sticky= W)

        #Add file text box
        fil = StringVar()
        self.input = Entry(frame, width = 35, textvariable = fil)
        self.input.grid(row=1,column=0)

        def GetFileName():
            # get filename
            filename = tkFileDialog.askopenfilename()
            print "%r" % (filename)
            fil.set(filename)

        #Add file Dilog box for the file to open
        self.inputdialog = Button(frame, text = "File", fg = "black", command = GetFileName )
        self.inputdialog.grid(row = 1, column = 2 )

        self.ftype = IntVar() 
        #Add HTML Radio Button
        self.HTMLbutton = Radiobutton(frame, text = "HTML", fg = "black", variable = self.ftype, value = 1)
        self.HTMLbutton.grid(row = 2,column = 0,sticky = E)

        #Add PDF Radio Button
        self.PDFbutton = Radiobutton(frame, text = "PDF ", fg = "black", variable = self.ftype, value = 2 )
        self.PDFbutton.grid(row = 2, column = 2)

        #Add text Radio button
        self.TXTbutton = Radiobutton(frame, text = "TXT", fg = "black", variable = self.ftype, value = 3)
        self.TXTbutton.grid(row = 2,column = 3)

        #Add keyword heading 
        self.head1 = Label(frame, text = "Keywords:")
        self.head1.grid(row = 4,column = 0,sticky = W)

        #Add keyword textbox
        self.keywordEnter = Entry(frame, width = 35)
        self.keywordEnter.grid(row = 5,column = 0)

        #Add excel heading
        self.head2 = Label(frame, text = "Output Excel File:")
        self.head2.grid(row = 6,column = 0,sticky = W)

        def GetFileName2():
            # get filename
            filename = tkFileDialog.askopenfilename()
            print "%r" % (filename)
            ex.set(filename)

        #add excel text box
        ex = StringVar()
        self.outputEnter = Entry(frame, width = 35, textvariable = ex)
        self.outputEnter.grid(row = 7,column = 0)

        #Add file Dilog box for the file to open
        self.outputdialog = Button(frame, text = "File", fg = "black", command = GetFileName2 )
        self.outputdialog.grid(row = 7, column = 2 )

        #Add go button
        self.GObutton = Button(frame,text = "Go!", fg = "black", command = self.Go )
        self.GObutton.grid(row = 8,column = 6)

    #Function for when go is clicked
    def Go(self):
        self.keyword = self.keywordEnter.get()
        self.excel = self.outputEnter.get()
        self.open = self.input.get()

        #open new screen displaying synonyms
        master1 = Tk()
        master1.title("Synonyms")
        w2 = SynonymWindow(master1, self.keyword, self.excel, self.open, self.ftype)

       #return list with keyword and correct synonyms

class SynonymWindow:

    def __init__(self, parent, keyword, excel, op, ftype):
        frame = Frame(parent)
        frame.pack()
        self.keyword = keyword
        self.excel = excel
        self.op = op
        self.ftype = ftype
        self.finalwords = list()

        self.words = list()
            
        #Create list with synonyms
        self.words.append("one")  
        self.words.append("two")
        self.words.append("three")
        self.words.append("four")
        self.words.append("five")

        #Add Synonym Label
        self.lab = Label(frame, text = "Synonyms for " + self.keyword + ":")
        self.lab.grid(row = 0,column = 0, sticky = W)

        i = 0;
        self.checks = dict()
        #Populate checkboxes with synonyms
        for w in self.words:
           self.checks[w] = IntVar()
           self.check = Checkbutton(frame, text = w, variable = self.checks[w], onvalue = 1, offvalue = 0)
           self.check.grid(row = i + 1, column = 0, sticky = W)
           i += 1

        #Add optional synonym box 
        self.otherEnter = Entry(frame, width = 30)
        self.otherEnter.grid(row = len(self.words) + 2, column = 0)
        
        self.lab1= Label(frame, text = "Others:")
        self.lab1.grid(row = len(self.words) + 1, column = 0, sticky = W)

        #Place the go button
        self.finishbutton = Button(frame, text = "Go!", command = self.go2)
        self.finishbutton.grid(row = len(self.words) + 2, column = 3)


    #Function for the second go button     
    def go2(self):

        #Add main word to list of words to be searched for
        self.finalwords.append(self.keyword)

        #Add optional synonyms to the list
        self.extra = self.otherEnter.get().split()
        for s in self.extra:
            self.finalwords.append(s)

        #Go through words and check if the checkboxes have been selected
        for w in self.words:
           print "%r  %d" % (w , self.checks[w].get() )
           if self.checks[w].get() == 1:
              self.finalwords.append(w)
              print "%r" % (w)

        print "%r" % (self.finalwords)

        #if html is selected
        if self.ftype.get() == 1:
            sock = urllib.urlopen("http://" + self.op + "/")
            htmlsource = sock.read()
            sock.close()
            soup = BeautifulSoup(htmlsource)
            result = soup.get_text()
            f = open('temp.txt','w')
            f.write(result.encode('utf8'))
            f.close()
            results = ReadTextFile("temp.txt", self.finalwords)
            os.remove("temp.txt")

        #if pdf is selected
        if self.ftype.get() == 2:
           print "PDF"
           os.system("python pdf2txt.py -o temp.txt " + self.op) 
           results = ReadTextFile("temp.txt", self.finalwords)
           #Delete the temporary file
           os.remove("temp.txt")

        #if txt file is selected
        if self.ftype.get() == 3:
           results = ReadTextFile(self.op, self.finalwords)

        #Write output to the excel file
        MakeExcel(self.excel, self.excel, results, self.keyword.capitalize());


def main():
    master = Tk()
    master.title("Project 2")
    w1 = WindowOne(master)
    mainloop()

if __name__ == '__main__':
    main()
