'''
Question: Functional Student Grade Filter

Write a function filter_passing_students(students, passing_score) that:

Takes a list of student dictionaries. Each dictionary has 'name' and 'score' keys.

Uses functional programming to:

Filter students who scored at least passing_score.

Return a list of student names who passed.

Example:

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 42},
    {'name': 'Charlie', 'score': 73},
]

print(filter_passing_students(students, 60))


Output:

['Alice', 'Charlie']
'''

def filter_passing_students(students, passing_score):
  filter_list = list(filter(lambda item: item['score'] >= passing_score, students))
  name_list = list(map(lambda item: item['name'], filter_list))
  return name_list

students = []

count = int(input('Enter The Number Of Students: '))
for i in range(count):
  s_dict = {}
  name = input('Enter Student\'s Name: ')
  score = int(input('Enter Student Score: '))
  s_dict = {'name': name, 'score': score}
  students.append(s_dict)

score = int(input('Enter Score: '))

print(filter_passing_students(students, score))