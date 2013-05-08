import os.path
import urllib
import os
from bs4 import BeautifulSoup
from urllib import urlencode, urlopen                                       
import urllib2    
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

       sock = urlopen(fil, urlencode(data))
       htmlsource = sock.read()
       sock.close()
       soup = BeautifulSoup(htmlsource)
       result = soup.get_text()
       f = open('temp.txt', 'w')
       f.write(result.encode('utf8'))
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
       f = open('temp.txt', 'w')
       f.write(result.encode('utf8'))
       f.close()
    results = ReadTextFile("temp.txt", **keywords)
    os.remove("temp.txt")

    return results


def DFS(wsh, phile, excel, keys, **keywords):
    #check if it is a file or directory
    print "DFS initiated"
    
    if os.path.isdir(phile):
    
       print "%r is a directory" % (phile)  
       #go through every file in the directory
       for f in os.listdir(phile):
          print "%r" % (f)
          DFS(wsh, phile + "/" + f, excel, keys, **keywords)
          
    else:

       print "%r is a file" % (phile)
       if phile.endswith('.pdf'):
          results = pdf(phile, **keywords)
          print "About to make excel file"
          MakeExcel(wsh, excel, phile, keys, **results)

       elif phile.endswith('.txt'):
          results = ReadTextFile(phile, **keywords)
          MakeExcel(wsh, excel, phile, keys, **results)

          
