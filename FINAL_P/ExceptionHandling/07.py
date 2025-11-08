'''
Q2. NegativeBalanceError

Problem Statement:
Define a custom exception NegativeBalanceError that is raised if a bank account balance goes below zero.
Write a program to simulate deposit and withdrawal operations, handling this exception gracefully.

Sample Input:

Initial balance: 1000  
Withdraw amount: 1200


Expected Output:

Error: Insufficient funds. Balance cannot go negative.
'''

class NegativeBalanceError(BaseException):
  def __init__(self, msg):
    self.msg = msg

class InvalidPinError(BaseException):
  def __init__(self, msg):
    self.msg = msg

class Bank:

  bank_name = 'SBI'
  bank_branch = 'Berhampur'
  bank_ifsc = 1136

  def __init__(self, name, accno, balance, pin):
    self.name = name
    self.accno = accno
    self.balance = balance
    self.pin = pin

  @staticmethod
  def intValue():
    int_val = int(input())
    return int_val
  
  def deposit(self):
    print('Enter The Amount To Deposit: ')
    amount = self.intValue()
    self.balance += amount
    print('Amount Successfully Deposited!')
  
  def checkBalance(self):
    print('Enter PIN to check balance: ')
    check_pin = self.intValue()
    if self.pin == check_pin:
      print('Account Balance:', self.balance)
    else:
      raise InvalidPinError('Incorrect Pin, Try Again!')
  
  def withdraw(self):
    print('Enter PIN to withdraw money:')
    pin_check = int(input())
    if pin_check == self.pin:
      print('Enter The Amount To Withdraw: ')
      amount = self.intValue()
      if amount <= self.balance:
        self.balance -= amount
      else:
        try:
          raise NegativeBalanceError('Amount More Then Current Account Balance')
        except NegativeBalanceError as NBE:
          print(NBE)
      print('Account Balance:', self.balance)
    else:
      try:
        raise InvalidPinError('Incorrect Pin, Try Again!')
      except InvalidPinError as IPE:
        print(IPE)

A = Bank('AB', 123, 10000, 1122)

# A.deposit()
A.withdraw()