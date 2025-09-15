'''
Filter non-empty strings.
Given a list of strings, return only the non-empty ones (exclude empty strings or strings with only spaces).
'''
strings = ["hello", "", " ", "world", "", "python", "   "]
print(list(filter(lambda string: len(string) > 1 and string.isalpha(), strings)))