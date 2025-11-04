'''
Given a dictionary of items and prices, create a new dictionary applying a 10% discount to prices greater than 100.

prices = {'apple': 120, 'banana': 80, 'mango': 150}
# Expected Output: {'apple': 108.0, 'banana': 80, 'mango': 135.0}
'''

prices = {'apple': 120, 'banana': 80, 'mango': 150}

discount = {key:(value-(value*.10)) for key, value in prices.items()}

print(discount)