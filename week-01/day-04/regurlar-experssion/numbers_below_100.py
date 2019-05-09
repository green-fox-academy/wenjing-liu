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

print('0 test:', pattern.match('0'))
print('9 test:', pattern.match('9'))
print('55 test:', pattern.match('55'))
print('100 test:', pattern.match('100'))
print('101 test:', pattern.match('101'))
print('-4 test:', pattern.match('-4'))
