'''
9. map() + filter()

Q: Given a list of student dictionaries, filter students who scored more than 80 and return their names in lowercase.

'''

students = [
    {"name": "Amit", "score": 91},
    {"name": "Neha", "score": 78},
    {"name": "Ravi", "score": 85},
    {"name": "Priya", "score": 69}
]

result = list(filter(lambda item: item if item['score'] > 80 else False, students))
print(list(map(lambda item: item['name'].lower(), result)))