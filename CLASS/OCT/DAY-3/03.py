'''
Count Occurrences of Each Character

Problem:
Write a function that takes a string and returns a dictionary with characters as keys and their frequency as values. Ignore case and spaces.

Example:
Input: "Programming"
Output: {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}
'''

def count_occrance(string):
  count_dict = {}
  for ch in string:
    if ch not in count_dict:
      count_dict[ch] = 1
    elif ch in count_dict:
      count_dict[ch] += 1
  return count_dict

print(count_occrance('Programming'))