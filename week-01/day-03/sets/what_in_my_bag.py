oliver_bag = {'Laptop', 'Notebook', 'Pen', 'Sunglasses', 'Hand sanitizer'}

ethan_bag = {'Sunglasses', 'Notebook', 'Phone'}

mia_bag = {'Laptop', 'Sunglasses', 'Hand sanitizer'}


def set_calc():
  print('What are the common items in Oliver\'s and Ethan\'s bag?')
  inter_set = None
  inter_set = oliver_bag.intersection(ethan_bag)
  if inter_set:
    print(', '.join(inter_set))

  print('What are the items that in Oliver\'s bag but not in Mia\'s bag?')
  diff_set = None
  diff_set = oliver_bag.difference(mia_bag)
  if diff_set:
    print(', '.join(diff_set))

  print('What are the common items in Oliver\'s, Ethan\'s and Mia\'s bag?')
  common_items = None
  common_items = oliver_bag.intersection(ethan_bag).intersection(mia_bag)
  if common_items:
    print(', '.join(common_items))

set_calc()





"""
# What's in my bag

We are going to represent bags using sets.

Oliver's bag contains the following items

- Laptop
- Notebook
- Pen
- Sunglasses
- Hand sanitizer

Ethan's bag contains the following items

- Sunglasses
- Notebook
- Phone

Mia's bag contains the following items

- Laptop
- Sunglasses
- Hand sanitizer

Write an application that answers the following questions

- What are the common items in Oliver's and Ethan's bag?
- What are the items that in Oliver's bag but not in Mia's bag?
- What are the common items in Oliver's, Ethan's and Mia's bag?
"""