'''
5. Check if a string is a palindrome (ignore spaces, case, punctuation).
str = 'A man, a plan, a canal: Panama'
'''

def isPalindrome(ip_str):
  alpha_str = ''
  for ch in ip_str:
    if ch.isalpha():
      alpha_str += ch.lower()
  if alpha_str == alpha_str[::-1]:
    return True
  else:
    return False

ip_str = 'A man, a plan, a canal: Panama'
print(isPalindrome(ip_str))