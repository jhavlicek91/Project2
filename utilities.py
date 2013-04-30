import os.path
import urllib
import xlwt
import xlrd
from xlutils.copy import copy
import os
import re
from bs4 import BeautifulSoup
from urllib import urlencode, urlopen                                       
import urllib2    
import nltk 
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn
from outputexcel import *
from readtext import *


def pdf(fil, **keywords):

    #If operating system is windows
    if os.name == "nt":
       if fil.endswith('.pdf'): 
          os.system("pdf2txt.py -o temp.txt " + fil) 
       else: 
          os.system("pdf2txt.py -o temp.txt " + fil + ".pdf")

    #if operating system is linux or mac
    elif os.name == "posix":
        if fil.endswith('.pdf'): 
          os.system("python pdf2txt.py -o temp.txt " + fil) 
        else: 
          os.system("python pdf2txt.py -o temp.txt " + fil + ".pdf")

    results = ReadTextFile("temp.txt", **keywords)
    #Delete the temporary file
    os.remove("temp.txt")

    return results
    
def html(user, passw, fil, **keywords):

    if passw != '' and user != '':
       data = {                                                                        
            'id': user,                                                          
            'PIN': passw,                                                        
            'submit': 'Request Access',                                          
            'wcuirs_uri':fil 
       }

       response = urlopen(fil, urlencode(data))                           
                              
       f = open('temp.txt', 'w')
       f.write(response.read())
       f.close()
       
    else: 

       if fil.startswith("http"):
          sock = urllib.urlopen(fil)
       else:
          sock = urllib.urlopen("http://" + fil + "/")
       htmlsource = sock.read()  
       sock.close()   
       soup = BeautifulSoup(htmlsource)
       result = soup.get_text()
       f = open('temp.txt','w')
       f.write(result.encode('utf8'))
       f.close()
    results = ReadTextFile("temp.txt", **keywords)
    os.remove("temp.txt")

    return results


def DFS(phile, excel, keys, **keywords):
    #check if it is a file or directory
    print "DFS initiated"
    
    if os.path.isdir(phile):
    
       print "%r is a directory" % (phile)  
       #go through every file in the directory
       for f in os.listdir(phile):
          print "%r" % (f)
          DFS(phile + "/" + f, excel, keys, **keywords)
          
    else:

       print "%r is a file" % (phile)
       if phile.endswith('.pdf'):
          results = pdf(phile, **keywords)
          print "About to make excel file"
          MakeExcel(excel, phile, keys, **results)

       elif phile.endswith('.txt'):
          results = ReadTextFile(phile, **keywords)
          MakeExcel(excel, phile, keys, **results)

          
