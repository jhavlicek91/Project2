import nltk

word = "season"

syns = word.synsets(a)
print "synsets:", syns

for s in syns:
    for l in s.lemmas:
        print l.name
    print s.definition
    print s.examples
