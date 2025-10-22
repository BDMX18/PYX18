'''
Question 7:
Given a dictionary of names and ages, create a new dictionary with names of people above 25 only.

people = {"Alice": 23, "Bob": 30, "Charlie": 27, "David": 22}
'''
people = {"Alice": 23, "Bob": 30, "Charlie": 27, "David": 22}

op_dict = {k:v for k,v in people.items() if v>25}

print(op_dict)
