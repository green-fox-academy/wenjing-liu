# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

magic_num = 5

print('Guess the number!')
is_found = False
while not(is_found) :
  guess_num = float(input('Please input a number(press enter to stop enter):\n'))
  if guess_num > magic_num:
    print('The stored number is lower')
  elif guess_num < magic_num:
    print('The stored number is higher')
  else:
    print(f'You found the number: {magic_num}')
    is_found = True