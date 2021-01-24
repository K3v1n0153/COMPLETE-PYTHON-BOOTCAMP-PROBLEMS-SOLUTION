"""
Create a generator that yields "n" random 
numbers between a low and high number (that are inputs).

Note: Use the random library. For example:

import random
random.randint(1, 10)

# EXAMPLE OUTPUT

for num in rand_num(1,10,12):
	print(num)

8
8
9
1
3
5
2
2
7
2
10
2
"""

#######################
## SOLUTION BY KEVIN ##
#######################

import random

def rand_num(low, high, n):

	for num in range(n):
		yield random.randint(low, high)

for num in rand_num(1,10,12):
	print(num)