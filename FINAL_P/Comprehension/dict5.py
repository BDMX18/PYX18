'''
Convert a dictionary of student marks to show only those who scored above 75.

marks = {'John': 85, 'Alice': 72, 'Bob': 90}
# Expected Output: {'John': 85, 'Bob': 90}
'''

marks = {'John': 85, 'Alice': 72, 'Bob': 90}

cutoff_dict = {key:value for key, value in marks.items() if value > 75}

print(cutoff_dict)