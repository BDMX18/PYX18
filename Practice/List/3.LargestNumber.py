# 3. Get Largest Number in List
# Write a Python program to get the largest number from a list.

list = eval(input('Enter A List: '))
largest = list[0]
for element in list:
  if element > largest:
    largest  = element
print('Largest Element In The List: ', largest)