# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"

import os 


def print_file_by_line(file_path):
  try:
    with open(file_path, 'r') as file:
      line_content = file.readline()
      while line_content:
        print(line_content, end = '')
        line_content = file.readline()
  except FileNotFoundError:
    print(f'{file_path} is not found.')


print_file_by_line('my-file.txt')
print()
print_file_by_line('my-file_1.txt')


