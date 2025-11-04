'''
Q7. Describe a Person (Default + kwargs)

Write a function describe_person(name, country="India", **details) that prints the person’s name, country, and all additional keyword details.

describe_person("Bibhu", age=23, hobby="Coding")
describe_person("Lina", country="USA", profession="Designer", experience=3)
'''

def describe_person(name = 'No Name Avilable!', country = 'India', **kwargs):
  print('Name:', name)
  print('Country', country)
  for key in kwargs:
    print(f'{key}:', kwargs[key])
  return '-'*20

print(describe_person("Bibhu", age=23, hobby="Coding"))
print(describe_person("Lina", country="USA", profession="Designer", experience=3))