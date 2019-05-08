shopping_list = ['eggs', 'milk', 'fish', 'apples', 'bread', 'chicken']


def ask_shop_list(shop_list, ques):
  print(f'Do we have {ques} in the list?')
  if ques in shop_list:
    print(f'Yes, we have {ques} in the list')
  else:
    print(f'No, we don\'t have {ques} in the list')

ask_shop_list(shopping_list, 'milk')
ask_shop_list(shopping_list, 'bananas')

"""
# Shopping list

We are going to represent a shopping list in a list containing strings.

- Create a list with the following items.
  - Eggs, milk, fish, apples, bread and chicken
- Create an application which solves the following problems.
  - Do we have milk on the list?
  - Do we have bananas on the list?

"""