'''
Q4. Highest Scoring Student (Using reduce)

Problem:
Given a list of students and their scores, find the student with the highest score using reduce.

Sample Input:

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 88}
]


Expected Output:

{'name': 'Bob', 'score': 92}
'''

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 88}
]

from functools import reduce

result = reduce(lambda a,b: a if a['score'] > b['score'] else b, students)

print(result)