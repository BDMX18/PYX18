'''
Q10. Product Price Validation

Problem:
Create a custom exception class InvalidPriceError.
Write a class Product with attributes name and price.
Raise InvalidPriceError if the price is less than or equal to zero.

Sample Data:

item = Product("Laptop", -500)


Expected Output:

InvalidPriceError: Price must be greater than zero.
'''

class InvalidPriceError(Exception):
  def __init__(self, message):
    self.message = message

class Product:
  
  def __init__(self, name, price):
    if price <= 0:
      raise InvalidPriceError('Price Must Be Greater Than Zero!')
    self.name = name
    self.price = price

  def product_details(self):
    print('Product Name:', self.name, 'Product Price:', self.price)

try:
    name = input('Enter The Name Of The Product You Want To Add: ')
    price = int(input('Enter The Price Of The Product You Want To Add: '))
    name = Product(name, price)
    print('Product Added Successfully!')
    Product.product_details(name)
except InvalidPriceError as error:
  print(f'Error: {error}')