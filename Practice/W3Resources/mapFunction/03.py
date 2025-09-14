'''
3. Listify Strings Map: Write a Python program to listify the list of given strings individually using Python map.

Original list: 
['Red', 'Blue', 'Black', 'White', 'Pink']

After listify the list of strings are:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
'''

print(list(map(list, ['Red', 'Blue', 'Black', 'White', 'Pink'])))