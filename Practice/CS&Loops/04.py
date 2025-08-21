# Sub-string in a given string

string = input('Enter A String: ')
sub_s = input('Enter A Sub-string To Search: ')
length = len(sub_s)
count = 0
for ip in range(len(string)):
  if sub_s == string[ip:ip+length]:
    count += 1
print(f'\'{sub_s}\' is present in {string} for {count} times')