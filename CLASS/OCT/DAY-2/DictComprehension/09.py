'''
Character Frequency Counter
Build a frequency dictionary of characters in a string.

Input: "banana"  
Output: {"b":1, "a":3, "n":2}
'''

text = 'banana'

result = {k: text.count(k) for k in text}

print(result)