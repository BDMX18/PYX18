'''
a. Aggregation is the process of creating object of one class in another class. In a way we can say aggregation is the process where one class owns another class.
b. We'll be making use of aggregation to represent 'has-a' relationship.
c. Aggregation can be achieved by pointing to the reference or creating the object of the class inside the other class.
-> Examples of Has-A Relationship: 
    > Customer has a Address,
    > Restaurant has a Menu,
    > Car has a driver,
    > Team has a player,

** Aggregation doesn't ensure that we'll be able to fetch the private entities of the class that the parent owns. Herein classes share a logical relationship which doesn't give them the capacity to access private entities.
'''

class Customer:

  def __init__(self, name, gender, age, address):
    self.name = name
    self.gender = gender
    self.age = age
    self.address = address
    # Herein, name, age and gender are simple enitities and can be represented as it is while creating object for the Customer class.
    # Whereas, address in itself is a complex entity which is made of: city, pin, district state. So it can be represented as another class, that shares a relation with Customer class.

  def printAddress(self):
    print(f'City: {self.address.get_city()} \nPincode: {self.address.pincode} \nDistrict: {self.address.district} \nState: {self.address.state}')

  @staticmethod
  def edit():
    info = input()
    return info
  
  def edit_profile(self):
    print('Enter Updated Name: ', end='')
    new_name = self.edit()
    self.name = new_name
    print('Enter City To Update: ', end='')
    new_city = self.edit()
    print('Enter State To Update: ', end='')
    new_state = self.edit()
    print('Enter District To Update: ', end='')
    new_district = self.edit()
    print('Enter Pincode To Update: ', end='')
    new_pincode = self.edit()
    self.address.edit_address(new_city, new_state, new_district, new_pincode)
  
  def updated_profile(self):
    return self.name, self.printAddress()


class Address:

  def __init__(self, city, pincode, district, state):
    self.__city = city
    self.pincode = pincode
    self.district = district
    self.state = state
  
  # Getter Method
  def get_city(self):
    return self.__city
  
  def edit_address(self, new_city, new_pincode, new_district, new_state):
    self.__city = new_city
    self.pincode = new_pincode
    self.district = new_district
    self.state = new_state

A1 = Address('Berhampur', 760007, 'Ganjam', 'Odisha')

C1 = Customer('Bibhu Dutta Mahapatra', 'Male', 23, A1)

Customer.printAddress(C1)

C1.edit_profile()

C1.printAddress()

print('-'*50)
C1.updated_profile()

