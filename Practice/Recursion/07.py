'''
Count Digits of a Number

Count how many digits are in a positive integer.
'''

# num = int(input())
# count = 0
# while num != 0:
#   num = num // 10
#   count += 1
# print(count)

def count(num):
  if num < 10:
    return 1
  return 1 + count(num//10)
print(count(12345))