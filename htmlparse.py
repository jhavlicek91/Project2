import urllib2
from bs4 import BeautifulSoup

def hello(name):
	print "hello " + name

html = urllib2.urlopen('http://www.chinesetop100.com/').read()

soup = BeautifulSoup(html)

print ((soup.get_text()).encode('utf8'))
