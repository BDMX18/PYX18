# Maximum among 5 number using nested if conditions

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if(a > b):
  if(a > c):
    if(a > d):
      if(a > e):
        print('Maximum: ', a)
      else:
        print('Maximum: ', e)
    else:
      if(d > e):
        print('Maximum:', d)
      else:
        print('Maximum', e)
  else:
    if(c > d):
      if(c > e):
        print('Maximum: ', c)
      else:
        print('Maximum: ', e)
    else:
      if(d > e):
        print('Maximum: ', d)
      else:
        print('Maximum: ', e)
else:
  if(b > c):
    if(b > d):
      if(b > e):
        print('Maximum: ', b)
      else:
        print('Maximum: ', e)
    else:
      if(d > e):
        print('Maximum: ', d)
      else:
        print('Maximum: ', e)
  else:
    if(c > d):
      if(c > e):
        print('Maximum: ', c)
      else:
        print('Maximum: ', e)
    else:
      if(d > e):
        print('Maximum: ', d)
      else:
        print('Maximum: ', e)