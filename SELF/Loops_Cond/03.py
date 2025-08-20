'''
3. Number Guessing Game

Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''

import random

count = 0
randomNo = random.randint(1, 9)

while True:
  guess = int(input('Enter A Number Between 1 to 9: '))
  count += 1
  if (guess == randomNo):
    print('Your Guess Is Correct!')
    break
print(f'Youu Won The Game After {count} Guesses')