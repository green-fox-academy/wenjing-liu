"""
# Mobile numbers

Create a regular expression that matches any other country's mobile numbers than
Hungary.
"""

import re

pattern = re.compile('\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[943210]|2[70]|7|1)\d{1,14}$')

testing_data = ['+36204732746', '+36302174912', '+36203173471', '+49204831273', '+8615019288737']

for value in testing_data:
  print(f'{value} test: {pattern.match(value)}')