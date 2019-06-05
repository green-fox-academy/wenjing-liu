'''
# Sum Digits

Given a non-negative integer n, return the sum of its digits recursively (without loops).

## Hint

Mod (%) by 10 yields the rightmost digit (e.g. 126 % 10 is 6)

### Java, C++, C#, Python

Divide (/) by 10 removes the rightmost digit (e.g. 126 / 10 is 12).

### JavaScript, TypeScript

There is no integer type in JavaScript. To remove the rightmost digit you must divide (/) the number by 10 and find a way to get the the whole number portion of that number.
'''

def sum_digit(number):
  length = len(str(number))
  if length == 1:
    return number
  else:
    divider = int('1' + '0' * (length - 1))
    return int(number/divider)+ sum_digit(number%divider)

number = int(input('Please input a number(press enter to end):\n'))
result = sum_digit(number)
print(result)