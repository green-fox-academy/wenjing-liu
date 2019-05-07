# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

rows = int(input('Please input a number(press enter to stop):\n'))

k = 0
for i in range(1, rows + 1):
  for space in range(1, (rows-i) + 1):
    print(end = '  ')
  while k != (2 * i - 1):
    print('* ', end = '')
    k += 1
  k = 0
  print()