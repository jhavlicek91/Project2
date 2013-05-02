from Tkinter import *
import tkFileDialog
import os
import nltk 
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn
from outputexcel import *
from readtext import *
from utilities import *

def makeLambda(f, *args):
	return lambda: f(*args) 

class SynonymWindow:
    def __init__(self, lastw, parent, keyword, excel, op, ftype, user, passw):

        self.lastw = lastw
        self.parent = parent
        frame = Frame(parent)
        frame.pack()
        self.keyword = keyword 
        self.excel = excel
        self.op = op
        self.ftype = ftype
        self.user = user
        self.passw = passw
        self.finalwords = dict()

        #get different keywords from box
        self.keywords = keyword.split(",")
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
                  self.dictionary[k].append(l.name.lower())
                  

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

        #if file is selected, depth first search through file/directory
        if self.ftype.get() == 1 or self.ftype.get() == 2:   
           self.wsh, self.wb = OpenExcel(self.excel, self.op)
           DFS(self.wsh, self.op, self.excel, self.keywords, **self.finalwords)
           CloseExcel(self.wb, self.excel)

        #if html is selected
        if self.ftype.get() == 3:
           self.results = html(self.user, self.passw, self.op, **self.finalwords)       
           #Write output to the excel file
           self.wsh, self.wb = OpenExcel(self.excel, self.op)
           MakeExcel(self.wsh, self.excel, self.op, self.keywords, **self.results)
           CloseExcel(self.wb, self.excel)

        #close window when done
        self.parent.destroy()
        self.lastw.destroy()

    def checkbox(self, k, w):
       print "%r %r" % (k, w)
       value = self.checks[k][w].get()
       if value == 0: self.checks[k][w].set(1)
       if value == 1: self.checks[k][w].set(0)

