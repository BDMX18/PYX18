'''
Keyword Stats Filter

Problem:
Write a function filter_stats(**kwargs) that accepts any keyword arguments.

Return only the ones whose values are numeric and greater than 50.

Sample Input:

filter_stats(math=75, english=45, science=90, name="Alice")


Expected Output:

{'math': 75, 'science': 90}
'''

def filter_stats(**kwargs):
  filter_kwargs = {}
  for key in kwargs:
    if (isinstance(kwargs[key], int) and kwargs[key] > 50):
      filter_kwargs.update({key: kwargs[key]})
  return filter_kwargs

print(filter_stats(math=75, english=45, science=90, name="Alice"))

# Dictionary Comprehension:

def filter_stats(**kwargs):
  return {k: v for k, v in kwargs.items() if(isinstance(v, int) and v > 50)}
print(filter_stats(math=75, english=45, science=90, name="Alice"))
