# WAP to find how many times a given sub-string is present in a given string

string = input('Enter A String: ')
sub_s = input('Enter A Sub-String To Search: ')
count = 0
for element in string:
  if sub_s == element:
    count += 1
print(f'\'{sub_s}\' is present in {string} for {count} time(s)')