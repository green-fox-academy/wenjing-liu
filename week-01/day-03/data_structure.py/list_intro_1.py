name_list = []
print(f'the num of list is {len(name_list)}')
name_list.append('William')

if not name_list:
  print('the list is empty')

name_list.append('John')
name_list.append('Amanda')
print(f'The number of list after two inster action is: {len(name_list)}')
print(f'The third element is {name_list[2]}')

for value in name_list:
  print(value)

for i in range(len(name_list)):
  print(f'{i + 1}. {name_list[i]}')

# name_list.pop(1)
# del name_list[1]
name_list[1:2] = []
print(name_list[::-1])



"""
# List introduction 1

We are going to play with lists. Feel free to use the built-in methods where
possible.

- Create an empty list which will contain names (strings)
- Print out the number of elements in the list
- Add William to the list
- Print out whether the list is empty or not
- Add John to the list
- Add Amanda to the list
- Print out the number of elements in the list
- Print out the 3rd element
- Iterate through the list and print out each name
  ```
  William
  John
  Amanda
  ```
- Iterate through the list and print
  ```
  1. William
  2. John
  3. Amanda
  ```
- Remove the 2nd element
- Iterate through the list in a reversed order and print out each name
  ```
  Amanda
  William
  ```
- Remove all elements

"""

name_list[:] = []
print(name_list)

