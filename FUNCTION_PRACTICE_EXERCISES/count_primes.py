"""
COUNT PRIMES: Write a function that returns 
the number of prime numbers that exist up to 
and including a given number

count_primes(100) --> 25

By convention, 0 and 1 are not prime.
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def count_primes(num):

	primes = [2]
	x = 3

	if num <= 1:
		return 0
	while x <= num:
		for y in range(2, x):
			if x%y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2

	print(primes)
	return len(primes)

print(count_primes(100))

# Faster Version
def count_primes(num):

	primes = [2]
	x = 3

	if num <= 1:
		return 0
	while x <= num:
		for y in primes:
			if x%y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2

	print(primes)
	return len(primes)

print(count_primes(100))