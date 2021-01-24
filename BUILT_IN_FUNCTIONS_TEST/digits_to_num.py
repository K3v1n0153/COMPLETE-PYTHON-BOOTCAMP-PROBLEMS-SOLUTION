"""
Use reduce() to take a list of digits and 
return the number that they correspond to. 
For example, [1, 2, 3] corresponds to one-hundred-twenty-three.

digits_to_num([3,4,3,2,1]) --> 34321

Do not convert the integers to strings!
"""

#######################
## SOLUTION BY KEVIN ##
#######################

from functools import reduce

def digits_to_num(digits):
	return reduce(lambda x,y: 10*x+y, digits)

print(digits_to_num([3,4,3,2,1]))