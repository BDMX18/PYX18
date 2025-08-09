# Armstrong number are those numbers which are equal to the sum of the digits of the number each raised to the power of number of the digits in the number itself.

number = int(input('Enter A Number: '))
dummy = number
sum = 0
while dummy != 0:
  remainder = dummy % 10
  dummy //= 10
  sum += remainder ** len(str(number))
if(sum == number):
  print('Number Is Armstrong!')
else:
  print('Number Is Not Armstrong!')