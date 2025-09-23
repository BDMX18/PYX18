'''
Sum of All Numbers:
Write a function that accepts any number of numeric arguments and returns their total sum.
'''

def sumN(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

def userInput():
  numList = []
  while True:
    num = int(input('Enter A Number: '))
    if num != 0:
      numList.append(num)
    else:
      print('Sum', sumN(*numList))
      break

userInput()

