# Disarium Number: A number is called disarium if sum of its digits powered with thier respective positions equual to the number itself.


# Approach 01: Using Built-in Method: 

number = int(input('Enter A Number: '))
dummy = number
sum = 0
while dummy > 0:
  remainder = dummy % 10
  sum += remainder ** len(str(dummy))
  dummy = dummy // 10
if(sum == number):
  print('Number Is Disarium!')
else:
  print('Number Is Not Disarium!')

# Approach 02: Without using Built-in method:

number = int(input('Enter A Number: '))
dummy1 = number
dummy2 = number
length = 0
sum = 0
while dummy1 > 0:
  dummy1 //= 10
  length += 1
print(length)
while dummy2 > 0:
  remainder = dummy2 % 10
  sum += remainder ** length
  dummy2 //= 10
  length -= 1
if(sum == number):
  print('Number Is Disarium!')
else:
  print('Number Is Not Disarium!')

