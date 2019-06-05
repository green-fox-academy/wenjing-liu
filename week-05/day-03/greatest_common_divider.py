'''
# Greatest Common Divisor

Find the greatest common divisor of two numbers using recursion.
'''


num_1, num_2 = [int(x) for x in input('Please input base and power (press enter to end):\n').split()]



def greatest_common_divisor(num_1, num_2):
  smaller = num_1 if num_1 < num_2 else num_2
  bigger = num_1 if num_1 >= num_2 else num_2
  next_divider = bigger%smaller
  if next_divider == 0:
    return smaller
  else:
    return greatest_common_divisor(smaller, next_divider)


result = greatest_common_divisor(num_1, num_2)
print(result)