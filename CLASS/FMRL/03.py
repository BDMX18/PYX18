'''
3. reduce() Question

Q: Write a program using reduce() to calculate the total salary of all employees.

(Hint: Use from functools import reduce)
'''

data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "David", "age": 28, "salary": 40000},
    {"name": "Eve", "age": 45, "salary": 80000},
    {"name": "Frank", "age": 22, "salary": 30000}
]

from functools import reduce as r
print(r(lambda total, item: total + item['salary'], data, 0))
