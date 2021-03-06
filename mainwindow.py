from Tkinter import *
import tkFileDialog
from synonymwindow import *
from errorwindows import *


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
        self.input.grid(row = 1,column = 0)

        def GetFileName():
            # get filename
            if self.ftype.get() == 1:
               filename = tkFileDialog.askopenfilename()
            elif self.ftype.get() == 2:
               filename = tkFileDialog.askdirectory()
            print "%r" % (filename)
            fil.set(filename)

        #Add file Dialog box for the file to open
        self.inputdialog = Button(frame, text = "File", fg = "black", command = GetFileName )
        self.inputdialog.grid(row = 1, column = 1 )

        self.ftype = IntVar() 
        #Add FILE Radio Button
        self.FILEbutton = Radiobutton(frame, text = "FILE", fg = "black", variable = self.ftype, value = 1)
        self.FILEbutton.grid(row = 2,column = 0, sticky = E)

        #Add Directory Radio Button
        self.dirButton = Radiobutton(frame, text = "Directory", fg = "black", variable = self.ftype, value = 2)
        self.dirButton.grid(row = 2, column = 1)

        #Add HTML Radio Button
        self.HTMLbutton = Radiobutton(frame, text = "HTML", fg = "black", variable = self.ftype, value = 3 )
        self.HTMLbutton.grid(row = 2, column = 2)

        #add username label
        self.usertext = Label(frame, text = "Username and Password (If needed)")
        self.usertext.grid(row = 4, column = 0, sticky = W)

        self.user = Entry(frame, width = 20)
        self.user.grid(row = 5, column = 0, sticky = W)

        self.passw = Entry(frame, width = 20)
        self.passw.grid(row = 6, column = 0, sticky = W)

        #Add keyword heading 
        self.head1 = Label(frame, text = "Keywords:")
        self.head1.grid(row = 8, column = 0, sticky = W)

        #Add keyword textbox
        self.keywordEnter = Entry(frame, width = 35)
        self.keywordEnter.grid(row = 9, column = 0)

        #Add excel heading
        self.head2 = Label(frame, text = "Output Excel File:")
        self.head2.grid(row = 10, column = 0, sticky = W)

        def GetFileName2():
            # get filename
            filename = tkFileDialog.asksaveasfilename()
            print "%r" % (filename)
            ex.set(filename)

        #add excel text box
        ex = StringVar()
        self.outputEnter = Entry(frame, width = 35, textvariable = ex)
        self.outputEnter.grid(row = 11,column = 0)

        #Add file Dilog box for the file to open
        self.outputdialog = Button(frame, text = "File", fg = "black", command = GetFileName2 )
        self.outputdialog.grid(row = 11, column = 1 )

        #Add excel work book page
        self.head3 = Label(frame, text = "Worksheet Title:").grid(row = 12, column = 0, sticky = W)

	#add workbook textbox
        sheet = StringVar()
        self.worksheetEnter = Entry(frame, width = 35, textvariable = sheet)
        self.worksheetEnter.grid(row = 13, column = 0)

        #Add go button
        self.GObutton = Button(frame,text = "Go!", fg = "black", command = self.Go )
        self.GObutton.grid(row = 14,column = 2)


    #Function for when go is clicked
    def Go(self):
        self.keyword = self.keywordEnter.get()
        self.excel = self.outputEnter.get()
        self.open = self.input.get()
        self.ws = self.worksheetEnter.get()
           
        if self.open == "": 
           e1 = Tk()
           e1.title("Oops")
           f = FileErrorWindow(e1)

        elif self.ftype.get() == 0: 
           e2 = Tk()
           e2.title("Oops")
           radio = NoRadioWindow(e2)
           
        elif self.excel == "":
           e3 = Tk()
           e3.title("Ooops")
           ex = ExcelErrorWindow(e3)
        
        else:
           #open new screen displaying synonyms
           master1 = Tk()
           master1.title("Synonyms")

           #Format excel file name
           if self.excel.endswith('.xls') :
              filename = self.excel
           else:
              filename = self.excel + '.xls'
           
           w2 = SynonymWindow(self.parent, master1,  self.keyword, filename, self.open, self.ftype, self.user, self.passw, self.ws)

    def CloseAndOpen(self):
        #close window when done
        self.parent.destroy() 
        master = Tk()
        master.title("Project 2")
        w1 = WindowOne(master)  

       
