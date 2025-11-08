'''
Q3. Convert List of Strings to Integers

Problem Statement:
Write a Python program to convert all elements of a list into integers.
If a conversion fails, skip that value and continue with the next.

Sample Input:

numbers = ["12", "45", "abc", "78", "xyz", "90"]


Expected Output:

Converted integers: [12, 45, 78, 90]
'''

numbers = ["12", "45", "abc", "78", "xyz", "90"]
int_list = []

for data in numbers:
  try:
      int_list.append(int(data))
  except ValueError as VE:
    continue
print(int_list)