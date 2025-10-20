'''
Filter a dictionary { 'a': 10, 'b': 5, 'c': 20 } to keep only items with value > 10 using dictionary comprehension.
'''

ip_dict = { 'a': 10, 'b': 5, 'c': 20 }
op_dict = {k:v for k,v in ip_dict.items() if v>10}
print(op_dict)