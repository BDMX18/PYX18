'''
Filter users older than 18.
Given a list of dictionaries representing users (e.g. {'name': 'Alice', 'age': 25}), return only those users who are older than 18.
'''

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 19},
    {"name": "Daisy", "age": 15},
    {"name": "Eve", "age": 30}
]


def isEligible(element):
  if element['age'] > 18:
    return True
  return False

print(list(filter(isEligible, users)))

print(list(filter(lambda x: x['age'] > 18, users)))