'''
Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
  add_tags('i', 'Python') -> '<i>Python</i>'
  add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>
'''

def tag(stag, string):
  print(f'<{stag}> {string} <{stag}>')

string = input('Enter The String: ')
stag = input('Enter The HTML Tag To Add: ')
tag(stag, string)