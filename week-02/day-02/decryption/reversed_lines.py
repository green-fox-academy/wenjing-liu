# Create a method that decrypts reversed-lines.txt
def decrypt(file_name, result_file_name):
  try:
    with open(file_name, 'r') as source_file:
      with open(result_file_name, 'a') as result_file:
        for line in source_file:
          reversed_result = reverse_line(line)
          result_file.write(reversed_result)
  except Exception as e:
    print(f'Error occurs when do decrypt {file_name}: {e}')
  

def reverse_line(line_content):
  return line_content[::-1]

decrypt('reversed_lines.txt', 'reversed_lines_result.txt')