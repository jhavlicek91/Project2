import urllib
from bs4 import BeautifulSoup

print "Please enter website"
website = raw_input()
print "Please enter word"
word = raw_input()
sock = urllib.urlopen("http://" + website + "/")
htmlsouce = sock.read()
sock.close()
soup = BeautifulSoup(htmlsouce)
result = soup.get_text()
f = open('result.txt','w')
f.write(result.encode('utf8'))
f.close()

