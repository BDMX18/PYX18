'''
Conditional Transformation
From a dict of numbers, double the even values and square the odd values.

Input: {"x":2, "y":3, "z":4}  
Output: {"x":4, "y":9, "z":8}
'''

ip_dict = {"x":2, "y":3, "z":4} 

result = {k: v*2 if v%2==0 else v**2 for k,v in ip_dict.items()}

print(result)