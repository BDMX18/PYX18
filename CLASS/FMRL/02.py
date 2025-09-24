'''
2. map() Question

Q: Write a program to increase the salary of every employee by 10% and return the updated list of salaries using map().
'''

data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "David", "age": 28, "salary": 40000},
    {"name": "Eve", "age": 45, "salary": 80000},
    {"name": "Frank", "age": 22, "salary": 30000}
]

def incrementSal(item):
  item['salary'] = item['salary'] + item['salary'] * .10
  return item

print(list(map(incrementSal, data)))

# Using lambda function:

print(list(map(lambda item: item.update({'salary': item['salary']+item['salary']*.10}) or item, data)))