# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(num):
  result = 1
  for i in range(1, int(num) + 1):
    result *= i
  return result

print(factorio(10))
