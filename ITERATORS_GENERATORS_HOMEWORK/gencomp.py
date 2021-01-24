"""
Can you explain what gencomp is in the code below?

# EXAMPLE OUTPUT

4
5
"""

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
	print(item)

# ANSWER

"""
gencomp is a generator expression that is similar to list comprehension 
but it yield and it save a lot of memory. This is helpfull if don't want 
all the values to return
"""

# Or

# https://stackoverflow.com/questions/364802/how-exactly-does-a-generator-comprehension-work