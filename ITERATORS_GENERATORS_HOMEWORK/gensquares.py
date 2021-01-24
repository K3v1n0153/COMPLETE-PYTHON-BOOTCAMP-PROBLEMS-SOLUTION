"""
Create a generator that generates the squares of numbers up to some number N.

# EXAMPLE OUTPUT

for x in gensquares(10):
	print(x)

0
1
4
9
16
25
36
49
64
81
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def gensquares(N):

	for num in range(N):
		yield num**2

for x in gensquares(10):
	print(x)