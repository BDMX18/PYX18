'''
Reverse Words in a Sentence (Without split())

Problem:
Reverse the order of words in a sentence manually by scanning the string.

Sample Input: "I love Python"
Expected Output: "Python love I"
'''

def reverseString(ip_str):

  words = []
  word = ''

  for ch in ip_str:
    if ch == ' ':
      words.append(word)
      word = ''
    else:
      word += ch
    
  if word:
    words.append(word)

  return ' '.join(words[::-1])

print(reverseString('I Love Python'))