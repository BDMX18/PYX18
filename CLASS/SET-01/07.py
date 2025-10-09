'''
Implement your own version of sum() using a for loop.

Implement your own sum function

Input: [1, 2, 3, 4, 5]

Output: 15
'''

def list_sum(ip_list):
  sum = 0
  for element in ip_list:
    sum += element
  return sum

ip_list = [1,2,3,4,5]
print(list_sum(ip_list))