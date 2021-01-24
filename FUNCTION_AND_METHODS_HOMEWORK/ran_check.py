"""
Write a function that checks whether a number 
is in a given range (inclusive of high and low)

ran_check(3, 2, 7) --> '3 is in the range between 2 and 7'
ran_check(9, 2, 7) --> 'Out of range!'
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def ran_check(num, low, high):

	if num > low and num < high:
		return f'{num} is in the range between {low} and {high}.'
	else:
		return f'{num} is out of range!'

print(ran_check(3, 2, 7))
print(ran_check(9, 2, 7))

# If you only wanted to return a boolean:
def ran_bool(num, low, high):
	return num > low and num < high

print(ran_bool(3, 2, 7))
print(ran_bool(9, 2, 7))