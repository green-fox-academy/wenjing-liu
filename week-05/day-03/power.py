'''
# Power

Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
'''

base, power_num = [int(x) for x in input('Please input base and power (press enter to end):\n').split()]


def power(base, power_num):
  if power_num == 1:
    return base
  else:
    return base * power(base, power_num - 1)


print(power(base, power_num))