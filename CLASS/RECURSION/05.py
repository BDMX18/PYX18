def sumOfList(list):
  if(len(list) == 0):
    return 0
  return list[0] + sumOfList(list[1:])
list = [1, 2, 3, 4, 5, 6, 7]
print(sumOfList(list))