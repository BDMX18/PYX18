class Bank:

  # Defining Generic Properties:
  bank_name = 'SBI'
  bank_branch = 'BLR'
  bank_roi = 5

  # Defining Specific Properties: 
  def __init__(self, cn, an, ba):
    self.cname = cn
    self.account = an
    self.balance = ba

  # Accessing Specific Properties:
  def customer_details(self):
    print('Customer Name: ', self.cname)
    print('Customer Account Number: ', self.account)
    print('Customer Balance: ', self.balance)
  
  # Modifying Generic Properties:
  def withdraw(self):
    amount = int(input('Enter The Amount To Withdraw: '))
    if amount <= self.balance:
      self.balance -= amount
      print('Amount Withdrawn Successfully!')
    else:
      print('Insufficient Funds')
    print('Available Balance: ', self.balance)
  
  def deposit(self):
    amount = int(input('Enter The Amount To Deposit: '))  
    self.balance += amount
    print(f'{amount} Deposited Successfully To {self.account}')

# Creating object:
bibhu = Bank('Bibhu Dutta Mahapatra', 123, 1000)
ram = Bank('Ram Prasad Majhi', 456, 3000)

'''
Constructor (__init__)

bibhu = Bank('Bibhu Dutta Mahapatra', 123, 1000)

Herein, as we create the object 'bibhu' and call the class.
  -> The object at first searches for the constructor,
  -> Since we've the constructor, herein the memory reference of the object 'bibhu' is passed onto __init__, along with the values that the constructor needs.

'''

#-------------------------------------------------------------------Generic Properties---------------------------------------------------------------------------------------#

# Scenario 01: Accessing generic properties by using class
print(Bank.bank_name)
print(Bank.bank_branch)
print(Bank.bank_roi)

# Scenario 02: Accessing generic properties by using object
print(bibhu.bank_name)
print(bibhu.bank_branch)
print(bibhu.bank_roi)

# Scenario 03: Modifying generic properties by using Class: Generic properties modified using class will be reflected in all the objects.
Bank.bank_branch = 'BAM'
print(Bank.bank_branch)
print(ram.bank_branch)

# Scenario 04: Modifying generic properties by using Object: Generic properties modified using object, is subjected to that specific object only.
ram.bank_roi = 2
print(Bank.bank_roi)
print(bibhu.bank_roi)
print(ram.bank_roi)

# Scenario 05: Creating generic properties using class
# Bank.bank_ifsc = 1234
# print(Bank.bank_ifsc)
# print(bibhu.bank_ifsc)
# print(ram.bank_ifsc)

# Scenario 6: Creating generic propeties by using object: Generic properties can't be defined by an object.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# For defining specific properties we'll using __init__ method. This method is used for constructing an object so hence it's also referred to as constructor.

'''
> Herein, our constructor is expecting three values. We've pass these three values when we create an object and call the class.
> As we know when we create an object, It'll search first for an constructor, so hence if we'll not pass the required values for the constructor then in that case, we'll get TypeError.
> The constructor will take one mandatory arguement, that is self. This self will hold the memory address of the invoked object dictionary. 
(All the object methods will take one mandatory arguement that is self.)
'''

#---------------------------------------------------------------------- Calling Object Method -----------------------------------------------------------------------------

# Scenario 1: Directly called by object: If we're calling an object method like this, then the memory address is implicitly passed to the customer_details() method.
bibhu.customer_details()
ram.withdraw()
bibhu.deposit()

# Scenario 2: Indirectly called using class: If we're calling an object method using class then in that case, we've specify explicitly the object while calling so hence the memory address can be passed to the object method. Like:
Bank.customer_details(ram) # Memory reference of instance 'ram'.
Bank.withdraw(bibhu)
Bank.deposit(ram)

'''
Bank.withdraw(bibhu)

Herein, 
  -> withdraw() is an object method, it'll work for the object but it belongs to the class.
  -> In-order to use withdraw(), it has to be called using object.
  -> But since it belongs to the class it can be called using the class as well (Indirectly).
  -> But if we're calling it using class we've to pass the object reference.
  -> The class will further pass the object reference given to the withdraw() method.
  -> withdraw() method will use the object reference to perform the defined operations.

'''
