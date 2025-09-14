# Print hello world for five times using recursion.
# Write a function that takes in a number and prints it. Print first 5 numbers: 1 2 3 4 5
import sys

# We can set the limit of recursion as per our requirement.
sys.setrecursionlimit(10)

# We can view the recursion limit that we've set here: 
# print(sys.getrecursionlimit())




def sumNum(num):
  if(num > num+5):
    return
  print(num, end='')
  sumNum(num+1)

sumNum(5)