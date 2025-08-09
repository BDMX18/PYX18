# INPUT :  [12, 11, 17, 21, 5]
# OUTPUT : ['even', 'prime', 'prime', 'odd', 'prime']

'''
Approach:
-> Using for loop we'll be iterating through each and every element of the list.
-> At first we'll determine whether the list element is prime or not.
    -> If it's not prime we'll check whether the number is even or odd.
-> We'll be using for-else loop, so if the number is neither prime nor it's even or odd, we'll break the for loop and we'll print it a prime in the else part.
'''

# -> Using for loop with CDT

num_list = eval(input('Enter A List: '))
new_list = []
for element in num_list:
  if element > 1:
    for i in range(2, element//2+1):
      if(element % i == 0):
        if(element % 2 == 0):
          new_list.append('even')
        else:
          new_list.append('odd')
        break
    else:
      new_list.append('prime')
  else:
    new_list.append('odd')
print(new_list)

# -> Modifying existing list and For loop with range:

number_list = eval(input('Enter A List: '))
for ip in range(len(number_list)):
  num = number_list[ip]
  if num > 1:
    for element in range(2, num//2+1):
      if(num % element == 0):
        if(num % 2 == 0):
          number_list[ip] = 'even'
        else:
          number_list[ip] = 'odd'
        break
    else:
      number_list[ip] = 'prime'
  else:
    number_list[ip] = 'odd'
print(number_list)


