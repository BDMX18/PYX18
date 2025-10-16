'''
02> Given a list of strings, use filter() to return only the strings that are palindromes.
'''

words = ['madam', 'python', 'level', 'world', 'civic', 'openai']


op_list = list(filter(lambda x: x == x[::-1], words))
print(op_list)