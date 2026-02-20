'''
Find the lengthiest palindrome string within a given string
haaha
'''

ip_str = 'haaha'
length = 2
palindrome = []
for i in range(len(ip_str)*2):
  for ip in range(len(ip_str)):
    word = ip_str[ip:ip+length]
    if word == word[::-1]:
      if len(palindrome) == 0:
        palindrome.append(word)
      else:
        if len(word) > len(palindrome[0]):
          palindrome.pop()
          palindrome.append(word)
  length += 1

print(palindrome)