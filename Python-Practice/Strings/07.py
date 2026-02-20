'''
Compress a String (Run-Length Encoding)

Problem:
Convert "aaabbcccaa" → "a3b2c3a2"
Do NOT use any Python library function that solves it automatically.
'''

ip_str = input('Enter A String: ')

ip = 1
count = 1
result = ''
while ip < len(ip_str):
  if ip_str[ip] == ip_str[ip-1]:
    count += 1
  else:
    result += ip_str[ip-1] + str(count)
    count = 1
  if ip == len(ip_str) - 1:
    result += ip_str[ip] + str(count)
  ip += 1
else:
  print(result)
  