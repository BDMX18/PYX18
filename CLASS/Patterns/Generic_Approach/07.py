n= int(input('Enter The Number Of Rows: '))
star = n
for row in range(1, n+1):
  for st in range(star):
    print("*", end="")
  print()
  star -= 1