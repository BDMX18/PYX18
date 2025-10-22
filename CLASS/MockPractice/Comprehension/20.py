'''
Question 5:
Generate a list of all possible combinations of characters from two lists, but skip combinations where the characters are equal.

list1 = ['a', 'b', 'c']
list2 = ['b', 'c', 'd']
'''

op_list = [c1+c2 for c1 in 'abc' for c2 in 'bcd' if c1 != c2]

print(op_list)