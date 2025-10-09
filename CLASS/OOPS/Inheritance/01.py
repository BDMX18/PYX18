'''
Scenario 1: The properties and functionalities of parent class are as it is in child class, along with that we're creating new functionality 'deposit()' in the child class.

Herein, we've two banks, Bank_V1 and Bank_V2:
-> Bank_V1 is parent to Bank_V2. so hence, Bank_V2 will be deriving all the properties and functionalities of Bank_V1. In Bank_V1, we've:
    a. Generic Properties: bank_name, bank_branch, bank_roi
    b. Specific Properties: cname, caccount, cbalance, __init__ [Constructor]
    c. Object Methods: customer_details(), withdraw()
    d. Class Methods: bank_details(), update_roi()
    e. Static Method: get_amount()

-> Bank_V2, will be deriving all the above properties, along with that it supports deposit as well, so hence we've a separate object method in Bank_V2. In Bank_V2, we've:
    a. Generic Properties: bank_name, bank_branch, bank_roi
    b. Specific Properties: cname, caccount, cbalance, 
    c. Object Methods: customer_details(), withdraw(), __init__ [Constructor], deposit()
    d. Class Methods: bank_details(), update_roi()
    e. Static Method: get_amount()

-> Herein, objects [Customers] of Bank_V1 will be able to withdraw and view customer details only, whereas the objects of Bank_V2 will be able to view customer details, withdraw as well as deposit.

'''

# Parent Class:

class Bank_V1:

  bank_name = 'SBI'
  bank_branch = 'BLR'
  bank_roi = 5

  def __init__(self, cn, ca, cb):
    self.cname = cn
    self.caccount = ca
    self.cbalance = cb

  @staticmethod
  def get_amount():
    amount = int(input())
    return amount

  @classmethod
  def bank_details(cls):
    print('Bank Details')
    print('Bank Name:', cls.bank_name)
    print('Bank Branch:', cls.bank_branch)
    print('Bank ROI:', cls.bank_roi)
  
  @classmethod
  def update_roi(cls):
    print('Enter New ROI Value: ')
    nroi = cls.get_amount
    cls.bank_roi = nroi
    print('ROI Updated')

  def customer_details(self):
    print('Customer Details')
    print('Customer Name:', self.cname)
    print('Customer Account:', self.caccount)
    print('Customer Balance:', self.cbalance)

  def withdraw(self):
    print('Enter The Amount To Withdraw: ')
    amount = self.get_amount()
    if amount <= self.cbalance:
      self.cbalance -= amount
      print('Withdrawl Successfull!')
    else:
      print('Insufficient Balance!')
    print('Account Balance', self.cbalance)

# Derived Class:

class  Bank_V2(Bank_V1):

  def deposit(self):
    print('Enter The Amount To Deposit: ')
    amount = self.get_amount()
    self.cbalance += amount
    print('Amount Deposited Successfully!')



# Driver Code:

Abhinav = Bank_V1('Abhinav A', 1001, 10000)

Abhinav.customer_details()
Bank_V1.withdraw(Abhinav)

# This is not possible since, Bank_V1 doesn't have any deposit() method.
#           AttributeError: 'Bank_V1' object has no attribute 'deposit'
Abhinav.deposit()

Arush = Bank_V2('Arush Sabat', 1101, 12000)
Arush.bank_details()
Arush.customer_details()
Arush.withdraw()

# Herein, since Arush is an object of Bank_V2, which has deposit() method, so hence it's being accessed by the object and modification can be done successfully without any issue.
Arush.deposit()





