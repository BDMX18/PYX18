'''
User Profile with **kwargs

Problem: Implement profile(name, **kwargs) where kwargs can be age, location, etc. Return dictionary.

Input: profile("Alice", age=23, location="NY")

Output: {'name':'Alice','age':23,'location':'NY'}
'''

def profile(name, **kwargs):
  kwargs['name'] = name
  return kwargs

print(profile("Alice", age=23, location="NY"))