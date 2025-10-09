# Find missing number in an array(using summation and XOR operation)

num_list = [1,2,4,5,6,7]

# Approach 1: Summation, Taking sum of n natural numbers.
# Formula: (n*(n+1))/2
n = num_list[-1]
natural_sum = (n*(n+1))//2
num_sum = 0
print(natural_sum)
for num in num_list:
  num_sum += num
print('Number Missing In', num_list, 'is', (natural_sum-num_sum))
