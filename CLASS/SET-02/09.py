'''
Print elements at even indices

Problem:
Given a list, print only the elements that appear at even indices.

Example:

Input → [10, 20, 30, 40, 50, 60]

Output → [10, 30, 50]
'''

ip_list = [10, 20, 30, 40, 50, 60]
even_ip = []
for ip in range(len(ip_list)):
  if ip%2 == 0:
    even_ip.append(ip_list[ip])
print(even_ip)