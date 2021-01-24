"""
Use enumerate() and other skills to return a 
dictionary which has the values of the list 
as keys and the index as the value. You may 
assume that a value will only appear once in 
the given list.

d_list(['a','b','c']) --> {'a': 0, 'b': 1, 'c': 2}
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def d_list(L):
	return dict([(key,value) for value, key in enumerate(L)])

print(d_list(['a','b','c']))