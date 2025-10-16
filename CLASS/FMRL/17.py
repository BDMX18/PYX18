'''
Given two lists of the same length, use map() to create a new list that contains the sum of elements from both lists.
'''

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]

sum_list = list(map(lambda a,b: a+b, list1, list2))

print(sum_list)

