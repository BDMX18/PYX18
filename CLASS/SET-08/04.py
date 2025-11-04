'''
Q4. Character Frequency (Dictionary Comprehension)

Write a program to count occurrences of each character in a given string using dictionary comprehension.

Sample Data:

text = "mississippi"


Expected Output:

{'m': 1, 'i': 4, 's': 4, 'p': 2}
'''

text = "mississippi"

occurance_dict = {key: text.count(key) for key in text}

print(occurance_dict)

manual_dict = {key:0 for key in text}

for key in text:
  manual_dict[key] += 1

print(manual_dict)