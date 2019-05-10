"""
# Matrix rotation

Create a program that can rotate a matrix by 90 degree.

Extend your program to work with any multiplication of 90 degree.
"""
import math

def rotate_matrix(matrix, degree):
  rotate_times = degree//90%4
  print(rotate_times)

  
  for rotate_time in range(rotate_times):
    tmp_matrix = []
    totalRowsOfRotatedMatrix = len(matrix)
    totalColsOfRotatedMatrix = len(matrix[0])
    for i in range(totalColsOfRotatedMatrix):
      tmp_matrix.append([None]*totalRowsOfRotatedMatrix)

    for row_num in range(totalRowsOfRotatedMatrix):
      for col_num in range(totalColsOfRotatedMatrix):
        tmp_matrix[totalColsOfRotatedMatrix - 1 - col_num][row_num] = matrix[row_num][col_num]
    matrix, tmp_matrix = tmp_matrix, matrix
  
  return matrix

matrix_x = [[12, 7, 3], [4, 5, 6]]
print(rotate_matrix(matrix_x, 90))
print(rotate_matrix(matrix_x, 180))
print(rotate_matrix(matrix_x, 270))
print(rotate_matrix(matrix_x, 360))
