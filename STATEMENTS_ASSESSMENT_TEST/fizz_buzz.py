"""
Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the 
number, and for the multiples of five print "Buzz". For 
numbers which are multiples of both three and five print 
"FizzBuzz".
"""

#######################
## SOLUTION BY KEVIN ##
#######################

for num in range(1, 100+1):
	if num%3 == 0:
		print('Fizz')
	elif num%5 == 0:
		print('Buzz')
	elif num%3 == 0 and num%5 == 0:
		print('FizzBuzz')
	else:
		print(num)