# 8. Find longest word in a list.

# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

stringList = eval(input('Enter A List Of Strings: '))
longest = stringList[0]
for element in stringList:
  if(len(element) > len(longest)):
    longest = element
print("Longest Word: ", longest, "\nLength: ", len(longest))
