# 9. Remove nth character from a string.
# Write a Python program to remove the nth index character from a nonempty string.

string = input('Enter A String: ')
index = int(input('Enter The Index Position Of Element To Remove: '))
string = string[:index] + string[index+1:]
print(string)
