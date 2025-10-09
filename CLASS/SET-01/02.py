'''
2. Given a string, count the number of vowels and consonants.
Input: "Hello World"
Output: Vowels: 3, Consonants: 7
'''

def count_v_c(ip_str):
  v_count = 0
  c_count = 0
  for ch in ip_str:
    if ch.isalpha():
      if ch in 'aeiou':
        v_count += 1
      else:
        c_count += 1
  return f'Vowels: {v_count}, Consonants: {c_count}'

print(count_v_c('Hello World'))

