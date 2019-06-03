"""
# Fizz Buzz generator

Create a generator which will always yield the next item from the [fizz buzz](https://en.wikipedia.org/wiki/Fizz_buzz)
sequence.
"""

def generator():
  index = 0
  while True:
    if index % 3 == 0 and index % 5 == 0:
      yield 'Fizz Buzz'
    elif index % 3 == 0:
      yield 'Fizz'
    elif index % 5 == 0:
      yield 'Buzz'
    else:
      yield index
    index += 1

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
print(next(g))
print(next(g))
print(next(g))
print(next(g))
