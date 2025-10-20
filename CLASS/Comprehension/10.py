'''
Given a string "A quick brown fox", use a list comprehension to create a list of ASCII values of vowels only.
'''

string = 'A quick brown fox'

op_list = [ord(ch) for ch in string if ch in 'aeiouAEIOU']
print(op_list)