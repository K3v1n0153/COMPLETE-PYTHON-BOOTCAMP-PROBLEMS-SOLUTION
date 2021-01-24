"""
Use enumerate() and other skills from above to 
return the count of the number of items in the 
list whose value equals its index.

count_match_index([0,2,2,1,5,5,6,10]) --> 4
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def count_match_index(L):

	e = list(filter(lambda cmi: cmi[0] == cmi[1], enumerate(L)))
	return len(e)

print(count_match_index([0,2,2,1,5,5,6,10]))