import re

pattern_1 = 'python'
pattern_2 = 'hello'
data = 'Hello, python is very powerful and it has lots of features'
match = re.match(pattern_2, data, re.IGNORECASE)
print(match)

# Regular Expression Object:

pattern = re.compile('hello')
print(pattern)
print(type(pattern))