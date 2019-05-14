# Create a method that decrypts reversed-order.txt

def decrypt(file_name, result_file_name):
  try:
    with open(file_name, 'r') as source_file:
      with open(result_file_name, 'a') as result_file:
        line_list = source_file.readlines()
        result_file.write(''.join(reverse_order(line_list)))
  except Exception as e:
    print(f'Error occurs when do decrypt {file_name}: {e}')
  

def reverse_order(line_list):
  return line_list[::-1]

decrypt('reversed_order.txt', 'reversed_order_result.txt')