'''
# Strings

Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
'''


def replace_x_with_y(string):
  index = string.find('x')
  if index == -1:
    return string
  else:
    return string[:index] + 'y' + replace_x_with_y(string[index+1:])


string = input('Please input a number(press enter to end):\n')
result = replace_x_with_y(string)
print(result)