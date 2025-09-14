# def sumL(L):
#   if len(L) == 0:
#     return 0
#   return sumL(L[1:]) + L[0]
# print(sumL([1,2,3,4,5]))

# def reverse(str):
#   rev = ''
#   for ch in str:
#     rev = ch + rev
#   return rev
# print(reverse('bibhu'))
  
# def reverse(str):
#   rev = ''
#   ip = -1
#   while ip >= -(len(str)):
#     rev += str[ip] 
#     ip -= 1
#   return rev

# print(reverse('bibhu'))


# def reverse(string):
#   if not string:
#     return ''
#   return reverse(string[1:]) + string[0]

# print(reverse('bibhu'))

# Factorial of a number:

def factorial(num):
  if(num == 0):
    return 1
  return num * factorial(num-1)

print(factorial(5))