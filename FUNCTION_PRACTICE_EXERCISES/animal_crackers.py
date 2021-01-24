"""
ANIMAL CRACKERS: Write a function takes a two-word string 
and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

#######################
## SOLUTION BY KEVIN ##
#######################

def animal_crackers(text):

	text = text.split()
	return text[0][0] == text[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))