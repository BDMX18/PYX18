'''
Filter by Type
From a dict, keep only the entries where values are integers.

Input: {"a":10, "b":"hi", "c":20.5, "d":30}  
Output: {"a":10, "d":30}
'''

ip_dict = {"a":10, "b":"hi", "c":20.5, "d":30} 

result = {k:v for k, v in ip_dict.items() if isinstance(v, int)}

print(result)