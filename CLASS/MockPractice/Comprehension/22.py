'''
Given a dictionary of students and scores, create a new dictionary with only students who scored above 70 and convert their names to uppercase.

scores = {"Alice": 85, "Bob": 65, "Charlie": 90, "David": 55}
'''

scores = {"Alice": 85, "Bob": 65, "Charlie": 90, "David": 55}

op_dict = {k.upper():v for k,v in scores.items() if v > 70}

print(op_dict)