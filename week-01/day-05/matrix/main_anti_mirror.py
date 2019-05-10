"""
# Main anti-diagonal mirroring

Create a program that can mirror the given matrix across the main anti-diagonal.
"""

def main_anti_mirror(matrix):
  if len(matrix) != len(matrix[0]):
    raise Exception('The input matrix is not square matrix.')
  
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if row == col:
        break
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
  
  return matrix

matrix_x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
print(main_anti_mirror(matrix_x))
