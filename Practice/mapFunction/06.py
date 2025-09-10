'''
Check If Each Number is Even:
Use map() to return a list of booleans indicating if each number is even.
Example input: [1, 2, 3, 4] → Output: [False, True, False, True]
'''

print(list(map(lambda n:n%2==0, [1, 2, 3, 4])))