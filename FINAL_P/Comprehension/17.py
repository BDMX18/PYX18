'''
Q6. Pairwise Concatenation

Problem:
You have two lists of strings. Use list comprehension with zip() to concatenate elements from both lists.

Sample Data:

list1 = ['red', 'blue', 'green']
list2 = ['apple', 'berry', 'leaf']


Expected Output:

['redapple', 'blueberry', 'greenleaf']
'''


list1 = ['red', 'blue', 'green']
list2 = ['apple', 'berry', 'leaf']


print([color+fruit for color, fruit in zip(list1, list2)])
