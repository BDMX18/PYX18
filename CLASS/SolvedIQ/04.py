# Write a python program to find out the common letters between two strings.

def common_letter(str1, str2):
  common = []
  for ch in str1:
    if ch in str2 and ch not in common:
      common.append(ch)
  return common

print(common_letter('NAINA', 'REENE'))
print(common_letter('HIMADRI', 'SHILA'))