'''
INPUT: 'aaabbddddcccaaaab'
OUTPUT: 'a3b2d4c3a4b'
'''

'''
Approach:
-> Herein, from the input string we'll be finding out occurance of each letter and will be printing the same along with their respective letter in a new string.
-> We'll be checking adjacent elements, if they're same or not, if they're same we'll incrementing the value of count.
-> Assuming the adjacent element to be same, and initilly we'll  be keeping the value of count = 1, as the count for the element we've taken for comparison.
-> We'll be parsing through each and every letter of the string, till the end of the string.
'''

# -> By using For loop with range and CDT

string = input('Enter A String: ')
count = 1
new_string = ''
for ip in range(1, len(string)):
  if(string[ip] == string[ip-1]):
    count += 1
  else:
    new_string = new_string + string[ip-1] + str(count)
    count = 1
new_string = new_string + string[ip] + str(count)
print(new_string)
