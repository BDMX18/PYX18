'''
Check for Duplicate Elements in a List

Given a list of integers, use nested loops to check if there are duplicate elements. Print "Duplicates found" if yes, otherwise print "No duplicates".
'''

# Sample list with duplicates
list1 = [1, 3, 5, 7, 3, 9]

# Sample list without duplicates
list_without_duplicates = [2, 4, 6, 8, 10]

for ip in range(len(list1)):
  check = list1[ip]
  for element in list1[ip+1:]:
    if check == element:
      print('Duplicate Exists!')
      break
  else:
    print('No Duplicates!')

