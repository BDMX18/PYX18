'''
Order Summary (Advanced - Combination)

Write a function order_summary(customer, *items, **order_info) that:

Prints the customer’s name,

Lists all ordered items,

Displays any extra order info (like delivery_date, address, etc.).

Sample Data:

order_summary("Bibhu", "Pizza", "Coke", "Garlic Bread", delivery_date="03-Nov", address="Bhubaneswar")
order_summary("Ananya", "Burger", "Fries", payment_mode="UPI")
'''

def order_summary(name, *args, **kwargs):
  print('User Information: ')
  print('Customer Name: ', name)
  print('Orders:')
  for arg in args:
    print('\t', arg)
  for key in kwargs:
    print(f'{key}: {kwargs[key]}')
  return print('-'*20)

order_summary("Bibhu", "Pizza", "Coke", "Garlic Bread", delivery_date="03-Nov", address="Bhubaneswar")
order_summary("Ananya", "Burger", "Fries", payment_mode="UPI")