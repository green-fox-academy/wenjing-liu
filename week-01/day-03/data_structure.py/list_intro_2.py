list_A = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']

list_B = list_A.copy()

if 'Durian' in list_A:
  print('\'Durian\' in the list_A')
else:
  print('\'Durian\' not in the list_A')

list_B.remove('Durian')

list_A.insert(4, 'Kiwifruit')

if len(list_A) > len(list_B):
  print('The length of list_A is longer than list_B')
elif len(list_A) == len(list_B):
  print('The lenght of list_A is equal to list_B')
else:
  print('The length of list_A is shorter than list_')

print(f"The index of \'Avocado\' in list_A is {list_A.index('Avocado')}")

if 'Durian' in list_B:
  print(f"The index of \'Durian\' in list_B is {list_B.get('Durian')}")
else:
  print('\'Durian\' is not in the list_B')


list_B.extend(['Passion Fruit', 'Pummelo'])
print(list_B)

print(f'The third element int list_A is {list_A[1]}')





"""
# List introduction 2

- Create a list ('`List A`') which contains the following values
  ```
  Apple, Avocado, Blueberries, Durian, Lychee
  ```
- Create a new list ('`List B`') with the values of `List A`
- Print out whether `List A` contains Durian or not
- Remove Durian from `List B`
- Add Kiwifruit to `List A` after the 4th element
- Compare the size of `List A` and `List B`
- Get the index of Avocado from `List A`
- Get the index of Durian from `List B`
- Add Passion Fruit and Pummelo to `List B` in a single statement
- Print out the 3rd element from `List A`

"""