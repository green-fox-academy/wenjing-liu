# Create a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
rows = 8
colums = 8
for i in range(1, rows + 1):
  if (i % 2 == 0):
    for j in range(1, colums // 2 + 1):
      print(' %', end = '')
    print()
  else:
    for j in range(1, colums // 2 + 1):
      print('% ', end = '')
    print()


