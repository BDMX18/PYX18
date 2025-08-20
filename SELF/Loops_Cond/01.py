# 1. Divisible by 7 and Multiples of 5
# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
for num in range(ll, ul+1):
  if(num % 7 == 0 and num % 5 == 0):
    print(num)
