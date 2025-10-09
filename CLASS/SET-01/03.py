'''
3. Remove all duplicate characters from a string while preserving order.
Input: "programming"
Output: "progamin"
'''

def remove_duplicates(ip_str):
  original = ''
  for ip in range(len(ip_str)):
    j = ip+1
    for j in range(len(ip_str)):
      if ip_str[ip] != j and ip_str[ip] not in original:
        original += ip_str[ip]
  return original

print(remove_duplicates('programming'))

