'''
Reverse keys and values in a dictionary {1: 'a', 2: 'b', 3: 'c'} using dictionary comprehension.
'''

ip_dict = {1: 'a', 2: 'b', 3: 'c'}
op_dict = {v: k for k,v in ip_dict.items()}
print(op_dict)