'''
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

r = int(input('Enter A Range: '))
dict_cube = {}
for i in range(1, r+1):
  dict_cube[i] = i**3
print(dict_cube)