'''
Extract First Character from Each String:
Use map() to extract the first character from each word in a list.
Example input: ["Python", "Map", "Function"] → Output: ["P", "M", "F"]
'''

print(list(map(lambda word: word[0], ["Python", "Map", "Function"])))