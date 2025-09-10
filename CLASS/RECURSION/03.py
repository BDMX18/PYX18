# Sum of individual digits of a number

def sum(num):
  if num == 0:
    return 0
  return num % 10 + sum(num//10)
print(sum(123)) 