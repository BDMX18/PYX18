'''
Apply Custom Function to Complex Data:
Given a list of tuples with (name, age), use map() to return a list of strings like "Alice is 25".
Example input: [("Alice", 25), ("Bob", 30)] → Output: ["Alice is 25", "Bob is 30"]
'''

print(list(map(lambda element: f'{element[0]} is {element[1]}', [("Alice", 25), ("Bob", 30)])))