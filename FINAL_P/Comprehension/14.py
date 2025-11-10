'''
Q3. Label Elements Based on Position

Problem:
Given a list of names, create a list of tuples using list comprehension and enumerate() where each tuple contains:
("Even" or "Odd" index, name)

Sample Data:

names = ['Alice', 'Bob', 'Charlie', 'David']


Expected Output:

[('Even', 'Alice'), ('Odd', 'Bob'), ('Even', 'Charlie'), ('Odd', 'David')]
'''

names = ['Alice', 'Bob', 'Charlie', 'David']

op_names = [('Even' if i%2==0 else 'Odd', name) for i, name in enumerate(names)]

print(op_names)