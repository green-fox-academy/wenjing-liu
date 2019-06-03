"""
# Filter

Create your own filter function. It should take an iterable and an other
function.
"""

import copy

def own_filter(func, iter):
  local_iter = copy.deepcopy(iter)
  for item in local_iter:
    if func(item):
      yield item

numbers = [-1, -2, 0, 1, 2, 3]


print(list(own_filter(lambda x: x > 0, numbers)))
print(list(own_filter(lambda x: x < 0, numbers)))
print(list(own_filter(lambda x: x%2==0, numbers)))