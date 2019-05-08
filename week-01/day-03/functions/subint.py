#  Create a function that takes a number and a list of numbers as a parameter
#  Returns the indeces of the numbers in the list where the first number is part of
#  Or returns an empty list if the number is not part of any of the numbers in the list

# Example
# print(subint(1, [1, 11, 34, 52, 61]))
# should print: `[0, 1, 4]`
# print(subint(9, [1, 11, 34, 52, 61]))
# should print: '[]'

def subint(num, test_list):
  indeces = []
  for i in test_list:
    if str(i).find(str(num)) != -1:
      indeces.append(test_list.index(i))
  
  return indeces

print(subint(1, [1, 11, 34, 52, 61]))
