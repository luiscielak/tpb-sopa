# The Pirate Bay SOPA
# luis@luiscielak.com

'''
Returns lists of tokens, tags, and items, then 
writes them to text files.
'''

import nltk

# Load text file
data=open("tpb_sopa.txt")
    # OUT: <type 'file'>

# Read file as string
input=data.read()
    # OUT: <type 'str'>

# Parse text lines into tokens
lines=nltk.line_tokenize(input)
# Write list of lines to disk
FILE=open("out/lines.txt","w")
for line in lines:
    FILE.writelines(str(line)+'\n')
FILE.close()
print "lines: "+str(len(lines))


# Parse sentences into tokens
sentences=nltk.sent_tokenize(input)
# Write list of sentences to disk
FILE=open("out/sentences.txt","w")
for sentence in sentences:
    FILE.writelines(str(sentence))
FILE.close()
print "sentences: "+str(len(sentences))


# Parse words into tokens
words=nltk.word_tokenize(input)
# Write list of words to disk
FILE=open("out/words.txt","w")
for word in words:
    FILE.writelines(word+'\n')
FILE.close()
print "words: "+ str(len(words))


# Count number of words
freq=nltk.FreqDist(words)
    # OUT: <class 'nltk.probability.FreqDist'>

# Sort word list by count
items=freq.items()
    # OUT: <type 'list'>

# Apply form of speech tag
tags=nltk.pos_tag(words)
    # OUT: <type 'list'>

# Save list of items by frequency
FILE=open("out/items.txt","w")
for item in items:
    FILE.writelines(str(item[0]+'\t'+str(item[1])+'\n'))
FILE.close()
print "items saved."

# Save list of speech tags
FILE=open("out/tags.txt","w")
for tag in tags:
    FILE.writelines(str(tag[0]+", "+str(tag[1])+'\n'))
FILE.close()
print "tags saved."




