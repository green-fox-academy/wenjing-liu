"""
# Scalar multiplication

Create a program that can multiply a matrix with a scalar.
"""

def scalar_multiply(scalar, matrix):
  result = []
  for row_num in range(len(matrix)):
    result.append([])
    for col_num in range(len(matrix[row_num])):
      result[row_num].append(scalar * matrix[row_num][col_num])
  return result


matrix_x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

print(scalar_multiply(3, matrix_x))