'''
Merge Dictionaries

Problem:
Write a function merge_dicts(*dicts, overwrite=True) that merges multiple dictionaries into one.

If overwrite is True, later values replace earlier ones; if False, earlier values are kept.

Sample Input 1:

merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4})


Expected Output 1 (default overwrite=True):

{'a': 1, 'b': 3, 'c': 4}


Sample Input 2:

merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4}, overwrite=False)


Expected Output 2:

{'a': 1, 'b': 2, 'c': 4}
'''

def merge_dicts(*args, overwrite=True):
  merged_dict = {}
  for dict in args:
    for k, v in dict.items():
      if overwrite:
        merged_dict[k] = v
      else:
        if k in merged_dict:
          continue
        merged_dict[k] = v
  return merged_dict

print(merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4}))
print(merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4}, overwrite=False))