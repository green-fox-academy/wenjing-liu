import csv
import re

def exams_performance(file_name):
  try:
    with open(file_name) as tsvfile:
      reader = csv.DictReader(tsvfile, dialect='excel-tab')
      performance = []
      for row in reader:
        row['time'] = convert_to_seconds(row['time'])
        if row['time']:
            row['ratio'] = float(row['points']) / row['time']
        else:
            row['ratio'] = -1
        performance.append(row)
      result = sorted(performance, key = lambda el: el['ratio'], reverse = True)
      return result[0]
  except Exception as e:
    print(f'Error occurs when handle file {file_name}: {e}')



def convert_to_seconds(time_string):
  
  regex_time_1 = re.compile(r'(?:((?:\.)?\d+)h)?(?:(\d+)m)?(\d+)s$')
  regex_time_2 = re.compile(r'(?:((?:\.)?\d+)h)?(\d+)m$')
  regex_time_3 = re.compile(r'(\.?\d+)h$')
  regex_time_4 = re.compile(r'(\d*):(\d*):(\d*)')
  hour_in_second = 3600
  min_in_second = 60

  time_in_second = 0.0
  if regex_time_1.match(time_string):
    groups = regex_time_1.match(time_string).groups()
    if groups[0]:
      time_in_second += float(hour_in_second) * float(groups[0])
    if groups[1]:
      time_in_second += float(min_in_second) * float(groups[1])
    time_in_second += float(groups[2])
  elif regex_time_2.match(time_string):
    groups = regex_time_2.match(time_string).groups()
    if groups[0]:
      time_in_second += float(hour_in_second) * float(groups[0])
    if groups[1]:
      time_in_second += float(min_in_second) * float(groups[1])
  elif regex_time_3.match(time_string):
    groups = regex_time_3.match(time_string).groups()
    if groups[0]:
      time_in_second += float(hour_in_second) * float(groups[0])
  elif regex_time_4.match(time_string):
    groups = regex_time_4.match(time_string).groups()
    if groups[0]:
      time_in_second += float(hour_in_second) * float(groups[0])
    if groups[1]:
      time_in_second += float(min_in_second) * float(groups[1])
    time_in_second += float(groups[2])
  return time_in_second

print(exams_performance('exams.tsv'))