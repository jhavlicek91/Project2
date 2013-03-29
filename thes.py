from nltk import wordnet as wn

word = "season"

syns = wn.synset(w)
print "synsets:", syns

for s in syns:
    for l in s.lemmas:
        print l.name
    print s.definition
    print s.examples
