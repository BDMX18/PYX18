'''
3. Sum of Nested Lists Using Recursion

Write a Python program to sum recursion lists using recursion.

Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
'''

def sumList(num_list):
  sum = 0
  for element in num_list:
    if(isinstance(element, int)):
      sum += element
    else:
      sum += sumList(element)
  return sum
print(sumList([1, 2, [3,4], [5,6]]))