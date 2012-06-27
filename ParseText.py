'''
    Returns lists of tokens, tags, items, and 
    writes them to text files.
'''

import nltk

# Load text file
data=open("tpb_sopa.txt")
    # OUT: <type 'file'>

# Read file as string
input=data.read()
    # OUT: <type 'str'>

# Parse string into tokens
tokens=nltk.word_tokenize(input)
    # OUT: <type 'list'>

# Calculate frequency distribution
freq=nltk.FreqDist(tokens)
    # OUT: <class 'nltk.probability.FreqDist'>

# Sort word list in decreasing order
items=freq.items()
    # OUT: <type 'list'>

# Apply form of speech tag
tags=nltk.pos_tag(tokens)
    # OUT: <type 'list'>

# Save list of tokens
FILE=open("out/tokens.txt","w")
for token in tokens:
    FILE.writelines(str(token+'\n'))
FILE.close()
print "tokens saved."

# Save list of items by frequency
FILE=open("out/items.txt","w")
for item in items:
    FILE.writelines(str(item[0]+", "+str(item[1])+'\n'))
FILE.close()
print "items saved."

# Save list of speech tags
FILE=open("out/tags.txt","w")
for tag in tags:
    FILE.writelines(str(tag[0]+", "+str(tag[1])+'\n'))
FILE.close()
print "tags saved."
