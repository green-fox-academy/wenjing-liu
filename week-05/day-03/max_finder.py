'''
# Maximum finder

Write a function that finds the largest element of an array using recursion.
'''

def max_finder(num_list):
  if len(num_list) == 1:
    return num_list[0]
  else:
    return num_list[0] if num_list[0] > max_finder(num_list[1:]) else max_finder(num_list[1:])



numbers = [1, 2, 5, 4, 1]

result = max_finder(numbers)

print(result)