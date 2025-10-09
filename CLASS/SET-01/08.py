'''
Flatten a nested list (without recursion)

Input: [1, [2, [3, 4]], 5]

Output: [1, 2, 3, 4, 5]
'''

def flatten_list(ip_list):
  flatten = []
  dummy = ip_list
  while dummy:
      element = dummy.pop(0)
      if(isinstance(element, list)):
        dummy = dummy + element
      else:
        flatten.append(element)
  return flatten

ip_list = [1, [2, [3, 4]], 5]
print(flatten_list(ip_list))