"""
PRINT BIG: Write a function that takes in a single letter, 
and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

HINT: Consider making a dictionary of possible patterns, 
and mapping the alphabet to specific 5-line combinations of patterns.

For purposes of this exercise, it's ok if your dictionary stops at "E".
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def print_big(a):

	pattern = {1: '  *  ', 2: '*   *', 3: '*****', 4: '*   *', 5: '****', 6: ' ****', 7: '*'}
	letter_a = {
				'A': [1, 2, 3, 4, 4], 
				'B': [5, 2, 5, 2, 5], 
				'C': [6, 7, 7, 7, 6], 
				'D': [5, 2, 2, 2, 5], 
				'E': [3,7,3,7,3]
	}

	for pat in letter_a[a.upper()]:
		print(pattern[pat])

print_big('e')