'''
Replace nested loops:

result = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            result.append((x, y))
'''

x = [1,2,3]
y = [3,1,4]
op_list = [(xe,ye) for xe in x for ye in y if xe != ye]
print(op_list)