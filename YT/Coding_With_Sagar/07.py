'''
Print the first 5 multiples of 3
E.O: 3 6 9 12 15
'''

target = int(input('Enter The Target: '))
count = 0
num = 1
while count != target:
  if(num%3 == 0):
    print(num, end=' ')
    count += 1
  num += 1