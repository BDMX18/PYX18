# 01. Sum Items in List
# Write a Python program to sum all the items in a list.

list = eval(input('Enter A List: '))
sum = 0
for element in list:
  if(isinstance(element, int)):
    sum += element
print('Sum Of Elements: ', sum)