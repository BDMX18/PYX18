'''
Given a list of numbers, find the second largest number.

Second largest number in a list

Input: [4, 2, 9, 7, 5]

Output: 7
'''

ip_list = [4, 2, 9, 7, 5]

def second_largest(ip_list):
  max_1 = max_2 = float('-inf')
  for element in ip_list:
    if element > max_1:
      max_2 = max_1
      max_1 = element
    elif element > max_2 and element != max_1:
      max_2  = element
  return max_2

print(second_largest(ip_list))
