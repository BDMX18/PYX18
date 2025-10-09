'''
5. Anagram Check

Problem:
Write a function that checks if two given strings are anagrams of each other (ignore spaces and case).

Example:
Input: "Listen", "Silent"
Output: True

Input: "Hello", "World"
Output: False
'''

# Will not work perfectly in all the scenarios
'''
  str1_sum = 0
  str2_sum = 0
  for ch in str1.lower():
    str1_sum += ord(ch)
  for ch in str2.lower():
    str2_sum += ord(ch)
  if str1_sum == str2_sum:
    return True
  else:
    return False
'''
def isAnagram(str1, str2):
  normal_str1=''
  normal_str2=''
  for ch in str1.lower():
    if not(ch.isspace()):
      normal_str1 += ch
  for ch in str2.lower():
    if not(ch.isspace()):
      normal_str2 += ch
  if len(normal_str1) == len(normal_str2):
    str1_dict = {}
    str1_count = 1
    for ch in normal_str1:
      if ch not in str1_dict:
        str1_dict[ch] = str1_count
      else:
        str1_dict[ch]+=1
    for ch in normal_str2:
      if ch in str1_dict:
        str1_dict[ch]-=1
      else:
        return False
    sum=0
    for val in str1_dict.values():
      sum += val
    if(sum == 0):
      return True
    else:
      return False
  else:
    return False
  


print(isAnagram('Listen', 'Silent'))

