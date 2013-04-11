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
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn

def makeLambda(f, *args):
	return lambda: f(*args)

#Class for searching textfiles for keywords        
def ReadTextFile(FileName, **finalwords):
    #Get the text file to search through and open it
    f = file(FileName, 'r')

    for k in finalwords:
       caps = list()
    
       for w in finalwords[k]: 
          #account for capital letters as well
          cap = w.capitalize()   
          caps.append(cap)

       for c in caps:
          finalwords[k].append(c)

    #Create dictionary that has each keyword and the 
    #number of times it appeared in the file
    complete = dict()
    for k in finalwords:
        complete[k] = dict()
        for w in finalwords[k]:
            complete[k][w] = 0

    #Go through each line in the text and search for every word in it
    for line in f:
        for k in complete:
            for w in complete[k]:
                instances = re.findall('\\b'+w+'\\b', line)
                amount = len(instances)
                new_amount = amount + complete[k][w]
                complete[k][w] = new_amount

    for k in complete:
        
        #sort dictionary
        sort = sorted(complete[k]) 
        
        #create a new dictionary without both capital and non capital letters
        comp = dict()
        halfway = len(complete[k]) / 2;
        for i in range(0, halfway):
           key = sort[i]
           key2 = sort[i + halfway]
           comp[key] = complete[k][key] + complete[k][key2] 
        complete[k] = comp

    #Close the file you read
    f.close()

    #need to return a dictionary of dictionaries
    return complete;

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

    if(os.path.isfile(excelfile)):
	tempbook = xlrd.open_workbook(excelfile, formatting_info=True)
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
          
       #Write the sum of the keywords
       worksheet.write(index + 1, column, "Total")
       worksheet.write(index + 1, column + 1, summ)
       column += 3

    workbook.save(filename)

class SynonymWindow:
    def __init__(self, parent, keyword, excel, op, ftype):
        frame = Frame(parent)
        frame.pack()
        self.keyword = keyword 
        self.excel = excel
        self.op = op
        self.ftype = ftype
        self.finalwords = dict()

        #get different keywords from box
        self.keywords = keyword.split()
        self.dictionary = dict()
        
        self.words = dict()
        self.synonyms = list()
        self.temp = list()

        for k in self.keywords: 
            self.dictionary[k] = list() 
            self.words[k] = list()  
            
            #Create lists with synonyms
            self.syns = wn.synsets(k)
            for si in self.syns:
               for l in si.lemmas:
                  self.dictionary[k].append(l.name)

        #get rid of duplicates in list of synonyms
        for k in self.keywords:
            self.dictionary[k] = set(self.dictionary[k])

        #self.temp replaced with dictionary

        #remove a word if it is the keyword & replace '_" with a space
        for ke in self.dictionary:
            
            for w in self.dictionary[ke]:
               key = 0

               #Check if the synonym is two words and contains the keyword in it
               for l in w.split("_"):
                  if l == ke or l == ke.capitalize(): key = 1      
                  
               if w != ke and w != ke.capitalize() and key == 0: self.words[ke].append(w.replace('_', ' '))
              
        #set current row and column
        self.currCol = 0
        self.endRow = 0;
        self.otherEnter = dict()
        self.checks = dict()

        #loop through keywords
        for k in self.keywords:
            self.checks[k] = dict()
        
            #Add Synonym Label
            self.lab = Label(frame, text = "Synonyms for " + k.capitalize() + ":")
            self.lab.grid(row = 0, column = self.currCol, sticky = W)

            i = 0;
            #Populate checkboxes with synonyms
            for w in self.words[k]:
               self.checks[k][w] = IntVar()
               self.check = Checkbutton(frame, text = w.capitalize(), variable = self.checks[k][w], command = makeLambda(self.checkbox, k, w))
               self.check.grid(row = i + 1, column = self.currCol, sticky = W)
               i += 1

            #Add optional synonym box 
            self.otherEnter[k] = Entry(frame, width = 30)
            self.otherEnter[k].grid(row = len(self.words[k]) + 2, column = self.currCol)
            
            self.lab1 = Label(frame, text = "Additional words to look up:")
            self.lab1.grid(row = len(self.words[k]) + 1, column = self.currCol, sticky = W)

            self.currCol += 1
            self.endRow = max(self.endRow, len(self.words[k]) )

        #Place the go button
        self.finishbutton = Button(frame, text = "Go!", command = self.go2)
        self.finishbutton.grid(row = self.endRow + 3, column = self.currCol)

    #Function for the second go button     
    def go2(self):

        #Add main word to list of words to be searched for
        for k in self.keywords:
            self.finalwords[k] = list()
            self.finalwords[k].append(k)
            self.extra = self.otherEnter[k].get().split()

            #Add optional synonyms to the list
            for s in self.extra:
                self.finalwords[k].append(s)
            print "%r" % (self.finalwords[k])
        

        #Go through words and check if the checkboxes have been selected
        for k in self.keywords:
            for w in self.words[k]:
               print "%r  %r" % (w , self.checks[k][w].get() )
               if self.checks[k][w].get() == 1:
                  self.finalwords[k].append(w)
                  print "%r" % (w)

        print "%r" % (self.finalwords)

        #if html is selected
        if self.ftype.get() == 1:
           if self.op.startswith("http"):
	      sock = urllib.urlopen(self.op)
	   else:
	      sock = urllib.urlopen("http://" + self.op + "/")
	   htmlsource = sock.read()
	   sock.close()
	   soup = BeautifulSoup(htmlsource)
	   result = soup.get_text()
	   f = open('temp.txt','w')
	   f.write(result.encode('utf8'))
	   f.close()
	   results = ReadTextFile("temp.txt", **self.finalwords)
	   os.remove("temp.txt")

        #if pdf is selected
        if self.ftype.get() == 2:
           print "PDF"
	   if self.op.endswith('.pdf'): os.system("python pdf2txt.py -o temp.txt " + self.op) 
	   else: os.system("python pdf2txt.py -o temp.txt " + self.op + ".pdf")
           results = ReadTextFile("temp.txt", **self.finalwords)
           #Delete the temporary file
           os.remove("temp.txt")

        #if txt file is selected
        if self.ftype.get() == 3:
           results = ReadTextFile(self.op, **self.finalwords)

        #Write output to the excel file
        MakeExcel(self.excel, self.op, self.keywords, **results);

    def checkbox(self, k, w):
       print "%r %r" % (k, w)
       value = self.checks[k][w].get()
       if value == 0: self.checks[k][w].set(1)
       if value == 1: self.checks[k][w].set(0)

