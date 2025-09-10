# Count the number of digits in a number using recursion.

def count(num):
  if num < 10:
    return 1
  return 1 + count(num//10)

print(count(556))