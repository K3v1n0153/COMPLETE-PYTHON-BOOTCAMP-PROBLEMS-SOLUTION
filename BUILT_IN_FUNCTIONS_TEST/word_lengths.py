"""
Use map() to create a function which finds the length of each word in 
the phrase (broken by spaces) and returns the values in a list.

word_lengths('How long are the words in this phrase') --> [3, 4, 3, 3, 5, 2, 4, 6]

The function will have an input of a string, and output a list of integers.
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def word_lengths(phrase):
	return list(map(len, phrase.split()))

print(word_lengths('How long are the words in this phrase'))