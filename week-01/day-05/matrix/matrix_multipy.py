def multiply_matrix(matrix_x, matrix_y):
  result = []
  if len(matrix_x[0]) != len(matrix_y):
    raise Exception('The colum of first matrix and is not equal with the row of second matrix')
  for row_number in range(len(matrix_x)):
    result.append([])
    for col_number in range(len(matrix_y[0])):
      item_value = 0
      for index in range(len(matrix_x[0])):
        item_value += matrix_x[row_number][index] * matrix_y[index][row_number]
      (result[row_number]).append(item_value)
  return result


matrix_x = [[1, 1, 1], [2, 2, 2]]
matrix_y = [[1, 1], [2, 2], [3, 3]]
matrix_z = [[5, 8, 1], [6, 7, 3]]

print(multiply_matrix(matrix_x, matrix_y))

print()
print('Throw exception test:')
print(multiply_matrix(matrix_x, matrix_z))