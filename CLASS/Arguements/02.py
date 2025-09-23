'''
Maximum Finder:
Create a function that finds and returns the maximum value from a variable number of numeric arguments.
'''

def maximum(*args):
  largest = args[0]
  for num in args:
    if num > largest:
      largest = num
  return largest

def userInput():
  numList = []
  while True:
    num = int(input('Enter A Number: '))
    if num != 0:
      numList.append(num)
    else:
      print('Maximum Number: ', maximum(*numList))
      break

userInput()
