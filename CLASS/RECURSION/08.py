# Write a recursive function to find the sum of all elements in a list.

def sum(L):
  if len(L) == 0:
    return 0
  return L[0] + sum(L[1:])

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))