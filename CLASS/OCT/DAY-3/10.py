'''
10. Check if One String is a Rotation of Another

Problem:
Write a function to check if one string is a rotation of another string.

Example:
Input: "waterbottle", "erbottlewat"
Output: True

Input: "hello", "lloeh"
Output: False
'''

def isRotation(str1, str2):
  if len(str1) == len(str2):
    concat = str1*2
    if(str2 in concat):
      return  True
    else:
      return False
  else:
    return False

print(isRotation("hello", "lloeh"))