import urllib
from bs4 import BeautifulSoup

print "Enter the website to search through"
site = raw_input()

# instantiate the parser and fed it some HTML
sock = urllib.urlopen("http://" + site + "/")
htmlsource = sock.read()
sock.close()

soup = BeautifulSoup(htmlsource)

print soup.get_text()


