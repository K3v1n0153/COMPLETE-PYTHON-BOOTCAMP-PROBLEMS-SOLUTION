"""
LESSER OF TWO EVENS: Write a function that returns 
the lesser of two given numbers if both numbers 
are even, but returns the greater if one or both 
numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def lesser_of_two_evens(a, b):

	if a%2 == 0 and b%2 == 0:
		# You can also use the min function
		if a < b:
			return a
		else:
			return b
	else:
		# You can also use the max function
		if a > b:
			return a
		else:
			return b

print(lesser_of_two_evens(2,0))
print(lesser_of_two_evens(10,5))