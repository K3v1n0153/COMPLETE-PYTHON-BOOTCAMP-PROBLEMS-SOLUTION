"""
Write a function that computes the volume of a sphere given its radius.

vol(2) --> 33.49333333333333

The volume of a sphere is given as 4/3π𝑟3
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def vol(rad):
	return 4/3*3.14*rad**3

print(vol(2))