# Print five numbers

def printNum(LR, UR):

  if(LR > UR):
    return
  printNum(LR+1, UR)
  print(LR)

printNum(1, 5)

  