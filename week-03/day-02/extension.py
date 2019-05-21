def add(a, b):
    return a + b

def max_of_three(a, b, c):
  bigger = a
  if bigger < b:
      bigger = b
  if bigger < c:
    bigger = c
  return bigger

def median(pool):
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve