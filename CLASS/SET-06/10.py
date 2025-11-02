'''
Reverse Words Order:
Input: "Python is fun" → Output: "fun is Python"
'''

ip_str = 'Python is fun'

ip_list = ip_str.split()

reverse = ' '.join(ip_list[::-1])

print(reverse)