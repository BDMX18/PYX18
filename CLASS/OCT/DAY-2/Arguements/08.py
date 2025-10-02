'''
Positional + Keyword Aggregator

Problem:
Write a function aggregate_data(id, *args, **kwargs) where:

id is mandatory.

*args contains numerical scores.

**kwargs contains additional info like name, department.

Return a dictionary with: id, total_score, average_score, and all keyword info.

Sample Input:

aggregate_data(101, 50, 60, 70, name="Alice", department="HR")


Expected Output:

{
    'id': 101,
    'total_score': 180,
    'average_score': 60.0,
    'name': 'Alice',
    'department': 'HR'
}
'''

def aggregate_data(id, *args, **kwargs):
  data_dict = {}
  total = 0
  for arg in args:
    total += arg
  average = total/len(args)
  data_dict.update({'id': id, 'total_score':total, 'average_score': average, **kwargs})
  return data_dict

print(aggregate_data(101, 50, 60, 70, name="Alice", department="HR"))