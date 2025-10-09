'''
Find out pairs with given sum value of an array.
'''

arr = [5,7,4,2,9,8,19,21]
sum = 17

pair_arr = []

for i in arr:
  for j in arr:
    if i+j == sum:
      pair_arr.append([i, j])
print(pair_arr)