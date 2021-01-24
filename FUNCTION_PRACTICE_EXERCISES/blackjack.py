"""
BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, return 
their sum. If their sum exceeds 21 and there's an 
eleven, reduce the total sum by 10. Finally, if the 
sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def blackjack(a, b, c):

	Sum = sum((a,b,c))

	if Sum <= 21:
		return Sum
	elif Sum > 21 and 11 in [a,b,c]:
		return Sum-10
	else:
		return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))