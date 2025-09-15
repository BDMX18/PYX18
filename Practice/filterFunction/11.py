'''
Question:
Given a dictionary of item prices, return a new dictionary with items priced above 50.
'''

prices = {
    "apple": 30,
    "banana": 60,
    "cherry": 75,
    "date": 45,
    "fig": 90
}

print(dict(filter(lambda item: item[1] > 50, prices.items())))