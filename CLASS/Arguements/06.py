'''
Index Matcher:
Create a function that takes any number of inputs and returns a dictionary where keys are indexes and values are the arguments passed.
'''

def final_dict(*args):
  result_dict = dict()
  for ip in range(len(args)):
    result_dict[ip] = args[ip]
  return result_dict

def user_input():
  input_list = []
  while True:
    item = input('Enter An Item: ')
    if item != ' ':
      input_list.append(item)
    else:
      print(final_dict(*input_list))
      break

user_input()