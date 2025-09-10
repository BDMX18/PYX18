# Write a recursive function that given an input n, sums all non-negative integers upto n

def sum_n(num):
  if(num == 0):
    return 0
  return num + sum_n(num-1)

print(sum_n(10))
