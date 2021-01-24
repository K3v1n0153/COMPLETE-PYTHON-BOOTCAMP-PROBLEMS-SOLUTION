"""
Use zip() and a list comprehension to return a 
list of the same length where each value is the 
two strings from L1 and L2 concatenated together 
with connector between them. Look at the example 
output below:

concatenate(['A','B'],['a','b'],'-') --> ['A-a', 'B-b']
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def concatenate(L1, L2, connector):
	return [l1+connector+l2 for l1,l2 in zip(L1, L2)]

print(concatenate(['A','B'],['a','b'],'-'))