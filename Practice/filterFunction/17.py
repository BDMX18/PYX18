'''
6. Filter out dictionary entries where value is None

Question:
Given a dictionary with possible None values, remove those entries.

Sample Data:
'''


user_profile = {
    "name": "Alice",
    "age": None,
    "email": "alice@example.com",
    "phone": None,
    "city": "Paris"
}

print(dict(filter(lambda item: item[1] is not None, user_profile.items())))