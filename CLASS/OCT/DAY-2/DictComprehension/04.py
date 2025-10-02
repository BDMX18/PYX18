'''
Filter Strings by Length
From a dict of {name: age}, keep only names with length > 3.

Input: {"Al":25, "John":30, "Eve":22}  
Output: {"John":30}
'''

profile = {"Al":25, "John":30, "Eve":22} 

result = {name: age for name, age in profile.items() if len(name) > 3}

print(result)