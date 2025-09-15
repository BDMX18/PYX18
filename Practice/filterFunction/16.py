'''
5. Filter dictionary to keep items where value is a string

Question:
Given a dictionary with mixed types, return only the key-value pairs where the value is a string.

Sample Data:
'''
data = {
    "name": "John",
    "age": 28,
    "city": "New York",
    "is_member": True,
    "email": "john@example.com"
}

print(dict(filter(lambda item: type(item[1]) == str, data.items())))