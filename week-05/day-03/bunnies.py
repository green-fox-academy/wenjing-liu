'''
# Bunnies

We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
'''

def bunnies(num):
  if num == 1:
    return 2
  else:
    return 2 + bunnies(num - 1)


number = int(input('Please input a number(press enter to end):\n'))
print(bunnies(number))