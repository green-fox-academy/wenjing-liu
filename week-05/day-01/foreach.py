"""
# Foreach

Create a function called `foreach` which can take an iterable and an other
function. Apply the function for all the elements in the iterable.
"""


def foreach(func, iter):
  result = []
  for item in iter:
    result.append(func(item))
  return result



def plus_one(num):
  num += 1
  return num


numbers = [1, 2, 3]

print(foreach(plus_one, numbers))
print(numbers)