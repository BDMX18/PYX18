'''
Custom Multiplier:
Write a function that takes any number of arguments and returns their product.
'''

def product(*args):
  product = 1
  for num in args:
    product *= num
  return product

def userInput():
  numList = []
  while True:
    num = int(input('Enter A Number: '))
    if num != 0:
      numList.append(num)
    else:
      print('Product is: ', product(*numList))
      break

userInput()