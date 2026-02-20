d1 = {'a': 20, 'b': 40, 'c': 25}
d2 = {'b': 250, 'c': 150, 'd': 200}

for key in d1:
  if key in d2:
    d2[key] += d1[key]
  elif key not in d2:
    d2.update([(key, d1[key])])
print(d2)