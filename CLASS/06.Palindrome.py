# Approach 01: Using While Loop:

number = int(input('Enter A Number: '))
dummy = number
reverse = 0
while dummy != 0:
  remainder = dummy % 10
  dummy //= 10
  reverse = reverse * 10 + remainder
if(number == reverse):
  print('Number Is Palindrome!')
else:
  print('Number Is Not Palindrome!')

# Approach 02: Using For Loop and Built-in Method:

number = int(input('Enter A Number: '))
reverse = 0
dummy = number
for i in range(len(str(number))):
  remainder = dummy % 10
  dummy //= 10
  reverse = reverse * 10 + remainder
if(number == reverse):
  print('Number Is Palindromee!')
else:
  print('Number Is Not Palinddrome!')
