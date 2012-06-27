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

# Sort in decreasing order
items=freq.items()
    # OUT: <type 'list'>

# Apply form of speech tag
tags=nltk.pos_tag(tokens)
    # OUT: <type 'list'>

# Save list of items
FILE=open("items.txt","w")
for item in items:
    FILE.writelines(str(item[0]+", "+str(item[1])+'\n'))
FILE.close()

# Save list of tags
FILE=open("tags.txt","w")
for tag in tags:
    FILE.writelines(str(tag[0]+", "+str(tag[1])+'\n'))
FILE.close()



