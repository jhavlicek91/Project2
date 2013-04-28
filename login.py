
import urllib import urlopen, urlencode                                           
import urllib2                                                                  

myId = 'xxxxxxxx'                                                              
myPin = 'xxxxxxx'                                                                

data = {                                                                        
            'id':myId,                                                          
            'PIN':myPin,                                                        
            'submit':'Request Access',                                          
            'wcuirs_uri':'https://cf.wcu.edu/busafrs/catcard/idsearch.cfm'      
        }                                                                       

opener = urllib2.build_opener()                                                 
opener.addheaders = [('User-agent','Mozilla/5.0')]                              

url = 'https://itapp.wcu.edu/BanAuthRedirector/Default.aspx'                    
request = urllib2.Request(url, urlencode(data))                                 

open("mycatpage.html", 'w').write(opener.open(request))
