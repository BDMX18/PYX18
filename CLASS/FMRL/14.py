'''
You are given a list of words. Use filter() to get only words that contain at least one vowel.
'''

words = ['sky', 'try', 'fly', 'apple', 'gym', 'orange', 'dry']

op_list = list(filter(lambda word: any(ch in 'aeiou' for ch in word), words))

print(op_list)

