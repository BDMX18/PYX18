# Count Strings with Same Start and End

# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list = eval(input('Enter The Elements Of The List: '))
count = 0
for element in list:
  if(isinstance(element, str)):
    if(len(element) > 1):
      if(element[0] == element[-1]):
        count += 1
    else:
      print('The String Should Have Atleast Two Characters!')
  else:
    print('None Of The Element In The List Is A String!')
print('String(s) With First And Last Character Same: ',  count)