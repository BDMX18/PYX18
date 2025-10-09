'''
4. Find the frequency of each word in the given sequence

Input: "this is a test this is only a test"

Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
'''

def word_occurance(ip_str):
  word_dict = {}
  count = 1
  for word in ip_str.split():
    if word not in word_dict:
      word_dict[word] = count
    else:
      word_dict[word]+=1
  return word_dict

print(word_occurance('this is a test this is only a test'))