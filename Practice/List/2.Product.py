# 2. Multiply Items in List
# Write a Python program to multiply all the items in a list.

list = eval(input('Enter A List: '))
product = 1
for element in list:
  if(isinstance(element, int)):
    product *= element
print('Product Of Elements: ', product)