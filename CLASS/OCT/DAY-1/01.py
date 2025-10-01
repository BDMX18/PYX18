'''
Question: Word Frequency Filter

Write a function in Python that takes a list of sentences and performs the following steps using a functional approach:

Break each sentence into words.

Flatten all words into a single list.

Filter out all words that are shorter than 4 characters.

Convert all words to lowercase.

Count the frequency of each word.

Return the top 5 most common words in the form of a list of tuples:
[(word1, count1), (word2, count2), ...]

🔒 Constraints:

You must not use loops (for or while).

You must use at least these functional tools:

map()

filter()

functools.reduce() (or another functional technique for counting)

You may use standard library functions like collections.Counter if integrated in a functional way.

🧪 Example:
input_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The quick red fox bit the lazy dog",
    "Why does the fox always go for the dog?"
]


Expected Output:

[('the', 6), ('fox', 3), ('lazy', 3), ('dog', 3), ('quick', 2)]
'''

from collections import Counter

def sentance(num):
  input_sentance = []
  for i in range(num):
    string = input(f'Enter Sentance {i+1}: ')
    input_sentance.append(string)
  word_list = list(map(lambda string: string.split(), input_sentance))
  flatten_list = [word for sub_list in word_list for word in sub_list]
  filter_list = list(filter(lambda string: string.lower() if len(string)>=4 else False, flatten_list))
  count = Counter(filter_list)
  top_5 = count.most_common(5)
  print(top_5)


num = int(input('Enter The Number Of Sentance You Want To Add: '))
sentance(num)
