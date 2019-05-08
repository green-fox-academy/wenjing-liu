# Write a function called `sum` that returns the sum of numbers from zero to the given parameter

def sum(num):
  total = 0 
  for i in range(num):
    total += i
  return total


print(sum(20))