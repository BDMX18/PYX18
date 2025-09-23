'''
Check Pronic Number in Python (5 Programs)
A pronic number is a special number made by multiplying two consecutive integers, like 6 (2×3) or 20 (4×5). These numbers are also called oblong numbers and are fun to work with in programming.
'''
# Approach 1: Using For Loop:
def isPronic(num):
  for p in range(0, num+1):
    if((p)*(p+1)) == num:
      return True
  return False

num = int(input('Enter A Number: '))
if(isPronic(num)):
  print('Pronic Number')
else:
  print('Not Pronic Number')

# Approach 02: Using While Loop:

def isPronic(num):
  init = 0
  while init * (init+1) <= num:
    if(init * (init+1)) == num:
      return True
    init += 1
  return False
    
num = int(input('Enter A Number: '))
if(isPronic(num)):
  print('Pronic Number')
else:
  print('Not Pronic Number')