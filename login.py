                                                                
data = {                                                                        
            'id':user,                                                          
            'PIN':passw,                                                        
            'submit':'Request Access',                                          
            'wcuirs_uri': fil      
        }                                                                       

opener = urllib2.build_opener()                                                 
opener.addheaders = [('User-agent','Mozilla/5.0')]                              

                 
request = urllib2.Request(fil, urlencode(data))                                 

open("temp.txt", 'w').write(opener.open(request))
