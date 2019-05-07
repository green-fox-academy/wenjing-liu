# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.
multi_three = 'Fizz'
multi_five = 'Buzz'
for x in range(1, 100):
  if x % 3 == 0 and x % 5 == 0:
    print(multi_three + multi_five)
  elif x % 3 == 0:
    print(multi_three)
  elif x % 5 == 0:
    print(multi_five)
  else:
    print(x)
