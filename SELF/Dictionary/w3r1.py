'''
1. Sort Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
'''

dict = eval(input('Enter Dictionary Elements: '))
print(dict)
value_list = []
value = dict.values()
for element in value:
  value_list.append(element)
print(value_list)
print('Ascending Order: ', sorted(value_list))
print('Descending Order: ', sorted(value_list, reverse=True))