"""
# All positive

Given a list with the following items:
`1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14`

Determine whether every number is positive or not using
[`all()`](https://docs.python.org/3/library/functions.html#all).
"""

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

map_result = map(lambda x: True if x > 0 else False, numbers)

print(all(map_result))