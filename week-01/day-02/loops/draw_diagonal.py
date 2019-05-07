# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

rows = int(input('Please input a number(press enter to stop):\n'))

for i in range(1, rows + 1):
  if i == 1 or i == rows:
    for j in range(1, rows + 1):
      print('%', end = '')
    print()
  else:
    print('%', end = '')
    for j in range(2, rows):
      if (j == i):
        print('%', end = '')
      else:
        print(' ', end = '')
    print('%', end = '')
    print()