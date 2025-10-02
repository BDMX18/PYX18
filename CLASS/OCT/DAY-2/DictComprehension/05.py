'''
Uppercase Keys
Convert all keys in a dict to uppercase.

Input: {"a":1, "b":2, "c":3}  
Output: {"A":1, "B":2, "C":3}
'''

ip_dict = {"a":1, "b":2, "c":3}  
result = {k.upper():v for k,v in ip_dict.items()}
print(result)