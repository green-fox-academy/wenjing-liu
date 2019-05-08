# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)

def print_params(*arg):
  for param in arg:
    print(param)

print_params(1, 2, 3, 4)