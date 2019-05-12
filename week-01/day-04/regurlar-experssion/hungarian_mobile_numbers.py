import re

# pattern_1 = re.compile('(^(\+|00)\s?(1|[2-9][0-9])?\s\d\d\s\d{3}\s\d{4}$)')

pattern_2 = re.compile('(\+|00)\s?36\s(1|[0-9][0-9])\s\d{3}\s\d{4}')

testing_data = ['+36 20 473 274', '+36 30 217 4912', '00 36 70 381 1288', '00 36 31 471 2818', '+36 20 3173 471', '+49 20 483 1273', '36 70 381 2183']

for value in testing_data:
  print(f'{value} test: {pattern_2.match(value)}')


"""
# Hungarian mobile numbers

Create a regular expression that matches the valid
[Hungarian mobile numbers][1].

[1]: https://en.wikipedia.org/wiki/Telephone_numbers_in_Hungary

| Task  |              Text |
|:------|------------------:|
| Match |   +36 20 473 2746 |
| Match |   +36 30 217 4912 |
| Match | 00 36 70 381 1288 |
| Match | 00 36 31 471 2818 |
| Skip  |  +36 20 3173 4717 |
| Skip  |  +36 102 237 1121 |
| Skip  |   +49 20 483 1273 |
| Skip  |    36 70 381 2183 |
"""
