'''
You have a list of dictionaries, each containing a key 'price'. Use map() to extract all the prices into a new list.
'''

products = [
    {'name': 'Laptop', 'price': 50000},
    {'name': 'Mouse', 'price': 700},
    {'name': 'Keyboard', 'price': 1500},
    {'name': 'Monitor', 'price': 12000}
]

price_list = list(map(lambda item: item['price'], products))

print(price_list)