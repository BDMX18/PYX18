'''
Filter floating-point numbers.
Given a list of mixed data types (ints, floats, strings, etc.), return only the floating-point numbers.
'''

items = [1, 2.5, "hello", 3.14, 7, 0.99, "42", 4.0]

print(list(filter(lambda x: isinstance(x, float), items)))