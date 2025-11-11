'''
Q3. Check Palindrome String

Problem:
Check if a given string is a palindrome using a for-else loop.

Sample Data:

word = "madam"


Expected Output:

madam is a palindrome.


(if input = "world")

world is not a palindrome.
'''

word = input('Enter A Word: ')

# for ip in range(len(word)//2+1):
#   if word[ip] != word[-ip-1]:
#     print(f'{word} is not palindrome!')
#     break
# else:
#   print(f'{word} is palindrome')

index = 0
while index <= len(word)//2+1:
  if word[index] != word[-index-1]:
    print(word, 'is not palindrome!')
    break
  index += 1
else:
  print(word, 'is palindrome')