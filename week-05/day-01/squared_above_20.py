"""
# Squared above 20

Given a list with the following items:
`1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14`

Create a new list which contains the numbers if their squared value is above 20.
"""

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 1]

squared_result = map(lambda n: n*n, numbers)

above_20_numbers = filter(lambda n: n > 20, squared_result)

print(list(above_20_numbers))