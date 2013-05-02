import re

#Class for searching textfiles for keywords        
def ReadTextFile(FileName, **finalwords):
    print "%r" % (finalwords)
     
    synonyms = finalwords
    #Get the text file to search through and open it
    f = file(FileName, 'r')

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
                #replace the 
                line = line.replace("\xe2\x80\xa9", " ")
                instances = re.findall('\\b' + w + '\\b', line.lower())
                print "%r" % (line.lower())
                amount = len(instances)
                new_amount = amount + complete[k][w]
                complete[k][w] = new_amount

    print "%r" % (complete)

    #Close the file you read
    f.close()

    #need to return a dictionary of dictionaries
    return complete;


