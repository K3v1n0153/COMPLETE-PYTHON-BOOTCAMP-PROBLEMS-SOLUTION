"""
Write a Python function that checks whether 
a passed in string is palindrome or not.

palindrome('helleh') --> True
palindrome('kevin')  --> False

Note: A palindrome is word, phrase, or 
sequence that reads the same backward as 
forward, e.g., madam or nurses run.
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def palindrome(s):
	return s == s[::-1]

print(palindrome('helleh'))
print(palindrome('kevin'))