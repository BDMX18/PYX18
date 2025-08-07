# 3. Get smallest Number in List
# Write a Python program to get the smallest number from a list.

list = eval(input('Enter A List: '))
smallest = list[0]
for element in list:
  if element < smallest:
    smallest  = element
print('Smallest Element In The List: ', smallest)