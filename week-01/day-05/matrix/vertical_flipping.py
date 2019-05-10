"""
# Vertical flipping

Create a program that can vertically flip a matrix.
"""

def vertical_flip(matrix):
  row_length = len(matrix)
  for row_index in range(row_length//2 + 1):
    if row_index != row_length - row_index:
      matrix[row_index], matrix[row_length - 1 - row_index] = matrix[row_length - 1 - row_index], matrix[row_index]
  return matrix


matrix_x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

print(vertical_flip(matrix_x))