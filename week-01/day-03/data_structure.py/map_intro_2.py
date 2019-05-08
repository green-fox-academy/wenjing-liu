map_intro = {
  '978-1-60309-452-8': 'A Letter to Jo',
  '978-1-60309-459-': 'Lupus',
  '978-1-60309-444-3': 'Red Panda and Moon Bear',
  '978-1-60309-461-0': 'The Lab'
}

for key, value in map_intro.items():
  print(f'{value} (ISBN: {key})') 

to_remove = None
for key, value in map_intro.items():
  if (value == 'The Lab'):
    to_remove = key
map_intro.pop(to_remove)
print('Map after remove: ', map_intro)

map_intro['978-1-60309-450-4'] = 'They Called Us Enemy'
map_intro['978-1-60309-453-5'] = 'Why Did We Trust Him?'

if '478-0-61159-424-8' in map_intro:
  print('There exists values of 478-0-61159-424-8')
else:
  print('There doesn\'t exist values of 478-0-61159-424-8')

if '978-1-60309-453-5' in map_intro:
  print(map_intro['978-1-60309-453-5'])






"""
# Map introduction 2

- Create a map where the keys are strings and the values are strings with the
following initial values

  | Key               | Value                   |
  |:------------------|:------------------------|
  | 978-1-60309-452-8 | A Letter to Jo          |
  | 978-1-60309-459-7 | Lupus                   |
  | 978-1-60309-444-3 | Red Panda and Moon Bear |
  | 978-1-60309-461-0 | The Lab                 |

- Print all the key-value pairs in the following format
  ```
  A Letter to Jo (ISBN: 978-1-60309-452-8)
  Lupus (ISBN: 978-1-60309-459-7)
  Red Panda and Moon Bear (ISBN: 978-1-60309-444-3)
  The Lab (ISBN: 978-1-60309-461-0)
  ```
- Remove the key-value pair with key 978-1-60309-444-3
- Remove the key-value pair with value The Lab
- Add the following key-value pairs to the map

  | Key               | Value                 |
  |:------------------|:----------------------|
  | 978-1-60309-450-4 | They Called Us Enemy  |
  | 978-1-60309-453-5 | Why Did We Trust Him? |

- Print whether there is an associated value with key 478-0-61159-424-8 or not
- Print the value associated with key 978-1-60309-453-5
"""