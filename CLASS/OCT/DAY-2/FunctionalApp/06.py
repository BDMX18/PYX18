'''
Compose Functions

Problem:
Write a function compose(f, g) that takes two functions f and g, and returns a new function h(x) that computes f(g(x)).
Then test it with:

f(x) = x + 2

g(x) = x * 3

Sample Input:

h(5)


Expected Output:

17 
'''


def compose(x):
  def outerDec(func):
    def innerDec():
      func(x)
      return innerDec
    return outerDec
  return compose
  


@compose(5)
def f(x):
  def 
  