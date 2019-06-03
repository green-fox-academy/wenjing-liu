from functools import reduce
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

"""
# Average of odd numbers

Given a list with the following items:
`1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14`

Calculate the average of the odd numbers.
"""

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

odd_numbers = list(filter(lambda x: x%2 == 1, numbers))
print(sum(odd_numbers)/len(odd_numbers))

