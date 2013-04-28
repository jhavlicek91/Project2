from urllib import urlopen, urlencode
myId = username
myPin = password
data = {
            'id':myId,
            'PIN':myPin,
            'submit':'Request Access',
            'wcuirs_uri':website
        }

url = website
response = urlopen(url, urlencode(data))
open("temp.txt",'w').write(response.read())
