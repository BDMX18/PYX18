'''
9. Filter dictionary of users to keep only those above age 18

Question:
Given a dictionary of users where values are dicts with an "age" field, return only users over 18.

Sample Data:

'''

users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 17},
    "user3": {"name": "Charlie", "age": 19},
    "user4": {"name": "Daisy", "age": 15}
}
print(dict(filter(lambda item: item[0], users.items())))