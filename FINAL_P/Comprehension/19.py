'''
Q7. Merge Unequal Lists with Default Value

Problem:
Given two lists of unequal lengths, use zip_longest() and dictionary comprehension to pair elements.
If one list is shorter, use "NA" as the missing value.

Sample Data:

countries = ['India', 'USA', 'UK']
capitals = ['Delhi', 'Washington D.C.']


Expected Output:

{'India': 'Delhi', 'USA': 'Washington D.C.', 'UK': 'NA'}

'''

from itertools import zip_longest

countries = ['India', 'USA', 'UK']
capitals = ['Delhi', 'Washington D.C.']

print({country:capital for country, capital in zip_longest(countries, capitals, fillvalue='NA')})