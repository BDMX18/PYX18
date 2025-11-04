'''
Concatenate Words

Write a function join_words(*args) that takes multiple string arguments and returns them combined into a single sentence separated by spaces.

Sample Data:

join_words("Python", "is", "awesome")
join_words("Variable", "arguments", "make", "functions", "flexible")
'''

def join_words(*args):
  op_str = ' '.join(args)
  return op_str

print(join_words("Python", "is", "awesome"))
print(join_words("Variable", "arguments", "make", "functions", "flexible"))