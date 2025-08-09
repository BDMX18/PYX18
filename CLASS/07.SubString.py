# Approach 01:

string = input('Enter A String: ')
sub_string = input('Enter The Sub-String To Search: ')
length = len(sub_string)
count = 0
for ip in range(0, len(string)):
  if(string[ip:ip+length] == sub_string):
    count += 1
print(f'Sub-String Avaliable in String for {count} times')

# Approach 02: To avoid un-necessary comparison. Optimized Solution

string = input('Enter A String: ')
sub = input('Enter Sub-string To Search: ')
count = 0
for ip in range(len(string) - len(sub)):
  if(string[ip:ip+len(sub)] == sub):
    count += 1
print(f'Sub-string in String for {count} time(s)')