'''
Add Corresponding Elements of Two Lists:
Use map() to add elements at the same position in two lists.
Example input: [1, 2, 3] and [4, 5, 6] → Output: [5, 7, 9]
'''
def sumElement(n, m):
  return n+m
print(list(map(sumElement, [1,2,3],[4,5,6])))

print(list(map(lambda n, m: n+m, [1,2,3],[4,5,6])))