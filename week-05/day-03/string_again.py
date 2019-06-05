'''
# Strings again

Given a string, compute recursively a new string where all the 'x' chars have been removed.
'''


def replace_x_with_nothing(string):
  index = string.find('x')
  if index == -1:
    return string
  else:
    return string[:index] + replace_x_with_nothing(string[index+1:])


string = input('Please input a number(press enter to end):\n')
result = replace_x_with_nothing(string)
print(result)