# WAP to find how many elements are present in a given string.

string = input('Enter A String: ')
count = 0
for element in string:
  count += 1
print('Number of elements present in string: ', count)