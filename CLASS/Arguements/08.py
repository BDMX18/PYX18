'''
Keyword Counter:
Create a function that returns the count of keyword arguments passed to it.
'''

def count(**kwargs):
  count = 0
  for key in kwargs:
    count += 1
  return count

def user_input():
  input_dict = {}
  while True:
    key = input('Enter Key: ')
    if key == 'CLOSE':
      break
    else:
      value = input('Enter Value: ')
      input_dict[key] = value
  print(count(**input_dict))

user_input()