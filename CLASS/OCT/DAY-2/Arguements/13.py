'''
Mixed Arguments

Problem: Implement build_profile(first, last, age=25, *skills, **details) returning a dictionary.

Input:
build_profile("John","Doe",30,"Python","Django",location="NY",hobby="Chess")

Output:
{'first':'John','last':'Doe','age':30,'skills':['Python','Django'],'location':'NY','hobby':'Chess'}

'''

def build_profile(first, last, age = 25, *skills, **details):
  profile = {
    'first': first,
    'last': last,
    'age': age,
    'skills': list(skills)
  }
  profile.update(details)
  return profile
  

print(build_profile("John","Doe",30,"Python","Django",location="NY",hobby="Chess"))