'''
Q2. Validate Vehicle Number Using Regex

Write a Python program that validates Indian vehicle registration numbers (like OD02AB1234).

Sample Data:

vehicle_numbers = ["OD02AB1234", "KA01CD5678", "OD2A1234", "MH14XY9999"]


Expected Output:

Valid: ['OD02AB1234', 'KA01CD5678', 'MH14XY9999']
Invalid: ['OD2A1234']
'''
import re

pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'

vehicle_numbers = ["OD02AB1234", "KA01CD5678", "OD2A1234", "MH14XY9999"]

str_num = ' '.join(vehicle_numbers)

valid = re.findall(pattern, str_num)

invalid = [num for num in vehicle_numbers if num not in valid]

print('Valid:', valid)
print('Invalid:', invalid)
