def write_multiple_lines(file_path, word, number):
  try:
    with open(file_path, 'a') as file:
      for _ in range(number):
        file.write(word+'\n')
  except FileNotFoundError:
    print(f'Unable to fount file: {file_path}')
  except IOError:
    print(f'Unable to write file: {file_path}')


write_multiple_lines('my_file_2.txt', 'apple', 10)


# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.