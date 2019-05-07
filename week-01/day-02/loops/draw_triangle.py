# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

rows = int(input('Please input a number(press enter to stop):\n'))

string = ''
if (rows < 1):
  print('Please input a number bigger than 1')
else:
  for i in range(rows):
    string += '*'
    print(string)
