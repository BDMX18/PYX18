'''
Filter Even Numbers:
Write a function that takes any number of integers and returns a list of even numbers.
'''

print(tuple(filter(lambda num: num if num%2 == 0 else False, (1, 2, 3, 4, 5, 6, 7, 8,9, 10))))

def evenNum(*args):
  evenList = []
  for num in args:
    if num%2 == 0:
      evenList.append(num)
  return evenList

def userInput():
  numList = []
  while True:
    num = int(input('Enter A Number: '))
    if num != 0:
      numList.append(num)
    else:
      print(evenNum(*numList))
      break

userInput()

