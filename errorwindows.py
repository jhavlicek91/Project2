from Tkinter import *

class NoRadioWindow:

    def __init__(self, parent):
       frame = Frame(parent)
       frame.pack()
       self.parent = parent

       #Add a text label with error message
       self.heading = Label(frame, text="Choose what type of file you selected")
       self.heading.grid(row = 0,column = 0,sticky= W)

class FileErrorWindow:
     
    def __init__(self, parent):
       frame = Frame(parent)
       frame.pack()
       self.parent = parent

       #Add a text label with error message
       self.heading = Label(frame, text="Forgot to enter a file name")
       self.heading.grid(row = 0,column = 0,sticky= W)

class ExcelErrorWindow:
     
    def __init__(self, parent):
       frame = Frame(parent)
       frame.pack()
       self.parent = parent

       #Add a text label with error message
       self.heading = Label(frame, text="Forgot to enter an output file")
       self.heading.grid(row = 0,column = 0,sticky= W)      

        
