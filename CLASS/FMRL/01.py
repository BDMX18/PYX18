data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "David", "age": 28, "salary": 40000},
    {"name": "Eve", "age": 45, "salary": 80000},
    {"name": "Frank", "age": 22, "salary": 30000}
]

# 1. filter() Question Q: Using the sample dataset, write a program to filter out all employees who are older than 30.

def filterAge(item):
  if item['age'] > 30:
    return True
  else:
    return False
  
print(list(filter(filterAge, data)))

# Using lambda function:

print(list(filter(lambda item: item if item['age'] > 30 else False, data)))