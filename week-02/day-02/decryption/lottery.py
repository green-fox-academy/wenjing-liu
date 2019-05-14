# Create a method that find the 5 most common lottery numbers in lottery.csv
def five_most_frequent(file_name):
  try:
    with open(file_name, 'r') as file:
      all_num = []
      for line in file:
        all_num.extend(line.split(';')[-5:-1])      
      count = {}
      for element in all_num:
        count[element] = count.get(element, 0) + 1
      ordered_count = sorted(count.items(), key=lambda item: item[1])
      if len(ordered_count) > 5:
        return ordered_count[-5:-1]
      else:
        return ordered_count
  except Exception as e:
    print(f'Error occurs when do decrypt {file_name}: {e}')


print(five_most_frequent('lottery.csv'))

