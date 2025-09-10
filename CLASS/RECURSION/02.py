# Factorial Of A Number:

def factorial(num):
  if num == 0:
    return 1
  return num*factorial(num-1)

num = int(input('Enter A Number: '))
print(f'Factorial Of {num}:', factorial(num))
