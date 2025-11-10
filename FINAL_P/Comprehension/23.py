'''
Q2. Zipping Multiple Lists with a Derived Key

Problem:
You have three lists — names, math_marks, and science_marks.
Use zip() and dictionary comprehension to create a dictionary where the key is the name and the value is the average of both marks.

Sample Data:

names = ['Alice', 'Bob', 'Charlie']
math_marks = [80, 75, 90]
science_marks = [85, 70, 88]


Expected Output:

{'Alice': 82.5, 'Bob': 72.5, 'Charlie': 89.0}
'''

names = ['Alice', 'Bob', 'Charlie']
math_marks = [80, 75, 90]
science_marks = [85, 70, 88]



print(average)

# print({name:mark for name, mark in zip(names)})