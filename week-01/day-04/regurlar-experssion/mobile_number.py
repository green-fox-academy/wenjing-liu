"""
# Mobile numbers

Create a regular expression that matches any other country's mobile numbers than
Hungary.
"""

import re

pattern = re.compile('\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[943210]|2[70]|7|1)\d{1,14}$')

print('+36204732746: ', pattern.match('+3620473274'))
print('+36302174912: ', pattern.match('+3630217491'))
print('+36203173471: ', pattern.match('+36203173471'))
print('+49204831273: ', pattern.match('+49204831273'))
print('+8615019288737: ', pattern.match('+861501928873'))