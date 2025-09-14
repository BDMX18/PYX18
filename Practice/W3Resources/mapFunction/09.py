'''
9. Tuple Elements and String to Int Map: Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
Original data:
[('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

Student name:
['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
Student name:
['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
Student weight:
[35, 37, 39, 35]
'''


L = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]
print(list(map(lambda element:element[0], L)))
print(list(map(lambda element:element[1], L)))
print(list(map(lambda element:int(element[2].rstrip('kg')), L)))