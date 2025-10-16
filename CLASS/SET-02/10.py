'''
Remove a specific element from a list without using remove()

Problem:
Given a list and a value, remove all occurrences of that value without using the built-in remove() function.

Example:

Input → lst = [1, 2, 3, 2, 4, 2, 5], val = 2

Output → [1, 3, 4, 5]
'''

def remove_duplicate(lst, num):
  original = []
  for element in lst:
    if element != num:
      original.append(element)
  return original


lst = [1, 2, 3, 2, 4, 2, 5]
val = 2

print(remove_duplicate(lst, val))