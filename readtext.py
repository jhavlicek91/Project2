import re

#Class for searching textfiles for keywords        
def ReadTextFile(FileName, **finalwords):
    print "%r" % (finalwords)
     
    synonyms = finalwords
    #Get the text file to search through and open it
    f = file(FileName, 'r')

    for k in synonyms:
       caps = list()
    
       for w in synonyms[k]: 
          #account for capital letters as well
          if w[0].isupper(): 
             cap = w.lower()
          else:
             cap = w.title()   
          caps.append(cap)

       for c in caps:
          synonyms[k].append(c)

    #Create dictionary that has each keyword and the 
    #number of times it appeared in the file
    complete = dict()
    for k in synonyms:
        complete[k] = dict()
        for w in synonyms[k]:
            complete[k][w] = 0

    #Go through each line in the text and search for every word in it
    for line in f:
        for k in complete:
            for w in complete[k]:
                instances = re.findall('\\b'+w+'\\b', line)
                amount = len(instances)
                new_amount = amount + complete[k][w]
                complete[k][w] = new_amount

    print "%r" % (complete)
    for k in complete:
        
        #sort dictionary
        sort = sorted(complete[k]) 
        print "%r" %(sort)
        
        #create a new dictionary without both capital and non capital letters
        comp = dict()
        halfway = len(complete[k]) / 2;
        for i in range(0, halfway):
           key = sort[i]
           key2 = sort[i + halfway]
           comp[key] = complete[k][key] + complete[k][key2] 
        complete[k] = comp
        print "%r" % (complete[k])

    #Close the file you read
    f.close()

    #need to return a dictionary of dictionaries
    return complete;


