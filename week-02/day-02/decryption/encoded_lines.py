# Create a method that decrypts reversed-lines.txt
def decode_lines(file_name, result_file_name):
  try:
    with open(file_name, 'r') as source_file:
      with open(result_file_name, 'a') as result_file:
        for line in source_file:
          reversed_result = []
          for char in line:
            if char == ' ':
              reversed_result.append(char)
              continue
            reversed_result.append(decode_char(char))
          result_file.write(''.join(reversed_result) + '\n')
  except Exception as e:
    print(f'Error occurs when do decrypt {file_name}: {e}')
  

def decode_char(char):
  return chr(ord(char) - 1)

decode_lines('encoded_lines.txt', 'decoded_lines_result.txt')