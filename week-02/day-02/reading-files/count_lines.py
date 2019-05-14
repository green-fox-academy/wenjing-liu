# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines(file_path):
  try:
    with open(file_path, 'r') as file:
      return len(file.readlines())
  except FileNotFoundError:
    return 0

print(count_lines('my-file.txt'))

print(count_lines('my-file_1.txt'))