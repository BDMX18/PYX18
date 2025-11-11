'''
Q10. Custom Exception for Product Price Validation

Create a custom exception InvalidPriceError.
Define a class Product that raises this exception if the price is ≤ 0 during initialization.

Sample Data:

products = [("Pen", 10), ("Notebook", 0), ("Marker", -5)]
'''

products = [("Pen", 10), ("Notebook", 0), ("Marker", -5)]

class InvalidPriceError(Exception):
  def __init__(self, msg):
    self.msg = msg

for product, price in products:
  try:
    if price <= 0:
      raise InvalidPriceError('Price should be greater than 0')
  except InvalidPriceError as error:
    print(error)
  else:
    print(product, price)