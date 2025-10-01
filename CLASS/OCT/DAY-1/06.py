'''
Question: Functional Sentence Word Counter

Write a function count_long_words(sentences, min_length) that:

Takes a list of sentences (sentences) and an integer min_length.

Uses functional programming (map, filter, lambda) to:

Split each sentence into words.

Flatten the list of all words from all sentences.

Filter words that have length at least min_length.

Returns the count of such words.

Example:

sentences = ["Hello world", "Functional programming is fun", "Keep it simple"]

print(count_long_words(sentences, 5))


Output:

4
'''

def count_long_words(sentances, min_length):
  split_list = list(map(lambda sentance: sentance.split(), sentances))
  flatten_list = [word for sub_list in split_list for word in sub_list]
  filter_list = list(filter(lambda word: len(word) >= min_length, flatten_list))
  count = len(filter_list)
  return count

count = int(input('Enter The Count Of Sentances You Want To Add To The List: '))
sentances = [input(f'Enter Sentance {i+1}: ') for i in range(count)]
min_length = int(input('Enter The Minimun Length: '))
print(count_long_words(sentances, min_length))