'''
String Concatenator:
Write a function that accepts any number of string arguments and returns a single concatenated string with spaces in between.
'''

def string_generator(*args):
  final_string = ''
  for string in args: 
    final_string += string + ' '
  return final_string

def userInput():
  string_list = []
  while True:
    string = input('Enter A String: ')
    if (string != ' '):
      string_list.append(string)
    else:
      print(string_generator(*string_list))
      break

userInput()