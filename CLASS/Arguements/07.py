'''
User Profile Creator:
Write a function that accepts any number of keyword arguments and returns a user profile as a dictionary.
'''

def userProfile(**kwargs):
  print('User Profile Details: ')
  for key in kwargs:
    print(key +'='+ kwargs[key])
  

def userInput():
  input_dict = dict()
  while True:
    key = input('Enter The Key (Enter \'Close\' To Close): ')
    if key == 'Close':
      break
    else:
      value = input('Enter The Value: ')
      input_dict[key] = value
  userProfile(**input_dict)

userInput()