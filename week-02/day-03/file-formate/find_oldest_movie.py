import csv

def read_csv_file(file_name):
  try:
    with open(file_name, 'r') as file:
      line_list = []
      reader = csv.reader(file, delimiter=';')
      for row in reader:
        line_list.append(row)
      return line_list
  except Exception as e:
    print(f'Error occurs when reading file {file_name}: {e}')
    return False


def find_oldest_movie(file_name):
  movie_list = read_csv_file(file_name)
  if movie_list:
    return sorted(movie_list, key = lambda el: el[1])[0]

print(find_oldest_movie('movies.csv'))