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
from mainwindow import WindowOne

def main():
    master = Tk()
    master.title("Project 2")
    w1 = WindowOne(master)
    mainloop()

if __name__ == '__main__':
    main()
