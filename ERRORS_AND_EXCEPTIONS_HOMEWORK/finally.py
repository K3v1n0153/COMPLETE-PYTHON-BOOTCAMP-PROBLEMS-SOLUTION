"""
Handle the exception thrown by the code below by using 
try and except blocks. Then use a finally block to print 
'All Done.'

x = 5
y = 0
z = x/y
"""

#######################
## SOLUTION BY KEVIN ##
#######################

try:
	x = 5
	y = 0
	z = x/y
except:
	print('An error occured!')
finally:
	print('All Done.')