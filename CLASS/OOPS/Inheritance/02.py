'''
Scenario 2: The properies and functuionalities of parent class will be as it is in child class, but apart from that we'll be adding functionalities and properties and modify the existing functionalities and properties of the parent class in the child class.

Herein, we've two banks, Bank_V1 and Bank_V3:
-> Bank_V1 is parent to Bank_V3. so hence, Bank_V3 will be deriving all the properties and functionalities of Bank_V1. In Bank_V1, we've:
    a. Generic Properties: bank_name, bank_branch, bank_roi
    b. Specific Properties: cname, caccount, cbalance, __init__ [Constructor]
    c. Object Methods: customer_details(), withdraw()
    d. Class Methods: bank_details(), update_roi()
    e. Static Method: get_amount()

-> Bank_V3, will be deriving all the above properties and functionalities, along with that it supports deposit apart from that it'll have extra generic properties and specific properties as well, so hence we've a separate object method in Bank_V3. In Bank_V3, we've:
    a. Generic Properties: bank_name, bank_branch, bank_roi, bank_ifsc
    b. Specific Properties: cname, caccount, cbalance, cpin, cmobile
    c. Object Methods: customer_details(), withdraw(), __init__ [Constructor], deposit()
    d. Class Methods: bank_details(), update_roi()
    e. Static Method: get_amount()

-> Herein, we're having extra generic properties and are also modifying the generic properties of the parent class in child class:
    During inheritance, if the values of the parent class properties are getting modified in child class, it's called Property Overriding.

-> Similarly, we're also making changes to the methods that are derived from the parent class in the child class
    -> During inheritance, if the implementation of the parent class methods are getting modified in child class, it's called Method Overriding.
    -> To achieve method overriding, we'll redefining the parent class methods in the child class with additional implementation.
    -> The method derived from the parent class will have the same name in the child class.
    ** Inheritance is mandatory for method overriding.

-> If method overring and inheritance will be implemented together, then in such a case there'll be code redundancy.

  a. In order to avoid this code redundancy, we've to perform inheritance and method overrinding along with chaining process.

      -> Calling a method or constructor of another class in current class method or constructor.

      We've two types of chaining:

        i. Constructor Chaining: The process of calling a constructor of another class in current class constructor is called constructor chaining.

        ii. Method Chaining: The process of calling a method of another class in current class methood is called method chaining.

  b. We can perform chaining by two ways:

    i. By using super() function:
      -> super() function is used only in case of inheritance,
      -> By using super() function we can call:
          -> calling the constructor of parent class in child class constructor in constructor chaining.
          ::              super().__init__(Arguments)

          -> calling the method of parent class in child class method in method chaining.
          ::              super().MethodName(Arguements)
      -> For using super() function, inheritance is mandatory

    ii. By using classname:
      -> We can make use of classname in case of inheritance as well as it can be used when there's no inheritance.
      -> By using classname we can call:
          -> calling the constructor of parent class in child class constructor in constructor chaining.
          ::              ClassName.__init__(self, Arguments)

          -> calling the method of parent class in child class method in method chaining.
          ::              super().MethodName(Arguements)
      -> Here, inheritance is not mandatory.

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

class Bank_V3(Bank_V1):

  bank_branch = 'Brahmapur'
  bank_ifsc = 1234
  
  def __init__(self, cn, ca, cb, cp, cm):
    super().__init__(cn, ca, cb)
    self.cpin = cp
    self.cmobile = cm

  def customer_details(self):
    super().customer_details()
    print('Customer Mobile:', self.cmobile)
  
  def withdraw(self):
    print('Enter PIN To Withdraw Money: ')
    pin = self.get_amount()
    if pin == self.cpin:
      super().withdraw()
    else:
      print('Invalid PIN!')
  
  def deposit(self):
    print('Enter The Amount To Deposit: ')
    amount = self.get_amount()
    self.cbalance += amount
    print('Amount Successfully Deposited!')
  
  # @classmethod
  # def bank_details(cls):
  #   super().bank_details()
  #   print('Bank IFSC:', cls.bank_ifsc)

  @classmethod
  def bank_details(cls):
    Bank_V1.bank_details()
    print('Bank IFSC:', cls.bank_ifsc)

  
Aarav =  Bank_V3('Aarav K', 1100, 10000, 1123, 1987262093)

# Aarav.customer_details()
# Aarav.withdraw()
Aarav.bank_details()