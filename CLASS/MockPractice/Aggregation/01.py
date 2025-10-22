'''
Question 1: Customer and Address

Scenario:
A Customer has an Address (city, state, pincode). The address can exist independently and can be assigned to multiple customers.

Guideline:
👉 Create the Address object in main space, and pass it to Customer — classic aggregation.

Question:
Write a Python program using two classes — Customer and Address.

The Customer class should store name, gender, and address object.

Create two customers sharing the same address and display their details.
'''

class Customer:

  def __init__(self, cname, cgender, caddress):
    self.cname = cname
    self.cgender = cgender
    self.caddress = caddress

  def display(self):
    print('\nCustomer Details: ')
    print('Customer Name:', self.cname)
    print('Customer Gender:', self.cgender)
    print('Customer Address:')
    print('City:', self.caddress.city)
    print('State:', self.caddress.state)
    print('Pincode:', self.caddress.pincode)


class Address:

  def __init__(self, city, state, pincode):
    self.city = city
    self.state = state
    self.pincode = pincode

A1 = Address('Brahmapur', 'Odisha', 760007)

C1 = Customer('Ram', 'Male', A1)
C2 = Customer('Sita', 'Female', A1)

C1.display()
C2.display()