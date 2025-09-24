'''
4. Combined filter() + map() Question

Q: Find the names of all employees younger than 30 and convert them to uppercase using a combination of filter() and map().
'''

data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "David", "age": 28, "salary": 40000},
    {"name": "Eve", "age": 45, "salary": 80000},
    {"name": "Frank", "age": 22, "salary": 30000}
]

result = list(filter(lambda item:item['age'] if item['age'] > 30 else False, data))
print(list(map(lambda item: item['name'].upper(), result)))