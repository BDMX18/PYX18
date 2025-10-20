'''
Generate all prime numbers from 1 to 50 using a list comprehension.
'''

for num in range(1, 51):
  if num > 2:
    for i in range(2, num//2+1):
      if num%i==0:
        break
    else:
      print(num)

