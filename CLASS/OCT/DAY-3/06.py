'''
6. Find All Palindromic Substrings

Problem:
Write a function that returns all substrings of a string that are palindromes of length ≥ 2.

Example:
Input: "ababa"
Output: ['aba', 'bab', 'ababa']
'''
def palindrome_string(ip_str):
  result_list = []
  for i in range(len(ip_str)):
    for j in range(i+1, len(ip_str)):
      sub_str = ip_str[i:j+1]
      if sub_str == sub_str[::-1]:
        if sub_str not in result_list:
          result_list.append(sub_str)
  return result_list

print(palindrome_string('ababa'))
