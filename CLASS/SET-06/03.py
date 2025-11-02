'''
Character Frequency (Dictionary):
Take a string input and display each character with its frequency using a dictionary.
'''

ip_str = input('Enter A String: ')
freq_dict = {}
for ch in ip_str:
  if ch not in freq_dict:
    freq_dict[ch] = 1
  else:
    freq_dict[ch] += 1
print(freq_dict)