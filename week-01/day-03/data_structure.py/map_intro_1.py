map_ex = {}
print(f'The length of the map is: {len(map_ex)}')

if not map_ex:
  print('The map is empty')

map_ex[97] = 'a'
map_ex[98] = 'b'
map_ex[99] = 'c'
map_ex[65] = 'A'
map_ex[66] = 'B'
map_ex[67] = 'C'

print('All keys in the map:')
for key in map_ex:
  print(key)

print('All values in the map:')
for key in map_ex:
  print(map_ex[key])

map_ex[68] = 'D'

print(f'The number of value-pair in map is {len(map_ex)}')

print(f'The value of key 99 in the map is {map_ex[99]}')

del map_ex[97]
print(map_ex)

if 100 in map_ex:
  print('The key 100 in the map')
else:
  print('The key 100 not in the map')

map_ex.clear()
print(map_ex)








"""
# Map introduction 1

We are going to play with maps. Feel free to use the built-in methods where
possible.

- Create an empty map where the keys are integers and the values are characters
- Print out whether the map is empty or not
- Add the following key-value pairs to the map

  | Key | Value |
  |:----|:------|
  | 97  | a     |
  | 98  | b     |
  | 99  | c     |
  | 65  | A     |
  | 66  | B     |
  | 67  | C     |

- Print all the keys
- Print all the values
- Add value D with the key 68
- Print how many key-value pairs are in the map
- Print the value that is associated with key 99
- Remove the key-value pair where with key 97
- Print whether there is an associated value with key 100 or not
- Remove all the key-value pairs
"""