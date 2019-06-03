"""
# Fibonacci generator

Create a generator which will always yield the next Fibonacci number.
"""

def fibonacci(number):
  result = [0, 1]
  if number <= 0:
    raise ValueError
  elif number == 1:
    return [result[0]]
  else:
    while len(result) < number:
      result.append(result[-1] + result[-2])
  return result

def generator():
  last_1 = 0
  last_2 = 0
  counter = 0
  while True:
    if counter == 0:
      result = 0
    elif counter == 1:
      result = 1
    else:
      result = last_1 + last_2
    yield result
    last_2 = last_1
    last_1 = result
    counter += 1


g = generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

