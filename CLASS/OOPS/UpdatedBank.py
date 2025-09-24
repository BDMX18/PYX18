class Bank:
  bank_name = 'SBI'
  bank_branch = 'BLR'
  bank_roi = 5

  # Constructor ||  Also a object method, for defining specific properties for each and every individual object.
  def __init__(self, cn, an, bb):
    self.cname = cn
    self.accountno = an
    self.balance = bb

  # Object method to display the customer details, for each and every object of the class.
  def customerDetails(self):
    print('Account Details')
    print(f'Customer Name: {self.cname}')
    print(f'Customer Account Number: {self.accountno}')
    print(f'Customer Account Balance: {self.balance}')

  # Static method, This method will help providing the values that the user will pass to perform operations with object methods (withdraw, deposit) and class method (updateROI). This method won't take any arguement to hold address of any object or class.
  @staticmethod
  def getInputFromUser():
    value = int(input())
    return value
    
  # Object Method: withdraw, This method will allow the user to withdraw money from the account. Since it'll be working with specific properties so hence it's a object method. 'self' is responsible to hold invoked instance adddress
  def withdraw(self):
    print('Enter The Amount To Withdraw: ')
    amount = self.getInputFromUser()
    if(amount <= self.balance):
      self.balance -= amount
      print('Amount Withdrawl Successful!')
    else:
      print('Insufficiant Balance!')
    print('Available Balance: ', self.balance)
  
  # Object Method: deposit, This will allow the user to deposit money into its account.
  def deposit(self):
    print('Enter The Amount To Deposit: ')
    amount = self.getInputFromUser()
    self.balance += amount
    print('Amount Deposited Successfully!')
  
  # Class method, This method will allow the class even the object, to modify the generic properties of the class. As this method will be working with generic properties defined in a class, so hence it's a class method. This method will take one mandatory arguement 'cls', responsible to hold the class memeory address.
  @classmethod
  def updateROI(cls):
    print('Enter The ROI Value To Update: ')
    amount = cls.getInputFromUser()
    cls.bank_roi = amount
    print('Bank ROI Updated!')
  
# Now wwe'll be creating instances of the class 'Bank':
manasa = Bank('Manasa A', 12345, 50000)
vijaya = Bank('Vijaya S', 57891, 20000)

#                                     Different Scenarios of accessing generic properties:

# Scenario 1: Using class
print('Accessing Generic Properties Using Class:')
print(Bank.bank_name, Bank.bank_branch, Bank.bank_roi, end='\n\n')

# Scenario 2: Using Object:
print('Accessing Generic Properties Using Object: ')
print(manasa.bank_name, manasa.bank_branch, manasa.bank_roi)
print(vijaya.bank_name, vijaya.bank_branch, vijaya.bank_roi, end='\n\n') 

# Scenario 3: Modifying generic properties using class: Changes will be reflected everywhere. (in class and objects as well)
print('Modifying Generic Properties Using Class: ')
Bank.bank_roi = 3
print(Bank.bank_roi, manasa.bank_roi, vijaya.bank_roi, end='\n\n')

# Scenario 4: Modifying generic properties using obejct: Changes will be specific to that particular object.
print('Modifying Generic Properties Using Object: ')
manasa.bank_roi = 7
print(manasa.bank_roi, Bank.bank_roi, vijaya.bank_roi, end='\n\n')

# Scenario 5: Creating generic properties using class, (New generic properties will be visible everywhere)
print('Creating New Generic Property Using Class: ')
Bank.bank_mobile = 1234567890
print(Bank.bank_mobile, manasa.bank_mobile, vijaya.bank_mobile, end='\n\n')

# Scenario 6: Creating generic properties using object. This scenario is not practically possible since a object cannot access generic properties.
print('Practically Not Possible!', end='\n\n')

#                                    Different Scenarios of accessing object methods

# Scenario 1: By object directly

print(manasa.customerDetails(), end='\n\n')

# Scenario 2: By class indirectly, using object reference

print(Bank.customerDetails(vijaya), end='\n\n')

# Making use of class method:

# Scenario 1: By class directly,
print('Generic Properties Modified Using Class Method will make changes everywhere:')
Bank.updateROI()
print('Updated ROI: ', Bank.bank_roi, manasa.bank_roi, vijaya.bank_roi, end='\n\n')

# Scenario 2: By using object:
print('Generic Properties Modified Using Class Method via object will make changes everywhere:')
manasa.updateROI()
print('Updated ROI: ', Bank.bank_roi, manasa.bank_roi, vijaya.bank_roi, end='\n\n')

# The static method is being called by the object methods as well as class method whenever we perform any kind of updating operation using the methods in the class.
  