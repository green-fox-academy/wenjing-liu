"""
# Image source

Create a regular expression that matches the source from
[HTML image element](1).

[1]:https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img

| Task    |                                                Text | Capture Groups        |
|:--------|----------------------------------------------------:|-----------------------|
| Capture |                               `<img src="dog.png">` | `dog.png`             |
| Capture | `<img alt="Cat picture" src="./images/cat-01.png">` | `./images/cat-01.png` |
| Skip    |                 `<script src="jquery.js"></script>` |                       |
"""

strings_to_test = ['<img src="dog.png">', '<img alt="Cat picture" src="./images/cat-01.png">', '<script src="jquery.js"></script>']

import re

pattern = re.compile('<img.+?src=[\"\'](.+?)[\"\'].*?>')

for value in strings_to_test:
  result = pattern.match(value)
  if result:
    print(f'{value}: ', result.groups())
  else:
    print('Not matched')