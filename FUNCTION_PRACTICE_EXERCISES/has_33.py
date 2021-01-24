"""
FIND 33:

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def has_33(nums):

	for idx in range(len(nums)-1):
		if nums[idx] == 3 and nums[idx+1] == 3:
			return True
	return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))