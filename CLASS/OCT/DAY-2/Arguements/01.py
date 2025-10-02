'''
Write a function create_user_profile(first_name, last_name, **kwargs) that takes mandatory first_name and last_name and any number of keyword arguments.

Return a dictionary containing the full user profile.

If age is not provided in kwargs, set it to 18 by default.

Ensure all string values in the dictionary are capitalized.

Sample Input:

create_user_profile("john", "doe", location="ny", hobby="chess")


Expected Output:

{
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 18,
    'location': 'Ny',
    'hobby': 'Chess'
}
'''

def create_user_profile(first_name, last_name, **kwargs):
  kwargs.setdefault('first_name', first_name)
  kwargs.setdefault('last_name', last_name)
  for key, value in kwargs.items():
    if(isinstance(value, str)):
      kwargs[key] = value.capitalize()
  return kwargs

print(create_user_profile('john', 'doe', age=18, location='ny', hobby='chess'))