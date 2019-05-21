import random

class CAB:
  def __init__(self):
    self.number = random.randint(1000, 9999)
    self.counter = 0
    self.state = 'not start'
  
  def guess(self, guess_number):
    if self.counter == 0:
      self.state == 'playing'
    self.counter += 1
    
    guess_str = str(guess_number)
    number_str = str(self.number)
    if len(guess_str) > 4:
      raise ValueError

    cow_counter = 0
    bull_counter = 0
    for index in range(len(guess_str)):
      if guess_str[index] == number_str[index]:
        cow_counter += 1
      elif guess_str[index] in number_str:
        bull_counter += 1

    if cow_counter == 4:
      self.state = 'finished'

    return f'{cow_counter} cow, {bull_counter} bull'

'''
# Cows and Bulls

Create a class what is capable of playing exactly one game of
[Cows and Bulls (CAB)](https://en.wikipedia.org/wiki/Bulls_and_Cows). The player
have to guess a 4 digit number. For every digit that the player guessed
correctly in the correct place, they have a “cow”. For every digit the player
guessed correctly in the wrong place is a “bull.” If the player types a number
that does not exist, that quess will not have any result.

Example: If the number to be found is "7624" and the player types "7296", the
result is: "1 cow, 2 bull".

- The CAB object should have a random 4 digit number, which is the goal to guess.
- The CAB object should have a state where the game state is stored (`playing`,
  `finished`).
- The CAB object should have a counter where it counts the guesses.
- The CAB object should have a guess method, which returns a string of the guess
  result
- All methods, including constructor should be tested
'''