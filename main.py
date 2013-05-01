from Tkinter import *
import tkFileDialog
from mainwindow import WindowOne

def main():
    master = Tk()
    master.title("Project 2")
    w1 = WindowOne(master)
    mainloop()

if __name__ == '__main__':
    main()
