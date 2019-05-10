"""
# Transposition

Create a program that calculates the transposition of a matrix.
"""

def transposition_matrix(matrix):
  result = []
  for col_num in range(len(matrix[0])):
    result.append([None]*len(matrix))
  print(result)
  for row_num in range(len(result)):
    for col_num in range(len(result[row_num])):
      result[row_num][col_num] = matrix[col_num][row_num]
  return result


matrix_x = [[12, 7, 3], [4, 5, 6]]
print(transposition_matrix(matrix_x))