import os.path
from Tkinter import *
import tkFileDialog
import urllib
import xlwt
import os
import re
from bs4 import BeautifulSoup
import nltk 
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn
from synonymwindow import SynonymWindow

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
        self.head2.grid(row = 6,column = 0, sticky = W)

	    #Add excel work book page
        #self.head3 = Label(frame, text = "Worksheet Title:").grid(row = 8, column = 0, sticky = W)

	    #add workbook textbox
        #self.worksheetEnter = Entry(frame, width = 35).grid(row = 9, column = 0)

        def GetFileName2():
            # get filename
            filename = tkFileDialog.asksaveasfilename()
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
        self.GObutton.grid(row = 9,column = 6)

    #Function for when go is clicked
    def Go(self):
        self.keyword = self.keywordEnter.get()
        self.excel = self.outputEnter.get()
        self.open = self.input.get()

        #open new screen displaying synonyms
        master1 = Tk()
        master1.title("Synonyms")
        w2 = SynonymWindow(master1, self.keyword, self.excel, self.open, self.ftype)
