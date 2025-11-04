'''
Write a dictionary comprehension to count the frequency of each word in a given string.

text = "python is great and python is easy"
# Expected Output:
# {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1}
'''

# Using List Built-in Method: count()
text = "python is great and python is easy"
text = text.split()
freq_dict = {key: text.count(key) for key in text}
print(freq_dict)

# Manual Implementation:

manual_dict = {word: 0 for word in text}
for word in text:
  manual_dict[word] += 1

print(manual_dict)