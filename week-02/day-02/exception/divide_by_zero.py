# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

def divide():
  divisor = float(input('Please Input a divisor\n'))
  return 10 / divisor
       
try:
  print(divide())
except ZeroDivisionError:
  print('Can\'t divide by zero!')
except ValueError:
  print('Must input a number!')