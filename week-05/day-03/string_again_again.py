'''
# Strings again and again

Given a string, compute recursively a new string where all the adjacent chars are now separated by a `*`
'''

def add_star_to_string(string):
  length = len(string)
  if length == 1:
    return string
  else:
    return string[0] + '*' + add_star_to_string(string[1:])


string = input('Please input a number(press enter to end):\n')
result = add_star_to_string(string)
print(result)