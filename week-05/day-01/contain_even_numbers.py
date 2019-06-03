"""
# Contains even numbers

Given a list with the following items:
`1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14`

Determine whether it contains even numbers or not using
[`any()`](https://docs.python.org/3/library/functions.html#any).
"""

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

map_result = map(lambda x: x%2, numbers)
print(any(map_result))

