"""
# Squared positives

Given a list with the following items:
`1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14`

Create a new list which contains the positive items' squared value.
"""

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
postives = filter(lambda x: x > 0, numbers)

result = map(lambda n: n*n, postives)
print(list(result))