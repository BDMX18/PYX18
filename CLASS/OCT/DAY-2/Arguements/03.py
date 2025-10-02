'''
Flexible Greeting

Problem:
Write a function greet(*names, greeting="Hello") that takes any number of names and a default greeting, and returns a list of personalized greetings.

Sample Input:

greet("Alice", "Bob", "Charlie")


Expected Output:

["Hello Alice", "Hello Bob", "Hello Charlie"]


Sample Input 2:

greet("Alice", "Bob", greeting="Hi")


Expected Output 2:

["Hi Alice", "Hi Bob"]
'''

def greet(*names, greeting='Hello'):
  greeting_list = []
  for name in names:
    greeting_list.append(greeting+' '+name)
  return greeting_list

print(greet("Alice", "Bob", "Charlie", greeting='Hi'))