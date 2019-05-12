"""
# Numbers below 100

Create a regular expression that matches the numbers between 0 (including) and
100 (including).

| Task  | Text |
|:------|-----:|
| Match |    0 |
| Match |    9 |
| Match |   55 |
| Match |  100 |
| Skip  |  101 |
| Skip  |   -4 |

"""

import re

pattern = re.compile('(^0$|^[1-9][0-9]?0?$)')

testing_data = [0, 9, 55, 100, 101, -4]

for value in testing_data:
  print(f'{value} test: {pattern.match(value)}' )
