# Write a python program to count the frequency of words appearing in a string.
# Sheena loves eating apple and mango. Her sister also loves eating apple and mango.

def word_occurance(ip_str):
  word_dict = {}
  count = 1
  for word in ip_str.split():
    if word not in word_dict:
      word_dict[word] = count
    else:
      word_dict[word]+=1
  return word_dict

print(word_occurance('Sheena loves eating apple and mango. Her sister also loves eating apple and mango.'))