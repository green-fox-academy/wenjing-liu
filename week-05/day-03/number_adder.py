'''
# Number adder

Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
'''

def add(number):
  if number == 1:
    return number
  else:
    return number + add(number - 1)

number = int(input('Please input a number(press enter to end):\n'))
print(add(number))