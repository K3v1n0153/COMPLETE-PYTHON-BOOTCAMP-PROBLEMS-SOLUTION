"""
For this challenge, create a bank account 
class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test 
to make sure the account can't be overdrawn.

# EXAMPLE OUTPUT

acct1 = Account('Jose',100)

# 2. Print the object
print(acct1) --> Account owner: Jose
				 Account Balance: $100

# 3. Show the account owner attribute
acct1.owner --> 'Jose'

# 4. Show the account balance attribute
acct1.balance --> 100

# 5. Make a series of deposits and withdrawals

acct1.deposit(50) --> Deposit Accepted
acct1.withdraw(75) --> Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) --> Funds Unavailable!
"""

class Account:

	def __init__(self, owner, balance=0):

		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner: {self.owner}\nAccount Balance: ${self.balance}'

	def deposit(self, dp_amount):

		self.balance += dp_amount
		print('Deposit Accepted')

	def withdraw(self, wd_amount):

		if wd_amount > self.balance:
			print('Funds Unavailable!')
		else:
			self.balance -= wd_amount
			print('Withdrawal Accepted')

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)