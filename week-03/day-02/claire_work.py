
class Apple:
  def get_apple(self):
    return 'apple'

'''
# Apples

- Create a class, with one method (eg. `get_apple()`) that returns a string
  (eg. `"apple"`)
- Create a test for that:
  - Create a test class
  - Create a test method
  - Instantiate an Object from your class in the method
  - Use the `assertEquals()`
  - The expected parameter should be the same string (eg. `"apple"`)
  - The actual parameter should be the return value of the method
    (eg. `myobject.get_apple()`)
- Run the test
- Change the expected value to make the test failing
- Run the test
- Fix the returned value to make the test succeeding again
'''
class Sum:
  def sum(self, number_list):
    result = 0
    if len(number_list) == 0:
      return result
    for item in number_list:
      if isinstance(item, int):
        result += item
      else:
        raise TypeError
    return result


'''
# Sum

- Create a sum method in your class which has a list of integers as parameter
- It should return the sum of the elements in the list
- Follow these steps:
  - Add a new test case
  - Instantiate your class
  - create a list of integers
  - use `assertEqual` to test the result of the created sum method
- Run it
- Create different tests where you
  - test your method with an empyt list
  - with a list with one element in it
  - with multiple elements in it
  - with `None`
- Run them
- Fix your code if needed
'''



def is_anagram(str1, str2):
  str1_copy = str1.lower().replace(' ', '')
  str2_copy = str2.lower().replace(' ', '')

  str1_set = set(str1_copy)
  str2_set = set(str2_copy)
  is_anagram = False 
  if str1_set == str2_set:
    is_anagram = True
    for value in str1_set:
      if str1_copy.count(value) != str2_copy.count(value):
        is_anagram = False
        break
  return is_anagram

'''
# Anagram

- Write a function, that takes two strings and returns a boolean value based on
  if the two strings are Anagramms or not.
- Create a test for that.
'''

def counter_letters(string):
  result = {}
  for char in string:
    result[char] = result.get(char, 0) + 1
  return result

'''
# Count Letters

- Write a function, that takes a string as an argument and returns a dictionary
  with all letters in the string as keys, and numbers as values that shows how
  many occurrences there are.
- Create a test for that.
'''


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

'''
# Fibonacci

- Write a function that computes a member of the fibonacci sequence by a given
  index
- Create tests for multiple test cases.
'''