import re
import xlwt

def ReadTextFile(FileName, keywords):
   #Get the text file to search through and open it
   f = file(FileName, 'r')

   #Get the keyword(s) you want to search for
   words = keywords.split()

   #Create dictionary that has each keyword and the 
   #number of times it appeared in the file
   new_dict = {}

   for w in words:
      new_dict[w] = 0

   for line in f:
      for w in words:
         instances = re.findall(w, line)
	 amount = len(instances)
	 new_amount = amount + new_dict[w]
	 new_dict[w] = new_amount

   for key in new_dict.keys():
      print "%r: %r" % (key, new_dict[key])

   #Close the file you read
   f.close()
