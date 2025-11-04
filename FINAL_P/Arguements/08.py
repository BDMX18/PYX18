'''
Q8. Mix of All — Dynamic Function

Create a function show_data(a, b=10, *args, **kwargs) that:

Prints the first two positional arguments,

Prints additional positional arguments (if any),

Prints all keyword arguments.

Sample Data:

show_data(5)
show_data(5, 15, 20, 25, name="Bibhu", role="Engineer")
'''

def show_data(a, b=10, *args, **kwargs):
  print(a,'\n',b)
  for arg in args:
    print(arg)
  for key in kwargs:
    print(f'{key}: {kwargs[key]}')
  return '-'*20

print(show_data(5))
print(show_data(5, 15, 20, 25, name="Bibhu", role="Engineer"))