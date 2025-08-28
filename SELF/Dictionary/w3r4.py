'''
4. Check Key Existence in Dictionary
Write a Python script to check whether a given key already exists in a dictionary.
'''

dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = int(input('Enter The Key You Want To Search: '))
if key in dict:
  print('Yes')
else:
  print('No')