'''
Count frequency of vowels in a string

Problem:
Return a dictionary showing how many times each vowel appears in the string.

Example:

Input → "education"

Output → {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
'''

ip_str = 'education'
vowel = {}
for ch in ip_str:
  if ch in 'aeiou':
    if ch not in vowel:
      vowel[ch] = 1
    else:
      vowel[ch] += 1
print(vowel)