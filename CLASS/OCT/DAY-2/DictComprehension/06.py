'''
Advanced Level

Swap Keys and Values
Swap the keys and values in a dictionary.

Input: {"a":1, "b":2, "c":3}  
Output: {1:"a", 2:"b", 3:"c"}
'''

ip_dict = {"a":1, "b":2, "c":3}  

result = {k: v for v, k in ip_dict.items()}

print(result)