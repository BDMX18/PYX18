'''
Filter positive numbers.
Given a list of integers (both positive and negative), return only the positive numbers.
'''

print(list(filter(lambda x: x>0, [-10, 0, 5, -3, 8, -22, 17])))