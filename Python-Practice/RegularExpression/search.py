import re

pattern = 'python'
data = 'python is very powerful and python has lots of features.'
match = re.search(pattern, data)
print(match)
print(type(match))

if match:
  print('found')
else:
  print('not found')

# Using Flags:
print()
print('-'*10+'IGNORECASE'+'-'*10+' Using Ignore Case!')
pattern = 'PYTHON'
data = 'python is very powerful and it has lots of features.'
match = re.search(pattern, data, re.IGNORECASE)
print(match)
print(type(match))




