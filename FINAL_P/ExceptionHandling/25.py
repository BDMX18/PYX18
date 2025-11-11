'''
Q7. Banking System Simulation

Create a custom exception InsufficientFundsError.
Write a class BankAccount with deposit() and withdraw() methods.
Raise the custom exception if withdrawal amount > balance.

Sample Data:

initial_balance = 1000
transactions = [('deposit', 500), ('withdraw', 300), ('withdraw', 1500)]
'''

initial_balance = 1000
transactions = [('deposit', 500), ('withdraw', 300), ('withdraw', 1500)]

class InsufficientFundsError(Exception):
  def __init__(self, msg):
    self.msg = msg

class BankAccount:

  def __init__(self, balance):
    self.balance = balance
  
  @staticmethod
  def getAmount():
    amount = int(input())
    return amount
  
  def withdraw(self):
    print('Enter The Amount To Withdraw: ')
    amount = self.getAmount()
    if amount > self.balance:
      raise InsufficientFundsError('Amount Shounldn\'t Be More Than Balance!')
    else:
      self.balance -= amount
      print('Amount Withdrawn Succesfully!')
    print('Available Balance:', self.balance)

  def deposit(self):
    print('Enter The Amount To Deposit: ')
    amount = self.getAmount()
    self.balance += amount
    print('Amount Deposited Successfully!')

Customer = BankAccount(initial_balance)

Customer.deposit()
try:
  Customer.withdraw()
except InsufficientFundsError as error:
  print(error)
try:
  Customer.withdraw()
except InsufficientFundsError as error:
  print(error)
