# Write a function that is able to manipulate a file
# By writing your name into it as a single line
# The file should be named "my-file.txt"
# In case the program is unable to write the file,
# It should print the following error message: "Unable to write file: my-file.txt"

def write_single_line(file_path):
  try:
    with open(file_path, 'w') as file:
      file.write('Claire Liu')
  except:
    print(f'Unable to write file: {file_path}')

write_single_line('my-file.txt')
