'''
Filter even numbers from a list.
Given a list of integers, use filter() to return only the even numbers.
'''
numList = eval(input('Enter A List: '))
print(list(filter(lambda num: num%2==0, numList)))
