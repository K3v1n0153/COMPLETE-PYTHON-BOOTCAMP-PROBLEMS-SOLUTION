"""
Write a function that asks for an integer and prints 
the square of it. Use a while loop with a try, except, 
else block to account for incorrect inputs.

# EXAMPLE OUTPUT

Input an integer: null
An error occured! Please try again!
Input an integer: 2
Thank you, your number squared is: 4
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def ask():

	asking = True

	while asking:
		try:
			num = int(input('Input an integer: '))
		except:
			print('An error occured! Please try again!')
			continue
		else:
			print(f'Thank you, your number squared is: {num**2}')
			asking = False

print(ask())