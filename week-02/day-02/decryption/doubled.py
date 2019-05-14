# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name, result_name):
  with open(file_name, 'r') as file:
    with open(result_name, 'a') as result_file:
      for line in file:
        character_list = list(filter(lambda x: x != '', line.split(' ')))
        result_list = []
        for char in character_list:
          result_list.append(unique_word(char))
        result_file.write(' '.join(result_list))


def unique_word(character):
  list = []
  for index in range(len(character)):
    if character[index] in list:
      continue
    list.append(character[index])
  return ''.join(list)

decrypt('duplicated-chars.txt', 'doubled_result.txt')
