'''
8. Use a nested list comprehension to transpose a matrix:

[[1, 2, 3],
 [4, 5, 6]]
→ [[1, 4], [2, 5], [3, 6]]
'''

a = [1,2,3]
b = [4,5,6]
op_list = [[a[ea], b[eb]] for ea in range(len(a)) for eb in range(len(b)) if ea == eb]
print(op_list)