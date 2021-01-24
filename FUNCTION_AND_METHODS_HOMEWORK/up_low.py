"""
Write a Python function that accepts a string and calculates 
the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def up_low(s):

	upper_case_count = 0
	lower_case_count = 0

	for letter in s:
		if letter.isupper():
			upper_case_count += 1
		elif letter.islower():
			lower_case_count += 1
		else:
			pass

	print(f'Original string: {s}')
	print(f'No. of Upper case characters: {upper_case_count}')
	print(f'No. of Lower case characters: {lower_case_count}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')