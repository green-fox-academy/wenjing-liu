# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

rows = int(input('Please input a number(press enter to stop):\n'))

middle = rows // 2 + 1

k = 0
for i in range(1, middle + 1):
  for space in range(1, (middle - i) + 1):
    print(end = '  ')
  while k != (2 * i - 1):
    print('* ', end = '')
    k += 1
  k = 0
  print()
for j in range(middle + 1, rows + 1): #from row 6 to 9
  for space in range(j - middle):
    print(end = '  ')
  for h in range((rows + 1 - j) * 2 - 1):
    print('* ', end = '')
  print()