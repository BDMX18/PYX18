'''
Nested Dictionary (Grades)
Given a list of students and subjects, assign all students a default grade "A".

Input: students=["Alice","Bob"], subjects=["Math","Science"]  
Output: {
    "Alice": {"Math":"A","Science":"A"},
    "Bob": {"Math":"A","Science":"A"}
}
'''

students=["Alice","Bob"]
subjects=["Math","Science"]  

result = {k: {}.fromkeys(subjects, 'A') for k in students}
print(result)


