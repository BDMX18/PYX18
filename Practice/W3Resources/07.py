'''
7. Sum of Series n + (n-2) + (n-4) ... Using Recursion
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .

Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''

def sumOfSeries(num):
  if num == 0:
    return 0
  return num + sumOfSeries(num-2)

print(sumOfSeries(10))

# def sumOfSeries(num):
#   sum = 0
#   init = 0
#   while init != num:
#     sum += (num - init)
#     init += 2
#   return sum

# print(sumOfSeries(10))
