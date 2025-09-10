'''
Using map() with lambda to Normalize Data:
Given a list of numbers, normalize them to a range between 0 and 1 using map() and lambda.
Example input: [10, 20, 30] → Output: [0.0, 0.5, 1.0]
'''

print(list(map(lambda element: (element-10)/(30-10), [10, 20, 30])))