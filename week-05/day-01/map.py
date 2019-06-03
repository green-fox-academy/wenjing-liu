"""
# Map

Create your own map function. It should take an iterable and an other function.
"""
import copy 


def own_map(func, iter):
  local_iter = copy.deepcopy(iter)
  for item in local_iter:
    yield func(item)


numbers = [1, 2, 3]

def square(num):
  return num * num

print(list(own_map(square, numbers)))

print(list(own_map(lambda x: x + 10, numbers)))