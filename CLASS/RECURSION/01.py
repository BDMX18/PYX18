# Flattening A List: 

def flatten(list_raw):
  flatten_list = []
  for element in list_raw:
    if(isinstance(element, list)):
      flatten_list.extend(flatten(element))
    else:
      flatten_list.append(element)
  return flatten_list

list_raw = [[11, 22, 33], 90, [[34, 24], 89]]
print(flatten(list_raw))


