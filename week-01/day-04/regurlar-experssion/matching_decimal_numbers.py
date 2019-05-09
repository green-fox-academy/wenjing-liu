import re

pattern = re.compile('[+-]?((\d+(,\d+)?(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?$')

str_list = ['3.14529', '-255.34', '128', '1.9e10', '123,340.00', '720p']

for item in str_list:
  print(f'{item}: ', pattern.match(item))