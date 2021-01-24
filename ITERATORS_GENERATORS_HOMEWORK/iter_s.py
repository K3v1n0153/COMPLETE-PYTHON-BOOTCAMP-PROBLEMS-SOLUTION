"""
Explain a use case for a generator using a yield 
statement where you would not want to use a 
normal function with a return statement.

# EXAMPLE OUTPUT

h
e
l
l
o
"""

#######################
## SOLUTION BY KEVIN ##
#######################

s = 'hello'

iter_s = iter(s)

print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))

# Or

for letter in iter_s:
	print(letter)