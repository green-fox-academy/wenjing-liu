"""
# Addition

Create a program that can substraction two matrices together.
"""


def substract_matrix(matrix_1, matrix_2):
  result = []
  if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
    raise Exception('The input two matrixes have different rows or colums')
  for row_number in range(len(matrix_1)):
    result.append([])
    for col_number in range(len(matrix_1[row_number])):
      (result[row_number]).append(matrix_1[row_number][col_number] - matrix_2[row_number][col_number])
  return result


matrix_x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
matrix_y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
matrix_z = [[5, 8, 1], [6, 7, 3]]

print('Right test:\n', substract_matrix(matrix_x, matrix_y))
print()
print('Throw exception test:')
substract_matrix(matrix_x, matrix_z)
