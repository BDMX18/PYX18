'''
Question 10:
Given a dictionary of products and prices, apply a 10% discount only to products costing more than 100 and create a new dictionary with updated prices.

products = {"Laptop": 1200, "Mouse": 50, "Keyboard": 150, "USB": 25}
'''

products = {"Laptop": 1200, "Mouse": 50, "Keyboard": 150, "USB": 25}

op_dict = {k:v*.90 for k,v in products.items() if v > 100}

print(op_dict)

