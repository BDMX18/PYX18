# 7. Remove Duplicates from List
# Write a Python program to remove duplicates from a list.

# Approach 01: By using built-in method:
ip_list = eval(input('Enter The Elements Of The List: '))
new_list = list(set(ip_list))
print(new_list)

# Approach 02: Manually:
ip_list = eval(input('Enter The Elements Of The List: '))
distinct_list = []
index = 0
while index < len(ip_list):
  if(ip_list[index] not in distinct_list):
    distinct_list.append(ip_list[index])
  index += 1
print(distinct_list)