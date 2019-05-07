# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
rows = 4
matrix = []
for i in range(0, rows):
  matrix.append([])
  for j in range(0, rows):
    if (j == i):
      matrix[i].append(1)
    else:
      matrix[i].append(0)

for i in range(0, rows):
  print(matrix[i])
