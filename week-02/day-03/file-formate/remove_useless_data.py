import csv

def remove_useless_data(file_name, result_file):
  try:
    with open(file_name, 'r') as file:
      with open(result_file, 'a') as result:
        useless_content = []
        reader = csv.reader(file, delimiter = ',')
        writer = csv.writer(result)
        for row in reader:
          if is_useful_line(row):
            writer.writerow(row)
          else:
            useless_content.append(row)
  except Exception as e:
    print(f'Occurs error when remove useless data from {file_name}: {e}')
    return False

def is_useful_line(line):
  if len(line) >= 4 and line[0] and line[1] and line[3]:
    return True
  return False

remove_useless_data('election.csv', 'election_result.csv')
# print(remove_useless_data('election.csv', 'election_result.csv'))

