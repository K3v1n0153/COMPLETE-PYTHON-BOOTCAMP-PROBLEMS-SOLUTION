"""
Use filter to return the words from a list of words which start with a target letter.

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

filter_words(l,'h') --> ['hello', 'ham', 'hi', 'heart']
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def filter_words(word_list, letter):
	return list(filter(lambda w: w[0] == letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

print(filter_words(l,'h'))