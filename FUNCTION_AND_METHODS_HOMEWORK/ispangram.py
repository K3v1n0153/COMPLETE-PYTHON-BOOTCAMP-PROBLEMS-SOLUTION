"""
Write a Python function to check whether a string is pangram or not.

ispangram("The quick brown fox jumps over the lazy dog") --> True
ispangram('fdfjdkjfeoeoirnvnvdfjd') --> False

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: Look at the string module
"""

#######################
## SOLUTION BY KEVIN ##
#######################

import string

def ispangram(str1, alphabet=string.ascii_lowercase):

	count = 0

	for alpha in alphabet:
		if alpha in set(str1):
			count += 1

	return count == 26

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram('fdfjdkjfeoeoirnvnvdfjd'))