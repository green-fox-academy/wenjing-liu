"""
# Horizontal flipping

Create a program that can horizontally flip a matrix.
"""


def horizontal_flip(matrix):
  col_length = len(matrix[0])
  for col_index in range(col_length//2 + 1):
    if col_index != col_length - 1 - col_index:
      for row in range(len(matrix)):
        matrix[row][col_index], matrix[row][col_length - 1 - col_index] = matrix[row][col_length - 1 - col_index], matrix[row][col_index]
  return matrix


matrix_x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

print(horizontal_flip(matrix_x))